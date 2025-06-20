"""
Run simulations for hard bodies without remote action
Reproduces Figure 1 from the paper: Velocity-density relation for different b values
"""

import numpy as np
import matplotlib.pyplot as plt
from pedestrian_simulator import PedestrianSimulator, run_fundamental_diagram_study
import pickle
import time

def run_hard_body_simulations():
    """
    Run simulations for hard bodies without remote action
    Tests different values of b parameter as in Figure 1
    """
    print("Running Hard Body Simulations (No Remote Action)")
    print("=" * 60)
    
    # Parameters from the paper
    b_values = [0.0, 0.56, 1.06]  # Different velocity dependence parameters
    densities = np.linspace(0.2, 3.0, 15)  # Density range (ped/m)
    
    print(f"Testing b values: {b_values}")
    print(f"Density range: {densities[0]:.1f} to {densities[-1]:.1f} ped/m")
    print(f"Number of density points: {len(densities)}")
    
    # Run simulations
    start_time = time.time()
    results = run_fundamental_diagram_study(
        b_values=b_values,
        densities=densities,
        use_remote_force=False  # Hard bodies without remote action
    )
    end_time = time.time()
    
    print(f"\nSimulations completed in {end_time - start_time:.1f} seconds")
    
    # Save results
    with open('/home/ubuntu/hard_body_results.pkl', 'wb') as f:
        pickle.dump(results, f)
    
    print("Results saved to hard_body_results.pkl")
    
    # Print summary
    print("\nSummary of Results:")
    print("-" * 40)
    for b in b_values:
        data = results[b]
        max_vel = np.max(data['velocities'])
        min_vel = np.min(data['velocities'])
        print(f"b = {b:4.2f}: velocity range {min_vel:.3f} - {max_vel:.3f} m/s")
    
    return results

def create_empirical_data():
    """
    Create approximate empirical data based on Weidmann's fundamental diagram
    This is a rough approximation for comparison purposes
    """
    densities = np.linspace(0.2, 3.0, 20)
    
    # Approximate Weidmann's fundamental diagram
    # v = v_free * (1 - rho/rho_max)^n where v_free ≈ 1.34 m/s, rho_max ≈ 5.4 ped/m²
    # For 1D: convert to linear density
    v_free = 1.34
    rho_max_2d = 5.4  # ped/m²
    rho_max_1d = 2.8  # Approximate conversion to ped/m
    n = 1.5
    
    velocities = []
    for rho in densities:
        if rho < rho_max_1d:
            v = v_free * (1 - rho/rho_max_1d)**n
        else:
            v = 0.1  # Minimum velocity
        velocities.append(max(v, 0.1))
    
    return np.array(densities), np.array(velocities)

def plot_results(results):
    """
    Create plots similar to Figure 1 in the paper
    """
    plt.figure(figsize=(10, 8))
    
    # Get empirical data for comparison
    emp_densities, emp_velocities = create_empirical_data()
    
    # Plot empirical data
    plt.plot(emp_densities, emp_velocities, 'k-', linewidth=2, 
             label='Empirical (Weidmann)', alpha=0.7)
    
    # Plot simulation results
    colors = ['red', 'blue', 'green']
    markers = ['s', 'o', '^']
    
    for i, b in enumerate([0.0, 0.56, 1.06]):
        if b in results:
            data = results[b]
            plt.plot(data['densities'], data['velocities'], 
                    color=colors[i], marker=markers[i], markersize=6,
                    linestyle='-', linewidth=1.5,
                    label=f'b = {b:.2f} s')
    
    plt.xlabel('Density ρ [1/m]', fontsize=12)
    plt.ylabel('Velocity v [m/s]', fontsize=12)
    plt.title('Velocity-Density Relation for Hard Bodies (No Remote Action)', fontsize=14)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.xlim(0, 3.0)
    plt.ylim(0, 1.4)
    
    # Add text annotation
    plt.text(0.5, 1.2, 'Hard bodies with a = 0.36 m', fontsize=10, 
             bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray"))
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/figure1_hard_body_no_remote.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("Plot saved as figure1_hard_body_no_remote.png")

if __name__ == "__main__":
    # Run the simulations
    results = run_hard_body_simulations()
    
    # Create plots
    plot_results(results)
    
    print("\nHard body simulations (no remote action) completed!")
    print("This reproduces the data for Figure 1 in the paper.")

