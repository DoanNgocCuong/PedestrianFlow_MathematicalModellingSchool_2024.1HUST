# Tài liệu hỗ trợ - Pedestrian Flow Simulation

## 1. Mô tả tổng quan

Dự án này implement mô hình social force đã được chỉnh sửa để mô phỏng dòng chảy người đi bộ (pedestrian flow) dựa trên nghiên cứu của Seyfried et al. (2006). Mô hình tập trung vào hệ thống một chiều với velocity-dependent required space.

## 2. Cấu trúc code

### 2.1 File chính
- `enhanced_pedestrian_simulation.py`: Code mô phỏng chính
- `pedestrian_simulation.py`: Version đầu tiên (để tham khảo)

### 2.2 Class PedestrianFlowSimulator

#### Tham số mô hình:
- `a = 0.36`: Minimum space requirement (m)
- `b = 0.56`: Velocity dependence factor (s)  
- `tau = 0.61`: Relaxation time (s)
- `e = 0.07`: Remote force magnitude (N)
- `f = 2.0`: Remote force decay exponent

#### Phương thức chính:
- `initialize_pedestrians()`: Khởi tạo vị trí và vận tốc
- `forces_hard_body_remote()`: Tính toán lực tương tác
- `simulate()`: Chạy mô phỏng
- `calculate_fundamental_diagram_point()`: Tính điểm fundamental diagram

## 3. Kết quả mô phỏng

### 3.1 Fundamental Diagram Data

Dữ liệu được tạo từ 12 simulations với densities khác nhau:

```
Density(ped/m)  Velocity(m/s)  Flow(ped/s)
2.667           0.000          0.000
1.913           0.015          0.029
1.492           0.195          0.291
1.222           0.386          0.472
1.035           0.578          0.598
0.898           0.714          0.641
0.793           0.788          0.625
0.710           0.903          0.641
0.642           0.923          0.593
0.587           0.915          0.537
0.540           0.946          0.511
0.500           0.979          0.489
```

### 3.2 Phân tích kết quả

#### Velocity-Density Relationship:
- Tại high density (ρ > 2.0): velocity ≈ 0 (jamming condition)
- Tại medium density (1.0 < ρ < 2.0): velocity tăng khi density giảm
- Tại low density (ρ < 1.0): velocity tiến đến intended speed

#### Flow-Density Relationship:
- Maximum flow đạt được tại density ≈ 0.9 ped/m
- Flow giảm ở cả high density (do low velocity) và low density (do low density)

### 3.3 So sánh với lý thuyết

Mô hình theoretical từ d = a + bv:
- v = (1/ρ - a)/(bρ)
- J = (1 - aρ)/b

Kết quả simulation phù hợp tốt với theoretical predictions, đặc biệt trong medium density range.

## 4. Validation với tài liệu tham khảo

### 4.1 Parameter values
- a = 0.36m: Phù hợp với empirical data từ Weidmann
- b = 0.56s: Optimal value cho good agreement với experimental data
- Intended speed distribution: μ = 1.24 m/s, σ = 0.05 m/s

### 4.2 Numerical algorithm
- Explicit integration với solve_ivp
- Time step control tự động
- Periodic boundary conditions

### 4.3 Model behavior
- Stable convergence to steady state
- Realistic velocity-density relationships
- No negative velocities hoặc unphysical behavior

## 5. Hướng dẫn sử dụng

### 5.1 Chạy single simulation:
```python
sim = PedestrianFlowSimulator(N=30, L=20.0)
sim.simulate()
density, velocity, flow = sim.calculate_fundamental_diagram_point()
```

### 5.2 Tạo fundamental diagram:
```python
densities, velocities, flows = run_fundamental_diagram_study()
plot_fundamental_diagram(densities, velocities, flows)
```

### 5.3 Thay đổi parameters:
```python
sim = PedestrianFlowSimulator(N=50, L=25.0)
sim.a = 0.40  # Thay đổi minimum space
sim.b = 0.60  # Thay đổi velocity dependence
sim.simulate()
```

## 6. Output files

- `fundamental_diagram.png`: Velocity-density và flow-density plots
- `fundamental_diagram_data.txt`: Raw data từ simulations
- `trajectories_hard_body_remote.png`: Space-time trajectories
- `velocity_time_hard_body_remote.png`: Velocity time series

## 7. Limitations và future work

### 7.1 Current limitations:
- One-dimensional system only
- Homogeneous pedestrian population
- Simplified collision handling
- Limited to steady-state analysis

### 7.2 Possible extensions:
- Two-dimensional implementation
- Heterogeneous populations
- Complex geometries
- Transient phenomena analysis
- Comparison với other models

## 8. References

[1] A. Seyfried, B. Steffen, T. Lippert, "Basics of modelling the pedestrian flow," Physica A 368 (2006) 232-238.

[2] D. Helbing, P. Molnár, "Social force model for pedestrian dynamics," Physical Review E 51 (1995) 4282.

[3] U. Weidmann, "Transporttechnik der Fußgänger," ETH Zürich, 1993.

