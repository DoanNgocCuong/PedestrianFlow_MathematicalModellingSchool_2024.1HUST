"""
Pedestrian Flow Simulator - Modified Social Force Model
Based on: Seyfried, A., Steffen, B., Lippert, T. (2006)
"Basics of modelling the pedestrian flow", Physica A 368:232-238

This implementation includes:
1. Hard bodies without remote action (Equation 5)
2. Hard bodies with remote action (Equation 6)
3. Velocity-dependent space requirements d = a + b*v
4. Simulation framework with periodic boundary conditions
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, List, Optional
import time

class PedestrianSimulator:
    """
    Modified Social Force Model for one-dimensional pedestrian flow
    """
    
    def __init__(self, 
                 L: float = 17.3,           # System length (m)
                 dt: float = 0.001,         # Time step (s)
                 tau: float = 0.61,         # Relaxation time (s)
                 a: float = 0.36,           # Minimum required length (m)
                 b: float = 0.56,           # Velocity dependence parameter (s)
                 v0_mean: float = 1.24,     # Mean intended speed (m/s)
                 v0_std: float = 0.05,      # Std of intended speed (m/s)
                 use_remote_force: bool = False,  # Use remote force interaction
                 e: float = 0.07,           # Remote force parameter (N)
                 f: float = 2.0):           # Remote force parameter
        
        self.L = L
        self.dt = dt
        self.tau = tau
        self.a = a
        self.b = b
        self.v0_mean = v0_mean
        self.v0_std = v0_std
        self.use_remote_force = use_remote_force
        self.e = e
        self.f = f
        
        # Simulation state
        self.positions = None
        self.velocities = None
        self.intended_speeds = None
        self.N = 0
        
    def initialize_system(self, density: float) -> None:
        """
        Initialize pedestrian positions and velocities
        
        Args:
            density: Pedestrian density (pedestrians/m)
        """
        self.N = int(density * self.L)
        if self.N < 2:
            self.N = 2
            
        # Initialize intended speeds from normal distribution
        self.intended_speeds = np.random.normal(self.v0_mean, self.v0_std, self.N)
        self.intended_speeds = np.maximum(self.intended_speeds, 0.1)  # Minimum speed
        
        # Initialize velocities to zero
        self.velocities = np.zeros(self.N)
        
        # Initialize positions randomly with minimum separation
        self.positions = np.zeros(self.N)
        for i in range(self.N):
            placed = False
            attempts = 0
            while not placed and attempts < 1000:
                pos = np.random.uniform(0, self.L)
                if i == 0:
                    self.positions[i] = pos
                    placed = True
                else:
                    # Check minimum distance to all other pedestrians
                    min_dist = float('inf')
                    for j in range(i):
                        dist = min(abs(pos - self.positions[j]), 
                                 self.L - abs(pos - self.positions[j]))
                        min_dist = min(min_dist, dist)
                    
                    if min_dist >= self.a:
                        self.positions[i] = pos
                        placed = True
                attempts += 1
            
            if not placed:
                # Fallback: place uniformly
                self.positions[i] = i * self.L / self.N
        
        # Sort positions to maintain order
        sorted_indices = np.argsort(self.positions)
        self.positions = self.positions[sorted_indices]
        self.intended_speeds = self.intended_speeds[sorted_indices]
        
    def get_required_length(self, velocity: float) -> float:
        """
        Calculate velocity-dependent required length
        d = a + b * v
        """
        return self.a + self.b * velocity
    
    def get_distance(self, pos1: float, pos2: float) -> float:
        """
        Calculate minimum distance considering periodic boundaries
        """
        direct_dist = abs(pos2 - pos1)
        periodic_dist = self.L - direct_dist
        return min(direct_dist, periodic_dist)
    
    def get_front_neighbor(self, i: int) -> int:
        """
        Get index of pedestrian in front considering periodic boundaries
        """
        return (i + 1) % self.N
    
    def calculate_forces_hard_body(self) -> np.ndarray:
        """
        Calculate forces for hard body model without remote action (Equation 5)
        """
        forces = np.zeros(self.N)
        
        for i in range(self.N):
            j = self.get_front_neighbor(i)
            
            # Calculate distance to front neighbor
            if j > i:
                distance = self.positions[j] - self.positions[i]
            else:  # Periodic boundary case
                distance = (self.positions[j] + self.L) - self.positions[i]
            
            required_length = self.get_required_length(self.velocities[i])
            
            if distance > required_length:
                # Driving force only
                forces[i] = (self.intended_speeds[i] - self.velocities[i]) / self.tau
            else:
                # Stop (set velocity to zero in update step)
                forces[i] = -self.velocities[i] / self.dt
                
        return forces
    
    def calculate_forces_remote_action(self) -> np.ndarray:
        """
        Calculate forces for hard body model with remote action (Equation 6)
        """
        forces = np.zeros(self.N)
        
        for i in range(self.N):
            j = self.get_front_neighbor(i)
            
            # Calculate distance to front neighbor
            if j > i:
                distance = self.positions[j] - self.positions[i]
            else:  # Periodic boundary case
                distance = (self.positions[j] + self.L) - self.positions[i]
            
            required_length = self.get_required_length(self.velocities[i])
            
            # Calculate G_i(t)
            driving_term = (self.intended_speeds[i] - self.velocities[i]) / self.tau
            
            if distance - required_length > 0:
                repulsive_term = self.e * self.f / (distance - required_length)
            else:
                repulsive_term = self.e * self.f / 0.001  # Large repulsive force
            
            G_i = driving_term - repulsive_term
            
            # Apply force based on current velocity
            if self.velocities[i] > 0:
                forces[i] = G_i
            else:
                forces[i] = max(0, G_i)
                
        return forces
    
    def update_step(self) -> None:
        """
        Perform one simulation time step
        """
        if self.use_remote_force:
            forces = self.calculate_forces_remote_action()
        else:
            forces = self.calculate_forces_hard_body()
        
        # Store old positions for constraint checking
        old_positions = self.positions.copy()
        old_velocities = self.velocities.copy()
        
        # Update velocities and positions
        new_velocities = self.velocities + forces * self.dt
        new_positions = self.positions + new_velocities * self.dt
        
        # Handle periodic boundaries
        new_positions = new_positions % self.L
        
        # For hard body without remote action, check constraints
        if not self.use_remote_force:
            self._check_and_correct_constraints(new_positions, new_velocities)
        else:
            # Ensure non-negative velocities
            new_velocities = np.maximum(new_velocities, 0)
            # Ensure velocities don't exceed intended speeds
            new_velocities = np.minimum(new_velocities, self.intended_speeds)
            
            self.velocities = new_velocities
            self.positions = new_positions
    
    def _check_and_correct_constraints(self, new_positions: np.ndarray, 
                                     new_velocities: np.ndarray) -> None:
        """
        Check and correct constraint violations for hard body model
        """
        corrected_positions = new_positions.copy()
        corrected_velocities = new_velocities.copy()
        
        # Check each pedestrian
        for i in range(self.N):
            j = self.get_front_neighbor(i)
            
            # Calculate distance after update
            if j > i:
                distance = corrected_positions[j] - corrected_positions[i]
                if distance < 0:  # Wrapped around
                    distance += self.L
            else:  # Periodic boundary case
                distance = (corrected_positions[j] + self.L) - corrected_positions[i]
            
            required_length = self.get_required_length(corrected_velocities[i])
            
            if distance <= required_length:
                # Constraint violation - stop pedestrian
                corrected_velocities[i] = 0
                corrected_positions[i] = self.positions[i]  # Reset to old position
        
        # Ensure non-negative velocities and speed limits
        corrected_velocities = np.maximum(corrected_velocities, 0)
        corrected_velocities = np.minimum(corrected_velocities, self.intended_speeds)
        
        self.velocities = corrected_velocities
        self.positions = corrected_positions
    
    def run_simulation(self, density: float, 
                      relaxation_steps: int = 300000,
                      measurement_steps: int = 300000) -> Tuple[float, float]:
        """
        Run complete simulation for given density
        
        Returns:
            (mean_velocity, density)
        """
        self.initialize_system(density)
        
        # Relaxation phase
        for step in range(relaxation_steps):
            self.update_step()
            
            # Progress indicator for long simulations
            if step % 50000 == 0:
                print(f"Relaxation: {step}/{relaxation_steps}")
        
        # Measurement phase
        velocity_sum = 0.0
        for step in range(measurement_steps):
            self.update_step()
            velocity_sum += np.mean(self.velocities)
            
            if step % 50000 == 0:
                print(f"Measurement: {step}/{measurement_steps}")
        
        mean_velocity = velocity_sum / measurement_steps
        actual_density = self.N / self.L
        
        return mean_velocity, actual_density

def run_fundamental_diagram_study(b_values: List[float], 
                                densities: np.ndarray,
                                use_remote_force: bool = False,
                                e: float = 0.07,
                                f: float = 2.0) -> dict:
    """
    Run fundamental diagram study for different b values
    """
    results = {}
    
    for b in b_values:
        print(f"\nRunning simulations for b = {b}")
        velocities = []
        actual_densities = []
        
        simulator = PedestrianSimulator(
            b=b, 
            use_remote_force=use_remote_force,
            e=e, 
            f=f
        )
        
        for density in densities:
            print(f"  Density: {density:.2f} ped/m")
            mean_vel, actual_dens = simulator.run_simulation(
                density, 
                relaxation_steps=30000,  # Reduced for faster testing
                measurement_steps=30000
            )
            velocities.append(mean_vel)
            actual_densities.append(actual_dens)
            print(f"    Mean velocity: {mean_vel:.3f} m/s")
        
        results[b] = {
            'densities': np.array(actual_densities),
            'velocities': np.array(velocities)
        }
    
    return results

if __name__ == "__main__":
    print("Pedestrian Flow Simulator - Modified Social Force Model")
    print("=" * 60)
    
    # Test basic functionality
    print("\nTesting basic simulation...")
    simulator = PedestrianSimulator(b=0.56, use_remote_force=False)
    mean_vel, density = simulator.run_simulation(
        density=1.0, 
        relaxation_steps=1000, 
        measurement_steps=1000
    )
    print(f"Test result: density={density:.2f}, mean_velocity={mean_vel:.3f}")
    
    print("\nSimulator implementation complete!")

