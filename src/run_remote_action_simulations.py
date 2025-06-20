"""
Run simulations for hard bodies with remote action
Reproduces Figure 2 from the paper: Comparison of remote action effects
"""

import numpy as np
import matplotlib.pyplot as plt
from pedestrian_simulator import PedestrianSimulator, run_fundamental_diagram_study
import pickle
import time

def run_remote_action_simulations():
    """
    Run simulations for hard bodies with remote action
    Tests the effect of remote forces as in Figure 2
    """
    print("Running Hard Body Simulations (With Remote Action)")
    print("=" * 60)
    
    # Parameters from the paper
    densities = np.linspace(0.2, 3.0, 15)  # Density range (ped/m)
    
    print(f"Density range: {densities[0]:.1f} to {densities[-1]:.1f} ped/m")
    print(f"Number of density points: {len(densities)}")
    print("Remote force parameters: e = 0.07 N, f = 2.0")
    
    # Test cases for Figure 2:
    # 1. Without remote action, b = 0.56 (reference)
    # 2. With remote action, b = 0 (shows effect of remote force alone)
    # 3. With remote action, b = 0.56 (combined effect)
    
    results = {}
    
    # Case 1: Without remote action, b = 0.56 (reference from previous simulation)
    print("\nCase 1: Without remote action, b = 0.56 (reference)")
    start_time = time.time()
    results_no_remote = run_fundamental_diagram_study(
        b_values=[0.56],
        densities=densities,
        use_remote_force=False
    )
    results['no_remote_b056'] = results_no_remote[0.56]
    print(f"Completed in {time.time() - start_time:.1f} seconds")
    
    # Case 2: With remote action, b = 0
    print("\nCase 2: With remote action, b = 0")
    start_time = time.time()
    results_remote_b0 = run_fundamental_diagram_study(
        b_values=[0.0],
        densities=densities,
        use_remote_force=True,
        e=0.07,
        f=2.0
    )
    results['remote_b000'] = results_remote_b0[0.0]
    print(f"Completed in {time.time() - start_time:.1f} seconds")
    
    # Case 3: With remote action, b = 0.56
    print("\nCase 3: With remote action, b = 0.56")
    start_time = time.time()
    results_remote_b056 = run_fundamental_diagram_study(
        b_values=[0.56],
        densities=densities,
        use_remote_force=True,
        e=0.07,
        f=2.0
    )
    results['remote_b056'] = results_remote_b056[0.56]
    print(f"Completed in {time.time() - start_time:.1f} seconds")
    
    # Save results
    with open('/home/ubuntu/remote_action_results.pkl', 'wb') as f:
        pickle.dump(results, f)
    
    print("\nResults saved to remote_action_results.pkl")
    
    # Print summary
    print("\nSummary of Results:")
    print("-" * 50)
    for case, data in results.items():
        max_vel = np.max(data['velocities'])
        min_vel = np.min(data['velocities'])
        print(f"{case:20}: velocity range {min_vel:.3f} - {max_vel:.3f} m/s")
    
    return results

def plot_remote_action_results(results):
    """
    Create plots similar to Figure 2 in the paper
    """
    plt.figure(figsize=(10, 8))
    
    # Plot the three cases
    cases = [
        ('no_remote_b056', 'without remote action, b=0.56', 'blue', 'o'),
        ('remote_b000', 'with remote action, b=0', 'red', 's'),
        ('remote_b056', 'with remote action, b=0.56', 'green', '^')
    ]
    
    for case_key, label, color, marker in cases:
        if case_key in results:
            data = results[case_key]
            plt.plot(data['densities'], data['velocities'], 
                    color=color, marker=marker, markersize=6,
                    linestyle='-', linewidth=1.5, label=label)
    
    plt.xlabel('Density ρ [1/m]', fontsize=12)
    plt.ylabel('Velocity v [m/s]', fontsize=12)
    plt.title('Velocity-Density Relation: Effect of Remote Action', fontsize=14)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.xlim(0, 3.0)
    plt.ylim(0, 1.4)
    
    # Add text annotation
    plt.text(0.5, 1.2, 'a = 0.36 m, e = 0.07 N, f = 2', fontsize=10, 
             bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray"))
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/figure2_remote_action_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("Plot saved as figure2_remote_action_comparison.png")

def analyze_density_waves(results):
    """
    Analyze if density waves appear in the remote action case with b=0
    """
    print("\nAnalyzing density wave formation...")
    
    if 'remote_b000' in results:
        data = results['remote_b000']
        densities = data['densities']
        velocities = data['velocities']
        
        # Look for gaps or discontinuities in the velocity-density relation
        velocity_diffs = np.diff(velocities)
        large_jumps = np.where(np.abs(velocity_diffs) > 0.05)[0]
        
        if len(large_jumps) > 0:
            print(f"Potential velocity gaps detected at densities:")
            for idx in large_jumps:
                print(f"  ρ ≈ {densities[idx]:.2f} - {densities[idx+1]:.2f} ped/m")
                print(f"  Velocity jump: {velocities[idx]:.3f} → {velocities[idx+1]:.3f} m/s")
        else:
            print("No significant velocity gaps detected in this simulation.")
    
    print("Note: Density waves may require longer simulations or specific conditions to manifest clearly.")

if __name__ == "__main__":
    # Run the simulations
    results = run_remote_action_simulations()
    
    # Create plots
    plot_remote_action_results(results)
    
    # Analyze density waves
    analyze_density_waves(results)
    
    print("\nRemote action simulations completed!")
    print("This reproduces the data for Figure 2 in the paper.")

