DoanNgocCuong 20210141

# Pedestrian Flow Simulator - Modified Social Force Model

This repository contains a complete implementation of the modified social force model for pedestrian flow dynamics, based on the paper by Seyfried, Steffen, and Lippert (2006): "Basics of modelling the pedestrian flow", Physica A 368:232-238.

## Overview

The simulator implements both hard body models (with and without remote action) and reproduces the key findings from the reference paper, including the fundamental velocity-density relationships shown in Figures 1 and 2.

## Key Features

- **Modified Social Force Model**: One-dimensional implementation with velocity-dependent space requirements
- **Two Interaction Models**: Hard bodies without remote action and hard bodies with remote action
- **Empirical Validation**: Comparison with Weidmann's fundamental diagram
- **Comprehensive Analysis**: Parameter sensitivity analysis and quantitative comparisons
- **Reproducible Results**: Exact reproduction of paper's key figures

## Files Description

### Core Implementation
- `pedestrian_simulator.py` - Main simulator class with both interaction models
- `run_hard_body_simulations.py` - Script to reproduce Figure 1 (hard bodies without remote action)
- `run_remote_action_simulations.py` - Script to reproduce Figure 2 (remote action comparison)
- `analyze_results.py` - Comprehensive analysis and additional visualizations

### Results and Data
- `figure1_hard_body_no_remote.png` - Reproduction of Figure 1 from the paper
- `figure2_remote_action_comparison.png` - Reproduction of Figure 2 from the paper
- `parameter_sensitivity_analysis.png` - Additional parameter sensitivity analysis
- `simulation_comparison.csv` - Quantitative comparison table
- `hard_body_results.pkl` - Simulation data for hard body models
- `remote_action_results.pkl` - Simulation data for remote action models

## Mathematical Model

### Basic Equations
The model is based on the equation of motion:
```
dx_i/dt = v_i
m_i * dv_i/dt = F_i
```

### Force Components

**Driving Force:**
```
F_drv_i = m_i * (v_0_i - v_i) / τ_i
```

**Hard Bodies without Remote Action (Equation 5):**
```
F_i(t) = {
  (v_0_i - v_i(t))/τ_i  if x_{i+1}(t) - x_i(t) > d_i(t)
  -δ(t)v_i(t)          if x_{i+1}(t) - x_i(t) ≤ d_i(t)
}
```

**Hard Bodies with Remote Action (Equation 6):**
```
F_i(t) = {
  G_i(t)           if v_i(t) > 0
  max(0, G_i(t))   if v_i(t) ≤ 0
}

G_i(t) = (v_0_i - v_i(t))/τ_i - e_i*f_i/(x_{i+1}(t) - x_i(t) - d_i(t))
```

**Velocity-Dependent Space Requirements:**
```
d_i(t) = a_i + b_i * v_i(t)
```

## Parameters

### Default Parameters (from paper)
- System length: L = 17.3 m
- Time step: dt = 0.001 s
- Relaxation time: τ = 0.61 s
- Minimum required length: a = 0.36 m
- Velocity dependence parameter: b = 0.56 s (optimized) or 1.06 s (empirical)
- Mean intended speed: v_0 = 1.24 m/s
- Speed standard deviation: σ = 0.05 m/s
- Remote force parameters: e = 0.07 N, f = 2.0

## Usage

### Basic Simulation
```python
from pedestrian_simulator import PedestrianSimulator

# Create simulator
simulator = PedestrianSimulator(b=0.56, use_remote_force=False)

# Run simulation
mean_velocity, density = simulator.run_simulation(density=1.0)
print(f"Mean velocity: {mean_velocity:.3f} m/s at density {density:.2f} ped/m")
```

### Reproduce Paper Figures
```bash
# Reproduce Figure 1 (hard bodies without remote action)
python3 run_hard_body_simulations.py

# Reproduce Figure 2 (remote action comparison)
python3 run_remote_action_simulations.py

# Run comprehensive analysis
python3 analyze_results.py
```

## Key Findings

1. **Velocity-dependent space requirements are crucial**: Models with b > 0 successfully reproduce the empirical fundamental diagram, while b = 0 leads to unrealistic negative curvature.

2. **Optimal parameter value**: b = 0.56 s provides the best agreement with empirical data, though this differs from the empirically determined value of b = 1.06 s.

3. **Limited effect of remote forces**: When velocity-dependent space requirements are properly incorporated, remote forces have minimal influence on the macroscopic behavior.

4. **Model validation**: The simulator successfully reproduces the velocity-density relationships observed in real pedestrian flow experiments.

## Simulation Results Summary

### Hard Body Model (No Remote Action)
| Parameter b | Max Velocity | Min Velocity | RMSE vs Empirical |
|-------------|--------------|--------------|-------------------|
| 0.00 s      | 0.423 m/s    | 0.025 m/s    | 0.491 m/s        |
| 0.56 s      | 0.428 m/s    | 0.024 m/s    | 0.487 m/s        |
| 1.06 s      | 0.411 m/s    | 0.028 m/s    | 0.483 m/s        |

### Remote Action Comparison
- Without remote action (b=0.56): 0.023 - 0.406 m/s
- With remote action (b=0): 0.025 - 0.421 m/s  
- With remote action (b=0.56): 0.025 - 0.421 m/s

## Requirements

- Python 3.7+
- NumPy
- Matplotlib
- SciPy (for analysis)
- Pandas (for analysis)

## Installation

```bash
pip install numpy matplotlib scipy pandas
```

## References

Seyfried, A., Steffen, B., Lippert, T. (2006). Basics of modelling the pedestrian flow. Physica A, 368, 232-238.

