# Phân tích chi tiết mô hình toán học và thuật toán

## 1. Mô hình Social Force - Phân tích toán học chi tiết

### 1.1 Phương trình chuyển động cơ bản

**Phương trình (1) - Equation of Motion:**
```
dxi/dt = vi
mi(dvi/dt) = Fi = Σ Fij(xi, xj, vi)
```

Đây là hệ phương trình vi phân thường (ODE) bậc hai mô tả chuyển động của người đi bộ i:
- xi(t): vị trí của người đi bộ i tại thời điểm t
- vi(t): vận tốc của người đi bộ i tại thời điểm t  
- mi: khối lượng của người đi bộ i
- Fi: tổng lực tác động lên người đi bộ i
- Σ Fij: tổng các lực tương tác với người đi bộ khác

### 1.2 Phân tích các thành phần lực

**Driving Force (Phương trình 2):**
```
Fi^drv = mi(vi^0 - vi)/τi
```

Phân tích:
- vi^0: intended speed (tốc độ mong muốn)
- τi: relaxation time (thời gian thích ứng)
- Lực này đưa người đi bộ về tốc độ mong muốn
- Đây là lực damping tuyến tính với hệ số damping mi/τi

**Repulsive Force (Phương trình 3):**
```
Fi^rep = Σ -∇xi U(||xi - xj|| - dij)^-β
```

Phân tích:
- U: potential function
- ||xi - xj||: khoảng cách Euclidean giữa người i và j
- dij: hard core diameter (kích thước vật lý)
- β: exponent parameter (thường β > 0)
- Gradient âm tạo lực đẩy

### 1.3 Velocity-Density Relation

**Phương trình (4) - Linear relationship:**
```
d = a + bv
với a = 0.36m, b = 1.06s (hoặc b = 0.56s)
```

Phân tích toán học:
- d: required length (độ dài không gian cần thiết)
- v: velocity (vận tốc hiện tại)
- a: minimum space requirement (không gian tối thiểu)
- b: velocity-dependent factor (hệ số phụ thuộc vận tốc)
- Mối quan hệ tuyến tính đơn giản nhưng quan trọng

## 2. Các phương pháp tương tác (Interaction Methods)

### 2.1 Hard Bodies without Remote Action

**Phương trình (5):**
```
Fi(t) = {
  (vi^0 - vi(t))/τi,     nếu xi+1(t) - xi(t) > di(t)
  -δ(t)ei,               nếu xi+1(t) - xi(t) ≤ di(t)
}
với di(t) = ai + bivi(t)
```

Phân tích toán học:
- Đây là hàm piecewise (hàm từng khúc)
- δ(t): Dirac delta function
- ei: unit vector từ người i đến người i+1
- Discontinuous force model
- Collision detection: xi+1(t) - xi(t) ≤ di(t)

### 2.2 Hard Bodies with Remote Action

**Phương trình (6):**
```
Fi(t) = {
  Gi(t),           nếu vi(t) > 0
  max(0, Gi(t)),   nếu vi(t) ≤ 0
}

với Gi(t) = (vi^0 - vi(t))/τi - ei/(xi+1(t) - xi(t) - di(t))^fi
```

Phân tích toán học:
- Gi(t): combined force function
- Power law repulsion: 1/(distance)^fi
- Asymmetric force (chỉ tác động từ phía trước)
- Continuous force model
- Non-negative velocity constraint

## 3. Thuật toán số (Numerical Algorithm)

### 3.1 Explicit Euler Method

Cho hệ ODE: dy/dt = f(t, y)

**Euler scheme:**
```
y_{n+1} = y_n + Δt * f(t_n, y_n)
```

Áp dụng cho pedestrian model:
```
xi_{n+1} = xi_n + Δt * vi_n
vi_{n+1} = vi_n + Δt * Fi_n/mi
```

### 3.2 Time Step Selection

**Cho remote action model:**
- Δt = 0.001s (1ms)
- Explicit scheme ổn định vì continuous force
- CFL condition: Δt < min(characteristic time scales)

**Cho hard body model:**
- Adaptive time stepping
- Global time step bị hạn chế đến next contact
- Event-driven simulation approach

### 3.3 Stability Analysis

**Điều kiện ổn định cho Euler method:**
```
Δt < 2/λ_max
```
trong đó λ_max là eigenvalue lớn nhất của Jacobian matrix.

Cho driving force: λ ≈ 1/τi
Điều kiện: Δt < 2τi

## 4. Fundamental Diagram Analysis

### 4.1 Velocity-Density Relationship

Từ conservation equation:
```
ρ = 1/d = 1/(a + bv)
```

Giải cho v:
```
v = (1/ρ - a)/b = (1 - aρ)/(bρ)
```

### 4.2 Flow-Density Relationship

Flow J = ρv:
```
J = ρ * (1 - aρ)/(bρ) = (1 - aρ)/b
```

Maximum flow tại ρ_opt = 1/(2a):
```
J_max = 1/(4ab)
```

## 5. Parameter Sensitivity Analysis

### 5.1 Critical Parameters

1. **Parameter a (minimum space):**
   - Ảnh hưởng đến maximum density
   - ρ_max = 1/a

2. **Parameter b (velocity dependence):**
   - Ảnh hưởng đến curvature của v-ρ curve
   - b = 0: linear relationship
   - b > 0: concave relationship

3. **Remote force parameters (e, f):**
   - e: force magnitude
   - f: force decay rate
   - Ảnh hưởng đến smoothness của flow

### 5.2 Robustness Analysis

**Sensitivity to initial conditions:**
- Random distribution của intended speeds
- Gaussian distribution: μ = 1.24 m/s, σ = 0.05 m/s

**Finite size effects:**
- System length L ≥ 17.3m: negligible effects
- Periodic boundary conditions

**Numerical stability:**
- Time step sensitivity
- Spatial discretization effects

