"""
Pedestrian Flow Simulation - Implementation of Social Force Model
Based on "Basics of modelling the pedestrian flow" by Seyfried et al.

This implementation includes:
1. Hard bodies without remote action
2. Hard bodies with remote action
3. Velocity-dependent required space
4. Numerical integration algorithms
5. Fundamental diagram generation
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import time

class PedestrianFlowSimulator:
    """
    Simulator for pedestrian flow using modified social force model
    """
    
    def __init__(self, N=50, L=17.3, model_type='hard_body_remote'):
        """
        Initialize the simulator
        
        Parameters:
        N: Number of pedestrians
        L: System length (meters)
        model_type: 'hard_body_remote' or 'hard_body_no_remote'
        """
        self.N = N  # Number of pedestrians
        self.L = L  # System length
        self.model_type = model_type
        
        # Model parameters from the reference
        self.a = 0.36  # Minimum space requirement (m)
        self.b = 0.56  # Velocity dependence factor (s)
        self.tau = 0.61  # Relaxation time (s)
        self.m = 1.0   # Mass (kg) - normalized
        
        # Remote action parameters (for hard_body_remote model)
        self.e = 0.07  # Force magnitude (N)
        self.f = 2.0   # Decay exponent
        
        # Intended speed distribution (Gaussian)
        self.v0_mean = 1.24  # Mean intended speed (m/s)
        self.v0_std = 0.05   # Standard deviation (m/s)
        
        # Numerical parameters
        self.dt = 0.001  # Time step (s)
        self.t_relax = 3000  # Relaxation steps
        self.t_measure = 30000  # Measurement steps
        
        # Initialize pedestrians
        self.initialize_pedestrians()
        
    def initialize_pedestrians(self):
        """Initialize pedestrian positions and velocities"""
        # Random positions with minimum spacing
        self.x = np.sort(np.random.uniform(0, self.L, self.N))
        
        # Ensure minimum spacing
        min_spacing = self.a
        for i in range(1, self.N):
            if self.x[i] - self.x[i-1] < min_spacing:
                self.x[i] = self.x[i-1] + min_spacing
        
        # Wrap around if necessary (periodic boundary)
        self.x = self.x % self.L
        
        # Initialize velocities to zero
        self.v = np.zeros(self.N)
        
        # Assign intended speeds from Gaussian distribution
        self.v0 = np.random.normal(self.v0_mean, self.v0_std, self.N)
        self.v0 = np.maximum(self.v0, 0.1)  # Ensure positive speeds
        
    def required_length(self, v):
        """Calculate velocity-dependent required length"""
        return self.a + self.b * v
    
    def distance(self, xi, xj):
        """Calculate distance with periodic boundary conditions"""
        dx = xj - xi
        # Handle periodic boundary
        if dx > self.L/2:
            dx -= self.L
        elif dx < -self.L/2:
            dx += self.L
        return dx
    
    def forces_hard_body_no_remote(self, state, t):
        """
        Calculate forces for hard body model without remote action
        """
        x = state[:self.N]
        v = state[self.N:]
        
        forces = np.zeros(self.N)
        
        for i in range(self.N):
            # Next pedestrian (with periodic boundary)
            j = (i + 1) % self.N
            
            # Distance to next pedestrian
            dist = self.distance(x[i], x[j])
            
            # Required length for current pedestrian
            d_req = self.required_length(v[i])
            
            if dist > d_req:
                # Free motion - only driving force
                forces[i] = (self.v0[i] - v[i]) / self.tau
            else:
                # Collision - apply impulse
                # This is simplified - in practice would need event detection
                forces[i] = -1000.0  # Large repulsive force
                
        return np.concatenate([v, forces/self.m])
    
    def forces_hard_body_remote(self, state, t):
        """
        Calculate forces for hard body model with remote action
        """
        x = state[:self.N]
        v = state[self.N:]
        
        forces = np.zeros(self.N)
        
        for i in range(self.N):
            # Next pedestrian (with periodic boundary)
            j = (i + 1) % self.N
            
            # Distance to next pedestrian
            dist = self.distance(x[i], x[j])
            
            # Required length for current pedestrian
            d_req = self.required_length(v[i])
            
            # Combined force G(t)
            driving_force = (self.v0[i] - v[i]) / self.tau
            
            # Remote repulsive force
            if dist - d_req > 0:
                repulsive_force = self.e / ((dist - d_req) ** self.f)
            else:
                repulsive_force = 1000.0  # Large force when too close
            
            G = driving_force - repulsive_force
            
            # Apply velocity constraint
            if v[i] > 0:
                forces[i] = G
            else:
                forces[i] = max(0, G)
                
        return np.concatenate([v, forces/self.m])
    
    def simulate(self):
        """Run the simulation"""
        print(f"Starting simulation with {self.N} pedestrians")
        print(f"Model type: {self.model_type}")
        print(f"System length: {self.L} m")
        
        # Choose force function based on model type
        if self.model_type == 'hard_body_remote':
            force_func = self.forces_hard_body_remote
        else:
            force_func = self.forces_hard_body_no_remote
        
        # Initial state
        state0 = np.concatenate([self.x, self.v])
        
        # Time arrays
        t_relax_array = np.arange(0, self.t_relax * self.dt, self.dt)
        t_measure_array = np.arange(0, self.t_measure * self.dt, self.dt)
        
        print("Relaxation phase...")
        # Relaxation phase
        sol_relax = odeint(force_func, state0, t_relax_array)
        
        # Use final state from relaxation as initial state for measurement
        state_final_relax = sol_relax[-1]
        
        print("Measurement phase...")
        # Measurement phase
        sol_measure = odeint(force_func, state_final_relax, t_measure_array)
        
        # Extract positions and velocities
        self.x_history = sol_measure[:, :self.N]
        self.v_history = sol_measure[:, self.N:]
        self.t_history = t_measure_array
        
        # Apply periodic boundary conditions to positions
        self.x_history = self.x_history % self.L
        
        print("Simulation completed!")
        
    def calculate_fundamental_diagram(self):
        """Calculate velocity-density relationship"""
        # Skip initial transient
        skip = len(self.t_history) // 4
        
        # Calculate average velocity over time
        v_avg = np.mean(self.v_history[skip:])
        
        # Calculate density
        density = self.N / self.L
        
        # Calculate flow
        flow = density * v_avg
        
        return density, v_avg, flow
    
    def plot_trajectories(self, max_time=10.0):
        """Plot space-time trajectories"""
        plt.figure(figsize=(12, 8))
        
        # Limit time for visualization
        time_mask = self.t_history <= max_time
        t_plot = self.t_history[time_mask]
        x_plot = self.x_history[time_mask]
        
        # Plot trajectories for subset of pedestrians
        step = max(1, self.N // 10)  # Show at most 10 trajectories
        for i in range(0, self.N, step):
            plt.plot(t_plot, x_plot[:, i], alpha=0.7, linewidth=1)
        
        plt.xlabel('Time (s)')
        plt.ylabel('Position (m)')
        plt.title(f'Pedestrian Trajectories - {self.model_type}')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(f'/home/ubuntu/trajectories_{self.model_type}.png', dpi=150)
        plt.show()
    
    def plot_velocity_time_series(self):
        """Plot velocity time series"""
        plt.figure(figsize=(12, 6))
        
        # Calculate average velocity over all pedestrians
        v_avg_time = np.mean(self.v_history, axis=1)
        
        plt.plot(self.t_history, v_avg_time, 'b-', linewidth=2)
        plt.xlabel('Time (s)')
        plt.ylabel('Average Velocity (m/s)')
        plt.title(f'Average Velocity vs Time - {self.model_type}')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(f'/home/ubuntu/velocity_time_{self.model_type}.png', dpi=150)
        plt.show()

def run_density_sweep():
    """Run simulations for different densities to generate fundamental diagram"""
    densities = []
    velocities = []
    flows = []
    
    # Different system lengths to achieve different densities
    N = 50
    lengths = np.linspace(15, 100, 10)
    
    for L in lengths:
        print(f"\nRunning simulation with L = {L:.1f} m")
        
        # Create and run simulator
        sim = PedestrianFlowSimulator(N=N, L=L, model_type='hard_body_remote')
        sim.simulate()
        
        # Calculate fundamental diagram point
        density, velocity, flow = sim.calculate_fundamental_diagram()
        
        densities.append(density)
        velocities.append(velocity)
        flows.append(flow)
        
        print(f"Density: {density:.3f} ped/m, Velocity: {velocity:.3f} m/s, Flow: {flow:.3f} ped/s")
    
    return np.array(densities), np.array(velocities), np.array(flows)

def plot_fundamental_diagram(densities, velocities, flows):
    """Plot fundamental diagram"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Velocity-density plot
    ax1.plot(densities, velocities, 'bo-', markersize=8, linewidth=2, label='Simulation')
    
    # Theoretical curve from d = a + bv
    a, b = 0.36, 0.56
    rho_theory = np.linspace(0.5, 2.5, 100)
    v_theory = (1/rho_theory - a) / (b * rho_theory)
    v_theory = np.maximum(v_theory, 0)  # Ensure non-negative
    
    ax1.plot(rho_theory, v_theory, 'r--', linewidth=2, label='Theory: v = (1/ρ - a)/(bρ)')
    ax1.set_xlabel('Density (ped/m)')
    ax1.set_ylabel('Velocity (m/s)')
    ax1.set_title('Velocity-Density Relationship')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # Flow-density plot
    ax2.plot(densities, flows, 'go-', markersize=8, linewidth=2, label='Simulation')
    
    # Theoretical flow
    J_theory = (1 - a * rho_theory) / b
    J_theory = np.maximum(J_theory, 0)
    
    ax2.plot(rho_theory, J_theory, 'r--', linewidth=2, label='Theory: J = (1 - aρ)/b')
    ax2.set_xlabel('Density (ped/m)')
    ax2.set_ylabel('Flow (ped/s)')
    ax2.set_title('Flow-Density Relationship')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/fundamental_diagram.png', dpi=150)
    plt.show()

if __name__ == "__main__":
    # Test single simulation
    print("Testing single simulation...")
    sim = PedestrianFlowSimulator(N=30, L=20.0, model_type='hard_body_remote')
    sim.simulate()
    
    # Plot results
    sim.plot_trajectories(max_time=5.0)
    sim.plot_velocity_time_series()
    
    # Calculate fundamental diagram point
    density, velocity, flow = sim.calculate_fundamental_diagram()
    print(f"\nFundamental diagram point:")
    print(f"Density: {density:.3f} ped/m")
    print(f"Velocity: {velocity:.3f} m/s") 
    print(f"Flow: {flow:.3f} ped/s")

