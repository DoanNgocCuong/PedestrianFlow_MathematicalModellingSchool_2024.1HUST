# Phân tích tài liệu tham khảo: Basics of modelling the pedestrian flow

## Thông tin cơ bản
- **Tác giả**: Armin Seyfried, Bernhard Steffen, Thomas Lippert
- **Tạp chí**: Physica A 368 (2006) 232-238
- **Từ khóa**: Pedestrian dynamics

## Abstract
Tài liệu nghiên cứu mô hình động lực học người đi bộ (pedestrian dynamics) bằng cách xem xét con người như các đối tượng tự điều khiển di chuyển trong không gian liên tục. Dựa trên mô hình social force đã được chỉnh sửa, họ phân tích định tính ảnh hưởng của các phương pháp tiếp cận khác nhau cho tương tác giữa người đi bộ đối với mối quan hệ velocity-density.

## 1. Introduction
- Mô hình vi mô (Microscopic models) là công nghệ tiên tiến cho mô phỏng máy tính về động lực học người đi bộ
- Có hai loại mô hình chính:
  1. **Cellular automata models** [3-7]: mô hình rời rạc
  2. **Models in continuous space** [8-11]: mô hình không gian liên tục
- Nghiên cứu tập trung vào mô hình không gian liên tục
- Mô hình social force giả định lực đẩy với tác động từ xa giữa người đi bộ [8,12-17]
- Các mô hình khác xử lý người đi bộ bằng cách thực hiện khoảng cách tối thiểu giữa các cá nhân [10,11]

## 2. Modification of the social force model

### 2.1 Motivation
Mô hình social force được giới thiệu bởi Ref. [8]. Nó mô hình hóa chuyển động một chiều của người đi bộ i tại vị trí xi(t) với vận tốc vi(t) và khối lượng mi bằng phương trình chuyển động:

**Phương trình (1):**
```
dxi/dt = vi,    mi(dvi/dt) = Fi = Σ Fij(xi, xj, vi)
```

Tổng j tính cho tương tác với người đi bộ khác. Giả định rằng ma sát tại biên giới và dao động ngẫu nhiên có thể bỏ qua, do đó các lực được rút gọn thành một driving term và một repulsive term: Fi = Fi^drv + Fi^rep.

**Driving force (Phương trình 2):**
```
Fi^drv = mi(vi^0 - vi)/τi
```

Trong đó vi^0 là tốc độ dự định và τi kiểm soát gia tốc.

**Repulsive force (Phương trình 3):**
```
Fi^rep = Σ -∇xi U(||xi - xj|| - dij)^-β
```

Trong đó dij phản ánh kích thước của người đi bộ i tác động với lực từ xa trên người đi bộ khác.



### Velocity-Density Relation
Một khía cạnh quan trọng khác trong bối cảnh này là sự phụ thuộc giữa vận tốc hiện tại và yêu cầu không gian. Như được đề xuất bởi Pauls trong mô hình ellipse mở rộng [26], diện tích được chiếm bởi một người đi bộ tăng lên với tốc độ tăng.

Trong hệ thống một chiều, không gian yêu cầu thay đổi thành độ dài yêu cầu d. Trong Ref. [25] đã chỉ ra rằng đối với chuyển động single-file, mối quan hệ giữa độ dài yêu cầu cho một người đi bộ di chuyển với vận tốc v và v chính nó là tuyến tính:

**Phương trình (4):**
```
d = a + bv với a = 0.36m và b = 1.06s
```

Ít nhất cho vận tốc 0.1 m/s < v < 1.0 m/s.

### 2.2 Interactions

Để điều tra ảnh hưởng của tác động từ xa, cả lực xử lý người đi bộ như các vật thể cứng đơn giản và lực theo Eq. (3), nơi có tác động từ xa, sẽ được giới thiệu.

#### 2.2.1 Hard bodies without remote action

**Phương trình (5):**
```
Fi(t) = {
  (vi^0 - vi(t))/τi, xi+1(t) - xi(t) > di(t)
  -δ(t)ei, xi+1(t) - xi(t) ≤ di(t)
}
với di(t) = ai + bivi(t)
```

Trong đó δ(t) là hàm Dirac delta và ei là vector đơn vị chỉ hướng từ người đi bộ i đến người đi bộ i+1.


#### 2.2.2 Hard bodies with remote action

**Phương trình (6):**
```
Fi(t) = {
  Gi(t): vi(t) > 0,
  max(0, Gi(t)): vi(t) ≤ 0
}
```

với:
```
Gi(t) = (vi^0 - vi(t))/τi - ei/(xi+1(t) - xi(t) - di(t))^fi
```

và di(t) = ai + bivi(t).

Lực chỉ bị ảnh hưởng bởi các hành động ở phía trước của người đi bộ. Bằng cách sử dụng độ dài yêu cầu di, phạm vi tương tác là một hàm của vận tốc vi. Hai tham số bổ sung, ei và fi, phải được giới thiệu để cố định phạm vi và cường độ của lực.

### 2.3 Time stepping algorithm

Mô hình social force đưa ra một hệ thống khá lớn các phương trình vi phân thường bậc hai. Đối với mô hình hard body với remote action, trong đó phía bên phải của ODEs liên tục dọc theo giải pháp, một phương pháp Euler rõ ràng với bước thời gian Δt = 0.001s đã được thử nghiệm và thấy đủ.

Tình huống cho mô hình hard body không có remote force phức tạp hơn. Ở đây phía bên phải là một phân phối, và vị trí của các Dirac spikes không được biết trước. Do đó, việc xử lý hoàn hảo là một thủ tục thích ứng, trong đó mỗi bước thời gian toàn cầu bị hạn chế đến khoảng thời gian lên đến tiếp xúc tiếp theo.

**Thuật toán:**
1. Sử dụng explicit Euler method với time step Δt = 0.001s cho mô hình với remote action
2. Đối với hard body model không có remote force: sử dụng adaptive procedure với global time step bị hạn chế đến interval up to next contact
3. Khoảng cách giữa hai người không thay đổi đủ để làm cho explicit scheme không ổn định


## 3. Results

### Thiết lập thử nghiệm
Để so sánh với fundamental diagram thực nghiệm của chuyển động single-file [25], họ chọn một hệ thống với điều kiện biên tuần hoàn và độ dài L = 17.3m. Đối với cả hai tương tác, họ chứng minh rằng:

- Đối với system-sizes L = 17.3, 20.0, 50.0m: finite size effects không có ảnh hưởng đáng kể đến kết quả
- Các giá trị cho intended speed v₀ᵢ được phân phối theo phân phối chuẩn với mean value a = 1.24 m/s và σ = 0.05 m/s
- Trong hệ thống một chiều, ảnh hưởng của người đi bộ với intended speed nhỏ nhất che khuất jamming effects

### Tham số mô hình
**Cho hard bodies (a = 0.36m, không có remote action):**
- Nếu required length độc lập với velocity: curvature âm của hàm v = v(ρ)
- Velocity-dependence kiểm soát curvature và b = 0.5s dẫn đến good agreement với empirical data
- Với b = 1.06s: tìm thấy sự khác biệt giữa velocity-density relation được dự đoán bởi mô hình và fundamental diagram thực nghiệm

**Cho interaction với remote action (Eq. 6):**
- Tham số: a = 0.36m, b = 0.5s
- Remote force parameters: e = 0.07N và f = 2
- Fundamental diagram cho interaction với remote action được trình bày trong Fig. 2

### Kết quả chính
1. **Velocity-density relation**: Mô hình cho thấy mối quan hệ giữa mean velocity và density
2. **Influence of required length**: Việc phụ thuộc vào velocity của required length có ảnh hưởng đáng kể
3. **Remote action effects**: Remote action có thể cải thiện sự phù hợp với dữ liệu thực nghiệm
4. **Parameter sensitivity**: Các tham số a, b, e, f khác nhau cho mỗi người đi bộ và tương quan với intended speed cá nhân


### Kết quả từ các hình vẽ

**Figure 1: Velocity-density relation for hard bodies với a = 0.36m và without remote action**
- So sánh với empirical data từ Ref. [25]
- Filled squares: kết quả từ simple hard bodies
- Introduction of required length với b = 0.56s dẫn đến good agreement với empirical data
- Các đường cong cho b = 0.0, b = 0.56, và b = 1.06

**Figure 2: Velocity-density relation for hard bodies với remote action**
- So sánh hard bodies với remote action vs. hard bodies without remote action (filled circles)
- Tham số: a = 0.36m và b = 0.56s
- Remote force parameter: e = 0.07N và f = 2
- Với b = 0: fundamental diagram khác định tính và có gap cho resulting velocities

### Quan sát chính từ kết quả:
1. **Hard bodies without remote action**: Việc giới thiệu required length phụ thuộc vào velocity (b = 0.56s) cải thiện đáng kể sự phù hợp với dữ liệu thực nghiệm
2. **Hard bodies with remote action**: Cho kết quả tương tự nhưng với cơ chế tương tác khác
3. **Parameter b**: Có ảnh hưởng quan trọng đến hình dạng của velocity-density curve
4. **Empirical validation**: Mô hình có thể tái tạo được fundamental diagram thực nghiệm với việc chọn tham số phù hợp


**Figure 3: Time-development of positions**
- Cho densities gần velocity-gap (ρ ≈ 1.2m⁻¹)
- Density waves có thể quan sát được
- Một số cá nhân có gaps lớn hơn nhiều so với average gaps ở phía trước

## 4. Discussion and Summary

### Kết luận chính:
1. **Mô hình được chỉnh sửa có thể tái tạo empirical fundamental diagram** của pedestrian movement cho hệ thống một chiều, nếu xem xét velocity-dependence của required length.

2. **Tham số b quan trọng**: 
   - Với b = 0.56s: good agreement với empirical fundamental diagram
   - Với b = 1.06s: có sự khác biệt với empirical data

3. **Remote action có ảnh hưởng đáng kể** chỉ khi required length độc lập với velocity. Trong trường hợp này, quan sát được distinct density waves dẫn đến velocity gap trong fundamental diagram.

4. **Mô hình có thể mở rộng**: Nghiên cứu cung cấp cơ sở cho việc mở rộng cẩn thận của modified social force model và upgrade lên hai chiều bao gồm further interactions.

### Ứng dụng thực tế:
- Mô hình có thể áp dụng cho building evacuation scenarios
- Ước tính thời gian cần thiết cho clearance của building
- Phát triển density estimates ở front của bottlenecks

### Hạn chế và hướng phát triển:
- Nghiên cứu tập trung vào hệ thống đơn giản nhất trong equilibrium với periodic boundary conditions
- Cần mở rộng lên hai chiều và các tình huống phức tạp hơn
- Cần nghiên cứu thêm về consistency ở microscopic level

### Sensitivity Analysis và Robustness:
- Mô hình nhạy cảm với tham số b (velocity-dependence của required length)
- Remote action parameters (e, f) ảnh hưởng đến hình dạng fundamental diagram
- Intended speed distribution ảnh hưởng đến overall behavior
- Finite size effects không đáng kể cho L ≥ 17.3m

