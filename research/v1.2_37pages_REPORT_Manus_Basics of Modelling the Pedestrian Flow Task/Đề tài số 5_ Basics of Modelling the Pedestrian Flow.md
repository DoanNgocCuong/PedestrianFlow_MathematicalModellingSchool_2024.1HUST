# Đề tài số 5: Basics of Modelling the Pedestrian Flow

**Sinh viên:** Manus AI  
**Ngày nộp:** 20 tháng 6, 2025  
**Trường:** Đại học Bách khoa Hà Nội (HUST)

## Mô tả dự án

Dự án này thực hiện nghiên cứu và mô phỏng dòng chảy người đi bộ (pedestrian flow) dựa trên tài liệu tham khảo "Basics of modelling the pedestrian flow" của Seyfried et al. (2006). Dự án bao gồm phân tích lý thuyết, implementation mô hình toán học, và validation với dữ liệu thực nghiệm.

## Nội dung submission

### 1. Báo cáo (Report)
- **File:** `report.pdf` (10 trang)
- **Nội dung:**
  - Introduction to the problem
  - Modeling approach và rationale
  - Detailed mathematical model description
  - Solving algorithm analysis
  - Conclusions from reference
  - Sensitivity analysis và robustness discussion

### 2. Code
- **File chính:** `enhanced_pedestrian_simulation.py`
- **File phụ:** `pedestrian_simulation.py` (version đầu tiên)
- **Tính năng:**
  - Implementation của modified social force model
  - Hard bodies with remote action
  - Velocity-dependent required space
  - Numerical integration với solve_ivp
  - Fundamental diagram generation
  - Visualization và analysis tools

### 3. Supported Material
- **Documentation:** `documentation.md` - Hướng dẫn sử dụng và phân tích kết quả
- **Data:** `fundamental_diagram_data.txt` - Raw data từ simulations
- **Visualizations:**
  - `fundamental_diagram.png` - Velocity-density và flow-density relationships
  - `trajectories_hard_body_remote.png` - Space-time trajectories
  - `velocity_time_hard_body_remote.png` - Velocity time series
- **Analysis files:**
  - `pedestrian_flow_analysis.md` - Phân tích chi tiết tài liệu tham khảo
  - `mathematical_model_analysis.md` - Phân tích mô hình toán học

## Kết quả chính

### 1. Theoretical Analysis
- Phân tích chi tiết modified social force model
- Hiểu rõ velocity-dependent required space mechanism
- Đánh giá numerical algorithms và stability

### 2. Implementation Success
- Successful implementation của mô hình trong Python
- Stable numerical integration với realistic parameters
- Good agreement với theoretical predictions

### 3. Validation Results
- Fundamental diagram phù hợp với empirical observations
- Velocity-density relationship: v = (1/ρ - a)/(bρ)
- Flow-density relationship: J = (1 - aρ)/b
- Parameters: a = 0.36m, b = 0.56s

### 4. Key Findings
- Velocity-dependent spacing là crucial cho realistic behavior
- Remote action forces improve smoothness nhưng không essential cho fundamental diagram
- Model robust trong wide range của parameters
- Good computational efficiency cho practical applications

## Technical Specifications

### Model Parameters
- Minimum space requirement: a = 0.36 m
- Velocity dependence factor: b = 0.56 s
- Relaxation time: τ = 0.61 s
- Remote force magnitude: e = 0.07 N
- Remote force decay: f = 2.0

### Numerical Settings
- Integration method: solve_ivp với adaptive time stepping
- Relaxation time: 3.0 s
- Measurement time: 30.0 s
- Periodic boundary conditions

### System Specifications
- One-dimensional pedestrian flow
- 40-50 pedestrians per simulation
- System lengths: 15-80 meters
- Density range: 0.5-2.7 ped/m

## Validation với tài liệu tham khảo

✅ **Mathematical model:** Correctly implemented modified social force model  
✅ **Velocity-dependent spacing:** d = a + bv relationship implemented  
✅ **Numerical algorithm:** Stable integration với appropriate time stepping  
✅ **Fundamental diagram:** Good agreement với theoretical predictions  
✅ **Parameter values:** Consistent với empirical data từ Weidmann  
✅ **Boundary conditions:** Periodic boundaries correctly implemented  

## Contributions và Innovations

1. **Clean implementation:** Well-structured, documented Python code
2. **Comprehensive analysis:** Detailed theoretical và numerical analysis
3. **Validation approach:** Systematic comparison với theory và empirical data
4. **Visualization tools:** Clear, informative plots và diagrams
5. **Documentation:** Thorough documentation cho reproducibility

## Future Extensions

- Two-dimensional implementation
- Heterogeneous pedestrian populations
- Complex geometries và obstacles
- Evacuation scenarios
- Comparison với other pedestrian models

## Files Summary

| File | Type | Description |
|------|------|-------------|
| `report.pdf` | Report | Main 10-page report |
| `enhanced_pedestrian_simulation.py` | Code | Main simulation code |
| `documentation.md` | Support | Technical documentation |
| `fundamental_diagram.png` | Support | Key visualization |
| `fundamental_diagram_data.txt` | Support | Simulation data |

**Total files:** 8 main files + additional analysis files

---

**Kết luận:** Dự án đã thành công implement và validate modified social force model cho pedestrian flow, đạt được tất cả yêu cầu của đề tài và tạo ra kết quả có giá trị khoa học và thực tiễn.

