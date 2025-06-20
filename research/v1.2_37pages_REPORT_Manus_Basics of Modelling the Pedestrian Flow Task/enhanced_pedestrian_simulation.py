"""
Enhanced Pedestrian Flow Simulation with Fundamental Diagram Generation
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import time

class PedestrianFlowSimulator:
    """
    Enhanced simulator for pedestrian flow using modified social force model
    """
    
    def __init__(self, N=50, L=17.3, model_type='hard_body_remote'):
        """
        Initialize the simulator
        """
        self.N = N  # Number of pedestrians
        self.L = L  # System length
        self.model_type = model_type
        
        # Model parameters from the reference
        self.a = 0.36  # Minimum space requirement (m)
        self.b = 0.56  # Velocity dependence factor (s)
        self.tau = 0.61  # Relaxation time (s)
        self.m = 1.0   # Mass (kg) - normalized
        
        # Remote action parameters
        self.e = 0.07  # Force magnitude (N)
        self.f = 2.0   # Decay exponent
        
        # Intended speed distribution
        self.v0_mean = 1.24  # Mean intended speed (m/s)
        self.v0_std = 0.05   # Standard deviation (m/s)
        
        # Numerical parameters
        self.dt = 0.001  # Time step (s)
        self.t_relax = 3.0   # Relaxation time (s)
        self.t_measure = 30.0  # Measurement time (s)
        
        # Initialize pedestrians
        self.initialize_pedestrians()
        
    def initialize_pedestrians(self):
        """Initialize pedestrian positions and velocities"""
        # Random positions with minimum spacing
        positions = []
        for i in range(self.N):
            if i == 0:
                pos = np.random.uniform(0, self.L/self.N)
            else:
                pos = positions[-1] + self.a + np.random.uniform(0, (self.L - self.N*self.a)/self.N)
            positions.append(pos % self.L)
        
        self.x = np.array(sorted(positions))
        
        # Initialize velocities to zero
        self.v = np.zeros(self.N)
        
        # Assign intended speeds
        self.v0 = np.random.normal(self.v0_mean, self.v0_std, self.N)
        self.v0 = np.maximum(self.v0, 0.1)  # Ensure positive speeds
        
    def required_length(self, v):
        """Calculate velocity-dependent required length"""
        return self.a + self.b * np.abs(v)
    
    def distance_to_next(self, x, i):
        """Calculate distance to next pedestrian with periodic boundary"""
        j = (i + 1) % self.N
        dx = x[j] - x[i]
        if dx < 0:
            dx += self.L
        return dx
    
    def forces_hard_body_remote(self, t, state):
        """Calculate forces for hard body model with remote action"""
        x = state[:self.N]
        v = state[self.N:]
        
        # Ensure positions are within bounds
        x = x % self.L
        
        forces = np.zeros(self.N)
        
        for i in range(self.N):
            # Distance to next pedestrian
            dist = self.distance_to_next(x, i)
            
            # Required length
            d_req = self.required_length(v[i])
            
            # Driving force
            driving_force = (self.v0[i] - v[i]) / self.tau
            
            # Remote repulsive force
            gap = dist - d_req
            if gap > 0.01:  # Small threshold to avoid division by zero
                repulsive_force = self.e / (gap ** self.f)
            else:
                repulsive_force = 100.0  # Large force when too close
            
            # Combined force
            G = driving_force - repulsive_force
            
            # Apply velocity constraint
            if v[i] > 0:
                forces[i] = G
            else:
                forces[i] = max(0, G)
        
        # Return derivatives [dx/dt, dv/dt]
        return np.concatenate([v, forces/self.m])
    
    def simulate(self):
        """Run the simulation using solve_ivp"""
        print(f"Simulating {self.N} pedestrians in {self.L:.1f}m system")
        
        # Initial state
        state0 = np.concatenate([self.x, self.v])
        
        # Relaxation phase
        print("Relaxation phase...")
        sol_relax = solve_ivp(
            self.forces_hard_body_remote, 
            [0, self.t_relax], 
            state0,
            max_step=self.dt,
            rtol=1e-6
        )
        
        if not sol_relax.success:
            print("Warning: Relaxation phase failed")
            return False
        
        # Measurement phase
        print("Measurement phase...")
        state_init = sol_relax.y[:, -1]
        sol_measure = solve_ivp(
            self.forces_hard_body_remote,
            [0, self.t_measure],
            state_init,
            max_step=self.dt,
            rtol=1e-6
        )
        
        if not sol_measure.success:
            print("Warning: Measurement phase failed")
            return False
        
        # Store results
        self.x_history = sol_measure.y[:self.N, :]
        self.v_history = sol_measure.y[self.N:, :]
        self.t_history = sol_measure.t
        
        # Apply periodic boundary conditions
        self.x_history = self.x_history % self.L
        
        print("Simulation completed successfully!")
        return True
    
    def calculate_fundamental_diagram_point(self):
        """Calculate single point for fundamental diagram"""
        if not hasattr(self, 'v_history'):
            print("No simulation data available")
            return None, None, None
        
        # Skip initial transient (first 25% of data)
        skip = len(self.t_history) // 4
        
        # Calculate average velocity
        v_avg = np.mean(self.v_history[:, skip:])
        
        # Calculate density
        density = self.N / self.L
        
        # Calculate flow
        flow = density * v_avg
        
        return density, v_avg, flow

def run_fundamental_diagram_study():
    """Generate fundamental diagram by varying density"""
    print("Generating Fundamental Diagram...")
    print("=" * 50)
    
    densities = []
    velocities = []
    flows = []
    
    # Fixed number of pedestrians, vary system length
    N = 40
    lengths = np.linspace(15, 80, 12)  # Different lengths for different densities
    
    for i, L in enumerate(lengths):
        print(f"\nRun {i+1}/{len(lengths)}: L = {L:.1f}m")
        
        # Create simulator
        sim = PedestrianFlowSimulator(N=N, L=L, model_type='hard_body_remote')
        
        # Run simulation
        success = sim.simulate()
        
        if success:
            # Calculate fundamental diagram point
            density, velocity, flow = sim.calculate_fundamental_diagram_point()
            
            if density is not None:
                densities.append(density)
                velocities.append(velocity)
                flows.append(flow)
                
                print(f"  Density: {density:.3f} ped/m")
                print(f"  Velocity: {velocity:.3f} m/s")
                print(f"  Flow: {flow:.3f} ped/s")
            else:
                print("  Failed to calculate fundamental diagram point")
        else:
            print("  Simulation failed")
    
    return np.array(densities), np.array(velocities), np.array(flows)

def plot_fundamental_diagram(densities, velocities, flows):
    """Create fundamental diagram plots"""
    print("\nCreating fundamental diagram plots...")
    
    # Create figure with subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Sort data by density for better plotting
    sort_idx = np.argsort(densities)
    densities_sorted = densities[sort_idx]
    velocities_sorted = velocities[sort_idx]
    flows_sorted = flows[sort_idx]
    
    # Velocity-density plot
    ax1.plot(densities_sorted, velocities_sorted, 'bo-', markersize=8, linewidth=2, 
             label='Simulation Results', markerfacecolor='lightblue')
    
    # Theoretical curve: v = (1/ρ - a)/(bρ)
    a, b = 0.36, 0.56
    rho_theory = np.linspace(0.3, 3.0, 100)
    v_theory = np.maximum(0, (1/rho_theory - a) / (b * rho_theory))
    
    ax1.plot(rho_theory, v_theory, 'r--', linewidth=2, 
             label=f'Theory: v = (1/ρ - {a})/(ρ·{b})')
    
    ax1.set_xlabel('Density ρ (ped/m)', fontsize=12)
    ax1.set_ylabel('Velocity v (m/s)', fontsize=12)
    ax1.set_title('Velocity-Density Relationship', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.legend(fontsize=10)
    ax1.set_xlim(0, max(densities_sorted) * 1.1)
    ax1.set_ylim(0, max(velocities_sorted) * 1.1)
    
    # Flow-density plot
    ax2.plot(densities_sorted, flows_sorted, 'go-', markersize=8, linewidth=2,
             label='Simulation Results', markerfacecolor='lightgreen')
    
    # Theoretical flow: J = (1 - aρ)/b
    J_theory = np.maximum(0, (1 - a * rho_theory) / b)
    
    ax2.plot(rho_theory, J_theory, 'r--', linewidth=2,
             label=f'Theory: J = (1 - {a}ρ)/{b}')
    
    ax2.set_xlabel('Density ρ (ped/m)', fontsize=12)
    ax2.set_ylabel('Flow J (ped/s)', fontsize=12)
    ax2.set_title('Flow-Density Relationship', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.legend(fontsize=10)
    ax2.set_xlim(0, max(densities_sorted) * 1.1)
    ax2.set_ylim(0, max(flows_sorted) * 1.1)
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/fundamental_diagram.png', dpi=150, bbox_inches='tight')
    print("Fundamental diagram saved as 'fundamental_diagram.png'")
    
    return fig

def compare_models():
    """Compare hard body with and without remote action"""
    print("\nComparing Models...")
    print("=" * 30)
    
    # Test parameters
    N = 30
    L = 20.0
    
    results = {}
    
    for model_type in ['hard_body_remote']:  # Focus on remote action model
        print(f"\nTesting {model_type} model:")
        
        sim = PedestrianFlowSimulator(N=N, L=L, model_type=model_type)
        success = sim.simulate()
        
        if success:
            density, velocity, flow = sim.calculate_fundamental_diagram_point()
            results[model_type] = {
                'density': density,
                'velocity': velocity,
                'flow': flow
            }
            
            print(f"  Density: {density:.3f} ped/m")
            print(f"  Velocity: {velocity:.3f} m/s")
            print(f"  Flow: {flow:.3f} ped/s")
        else:
            print(f"  {model_type} simulation failed")
    
    return results

if __name__ == "__main__":
    print("Pedestrian Flow Simulation")
    print("Based on Seyfried et al. (2006)")
    print("=" * 50)
    
    # Test single simulation
    print("\n1. Testing single simulation...")
    sim = PedestrianFlowSimulator(N=25, L=18.0)
    success = sim.simulate()
    
    if success:
        density, velocity, flow = sim.calculate_fundamental_diagram_point()
        print(f"Single simulation result:")
        print(f"  Density: {density:.3f} ped/m")
        print(f"  Velocity: {velocity:.3f} m/s")
        print(f"  Flow: {flow:.3f} ped/s")
    
    # Generate fundamental diagram
    print("\n2. Generating fundamental diagram...")
    densities, velocities, flows = run_fundamental_diagram_study()
    
    if len(densities) > 0:
        # Create plots
        fig = plot_fundamental_diagram(densities, velocities, flows)
        
        # Save data
        np.savetxt('/home/ubuntu/fundamental_diagram_data.txt', 
                   np.column_stack([densities, velocities, flows]),
                   header='Density(ped/m) Velocity(m/s) Flow(ped/s)',
                   fmt='%.6f')
        print("Data saved as 'fundamental_diagram_data.txt'")
        
        # Print summary statistics
        print(f"\nSummary Statistics:")
        print(f"  Density range: {np.min(densities):.3f} - {np.max(densities):.3f} ped/m")
        print(f"  Velocity range: {np.min(velocities):.3f} - {np.max(velocities):.3f} m/s")
        print(f"  Flow range: {np.min(flows):.3f} - {np.max(flows):.3f} ped/s")
    else:
        print("No successful simulations for fundamental diagram")
    
    print("\nSimulation study completed!")

