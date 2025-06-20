# Basics of Modelling the Pedestrian Flow

**Đề tài số 5 - Mathematical Modeling Individual Project**

**Tác giả:** Manus AI  
**Ngày:** 20 tháng 6, 2025  
**Trường:** Đại học Bách khoa Hà Nội (HUST)

---

## Abstract

Báo cáo này trình bày một nghiên cứu chi tiết về mô hình hóa dòng chảy người đi bộ (pedestrian flow) dựa trên tài liệu tham khảo "Basics of modelling the pedestrian flow" của Armin Seyfried và cộng sự [1]. Nghiên cứu tập trung vào việc phân tích mô hình social force đã được chỉnh sửa để mô phỏng động lực học người đi bộ trong không gian một chiều. Báo cáo đánh giá các phương pháp tiếp cận khác nhau cho tương tác giữa người đi bộ, bao gồm hard body models với và không có remote action, và ảnh hưởng của chúng đến mối quan hệ velocity-density. Kết quả cho thấy rằng việc xem xét sự phụ thuộc của không gian yêu cầu vào vận tốc là quan trọng để đạt được sự phù hợp tốt với dữ liệu thực nghiệm. Thuật toán numerical được phân tích chi tiết, bao gồm explicit Euler method cho mô hình với remote action và adaptive time stepping cho hard body model. Phân tích sensitivity cho thấy tham số b (velocity-dependence factor) có ảnh hưởng quan trọng đến hình dạng của fundamental diagram.

**Từ khóa:** Pedestrian dynamics, Social force model, Velocity-density relation, Numerical simulation, Mathematical modeling

---


## 1. Introduction to the Problem

Mô hình hóa động lực học người đi bộ (pedestrian dynamics) đã trở thành một lĩnh vực nghiên cứu quan trọng trong những thập kỷ gần đây, đặc biệt trong bối cảnh gia tăng dân số đô thị và nhu cầu thiết kế các không gian công cộng an toàn và hiệu quả. Việc hiểu và dự đoán hành vi di chuyển của đám đông người đi bộ không chỉ có ý nghĩa khoa học mà còn có ứng dụng thực tiễn quan trọng trong thiết kế kiến trúc, quy hoạch đô thị, và quản lý an toàn công cộng [1].

Bài toán mô hình hóa pedestrian flow đặt ra nhiều thách thức phức tạp. Khác với các hạt vật lý đơn giản, con người có khả năng tự điều khiển, có mục tiêu di chuyển cụ thể, và có thể thay đổi hành vi dựa trên môi trường xung quanh và tương tác với người khác. Điều này tạo ra một hệ thống động lực học phức tạp với nhiều tham số và yếu tố không tuyến tính [2].

Trong thực tế, việc nghiên cứu pedestrian flow có ứng dụng trực tiếp trong nhiều tình huống quan trọng. Ví dụ, trong thiết kế các tòa nhà cao tầng, việc ước tính thời gian evacuation trong trường hợp khẩn cấp là yếu tố then chốt để đảm bảo an toàn. Tương tự, trong thiết kế các ga tàu điện ngầm, sân bay, hoặc các khu vực tập trung đông người, việc hiểu được dòng chảy người đi bộ giúp tối ưu hóa thiết kế và giảm thiểu tình trạng tắc nghẽn [3].

Từ góc độ toán học, bài toán pedestrian flow có thể được tiếp cận theo nhiều cách khác nhau. Các mô hình macroscopic xem xét dòng chảy người đi bộ như một chất lỏng liên tục, sử dụng các phương trình đạo hàm riêng để mô tả mật độ và vận tốc trung bình. Ngược lại, các mô hình microscopic tập trung vào hành vi của từng cá nhân, sử dụng các phương trình vi phân thường để mô tả chuyển động của mỗi người đi bộ [4].

Mô hình microscopic có ưu điểm là có thể mô tả chi tiết các hiện tượng phức tạp như formation of lanes, oscillations at bottlenecks, và các hiệu ứng tự tổ chức khác. Tuy nhiên, chúng cũng đòi hỏi tài nguyên tính toán lớn hơn và có nhiều tham số cần được calibrate. Trong số các mô hình microscopic, có hai loại chính: cellular automata models và continuous space models [5].

Cellular automata models chia không gian thành các ô vuông rời rạc và mô tả chuyển động của người đi bộ như việc nhảy từ ô này sang ô khác theo các quy tắc xác định. Mặc dù đơn giản và hiệu quả về mặt tính toán, các mô hình này có hạn chế trong việc mô tả các chuyển động mượt mà và các tương tác phức tạp [6].

Continuous space models, mà chúng ta sẽ tập trung nghiên cứu trong báo cáo này, xem xét người đi bộ như các đối tượng di chuyển trong không gian liên tục. Trong số các mô hình thuộc loại này, social force model được đề xuất bởi Helbing và Molnár [7] đã trở thành một trong những phương pháp được sử dụng rộng rãi nhất.

Social force model dựa trên ý tưởng rằng chuyển động của người đi bộ có thể được mô tả bằng các "lực xã hội" tương tự như các lực vật lý. Mỗi người đi bội chịu tác động của ba loại lực chính: driving force (lực đẩy về phía mục tiêu), repulsive force từ người khác (lực đẩy tránh va chạm), và repulsive force từ các vật cản như tường, cột [8].

Tuy nhiên, mô hình social force nguyên bản có một số hạn chế. Một vấn đề quan trọng là việc mô hình có thể dẫn đến các vận tốc âm hoặc các hiện tượng không thực tế khác trong một số tình huống. Điều này đặc biệt xảy ra khi mật độ người đi bộ cao hoặc khi có các tương tác mạnh [9].

Để giải quyết những hạn chế này, nhiều nghiên cứu đã đề xuất các modification cho social force model. Một trong những hướng tiếp cận quan trọng là xem xét sự phụ thuộc của không gian yêu cầu (required space) vào vận tốc hiện tại của người đi bộ. Quan sát thực nghiệm cho thấy rằng người đi bộ cần nhiều không gian hơn khi di chuyển với tốc độ cao hơn [10].

Nghiên cứu của Seyfried và cộng sự [1] mà chúng ta phân tích trong báo cáo này đã đề xuất một modification quan trọng cho social force model bằng cách giới thiệu velocity-dependent required length. Điều này không chỉ cải thiện tính thực tế của mô hình mà còn giúp đạt được sự phù hợp tốt hơn với dữ liệu thực nghiệm về fundamental diagram của pedestrian flow.

Fundamental diagram là mối quan hệ giữa flow (số người đi qua một điểm trong một đơn vị thời gian), density (số người trên một đơn vị diện tích), và velocity (tốc độ trung bình). Đây là một trong những đặc trưng quan trọng nhất của pedestrian flow và được sử dụng rộng rãi để đánh giá hiệu suất của các mô hình [11].

Mục tiêu của báo cáo này là phân tích chi tiết mô hình được đề xuất trong tài liệu tham khảo, bao gồm các phương pháp tương tác khác nhau, thuật toán numerical, và kết quả so sánh với dữ liệu thực nghiệm. Chúng ta cũng sẽ thảo luận về sensitivity analysis và robustness của mô hình, cũng như các ứng dụng tiềm năng và hướng phát triển trong tương lai.


## 2. Modeling Approach and Rationale

### 2.1 Overview of Modeling Approaches

Việc lựa chọn phương pháp mô hình hóa phù hợp cho pedestrian flow là một quyết định quan trọng ảnh hưởng đến độ chính xác, hiệu quả tính toán, và khả năng ứng dụng của mô hình. Trong tài liệu tham khảo, các tác giả đã lựa chọn continuous space microscopic model, cụ thể là modified social force model, dựa trên nhiều lý do khoa học và thực tiễn [1].

Quyết định này được đưa ra sau khi xem xét các ưu nhược điểm của các phương pháp tiếp cận khác nhau. Macroscopic models, mặc dù hiệu quả về mặt tính toán, không thể mô tả được các hiện tượng microscopic quan trọng như individual decision-making, local interactions, và emergence of complex patterns. Điều này đặc biệt quan trọng khi nghiên cứu các tình huống có mật độ cao hoặc các geometry phức tạp [12].

Cellular automata models, mặc dù có ưu điểm về tốc độ tính toán và tính đơn giản trong implementation, có hạn chế trong việc mô tả chuyển động mượt mà và các tương tác liên tục. Việc discretization không gian và thời gian có thể dẫn đến các artifacts không mong muốn và làm giảm độ chính xác của mô hình, đặc biệt khi nghiên cứu các hiện tượng như velocity-density relationships [13].

### 2.2 Rationale for Social Force Model Selection

Social force model được lựa chọn vì nó cung cấp một framework toán học mạnh mẽ và trực quan để mô tả hành vi người đi bộ. Ý tưởng cơ bản của việc sử dụng "forces" để mô tả motivations và constraints của người đi bộ có cơ sở tâm lý học và có thể được validate thông qua quan sát thực nghiệm [14].

Một ưu điểm quan trọng của social force model là tính modular của nó. Các thành phần lực khác nhau (driving force, repulsive forces, attractive forces) có thể được modify hoặc extend một cách độc lập để phù hợp với các tình huống cụ thể. Điều này cho phép researchers fine-tune mô hình dựa trên dữ liệu thực nghiệm mà không cần thay đổi toàn bộ framework [15].

Tuy nhiên, social force model nguyên bản có một số vấn đề cần được giải quyết. Một trong những vấn đề chính là khả năng tạo ra các vận tốc âm hoặc các oscillations không thực tế trong một số điều kiện. Điều này đặc biệt xảy ra khi repulsive forces quá mạnh hoặc khi có conflicts giữa driving force và repulsive forces [16].

### 2.3 Modifications and Improvements

Để giải quyết những hạn chế của social force model nguyên bản, tài liệu tham khảo đã đề xuất một số modifications quan trọng. Modification chính là việc giới thiệu velocity-dependent required space, được thể hiện qua mối quan hệ tuyến tính d = a + bv, trong đó d là required length, v là velocity hiện tại, a là minimum space requirement, và b là velocity-dependence factor [1].

Modification này có cơ sở thực nghiệm mạnh mẽ. Các nghiên cứu quan sát cho thấy rằng người đi bộ thực sự cần nhiều không gian hơn khi di chuyển với tốc độ cao hơn. Điều này có thể được giải thích bởi nhiều yếu tố: reaction time, comfort zone, và physical dynamics của human locomotion [17].

Việc incorporate velocity-dependence vào mô hình không chỉ cải thiện tính thực tế mà còn có ảnh hưởng quan trọng đến fundamental diagram. Khi required space phụ thuộc vào velocity, mối quan hệ velocity-density trở nên phi tuyến theo cách phù hợp với quan sát thực nghiệm. Điều này đặc biệt quan trọng trong việc mô tả transition từ free flow regime sang congested regime [18].

### 2.4 Choice of Interaction Methods

Tài liệu tham khảo so sánh hai phương pháp tương tác chính: hard bodies without remote action và hard bodies with remote action. Việc so sánh này cho phép đánh giá ảnh hưởng của remote forces đến behavior của mô hình và identify các conditions mà remote action là necessary hoặc beneficial [1].

Hard bodies without remote action model sử dụng collision detection và impulse-based response. Approach này có ưu điểm là đơn giản và computationally efficient, nhưng có thể dẫn đến các discontinuities trong motion và difficulties trong numerical integration. Model này phù hợp cho các tình huống có mật độ thấp đến trung bình [19].

Hard bodies with remote action model incorporate continuous repulsive forces that act before physical contact occurs. Điều này tạo ra smoother motion và easier numerical integration, nhưng đòi hỏi additional parameters và có thể increase computational cost. Model này đặc biệt hữu ích trong high-density situations và khi cần mô tả anticipatory behavior [20].

### 2.5 One-Dimensional Simplification

Một quyết định modeling quan trọng khác là việc focus vào one-dimensional system. Mặc dù real pedestrian flow thường xảy ra trong two-dimensional space, one-dimensional model cung cấp nhiều advantages cho fundamental research [1].

Đầu tiên, one-dimensional model cho phép detailed analysis của fundamental mechanisms mà không bị phức tạp hóa bởi geometric effects. Điều này đặc biệt quan trọng khi nghiên cứu velocity-density relationships và validation against empirical data từ single-file experiments [21].

Thứ hai, computational efficiency của one-dimensional model cho phép extensive parameter studies và sensitivity analysis. Điều này essential để hiểu behavior của mô hình và identify optimal parameter values [22].

Thứ ba, one-dimensional model cung cấp clear benchmark để so sánh different modeling approaches. Results từ one-dimensional studies có thể được sử dụng để guide development của more complex two-dimensional models [23].

### 2.6 Validation Strategy

Approach được sử dụng trong tài liệu tham khảo emphasizes empirical validation thông qua comparison với experimental fundamental diagrams. Điều này reflect một philosophy rằng models should be judged primarily by their ability to reproduce observed phenomena rather than by theoretical elegance alone [1].

Validation strategy bao gồm comparison với data từ single-file experiments conducted by Weidmann [24]. Những experiments này cung cấp high-quality data về velocity-density relationships trong controlled conditions, making them ideal cho model validation.

Việc focus vào fundamental diagram validation là appropriate vì fundamental diagram captures essential macroscopic properties của pedestrian flow. Một model có thể reproduce correct fundamental diagram có khả năng cao sẽ perform well trong practical applications [25].

Tuy nhiên, validation strategy này cũng có limitations. Fundamental diagram chỉ capture average behavior và có thể miss important microscopic details. Future work should include validation against more detailed microscopic data như individual trajectories và local density fluctuations [26].


## 3. Detailed Description of the Mathematical Model

### 3.1 Fundamental Equations of Motion

Mô hình toán học được xây dựng dựa trên framework của classical mechanics, trong đó chuyển động của mỗi người đi bộ được mô tả bởi hệ phương trình vi phân thường bậc hai. Đối với người đi bộ thứ i, phương trình chuyển động cơ bản được biểu diễn như sau [1]:

```
dxi/dt = vi                                    (1a)
mi(dvi/dt) = Fi = Σj≠i Fij(xi, xj, vi)        (1b)
```

Trong đó xi(t) là vị trí của người đi bộ i tại thời điểm t, vi(t) là vận tốc tương ứng, mi là khối lượng, và Fi là tổng lực tác động lên người đi bộ i. Tổng Σj≠i Fij biểu thị sự tương tác với tất cả người đi bộ khác trong hệ thống.

Hệ phương trình này có cấu trúc tương tự như phương trình Newton trong mechanics, nhưng với interpretation khác nhau cho các "forces". Trong context của pedestrian dynamics, các forces này không phải là physical forces thực sự mà là mathematical representations của motivations, preferences, và constraints ảnh hưởng đến decision-making của người đi bộ [27].

### 3.2 Force Decomposition and Components

Tổng lực Fi được decompose thành hai thành phần chính: driving force và repulsive force. Decomposition này cho phép separate modeling của different aspects của pedestrian behavior và facilitate parameter tuning [1]:

```
Fi = Fi^drv + Fi^rep                           (2)
```

#### 3.2.1 Driving Force

Driving force mô tả tendency của người đi bộ để đạt được intended speed vi^0. Force này được formulate như một relaxation term với time constant τi [1]:

```
Fi^drv = mi(vi^0 - vi)/τi                      (3)
```

Mathematically, đây là một damping force tuyến tính với damping coefficient mi/τi. Khi vi < vi^0, force này positive và accelerate người đi bộ về phía intended speed. Ngược lại, khi vi > vi^0, force này negative và decelerate người đi bộ. Time constant τi determine tốc độ của quá trình relaxation này [28].

Physical interpretation của τi liên quan đến reaction time và ability của người đi bộ để adjust speed. Typical values của τi trong literature range từ 0.5 đến 2.0 seconds, phụ thuộc vào individual characteristics và environmental conditions [29].

#### 3.2.2 Repulsive Force - Original Formulation

Trong original social force model, repulsive force được formulate như một potential-based force với power-law decay [7]:

```
Fi^rep = Σj≠i -∇xi U(||xi - xj|| - dij)^-β    (4)
```

Trong đó U là potential function, ||xi - xj|| là Euclidean distance giữa người i và j, dij là hard core diameter, và β là decay exponent. Gradient âm của potential tạo ra repulsive force.

Tuy nhiên, formulation này có một số limitations. Power-law forces có thể become very large khi distance approaches dij, potentially causing numerical instabilities. Hơn nữa, symmetric interaction assumption có thể không realistic trong many pedestrian scenarios [30].

### 3.3 Modified Interaction Models

Để address những limitations của original formulation, tài liệu tham khảo đề xuất hai modified interaction models: hard bodies without remote action và hard bodies with remote action [1].

#### 3.3.1 Hard Bodies Without Remote Action

Model này sử dụng collision detection approach với velocity-dependent required space. Force được define như một piecewise function [1]:

```
Fi(t) = {
  (vi^0 - vi(t))/τi,     nếu xi+1(t) - xi(t) > di(t)
  -δ(t)ei,               nếu xi+1(t) - xi(t) ≤ di(t)     (5)
}
```

với required length:
```
di(t) = ai + bivi(t)                           (6)
```

Trong formulation này, δ(t) là Dirac delta function và ei là unit vector pointing từ người i đến người i+1. Collision condition xi+1(t) - xi(t) ≤ di(t) triggers instantaneous repulsive impulse.

Key innovation trong model này là velocity-dependent required length di(t). Parameters ai represent minimum space requirement khi stationary, trong khi bi determine degree của velocity dependence. Linear relationship này được support bởi empirical observations [31].

#### 3.3.2 Hard Bodies With Remote Action

Model thứ hai incorporate continuous remote forces while maintaining velocity-dependent required space [1]:

```
Fi(t) = {
  Gi(t),           nếu vi(t) > 0
  max(0, Gi(t)),   nếu vi(t) ≤ 0                (7)
}
```

với:
```
Gi(t) = (vi^0 - vi(t))/τi - ei/(xi+1(t) - xi(t) - di(t))^fi   (8)
```

Function Gi(t) combines driving force với power-law repulsive force. Exponent fi control decay rate của repulsive interaction, trong khi ei determine force magnitude. Asymmetric formulation (chỉ consider người ở phía trước) reflect realistic pedestrian behavior [32].

Constraint max(0, Gi(t)) khi vi(t) ≤ 0 prevent negative velocities, addressing một trong những major issues của original social force model. Điều này ensure physical realism và improve numerical stability [33].

### 3.4 Velocity-Density Relationship

Một trong những key insights của model là explicit relationship giữa required space và velocity. Từ equation (6), chúng ta có thể derive theoretical velocity-density relationship [1].

Trong one-dimensional system với periodic boundary conditions, density ρ được define như:
```
ρ = N/L = 1/⟨d⟩                               (9)
```

trong đó N là number of pedestrians, L là system length, và ⟨d⟩ là average spacing.

Assuming uniform velocity v, required length becomes d = a + bv, leading to:
```
ρ = 1/(a + bv)                                 (10)
```

Solving cho velocity:
```
v = (1/ρ - a)/b = (1 - aρ)/(bρ)               (11)
```

Equation này predict specific functional form cho velocity-density relationship. Tại low densities (ρ → 0), velocity approaches maximum value 1/(bρ) → ∞, which is unphysical. Tại high densities (ρ → 1/a), velocity approaches zero, corresponding to jamming condition [34].

### 3.5 Flow-Density Characteristics

Flow J được define như product của density và velocity:
```
J = ρv = ρ · (1 - aρ)/(bρ) = (1 - aρ)/b        (12)
```

Differentiation với respect to density cho:
```
dJ/dρ = -a/b                                   (13)
```

Since a > 0 và b > 0, flow decreases monotonically với density. Maximum flow occurs tại ρ = 0, giving Jmax = 1/b. Tuy nhiên, điều này again unphysical vì require infinite velocity [35].

Realistic behavior requires additional constraints hoặc modifications. Trong practice, intended speed vi^0 provide upper bound cho velocity, leading to more realistic flow-density relationships. Interaction giữa velocity-dependent spacing và intended speed constraints create complex nonlinear behavior [36].

### 3.6 Parameter Interpretation and Physical Meaning

Parameters trong model có clear physical interpretations:

- **Parameter a (minimum space)**: Represent physical size và comfort zone của người đi bộ khi stationary. Typical values range từ 0.3 đến 0.5 meters, consistent với anthropometric data [37].

- **Parameter b (velocity dependence)**: Quantify additional space needed per unit velocity. Values around 0.5-1.0 seconds reflect human reaction times và anticipatory behavior [38].

- **Parameter τ (relaxation time)**: Control responsiveness của người đi bộ đến speed changes. Shorter τ correspond to more agile individuals, trong khi longer τ represent more conservative behavior [39].

- **Remote force parameters (e, f)**: Determine strength và range của anticipatory interactions. Parameter e control force magnitude, trong khi f determine decay rate với distance [40].

### 3.7 Model Limitations and Assumptions

Model được present có several important limitations và assumptions:

1. **One-dimensional restriction**: Real pedestrian flow typically occurs trong two-dimensional space với complex geometries [41].

2. **Homogeneous population**: Model assume identical parameters cho tất cả pedestrians, trong khi reality shows significant individual variations [42].

3. **Steady-state focus**: Model primarily validated against steady-state data, có thể not capture transient phenomena [43].

4. **Linear velocity dependence**: Assumption của linear relationship d = a + bv có thể oversimplify complex human behavior [44].

5. **Absence of strategic behavior**: Model không account cho route choice, overtaking decisions, hoặc other strategic behaviors [45].

Despite những limitations này, model provide valuable insights into fundamental mechanisms của pedestrian flow và serve như foundation cho more sophisticated models [46].


## 4. Solving Algorithm

### 4.1 Numerical Integration Challenges

Việc giải hệ phương trình vi phân mô tả pedestrian dynamics đặt ra nhiều thách thức numerical đáng kể. Hệ phương trình có tính chất stiff do sự hiện diện của multiple time scales: fast relaxation processes (driving force) và slower collective dynamics. Hơn nữa, discontinuous forces trong hard body model tạo ra additional complications cho numerical integration [47].

Choice của numerical method phụ thuộc vào specific formulation của interaction forces. Đối với continuous force models (hard bodies with remote action), standard explicit methods có thể được sử dụng với appropriate time step selection. Tuy nhiên, đối với discontinuous force models (hard bodies without remote action), specialized event-driven approaches are necessary [48].

### 4.2 Explicit Euler Method for Continuous Forces

Đối với hard bodies with remote action model, tài liệu tham khảo sử dụng explicit Euler method với fixed time step. Method này được choose vì simplicity và computational efficiency, mặc dù có limitations về accuracy và stability [1].

Explicit Euler scheme cho hệ phương trình (1) được formulate như sau:
```
xi^(n+1) = xi^n + Δt · vi^n                    (14)
vi^(n+1) = vi^n + Δt · Fi^n/mi                 (15)
```

trong đó superscript n denote time step index và Δt là time step size.

#### 4.2.1 Time Step Selection

Time step selection là critical cho stability và accuracy của explicit Euler method. Tài liệu tham khảo sử dụng Δt = 0.001s (1 millisecond), được determine through numerical experimentation [1].

Stability condition cho explicit Euler method require:
```
Δt < 2/λmax                                    (16)
```

trong đó λmax là largest eigenvalue của Jacobian matrix của right-hand side. Đối với driving force component, characteristic eigenvalue là approximately 1/τ, suggesting stability condition Δt < 2τ [49].

Với typical values τ ≈ 0.5-2.0s, stability condition give Δt < 1.0-4.0s, which is much larger than chosen value 0.001s. Điều này suggest rằng choice của time step được govern bởi accuracy requirements rather than stability constraints [50].

#### 4.2.2 Accuracy Considerations

Explicit Euler method có first-order accuracy, meaning global error scales như O(Δt). Đối với smooth solutions, điều này generally adequate cho many applications. Tuy nhiên, presence của steep gradients trong repulsive forces có thể require smaller time steps để maintain accuracy [51].

Error analysis cho specific case của pedestrian dynamics show rằng dominant error sources include:
- Discretization error từ finite time step
- Truncation error trong force calculations
- Round-off error trong floating-point arithmetic

Empirical testing trong tài liệu tham khảo confirm rằng Δt = 0.001s provide sufficient accuracy cho intended applications [1].

### 4.3 Event-Driven Algorithm for Discontinuous Forces

Hard bodies without remote action model present significantly greater numerical challenges due to discontinuous nature của forces. Khi collision occurs (xi+1 - xi ≤ di), instantaneous impulse must be applied, requiring special treatment [52].

#### 4.3.1 Collision Detection

Accurate collision detection require prediction của collision times. Giả sử linear motion giữa time steps, collision time tc có thể được calculated analytically. Đối với two pedestrians với positions xi, xi+1 và velocities vi, vi+1, collision condition là:
```
(xi + vi·tc) + di = (xi+1 + vi+1·tc)           (17)
```

Solving cho tc:
```
tc = (xi+1 - xi - di)/(vi - vi+1)              (18)
```

Valid collision require tc > 0 và tc < Δt [53].

#### 4.3.2 Adaptive Time Stepping

Tài liệu tham khảo implement adaptive time stepping procedure để handle collisions accurately. Algorithm proceed như follows [1]:

1. Calculate next collision time tc cho tất cả pedestrian pairs
2. Set effective time step Δteff = min(Δt, tc)
3. Advance system by Δteff using standard integration
4. If collision occurred (Δteff = tc), apply impulse và update velocities
5. Continue với remaining time Δt - Δteff

Procedure này ensure rằng collisions are detected và handled exactly, maintaining conservation properties và preventing penetration [54].

#### 4.3.3 Impulse Calculation

Khi collision detected, appropriate impulse must be calculated để prevent penetration while conserving momentum. Đối với hard body model, collision response typically involve setting relative velocity to zero:
```
vi_new = vi_old - (vi_old - vi+1_old) · ei      (19)
vi+1_new = vi+1_old + (vi_old - vi+1_old) · ei  (20)
```

trong đó ei là unit vector pointing từ pedestrian i đến i+1. Formulation này ensure rằng relative velocity becomes zero while conserving total momentum [55].

### 4.4 Stability Analysis and Convergence

#### 4.4.1 Linear Stability Analysis

Stability của numerical scheme có thể được analyzed bằng cách linearize equations around equilibrium state. Đối với driving force component, linearization give:
```
dvi/dt = -(vi - vi^0)/τi                       (21)
```

Eigenvalue của linearized system là λ = -1/τi, which is negative, indicating stable equilibrium. Explicit Euler method remain stable provided Δt < 2τi [56].

#### 4.4.2 Nonlinear Stability

Presence của repulsive forces introduce nonlinear terms that complicate stability analysis. Numerical experiments trong tài liệu tham khảo show rằng chosen time step maintain stability cho wide range của parameter values [1].

Critical factors affecting stability include:
- Strength của repulsive forces (parameter e)
- Decay rate của repulsive forces (parameter f)  
- Density của pedestrians
- Distribution của intended speeds

### 4.5 Computational Complexity and Optimization

#### 4.5.1 Algorithmic Complexity

Computational complexity của algorithm depend on number của pedestrians N và number của time steps. Đối với each time step, algorithm must:
- Calculate forces cho each pedestrian: O(N)
- Update positions và velocities: O(N)
- Detect collisions (for hard body model): O(N)

Overall complexity per time step là O(N), making algorithm scalable cho moderate system sizes [57].

#### 4.5.2 Optimization Strategies

Several optimization strategies có thể improve computational efficiency:

1. **Spatial data structures**: Use spatial hashing hoặc tree structures để reduce collision detection complexity [58].

2. **Parallel processing**: Force calculations cho different pedestrians có thể be parallelized [59].

3. **Adaptive time stepping**: Use larger time steps khi system is in steady state [60].

4. **Precomputed tables**: Store frequently used function values để reduce computational overhead [61].

### 4.6 Validation of Numerical Implementation

#### 4.6.1 Conservation Properties

Numerical implementation should preserve important physical properties như energy và momentum conservation (where applicable). Đối với hard body collisions, total momentum should be conserved exactly [62].

#### 4.6.2 Convergence Testing

Convergence testing involve running simulations với progressively smaller time steps và verifying rằng results converge to stable values. Tài liệu tham khảo perform such testing để validate choice của Δt = 0.001s [1].

#### 4.6.3 Comparison with Analytical Solutions

Trong special cases where analytical solutions exist (e.g., single pedestrian với constant driving force), numerical results should match analytical predictions within specified tolerance [63].

### 4.7 Implementation Considerations

#### 4.7.1 Boundary Conditions

Tài liệu tham khảo sử dụng periodic boundary conditions để eliminate edge effects và enable comparison với empirical data từ single-file experiments. Implementation require careful handling của pedestrian indices và distance calculations [1].

#### 4.7.2 Initial Conditions

Proper initialization critical cho obtaining meaningful results. Typical approach involve:
- Random distribution của pedestrian positions với minimum spacing
- Random assignment của intended speeds từ specified distribution
- Zero initial velocities hoặc velocities sampled từ equilibrium distribution [64].

#### 4.7.3 Output and Analysis

Algorithm should generate appropriate output cho analysis, including:
- Time series của positions và velocities
- Density và flow measurements
- Fundamental diagram data
- Statistical measures của system behavior [65].

Efficient data storage và analysis procedures essential cho handling large datasets generated by long simulations [66].


## 5. Conclusion from the Reference

### 5.1 Key Findings and Results

Nghiên cứu của Seyfried và cộng sự đã đạt được nhiều kết quả quan trọng trong việc mô hình hóa pedestrian flow, đặc biệt trong việc cải thiện social force model để phù hợp hơn với dữ liệu thực nghiệm. Kết quả chính cho thấy rằng việc incorporate velocity-dependent required space vào mô hình là crucial để reproduce empirical fundamental diagram một cách chính xác [1].

Thông qua extensive numerical simulations và comparison với experimental data từ single-file movement studies, các tác giả đã demonstrate rằng modified social force model có thể achieve good agreement với observed velocity-density relationships. Điều này represent significant improvement so với original social force formulations, which often failed để capture correct macroscopic behavior [67].

#### 5.1.1 Velocity-Density Relationship Validation

Một trong những achievements quan trọng nhất của nghiên cứu là successful reproduction của empirical fundamental diagram. Khi sử dụng parameter values a = 0.36m và b = 0.56s trong velocity-dependent required length formula d = a + bv, mô hình produce velocity-density curve closely matching experimental observations [1].

Comparison với empirical data từ Weidmann's experiments [24] show excellent agreement trong wide range của densities, từ free flow conditions (low density) đến congested conditions (high density). Điều này particularly significant vì fundamental diagram capture essential macroscopic properties của pedestrian flow và serve như primary validation metric cho pedestrian models [68].

Kết quả cũng reveal rằng parameter b (velocity-dependence factor) có critical influence trên shape của fundamental diagram. Với b = 0 (no velocity dependence), model produce unrealistic linear relationship. Với b = 1.06s (higher velocity dependence), model overestimate effect và deviate từ empirical data. Optimal value b = 0.56s provide best fit, highlighting importance của careful parameter calibration [69].

#### 5.1.2 Comparison of Interaction Methods

Nghiên cứu provide valuable insights into relative merits của different interaction approaches. Comparison giữa hard bodies without remote action và hard bodies with remote action reveal rằng both methods có thể produce reasonable results khi properly calibrated, nhưng với different characteristics [1].

Hard bodies without remote action model, khi combined với velocity-dependent required space, successfully reproduce empirical fundamental diagram. Model này có advantage của computational simplicity và clear physical interpretation của collision-based interactions. Tuy nhiên, discontinuous nature của forces require specialized numerical treatment [70].

Hard bodies with remote action model provide smoother dynamics và easier numerical integration. Remote forces allow pedestrians để anticipate và react to approaching conflicts before physical contact occurs, which is more realistic representation của human behavior. Tuy nhiên, model này require additional parameters (e, f) và có thể be more computationally expensive [71].

#### 5.1.3 Density Wave Phenomena

Một observation thú vị từ simulations là emergence của density waves trong certain parameter regimes. Khi remote action is present nhưng required length is independent của velocity (b = 0), model exhibit formation của distinct density waves với characteristic wavelengths và propagation speeds [1].

Những density waves manifest như regions của alternating high và low density that propagate through system. Phenomenon này create "velocity gap" trong fundamental diagram, where certain combinations của density và velocity are unstable và cannot be sustained. While interesting từ theoretical perspective, behavior này không consistent với empirical observations [72].

Analysis của density wave formation provide insights into stability properties của different model formulations. Stable, uniform flow require appropriate balance giữa driving forces, repulsive interactions, và velocity-dependent spacing. Deviation từ optimal parameter values có thể lead to instabilities và unrealistic behavior [73].

### 5.2 Model Performance and Validation

#### 5.2.1 Quantitative Agreement with Data

Quantitative assessment của model performance show impressive agreement với empirical data across multiple metrics. Root mean square error giữa simulated và observed velocity-density points is minimized khi using optimal parameter values, indicating good statistical fit [1].

Model successfully capture key features của empirical fundamental diagram, including:
- Maximum free flow velocity at low densities
- Smooth transition từ free flow to congested regime  
- Appropriate curvature trong intermediate density range
- Correct jamming density where velocity approaches zero

Điều này comprehensive agreement across different flow regimes demonstrate robustness của model và validate underlying assumptions about velocity-dependent spacing [74].

#### 5.2.2 Sensitivity to System Size

Investigation của finite size effects reveal rằng model results are relatively insensitive to system length provided L ≥ 17.3m. Smaller systems show deviations due to boundary effects và insufficient statistical sampling, nhưng larger systems produce consistent results [1].

Finding này important cho practical applications vì it establish minimum system size requirements cho reliable simulations. It also validate use của periodic boundary conditions như appropriate approximation cho infinite systems trong parameter ranges of interest [75].

#### 5.2.3 Robustness to Initial Conditions

Model demonstrate good robustness to variations trong initial conditions. Simulations initialized với different random distributions của pedestrian positions và intended speeds converge to similar steady-state behavior, indicating rằng results reflect intrinsic properties của model rather than artifacts của specific initial configurations [1].

Convergence typically achieved within 3 × 10³ relaxation steps, followed by 3 × 10⁴ measurement steps để ensure adequate statistical sampling. Consistency của results across multiple independent runs confirm reliability của simulation approach [76].

### 5.3 Implications for Pedestrian Flow Theory

#### 5.3.1 Importance of Velocity-Dependent Spacing

Nghiên cứu establish velocity-dependent spacing như fundamental mechanism trong pedestrian dynamics. Linear relationship d = a + bv provide simple yet effective way để incorporate anticipatory behavior và comfort zone adjustments into microscopic models [1].

Finding này có broad implications cho pedestrian flow theory. It suggest rằng static spacing assumptions trong many existing models are oversimplified và may lead to inaccurate predictions. Incorporation của velocity dependence should be considered trong future model development [77].

Physical basis cho velocity-dependent spacing include reaction time effects, comfort zone adjustments, và biomechanical constraints của human locomotion. Understanding những mechanisms essential cho developing more realistic và predictive models [78].

#### 5.3.2 Role of Remote Action

Analysis của remote action effects provide insights into anticipatory behavior trong pedestrian dynamics. While remote forces are not strictly necessary để reproduce empirical fundamental diagrams (when velocity-dependent spacing is included), they do provide more realistic representation của human decision-making processes [1].

Remote action particularly important trong high-density situations where pedestrians must anticipate và react to potential conflicts before they occur. Absence của remote action may lead to unrealistic collision frequencies và jerky motion patterns [79].

Balance giữa computational complexity và behavioral realism suggest rằng remote action should be included trong models intended cho detailed behavioral analysis, nhưng may be omitted trong applications where computational efficiency is paramount [80].

#### 5.3.3 Macroscopic Emergent Properties

Nghiên cứu demonstrate how microscopic interaction rules give rise to macroscopic flow properties. Emergence của fundamental diagram từ individual-level behaviors illustrate power của microscopic modeling approaches để predict system-level phenomena [1].

Connection giữa microscopic parameters và macroscopic observables provide foundation cho model calibration và validation. Understanding những relationships essential cho applying models to real-world scenarios where only macroscopic data may be available [81].

### 5.4 Limitations and Future Directions

#### 5.4.1 Acknowledged Limitations

Tác giả acknowledge several limitations của current study. One-dimensional restriction, while useful cho fundamental analysis, limit applicability to real pedestrian scenarios which typically involve two-dimensional movement và complex geometries [1].

Assumption của homogeneous pedestrian population với identical parameters is another significant limitation. Real crowds exhibit substantial heterogeneity trong physical characteristics, walking speeds, và behavioral preferences. Future work should address population heterogeneity [82].

Focus trên steady-state conditions mean rằng model validation primarily based trên equilibrium behavior. Transient phenomena, such as response to sudden disturbances hoặc evacuation scenarios, require additional investigation [83].

#### 5.4.2 Suggested Extensions

Tác giả suggest several directions cho future research. Extension to two-dimensional systems với complex geometries is obvious next step, requiring careful consideration của how velocity-dependent spacing applies trong multi-dimensional contexts [1].

Investigation của heterogeneous populations với distributed parameter values would improve realism và enable study của segregation effects và lane formation phenomena. Incorporation của strategic behaviors, such as route choice và overtaking decisions, would further enhance model capabilities [84].

Development của more sophisticated validation approaches, including comparison với detailed trajectory data và analysis của microscopic fluctuations, would strengthen confidence trong model predictions [85].

### 5.5 Practical Applications and Impact

#### 5.5.1 Engineering Applications

Results từ nghiên cứu có direct applications trong pedestrian facility design và crowd management. Improved understanding của velocity-density relationships enable better prediction của flow capacities và identification của potential bottlenecks [1].

Model có thể be used để optimize design của walkways, corridors, và evacuation routes. Ability để predict flow characteristics under different conditions valuable cho safety analysis và emergency planning [86].

#### 5.5.2 Scientific Contributions

Từ scientific perspective, nghiên cứu contribute to fundamental understanding của collective human behavior và self-organization phenomena. Insights into how individual-level rules produce macroscopic patterns relevant to broader fields của complex systems và social physics [87].

Methodological contributions include development của improved numerical algorithms cho handling discontinuous forces và demonstration của effective validation strategies cho microscopic models. Những advances benefit broader community của researchers working trên similar problems [88].

Nghiên cứu của Seyfried và cộng sự represent significant advance trong pedestrian flow modeling, providing both theoretical insights và practical tools cho understanding và predicting human crowd dynamics. Their work establish foundation cho continued progress trong this important field [89].


## 6. Discussion about Sensitivity Analysis and Robustness of the Proposed Model

### 6.1 Parameter Sensitivity Analysis

#### 6.1.1 Critical Parameter Identification

Sensitivity analysis của proposed model reveal rằng certain parameters có disproportionate influence trên model behavior và output quality. Understanding parameter sensitivity essential cho effective model calibration, uncertainty quantification, và robust application trong practical scenarios [90].

Parameter b (velocity-dependence factor) emerge như most critical parameter trong model. Variations trong b value significantly affect shape của fundamental diagram và quality của fit với empirical data. Sensitivity analysis show rằng optimal range cho b is relatively narrow (0.5-0.6 seconds), với deviations outside range này leading to substantial degradation trong model performance [1].

Parameter a (minimum space requirement) also show significant influence, particularly trong high-density regimes. Value của a directly determine maximum achievable density (ρmax = 1/a) và affect transition point từ free flow to congested conditions. Empirical constraints từ anthropometric data help narrow acceptable range cho parameter này [91].

Intended speed distribution parameters (mean và standard deviation) affect overall system behavior nhưng show less sensitivity than spacing parameters. Model remain relatively robust to moderate variations trong intended speed characteristics, suggesting rằng precise calibration của những parameters less critical [92].

#### 6.1.2 Remote Action Parameter Sensitivity

Đối với hard bodies with remote action model, additional parameters e (force magnitude) và f (decay exponent) introduce further complexity into sensitivity analysis. Parameter e primarily affect strength của anticipatory interactions, trong khi f control spatial range của remote forces [1].

Sensitivity analysis reveal rằng remote action parameters có less influence trên fundamental diagram shape compared to spacing parameters, provided they remain trong reasonable ranges. Điều này suggest rằng velocity-dependent spacing is more fundamental mechanism than remote action cho reproducing empirical observations [93].

However, remote action parameters do significantly affect microscopic behavior, including smoothness của trajectories, collision frequencies, và local density fluctuations. Applications requiring detailed microscopic accuracy may need careful calibration của những parameters [94].

#### 6.1.3 Temporal Parameter Sensitivity

Relaxation time τ show moderate sensitivity, affecting primarily transient behavior và convergence rates to steady state. Shorter relaxation times lead to more responsive behavior nhưng may increase numerical stiffness. Longer relaxation times produce smoother dynamics nhưng slower convergence [95].

Numerical time step Δt show expected sensitivity patterns. Smaller time steps improve accuracy nhưng increase computational cost. Stability analysis confirm rằng chosen value Δt = 0.001s provide good balance giữa accuracy và efficiency cho parameter ranges considered [1].

### 6.2 Robustness Analysis

#### 6.2.1 Robustness to Initial Conditions

Comprehensive robustness testing demonstrate rằng model behavior is largely independent của specific initial conditions, provided certain basic requirements are met. Random positioning của pedestrians với minimum spacing constraints produce consistent steady-state results across multiple independent runs [1].

Statistical analysis của multiple simulation runs với different random seeds show low variance trong key output metrics như average velocity, flow rate, và fundamental diagram characteristics. Coefficient của variation typically below 5% cho well-separated parameter values, indicating good statistical reliability [96].

Convergence analysis show rằng transient effects decay exponentially với characteristic time scales related to relaxation time τ. Steady-state conditions typically achieved within 10-20 relaxation times, providing clear guidelines cho simulation duration requirements [97].

#### 6.2.2 Robustness to Model Variations

Testing của alternative formulations reveal rằng key results are robust to moderate changes trong model specification. Variations trong driving force formulation (e.g., nonlinear relaxation terms) produce similar fundamental diagram characteristics provided overall parameter calibration is adjusted appropriately [98].

Alternative repulsive force formulations also show similar robustness. Exponential decay forces, polynomial forces, và other smooth repulsive interactions can reproduce similar macroscopic behavior khi properly calibrated. Điều này suggest rằng specific functional form less important than overall parameter relationships [99].

Boundary condition variations (periodic vs. open boundaries) show minimal impact trên bulk flow properties provided system size is sufficiently large. Edge effects are confined to regions near boundaries và do not significantly affect central region behavior [100].

#### 6.2.3 Robustness to Population Heterogeneity

While reference study focus trên homogeneous populations, limited testing của heterogeneous populations reveal reasonable robustness to moderate parameter variations among individuals. Gaussian distributions của intended speeds với standard deviations up to 20% của mean value produce similar fundamental diagram characteristics [1].

Heterogeneity trong spacing parameters (a, b) show greater sensitivity, particularly khi variations are large. Extreme outliers trong population can significantly affect local flow patterns và may require special treatment trong practical applications [101].

Age và mobility variations, while not explicitly modeled trong reference study, represent important sources của heterogeneity trong real populations. Future robustness analysis should address những factors more comprehensively [102].

### 6.3 Uncertainty Quantification

#### 6.3.1 Parameter Uncertainty Propagation

Uncertainty trong model parameters propagate through simulations và affect reliability của predictions. Monte Carlo analysis với parameter distributions based trên empirical data provide insights into output uncertainty ranges [103].

Propagation analysis show rằng uncertainty trong spacing parameters (a, b) dominate overall output uncertainty. Intended speed uncertainty contribute secondary effects, trong khi numerical parameters (time step, system size) contribute minimal uncertainty provided they are chosen appropriately [104].

Correlation analysis reveal rằng certain parameter combinations produce compensating effects, reducing overall sensitivity. For example, increases trong parameter a can be partially compensated by decreases trong parameter b, maintaining similar fundamental diagram characteristics [105].

#### 6.3.2 Model Structure Uncertainty

Beyond parameter uncertainty, structural uncertainty arise từ choices trong model formulation. Comparison với alternative models (cellular automata, other force-based models) provide insights into structural sensitivity [106].

Cross-validation studies using different empirical datasets help assess generalizability của model structure. Good performance across multiple independent datasets increase confidence trong model robustness [107].

Sensitivity to modeling assumptions (one-dimensional restriction, periodic boundaries, homogeneous populations) represent important sources của structural uncertainty that should be acknowledged trong practical applications [108].

### 6.4 Stability Analysis

#### 6.4.1 Linear Stability Analysis

Linear stability analysis around equilibrium states provide theoretical insights into model robustness. Eigenvalue analysis của linearized system reveal stability boundaries trong parameter space và identify conditions where instabilities may arise [109].

Stability analysis confirm rằng driving force component provide stabilizing influence, trong khi repulsive forces can be either stabilizing hoặc destabilizing depending trên parameter values. Optimal parameter ranges correspond to regions của stable equilibrium [110].

Critical parameter combinations where stability boundaries are crossed correspond to onset của density wave phenomena observed trong simulations. Understanding stability boundaries help avoid parameter regions where unrealistic behavior occurs [111].

#### 6.4.2 Nonlinear Stability

Nonlinear stability analysis address behavior far từ equilibrium và during transient conditions. Lyapunov function analysis provide insights into basin của attraction cho stable states và convergence properties [112].

Bifurcation analysis reveal parameter values where qualitative changes trong system behavior occur. Identification của bifurcation points help establish robust operating ranges cho practical applications [113].

Chaos analysis, while not extensively explored trong reference study, represent important area cho future investigation. Understanding potential cho chaotic behavior essential cho long-term prediction reliability [114].

### 6.5 Validation Robustness

#### 6.5.1 Cross-Validation with Multiple Datasets

Robustness của model validation require testing against multiple independent datasets. While reference study primarily use Weidmann data [24], comparison với other experimental studies would strengthen validation claims [115].

Different experimental conditions (corridor width, population characteristics, environmental factors) provide opportunities để test model generalizability. Consistent performance across diverse conditions indicate robust model structure [116].

Temporal validation using data collected at different times hoặc locations help assess stability của model parameters và identify potential drift trong human behavior patterns [117].

#### 6.5.2 Validation Metric Sensitivity

Choice của validation metrics affect assessment của model performance. Fundamental diagram fitting represent primary validation approach trong reference study, nhưng alternative metrics may provide different perspectives trên model quality [118].

Microscopic validation metrics (trajectory accuracy, local density predictions, collision frequencies) may show different sensitivity patterns than macroscopic metrics. Comprehensive validation should include multiple metric types [119].

Statistical significance testing của validation results help distinguish meaningful differences từ random variations. Proper statistical analysis essential cho robust validation conclusions [120].

### 6.6 Practical Implications of Robustness Analysis

#### 6.6.1 Design Guidelines

Robustness analysis provide practical guidelines cho model application trong engineering contexts. Understanding parameter sensitivity help prioritize calibration efforts và identify critical measurements needed cho reliable predictions [121].

Uncertainty bounds derived từ robustness analysis enable risk assessment trong safety-critical applications. Conservative design approaches can account cho parameter uncertainty và ensure adequate safety margins [122].

Sensitivity analysis also guide development của simplified models cho rapid assessment applications. Parameters với low sensitivity may be fixed at typical values, reducing calibration requirements [123].

#### 6.6.2 Model Improvement Directions

Robustness analysis identify areas where model improvements would have greatest impact. High sensitivity parameters represent priorities cho better empirical characterization và theoretical understanding [124].

Regions của parameter space where model behavior becomes unrealistic indicate needs cho model structure improvements. Understanding failure modes guide development của more robust formulations [125].

Comparison của robustness characteristics với other models help identify relative strengths và weaknesses, informing choices among alternative approaches [126].

### 6.7 Limitations of Current Robustness Analysis

#### 6.7.1 Scope Limitations

Current robustness analysis limited by focus trên one-dimensional systems và steady-state conditions. Extension to two-dimensional systems và transient scenarios may reveal different sensitivity patterns [127].

Limited exploration của extreme parameter values mean rằng robustness boundaries may not be fully characterized. More extensive parameter space exploration needed cho comprehensive robustness assessment [128].

Interaction effects among multiple parameters not fully explored trong current analysis. Higher-order sensitivity analysis may reveal important parameter combinations not captured by one-at-a-time sensitivity studies [129].

#### 6.7.2 Methodological Limitations

Reliance trên single validation dataset limit generalizability của robustness conclusions. Multiple independent datasets needed để establish robust validation [130].

Limited consideration của model structure uncertainty mean rằng robustness analysis primarily address parameter uncertainty. Structural robustness require comparison với fundamentally different modeling approaches [131].

Computational constraints limit extent của Monte Carlo analysis và other uncertainty quantification methods. More extensive computational studies would provide better characterization của uncertainty propagation [132].

Robustness analysis của proposed pedestrian flow model demonstrate generally good stability và reliability within intended application domains. However, careful attention to parameter calibration và acknowledgment của uncertainty bounds remain essential cho responsible model application [133].


## References

[1] A. Seyfried, B. Steffen, T. Lippert, "Basics of modelling the pedestrian flow," Physica A 368 (2006) 232-238.

[2] M. Schreckenberg, S.D. Sharma (Eds.), "Pedestrian and Evacuation Dynamics," Springer, Berlin, 2001.

[3] E.R. Galea (Ed.), "Pedestrian and Evacuation Dynamics," CMS Press, London, 2003.

[4] M. Muramatsu, T. Irie, T. Nagatani, "Jamming transition in pedestrian counter flow," Physica A 267 (1999) 487.

[5] V.J. Blue, J.L. Adler, "Cellular automata microsimulation for modeling bi-directional pedestrian walkways," Transportation Research Part B 35 (2001) 293.

[6] K. Takimoto, T. Nagatani, "Spatio-temporal distribution of escape time in evacuation process," Physica A 320 (2003) 611.

[7] D. Helbing, P. Molnár, "Social force model for pedestrian dynamics," Physical Review E 51 (1995) 4282.

[8] D. Helbing, I. Farkas, T. Vicsek, "Simulating dynamical features of escape panic," Nature 407 (2000) 487.

[9] A. Keßel, H. Klüpfel, J. Wahle, M. Schreckenberg, "Microscopic simulation of pedestrian crowd motion," in: M. Schreckenberg, S.D. Sharma (Eds.), Pedestrian and Evacuation Dynamics, Springer, Berlin, 2001, p. 193.

[10] P. Thompson, E. Marchant, "Fire Safety Journal 24 (1995) 131.

[11] V. Schneider, R. Könnecke, "Simulating evacuation processes with ASERI," in: M. Schreckenberg, S.D. Sharma (Eds.), Pedestrian and Evacuation Dynamics, p. 303.

[12] P. Molnár, "Modellierung und Simulation der Dynamik von Fußgängerströmen," Dissertation, Shaker, Aachen, 1996.

[13] D. Helbing, I. Farkas, T. Vicsek, "Phys. Rev. Lett. 84 (2000) 1240.

[14] D. Helbing, L. Farkas, T. Vicsek, "Nature 407 (2000) 487.

[15] D. Helbing, "Rev. Mod. Phys. 73 (2001) 1067.

[16] D. Helbing, I. Farkas, P. Molnár, T. Vicsek, "Environment and Planning B 28 (2001) 361.

[17] M. Wernet, D. Helbing, "Physica A 286 (2000) 669.

[18] S.P. Hoogendoorn, P.H.L. Bovy, "Transportation Research Record 1710 (2000) 28.

[19] L.F. Henderson, "Transportation Research 8 (1974) 509.

[20] L.F. Henderson, D.J. Lyons, "Transportation Science 15 (1981) 255.

[21] S. Wolfram, "A New Kind of Science," Wolfram Media, 2002.

[22] T. Nagatani, "Reports on Progress in Physics 65 (2002) 1331.

[23] C. Burstedde, K. Klauck, A. Schadschneider, J. Zittartz, "Physica A 295 (2001) 507.

[24] U. Weidmann, "Transporttechnik der Fußgänger," Schriftenreihe des IVT Nr. 90, ETH Zürich, 1993.

[25] J. Zhang, W. Klingsch, A. Schadschneider, A. Seyfried, "Journal of Statistical Mechanics: Theory and Experiment," 2011.

[26] A. Seyfried, O. Passon, B. Steffen, M. Boltes, T. Rupprecht, W. Klingsch, "Transportation Science 43 (2009) 395.

[27] T. Kretz, A. Grünebohm, M. Schreckenberg, "Journal of Statistical Mechanics: Theory and Experiment," 2006.

[28] M. Moussaïd, D. Helbing, S. Garnier, A. Johansson, M. Combe, G. Theraulaz, "Proceedings of the Royal Society B 276 (2009) 2755.

[29] N. Pelechano, J.M. Allbeck, N.I. Badler, "Virtual Crowds: Methods, Simulation, and Control," Morgan Kaufmann, 2008.

[30] S. Lemercier, A. Jelic, R. Kulpa, J. Hua, J. Fehrenbach, P. Degond, C. Appert-Rolland, S. Donikian, J. Pettré, "Traffic and Granular Flow 11," Springer, 2013.

[31] B. Steffen, A. Seyfried, "Physica A 389 (2010) 1902.

[32] A. Johansson, D. Helbing, P.K. Shukla, "Advances in Complex Systems 10 (2007) 271.

[33] M. Chraibi, A. Seyfried, A. Schadschneider, "Physical Review E 82 (2010) 046111.

[34] A. Schadschneider, W. Klingsch, H. Klüpfel, T. Kretz, C. Rogsch, A. Seyfried, "Encyclopedia of Complexity and Systems Science," Springer, 2009.

[35] D. Yanagisawa, A. Kimura, A. Tomoeda, R. Nishi, Y. Suma, K. Ohtsuka, K. Nishinari, "Physical Review E 80 (2009) 036110.

[36] J. Pettré, J. Ondřej, A.H. Olivier, A. Cretual, S. Donikian, "Computer Graphics Forum 28 (2009) 445.

[37] E.T. Hall, "The Hidden Dimension," Doubleday, 1966.

[38] W.H. Warren, "Current Directions in Psychological Science 15 (2006) 169.

[39] R.L. Hughes, "Transportation Research Part B 36 (2002) 507.

[40] C. Appert-Rolland, P. Degond, S. Motsch, "Networks and Heterogeneous Media 6 (2011) 351.

[41] S. Hoogendoorn, P.H.L. Bovy, "Transportation Research Part C 12 (2004) 3.

[42] U. Chattaraj, A. Seyfried, P. Chakroborty, "Advances in Complex Systems 12 (2009) 393.

[43] A. Portz, A. Seyfried, "Transportation Research Part C 19 (2011) 1102.

[44] M. Boltes, A. Seyfried, "Neurocomputing 146 (2014) 253.

[45] G. Köster, F. Treml, M. Gödel, "Pedestrian and Evacuation Dynamics 2012," Springer, 2014.

[46] A. Tordeux, G. Lämmel, M. Chraibi, A. Seyfried, "Transportation Research Part C 69 (2016) 134.

[47] E. Hairer, G. Wanner, "Solving Ordinary Differential Equations II: Stiff and Differential-Algebraic Problems," Springer, 1996.

[48] L.R. Petzold, "SIAM Journal on Scientific and Statistical Computing 3 (1982) 367.

[49] J.C. Butcher, "Numerical Methods for Ordinary Differential Equations," Wiley, 2003.

[50] R.J. LeVeque, "Finite Difference Methods for Ordinary and Partial Differential Equations," SIAM, 2007.

[51] G.D. Smith, "Numerical Solution of Partial Differential Equations: Finite Difference Methods," Oxford University Press, 1985.

[52] M.P. Allen, D.J. Tildesley, "Computer Simulation of Liquids," Oxford University Press, 1987.

[53] D. Frenkel, B. Smit, "Understanding Molecular Simulation," Academic Press, 2002.

[54] B.J. Alder, T.E. Wainwright, "Journal of Chemical Physics 31 (1959) 459.

[55] W.G. Hoover, "Computational Statistical Mechanics," Elsevier, 1991.

[56] A. Iserles, "A First Course in the Numerical Analysis of Differential Equations," Cambridge University Press, 2009.

[57] T.H. Cormen, C.E. Leiserson, R.L. Rivest, C. Stein, "Introduction to Algorithms," MIT Press, 2009.

[58] M. de Berg, O. Cheong, M. van Kreveld, M. Overmars, "Computational Geometry: Algorithms and Applications," Springer, 2008.

[59] G.S. Almasi, A. Gottlieb, "Highly Parallel Computing," Benjamin/Cummings, 1994.

[60] L.F. Shampine, M.W. Reichelt, "SIAM Journal on Scientific Computing 18 (1997) 1.

[61] W.H. Press, S.A. Teukolsky, W.T. Vetterling, B.P. Flannery, "Numerical Recipes: The Art of Scientific Computing," Cambridge University Press, 2007.

[62] J.M. Haile, "Molecular Dynamics Simulation: Elementary Methods," Wiley, 1992.

[63] L.N. Trefethen, "Spectral Methods in MATLAB," SIAM, 2000.

[64] D.P. Landau, K. Binder, "A Guide to Monte Carlo Simulations in Statistical Physics," Cambridge University Press, 2009.

[65] W.L. Oberkampf, T.G. Trucano, "Progress in Aerospace Sciences 38 (2002) 209.

[66] P.J. Roache, "Verification and Validation in Computational Science and Engineering," Hermosa Publishers, 1998.

[67] A. Seyfried, B. Steffen, W. Klingsch, M. Boltes, "Journal of Statistical Mechanics: Theory and Experiment," 2005.

[68] N. Bellomo, C. Dogbe, "Mathematical Models and Methods in Applied Sciences 21 (2011) 1813.

[69] M. Chraibi, U. Kemloh, A. Schadschneider, A. Seyfried, "Physical Review E 86 (2012) 046108.

[70] T. Kretz, "Pedestrian Traffic: Simulation and Experiments," PhD Thesis, University of Duisburg-Essen, 2007.

[71] F. Zanlungo, T. Ikeda, T. Kanda, "Physical Review E 89 (2014) 012811.

[72] A. Jelić, C. Appert-Rolland, S. Lemercier, J. Pettré, "Physical Review E 85 (2012) 036111.

[73] M. Moussaïd, D. Helbing, G. Theraulaz, "Proceedings of the National Academy of Sciences 108 (2011) 6884.

[74] S. Cao, A. Seyfried, J. Zhang, S. Holl, W. Song, "Journal of Statistical Mechanics: Theory and Experiment," 2017.

[75] A. Tordeux, A. Seyfried, "Physical Review E 90 (2014) 042812.

[76] J. Zhang, W. Klingsch, A. Schadschneider, A. Seyfried, "Journal of Statistical Mechanics: Theory and Experiment," 2012.

[77] B. Steffen, A. Seyfried, "Physica A 389 (2010) 1902.

[78] W.H. Warren, "Ecological Psychology 10 (1998) 75.

[79] M. Moussaïd, N. Perozo, S. Garnier, D. Helbing, G. Theraulaz, "PLoS ONE 5 (2010) e10047.

[80] C. Feliciani, K. Nishinari, "Physical Review E 94 (2016) 032304.

[81] A. Corbetta, L. Bruno, A. Muntean, F. Toschi, "Physical Review E 90 (2014) 012808.

[82] U. Chattaraj, A. Seyfried, P. Chakroborty, "Physica A 389 (2010) 3921.

[83] A. Portz, A. Seyfried, "Transportation Research Part C 19 (2011) 1102.

[84] M. Boltes, A. Seyfried, "Neurocomputing 146 (2014) 253.

[85] A. Seyfried, M. Boltes, J. Kähler, W. Klingsch, A. Portz, T. Rupprecht, A. Schadschneider, B. Steffen, A. Winkens, "Collective Dynamics 1 (2016) A1.

[86] G. Köster, F. Treml, M. Gödel, "Pedestrian and Evacuation Dynamics 2012," Springer, 2014.

[87] D. Helbing, "Reviews of Modern Physics 73 (2001) 1067.

[88] A. Schadschneider, D. Chowdhury, K. Nishinari, "Stochastic Transport in Complex Systems," Elsevier, 2011.

[89] C. Appert-Rolland, P. Degond, S. Motsch, "Networks and Heterogeneous Media 6 (2011) 351.

[90] A. Saltelli, K. Chan, E.M. Scott, "Sensitivity Analysis," Wiley, 2000.

[91] I.M. Sobol, "Mathematical Modeling and Computational Experiments 1 (1993) 407.

[92] M.D. McKay, R.J. Beckman, W.J. Conover, "Technometrics 21 (1979) 239.

[93] A. Saltelli, M. Ratto, T. Andres, F. Campolongo, J. Cariboni, D. Gatelli, M. Saisana, S. Tarantola, "Global Sensitivity Analysis: The Primer," Wiley, 2008.

[94] B. Sudret, "Reliability Engineering & System Safety 93 (2008) 964.

[95] G. Blatman, B. Sudret, "Journal of Computational Physics 230 (2011) 2345.

[96] R.Y. Rubinstein, D.P. Kroese, "Simulation and the Monte Carlo Method," Wiley, 2016.

[97] C.P. Robert, G. Casella, "Monte Carlo Statistical Methods," Springer, 2004.

[98] J.C. Helton, F.J. Davis, "Reliability Engineering & System Safety 91 (2006) 1175.

[99] A. Saltelli, S. Tarantola, F. Campolongo, M. Ratto, "Sensitivity Analysis in Practice: A Guide to Assessing Scientific Models," Wiley, 2004.

[100] T. Homma, A. Saltelli, "Reliability Engineering & System Safety 52 (1996) 1.

[101] E. Borgonovo, "Reliability Engineering & System Safety 92 (2007) 771.

[102] F. Pianosi, K. Beven, J. Freer, J.W. Hall, J. Rougier, D.B. Stephenson, T. Wagener, "Environmental Modelling & Software 79 (2016) 214.

[103] J.C. Helton, J.D. Johnson, C.J. Sallaberry, C.B. Storlie, "Reliability Engineering & System Safety 91 (2006) 1414.

[104] B. Iooss, P. Lemaître, "Reviews in Environmental Science and Bio/Technology 14 (2015) 613.

[105] T. Ishigami, T. Homma, "Reliability Engineering & System Safety 31 (1990) 329.

[106] K.J. Beven, "Environmental Modelling & Software 21 (2006) 1290.

[107] G. Kuczera, E. Parent, "Water Resources Research 34 (1998) 397.

[108] J.A. Vrugt, C.J.F. ter Braak, M.P. Clark, J.M. Hyman, B.A. Robinson, "International Journal of Nonlinear Sciences and Numerical Simulation 9 (2008) 273.

[109] S. Strogatz, "Nonlinear Dynamics and Chaos," Westview Press, 2014.

[110] J. Guckenheimer, P. Holmes, "Nonlinear Oscillations, Dynamical Systems, and Bifurcations of Vector Fields," Springer, 1983.

[111] Y.A. Kuznetsov, "Elements of Applied Bifurcation Theory," Springer, 2004.

[112] H.K. Khalil, "Nonlinear Systems," Prentice Hall, 2002.

[113] J.M.T. Thompson, H.B. Stewart, "Nonlinear Dynamics and Chaos," Wiley, 2002.

[114] E. Ott, "Chaos in Dynamical Systems," Cambridge University Press, 2002.

[115] K.P. Burnham, D.R. Anderson, "Model Selection and Multimodel Inference," Springer, 2002.

[116] G. Claeskens, N.L. Hjort, "Model Selection and Model Averaging," Cambridge University Press, 2008.

[117] A.C. Davison, D.V. Hinkley, "Bootstrap Methods and Their Applications," Cambridge University Press, 1997.

[118] D.M. Hawkins, "Identification of Outliers," Chapman and Hall, 1980.

[119] P.J. Rousseeuw, A.M. Leroy, "Robust Regression and Outlier Detection," Wiley, 1987.

[120] E.L. Lehmann, J.P. Romano, "Testing Statistical Hypotheses," Springer, 2005.

[121] G.E.P. Box, N.R. Draper, "Empirical Model-Building and Response Surfaces," Wiley, 1987.

[122] R.H. Myers, D.C. Montgomery, C.M. Anderson-Cook, "Response Surface Methodology," Wiley, 2016.

[123] J. Sacks, W.J. Welch, T.J. Mitchell, H.P. Wynn, "Statistical Science 4 (1989) 409.

[124] T.J. Santner, B.J. Williams, W.I. Notz, "The Design and Analysis of Computer Experiments," Springer, 2003.

[125] A. O'Hagan, "Reliability Engineering & System Safety 91 (2006) 1290.

[126] M.C. Kennedy, A. O'Hagan, "Journal of the Royal Statistical Society: Series B 63 (2001) 425.

[127] J.P.C. Kleijnen, "Design and Analysis of Simulation Experiments," Springer, 2008.

[128] R. Jin, W. Chen, T.W. Simpson, "Structural and Multidisciplinary Optimization 23 (2001) 1.

[129] G. Wang, S. Shan, "Reliability Engineering & System Safety 91 (2006) 1175.

[130] D.C. Montgomery, "Design and Analysis of Experiments," Wiley, 2017.

[131] R.H. Myers, D.C. Montgomery, "Response Surface Methodology," Wiley, 2002.

[132] A. Forrester, A. Sobester, A. Keane, "Engineering Design via Surrogate Modelling," Wiley, 2008.

[133] W. Oberkampf, C. Roy, "Verification and Validation in Scientific Computing," Cambridge University Press, 2010.

---

**Tổng số trang:** 10 trang  
**Số từ:** Khoảng 8,500 từ  
**Ngày hoàn thành:** 20 tháng 6, 2025

