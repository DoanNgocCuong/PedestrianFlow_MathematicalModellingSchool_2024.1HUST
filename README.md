1. Slides: https://drive.google.com/drive/folders/1WPyf7A7b08HYqpUEWHTjR8QHi_zO1P8z?usp=sharing
2. Slides: https://drive.google.com/drive/folders/1T7ENrCeUCMN2mKRdtJ2jipN48uLl--F2?usp=sharing
3. Notebook LLMs: https://notebooklm.google.com/notebook/fc927178-87c4-4f01-8485-45a1d88139b5
4. Link record buổi presentation: https://youtu.be/VxJRxsW9tMA

---

```bash

Các nguồn này tập trung vào **mô hình hóa toán học**, một quy trình năm bước để giải quyết các vấn đề trong thế giới thực bằng cách dịch chúng sang ngôn ngữ toán học. Chúng khám phá ba loại mô hình chính: **mô hình tối ưu hóa** (bao gồm tối ưu hóa một biến, đa biến, lập trình tuyến tính và lập trình rời rạc), **mô hình động** (nghiên cứu các hệ thống thay đổi theo thời gian và trạng thái ổn định), và **mô hình xác suất** (xử lý sự không chắc chắn thông qua mô hình rời rạc, liên tục, quy trình Markov và mô phỏng Monte Carlo). Các văn bản cũng nhấn mạnh tầm quan trọng của **phân tích độ nhạy** và **tính mạnh mẽ** để đánh giá độ tin cậy của mô hình trước những thay đổi về giả định hoặc dữ liệu.
```

---

```bash
Dưới đây là một ví dụ chi tiết cho mỗi loại mô hình chính bạn đã đề cập, được trích dẫn từ các nguồn đã cung cấp:

## 1. Mô hình tối ưu hóa (Optimization Model)

Các mô hình tối ưu hóa nhằm mục đích tìm ra giá trị tối đa hoặc tối thiểu của một hàm mục tiêu bằng cách điều chỉnh các biến điều khiển, thường là để tối đa hóa lợi nhuận hoặc giảm thiểu chi phí.

### a. Tối ưu hóa một biến (One-variable optimization)

*   **Ví dụ: Bài toán bán heo**
    *   **Vấn đề**: Một con heo nặng 200 pound, tăng 5 pound mỗi ngày và chi phí nuôi là 45 xu mỗi ngày. Giá thị trường cho heo là 65 xu mỗi pound nhưng giảm 1 xu mỗi ngày. Khi nào nên bán con heo để tối đa hóa lợi nhuận?
    *   **Bước 1: Đặt câu hỏi**:
        *   **Các biến**:
            *   t = thời gian (ngày)
            *   w = trọng lượng heo (lbs)
            *   p = giá bán heo ($/lb)
            *   C = chi phí nuôi heo trong t ngày ($)
            *   R = doanh thu thu được khi bán heo ($)
            *   P = lợi nhuận từ việc bán heo ($)
        *   **Các giả định**:
            *   Trọng lượng heo: `w = 200 + 5t`
            *   Giá thị trường: `p = 0.65 - 0.01t`
            *   Chi phí nuôi: `C = 0.45t`
            *   Doanh thu: `R = p × w`
            *   Lợi nhuận: `P = R - C`
            *   Thời gian: `t ≥ 0`
        *   **Mục tiêu**: `Tối đa hóa P`.
    *   **Bước 2: Chọn phương pháp mô hình hóa**: Sử dụng phương pháp tối ưu hóa một biến, tìm điểm cực đại của một hàm khả vi `y = f(x)` trên một tập con của đường số thực bằng cách đặt đạo hàm `f'(x) = 0`.
    *   **Bước 3: Xây dựng mô hình**: Hàm lợi nhuận `P` được xây dựng dưới dạng hàm của `t`:
        `P = (0.65 - 0.01t)(200 + 5t) - 0.45t`.
        Đặt `y = P` và `x = t`, bài toán là tối đa hóa `f(x) = (0.65 - 0.01x)(200 + 5x) - 0.45x` trên tập `S = {x: x ≥ 0}`.
    *   **Bước 4: Giải mô hình**: Tính đạo hàm của `f(x)`: `f'(x) = (8 - x)/10`. Đặt `f'(x) = 0` để tìm điểm tối ưu, ta được `x = 8`. Tại `x = 8`, lợi nhuận `y = f(8) = 133.2`.
    *   **Bước 5: Trả lời câu hỏi**: Nên bán con heo sau 8 ngày để đạt được lợi nhuận ròng là 133.2 đô la.

### b. Tối ưu hóa đa biến (Multivariable optimization - không ràng buộc)

*   **Ví dụ: Bài toán kế hoạch sản xuất TV**
    *   **Vấn đề**: Một nhà sản xuất TV dự định giới thiệu hai sản phẩm mới: TV LCD 19 inch (giá bán lẻ đề xuất $339) và TV LCD 21 inch (giá bán lẻ đề xuất $399). Chi phí sản xuất là $195/chiếc 19 inch và $225/chiếc 21 inch, cộng thêm $400,000 chi phí cố định. Giá bán trung bình của mỗi loại TV giảm 1 cent cho mỗi đơn vị bán thêm. Ngoài ra, doanh số TV 19 inch ảnh hưởng đến TV 21 inch và ngược lại (giá TV 19 inch giảm 0.3 cent cho mỗi chiếc 21 inch bán ra, giá TV 21 inch giảm 0.4 cent cho mỗi chiếc 19 inch bán ra). Cần sản xuất bao nhiêu đơn vị mỗi loại để tối đa hóa lợi nhuận?
    *   **Bước 1: Đặt câu hỏi**:
        *   **Các biến**:
            *   s = số lượng TV 19 inch bán ra (mỗi năm)
            *   t = số lượng TV 21 inch bán ra (mỗi năm)
            *   p = giá bán TV 19 inch ($)
            *   q = giá bán TV 21 inch ($)
            *   C = chi phí sản xuất ($/năm)
            *   R = doanh thu ($/năm)
            *   P = lợi nhuận ($/năm)
        *   **Các giả định**:
            *   Giá bán TV 19 inch: `p = 339 - 0.01s - 0.003t`
            *   Giá bán TV 21 inch: `q = 399 - 0.004s - 0.01t`
            *   Tổng doanh thu: `R = ps + qt`
            *   Tổng chi phí: `C = 400,000 + 195s + 225t`
            *   Lợi nhuận: `P = R - C`
            *   Số lượng bán: `s ≥ 0`, `t ≥ 0`
        *   **Mục tiêu**: `Tối đa hóa P`.
    *   **Bước 2: Chọn phương pháp mô hình hóa**: Giải bài toán này như một bài toán tối ưu hóa đa biến không ràng buộc. Phương pháp chung là tìm các điểm mà tất cả các đạo hàm riêng của hàm mục tiêu bằng 0.
    *   **Bước 3: Xây dựng mô hình**: Hàm lợi nhuận `P` được biểu diễn dưới dạng hàm của `s` và `t`:
        `P = (339 - 0.01s - 0.003t)s + (399 - 0.004s - 0.01t)t - (400,000 + 195s + 225t)`.
        Đặt `y = P`, `x1 = s`, `x2 = t`, ta có `y = f(x1, x2)`.
    *   **Bước 4: Giải mô hình**: Để tìm điểm cực đại, tính các đạo hàm riêng và đặt chúng bằng 0:
        *   `∂f/∂x1 = 144 - 0.02x1 - 0.007x2 = 0`
        *   `∂f/∂x2 = 174 - 0.007x1 - 0.02x2 = 0`
        Giải hệ phương trình này, ta được `x1 ≈ 4735` và `x2 ≈ 7043`. Lợi nhuận tối đa tại điểm này là `y ≈ 553641`.
    *   **Bước 5: Trả lời câu hỏi**: Công ty có thể tối đa hóa lợi nhuận bằng cách sản xuất 4,735 chiếc TV 19 inch và 7,043 chiếc TV 21 inch, mang lại lợi nhuận ròng khoảng $553,641 mỗi năm.

### c. Lập trình tuyến tính (Linear Programming)

*   **Ví dụ: Bài toán tối ưu hóa trồng trọt**
    *   **Vấn đề**: Một nông trại có 625 mẫu đất để trồng trọt. Các loại cây trồng là ngô, lúa mì và yến mạch. Dự kiến có 1,000 acre-ft nước tưới và 300 giờ lao động mỗi tuần. Tìm lượng cây trồng mỗi loại để tối đa hóa lợi nhuận.
    *   **Bước 1: Đặt câu hỏi**:
        *   **Các biến**:
            *   `x1` = diện tích ngô trồng (acres)
            *   `x2` = diện tích lúa mì trồng (acres)
            *   `x3` = diện tích yến mạch trồng (acres)
            *   `w` = lượng nước tưới cần thiết (acre-ft)
            *   `l` = lượng lao động cần thiết (người-giờ/tuần)
            *   `t` = tổng diện tích trồng
            *   `y` = tổng lợi nhuận ($)
        *   **Các giả định**:
            *   Nước tưới: `w = 3.0x1 + 1.0x2 + 1.5x3`
            *   Lao động: `l = 0.8x1 + 0.2x2 + 0.3x3`
            *   Tổng diện tích: `t = x1 + x2 + x3`
            *   Tổng lợi nhuận: `y = 400x1 + 200x2 + 250x3`
            *   Ràng buộc nước: `w ≤ 1000`
            *   Ràng buộc lao động: `l ≤ 300`
            *   Ràng buộc đất: `t ≤ 625`
            *   Không âm: `x1 ≥ 0; x2 ≥ 0; x3 ≥ 0`
        *   **Mục tiêu**: `Tối đa hóa y`.
    *   **Bước 2: Chọn phương pháp mô hình hóa**: Mô hình hóa bài toán này như một bài toán lập trình tuyến tính, vì cả hàm mục tiêu và các hàm ràng buộc đều là tuyến tính.
    *   **Bước 3: Xây dựng mô hình**:
        *   **Các biến quyết định**: `x1, x2, x3`.
        *   **Hàm mục tiêu**: Tối đa hóa `y = 400x1 + 200x2 + 250x3`.
        *   **Các ràng buộc**:
            *   `3x1 + x2 + 1.5x3 ≤ 1000` (nước)
            *   `0.8x1 + 0.2x2 + 0.3x3 ≤ 300` (lao động)
            *   `x1 + x2 + x3 ≤ 625` (đất)
            *   `x1, x2, x3 ≥ 0`
    *   **Bước 4: Giải mô hình**: Sử dụng các thư viện phần mềm lập trình tuyến tính như Google OR-TOOLS.
    *   **Bước 5: Trả lời câu hỏi**: Giải pháp tối ưu là trồng 187.5 mẫu ngô, 437.5 mẫu lúa mì và không trồng yến mạch. Điều này dự kiến mang lại lợi nhuận $162,500. Kế hoạch này sử dụng toàn bộ 625 mẫu đất và 1,000 acre-ft nước tưới, nhưng chỉ 237.5 trong số 300 người-giờ lao động có sẵn mỗi tuần.

### d. Lập trình rời rạc (Discrete optimization - Lập trình số nguyên)

*   **Ví dụ: Bài toán trồng trọt (phiên bản số nguyên)**
    *   **Vấn đề**: Gia đình có 625 mẫu đất để trồng, bao gồm 5 mảnh 120 mẫu mỗi mảnh và 1 mảnh 25 mẫu. Gia đình muốn trồng mỗi mảnh đất chỉ một loại cây: ngô, lúa mì hoặc yến mạch. Tìm loại cây nên trồng ở mỗi mảnh đất để tối đa hóa lợi nhuận.
    *   **Bước 1: Đặt câu hỏi**: Tương tự như bài toán trồng trọt tuyến tính, nhưng các quyết định liên quan đến việc trồng trên các mảnh đất cụ thể, ngụ ý các biến phải là số nguyên.
    *   **Bước 2: Chọn phương pháp mô hình hóa**: Mô hình hóa bài toán này như một bài toán lập trình số nguyên (integer programming) vì các biến quyết định phải là số nguyên (ví dụ: số mảnh đất).
    *   **Bước 3: Xây dựng mô hình**:
        *   **Các biến quyết định**: Số lượng mảnh đất 120 mẫu và 25 mẫu để trồng ngô, lúa mì hoặc yến mạch (x1, x2, x3, x4, x5, x6). Các biến này phải là số nguyên (`x1, ..., x6 ∈ Z+`).
        *   **Hàm mục tiêu**: Tối đa hóa `y = 48000x1 + 24000x2 + 30000x3 + 10000x4 + 5000x5 + 6250x6` (lợi nhuận theo mảnh đất đã được điều chỉnh).
        *   **Các ràng buộc**: Tương tự như lập trình tuyến tính, nhưng các biến đại diện cho các mảnh đất được gán cho một loại cây trồng cụ thể.
    *   **Bước 4: Giải mô hình**: Sử dụng gói phần mềm chuyên dụng cho lập trình số nguyên. Giải pháp tối ưu `y = 156250` đạt được khi `x3 = 5` (trồng yến mạch trên 5 mảnh 120 mẫu), `x6 = 1` (trồng yến mạch trên mảnh 25 mẫu), và các biến quyết định khác bằng 0.
    *   **Bước 5: Trả lời câu hỏi**: Kế hoạch tốt nhất là trồng yến mạch trên tất cả các mảnh đất. Điều này mang lại tổng lợi nhuận dự kiến là $156,250 cho mùa vụ.

## 2. Mô hình động (Dynamic Model)

Mô hình động được sử dụng để biểu diễn hành vi thay đổi theo thời gian của các hệ thống, nghiên cứu các quá trình phát triển theo thời gian.

### a. Phân tích trạng thái ổn định (Steady state analysis)

*   **Ví dụ: Bài toán cạnh tranh cây gỗ trong rừng**
    *   **Vấn đề**: Trong một khu rừng không được quản lý, cây gỗ cứng và cây gỗ mềm cạnh tranh đất đai và nước. Cây gỗ cứng phát triển chậm hơn nhưng bền và có giá trị hơn. Cây gỗ mềm cạnh tranh bằng cách phát triển nhanh và tiêu thụ nước, chất dinh dưỡng. Cây gỗ cứng cạnh tranh bằng cách cao hơn và che bóng cây non gỗ mềm, cũng kháng bệnh tốt hơn. Liệu hai loại cây này có thể cùng tồn tại vĩnh viễn, hay một loại sẽ loại bỏ loại kia?
    *   **Bước 1: Đặt câu hỏi**:
        *   **Các biến**:
            *   `H` = quần thể gỗ cứng (tấn/mẫu Anh)
            *   `S` = quần thể gỗ mềm (tấn/mẫu Anh)
            *   `gH` = tốc độ tăng trưởng gỗ cứng (tấn/mẫu Anh/năm)
            *   `gS` = tốc độ tăng trưởng gỗ mềm (tấn/mẫu Anh/năm)
            *   `cH` = mất mát do cạnh tranh cho gỗ cứng (tấn/mẫu Anh/năm)
            *   `cS` = mất mát do cạnh tranh cho gỗ mềm (tấn/mẫu Anh/năm)
        *   **Các giả định**:
            *   `gH = r1H - a1H^2`
            *   `gS = r2S - a2S^2`
            *   `cH = b1SH`
            *   `cS = b2SH`
            *   `H ≥ 0, S ≥ 0`
            *   `r1, r2, a1, a2, b1, b2` là các số thực dương
        *   **Mục tiêu**: Xác định liệu `H → 0` hoặc `S → 0` (tức là một loài bị tuyệt chủng).
    *   **Bước 2: Chọn phương pháp mô hình hóa**: Mô hình hóa bài toán này như một mô hình động trong trạng thái ổn định (equilibrium point), nơi tốc độ thay đổi của các biến bằng 0.
    *   **Bước 3: Xây dựng mô hình**: Đặt `x1 = H` và `x2 = S` là các biến trạng thái. Các phương trình trạng thái ổn định được thiết lập bằng cách đặt tốc độ thay đổi của H và S bằng 0.
    *   **Bước 4: Giải mô hình**: Giải hệ phương trình trạng thái ổn định để tìm các điểm cân bằng. Có ba điểm giải pháp: `(0,0)`, và các điểm giao nhau của các đường. Với giả định bổ sung rằng ảnh hưởng của cạnh tranh giữa các thành viên cùng loài mạnh hơn cạnh tranh giữa các loài (`ai > bi`), điều kiện để cùng tồn tại là `r1/b1 > r2/a2` và `r2/b2 > r1/a1`.
    *   **Bước 5: Trả lời câu hỏi**: Điều kiện để hai loại cây cùng tồn tại là mỗi loại cây đạt đến điểm mà nó tự giới hạn sự tăng trưởng của mình trước khi nó đạt đến điểm mà nó giới hạn sự tăng trưởng của loại cây kia.

### b. Hệ thống động lực (Dynamical system - Continuous-time dynamics)

*   **Ví dụ: Bài toán cạnh tranh cá voi xanh và cá voi vây**
    *   **Vấn đề**: Cá voi xanh và cá voi vây cạnh tranh trong cùng một khu vực. Tốc độ tăng trưởng nội tại của mỗi loài được ước tính lần lượt là 5% và 8% mỗi năm. Sức chứa môi trường là 150,000 cá voi xanh và 400,000 cá voi vây. Sau 100 năm khai thác, quần thể cá voi giảm xuống khoảng 5,000 cá voi xanh và 70,000 cá voi vây. Liệu cá voi xanh có bị tuyệt chủng?
    *   **Bước 1: Đặt câu hỏi**:
        *   **Các biến**:
            *   `B` = số lượng cá voi xanh
            *   `F` = số lượng cá voi vây
            *   `gB` = tốc độ tăng trưởng quần thể cá voi xanh (mỗi năm)
            *   `gF` = tốc độ tăng trưởng quần thể cá voi vây (mỗi năm)
            *   `cB` = ảnh hưởng của cạnh tranh lên cá voi xanh (số cá voi mỗi năm)
            *   `cF` = ảnh hưởng của cạnh tranh lên cá voi vây (số cá voi mỗi năm)
        *   **Các giả định**:
            *   `gB = 0.05B(1 - B/150000)`
            *   `gF = 0.08F(1 - F/400000)`
            *   Ảnh hưởng cạnh tranh: `cB = cF = αBF` (với `α` là một số thực dương)
            *   `B ≥ 0, F ≥ 0`
        *   **Mục tiêu**: Xác định liệu hệ thống động lực có thể đạt đến trạng thái cân bằng ổn định bắt đầu từ `B = 5000` và `F = 70000`.
    *   **Bước 2: Chọn phương pháp mô hình hóa**: Mô hình hóa bài toán này như một hệ thống động lực, trong đó các lực thay đổi được biểu diễn bằng các phương trình vi phân.
    *   **Bước 3: Xây dựng mô hình**: Đặt `x1 = B` và `x2 = F`. Các phương trình hệ thống động lực được viết dưới dạng `dx1/dt = f1(x1, x2)` và `dx2/dt = f2(x1, x2)`, bao gồm các tốc độ tăng trưởng và ảnh hưởng cạnh tranh.
    *   **Bước 4: Giải mô hình**: Từ đồ thị hệ thống động lực, có 4 điểm cân bằng: `(0,0)`, `(150000, 0)`, `(0, 400000)`, và một điểm phụ thuộc vào `α`. Với điều kiện ban đầu `x1(0) = 5000`, `x2(0) = 70000`, giải pháp có xu hướng tiến đến điểm cân bằng thứ tư (nếu `α < 1.25 × 10^-7`).
    *   **Bước 5: Trả lời câu hỏi**: Nếu không có thêm khai thác, quần thể cá voi sẽ phát triển trở lại mức tự nhiên của chúng, và hệ sinh thái sẽ duy trì ở trạng thái cân bằng ổn định.

### c. Hệ thống động lực thời gian rời rạc (Discrete-time dynamic systems)

*   **Ví dụ: Bài toán điều khiển cập bến tàu vũ trụ**
    *   **Vấn đề**: Phi hành gia phải thực hành thao tác cập bến tàu vũ trụ, đưa một tàu vũ trụ đang bay vào trạng thái nghỉ so với một tàu khác. Các điều khiển tay cung cấp gia tốc và giảm tốc biến đổi. Một thiết bị đo tốc độ đóng giữa hai tàu. Chiến lược được đề xuất: nếu vận tốc đóng bằng 0 thì hoàn thành. Nếu không, ghi nhớ vận tốc đóng và điều chỉnh gia tốc ngược chiều và tỉ lệ với vận tốc đóng. Sau một thời gian, lại kiểm tra và lặp lại. Chiến lược này hiệu quả trong những trường hợp nào?
    *   **Bước 1: Đặt câu hỏi**:
        *   **Các biến**:
            *   `tn` = thời điểm quan sát vận tốc thứ `n` (giây)
            *   `vn` = vận tốc tại thời điểm `tn` (m/giây)
            *   `cn` = thời gian điều chỉnh thứ `n` (giây)
            *   `an` = gia tốc sau điều chỉnh thứ `n` (m/giây²)
            *   `wn` = thời gian chờ trước quan sát thứ `n+1` (giây)
        *   **Các giả định**:
            *   `tn+1 = tn + cn + wn`
            *   `vn+1 = vn + an-1cn + anwn`
            *   `cn ≥ 0, wn ≥ 0`
            *   `an = -kvn + εn` (trong đó `εn` là sai số ngẫu nhiên, `k` là hằng số)
        *   **Mục tiêu**: Xác định liệu `vn → 0` (vận tốc về 0).
    *   **Bước 2: Chọn phương pháp mô hình hóa**: Mô hình hóa bài toán này như một hệ thống động lực thời gian rời rạc.
    *   **Bước 3: Xây dựng mô hình**: Để đơn giản hóa phân tích, giả sử `cn = c` và `wn = w` là hằng số. Đặt `x1(n) = vn` và `x2(n) = vn-1`. Các phương trình sai phân là:
        *   `Δx1 = -kwx1 - kcx2` (thay đổi vận tốc)
        *   `Δx2 = x1 - x2` (vận tốc trước đó)
        Không gian trạng thái là `x1, x2 ∈ R2`.
    *   **Bước 4: Giải mô hình**: Có một điểm cân bằng `(0,0)` tại giao điểm của các đường khi `Δx1 = 0` và `Δx2 = 0`. Mặc dù biểu đồ vector trường gợi ý rằng các giải pháp có thể tiến về cân bằng, nhưng rất khó để xác định chắc chắn tính ổn định, đặc biệt nếu `k, c, w` lớn.
    *   **Bước 5: Trả lời câu hỏi**: Chiến lược điều khiển sẽ hiệu quả miễn là các điều chỉnh không quá mạnh. Thời gian giữa các điều chỉnh càng dài, các điều chỉnh đó phải càng nhẹ. Mối quan hệ là tỷ lệ: nếu đợi lâu gấp đôi giữa các điều chỉnh, chỉ có thể sử dụng một nửa lực điều khiển.

## 3. Mô hình xác suất (Probability Model)

Các mô hình xác suất được sử dụng để xử lý sự không chắc chắn và các yếu tố ngẫu nhiên trong các vấn đề thực tế.

### a. Mô hình xác suất rời rạc (Discrete probability model)

*   **Ví dụ: Bài toán kiểm soát chất lượng diode**
    *   **Vấn đề**: Một nhà sản xuất linh kiện điện tử sản xuất các loại diode. Ước tính 0.3% diode bị lỗi. Có thể kiểm tra từng diode (5 cent/chiếc) hoặc kiểm tra nhóm (4 + n cent/nhóm n > 1). Nếu kiểm tra nhóm thất bại, phải kiểm tra từng diode trong nhóm. Tìm quy trình kiểm soát chất lượng hiệu quả nhất về chi phí.
    *   **Bước 1: Đặt câu hỏi**:
        *   **Các biến**:
            *   `n` = số diode mỗi nhóm thử nghiệm
            *   `C` = chi phí thử nghiệm cho một nhóm (cents)
            *   `A` = chi phí thử nghiệm trung bình (cents/diode)
        *   **Các giả định**:
            *   Nếu `n = 1`, `A = 5` cents
            *   Nếu `n > 1`, `C = 4 + n` nếu tất cả diode tốt; `C = 4 + n + 5n` nếu nhóm thất bại (phải kiểm tra lại từng cái)
            *   Chi phí trung bình: `A = (Giá trị trung bình của C)/n`
        *   **Mục tiêu**: Tìm giá trị của `n` để tối thiểu hóa `A`.
    *   **Bước 2: Chọn phương pháp mô hình hóa**: Chọn một mô hình xác suất rời rạc, sử dụng khái niệm giá trị kỳ vọng `E[X] = ∑xi pi`.
    *   **Bước 3: Xây dựng mô hình**: Biến ngẫu nhiên `C` (chi phí) có hai giá trị có thể. Chi phí kỳ vọng của `C` là:
        `E[C] = (4 + n)p + [4 + n + 5n](1 - p)`
        trong đó `p` là xác suất tất cả các diode trong nhóm đều tốt.
    *   **Bước 4: Giải mô hình**: Xác suất một diode riêng lẻ tốt là `0.997`. Giả sử độc lập, xác suất tất cả `n` diode trong một nhóm đều tốt là `p = 0.997^n`.
        Chi phí thử nghiệm trung bình trên mỗi diode là: `A = (4/n) + 6 - 5(0.997)^n`.
        Tối thiểu hóa `A` theo `n` cho thấy giá trị tối thiểu của `A` là `1.48` cents/diode xảy ra tại `n = 17`.
    *   **Bước 5: Trả lời câu hỏi**: Bằng cách kiểm tra nhóm 17 diode mỗi lần, chi phí kiểm tra có thể giảm ba lần (xuống khoảng 1.5 cents/diode) mà không ảnh hưởng đến chất lượng.

### b. Mô hình xác suất liên tục (Continuous probability model)

*   **Ví dụ: Bài toán bộ đếm phân rã phóng xạ**
    *   **Vấn đề**: Một "bộ đếm loại I" được sử dụng để đo phân rã phóng xạ. Phân rã xảy ra ngẫu nhiên, với tốc độ không xác định. Mỗi phân rã khóa bộ đếm trong `3 × 10^-9` giây, trong thời gian đó, bất kỳ phân rã nào xảy ra đều không được đếm. Dữ liệu nhận được từ bộ đếm nên được điều chỉnh như thế nào để tính đến thông tin bị mất?
    *   **Bước 1: Đặt câu hỏi**:
        *   **Các biến**:
            *   `λ` = tốc độ phân rã (mỗi giây)
            *   `Tn` = thời điểm phân rã quan sát được thứ `n`
        *   **Các giả định**: Phân rã phóng xạ xảy ra ngẫu nhiên với tốc độ `λ`. Thời gian giữa hai phân rã quan sát được liên tiếp: `Tn+1 - Tn ≥ 3 × 10^-9` cho tất cả `n`.
        *   **Mục tiêu**: Tìm `λ` dựa trên số lượng hữu hạn các quan sát `T1, ..., Tn`.
    *   **Bước 2: Chọn phương pháp mô hình hóa**: Sử dụng mô hình xác suất liên tục, đặc biệt là phân phối mũ (exponential distribution) cho thời gian giữa các lần đến liên tiếp, vì nó có tính chất không nhớ.
    *   **Bước 3: Xây dựng mô hình**: Giả sử thời gian giữa các phân rã phóng xạ thực tế là độc lập và tuân theo phân phối mũ với tham số tốc độ `λ`.
        Đặt `Xn = Tn - Tn-1` là thời gian giữa các quan sát liên tiếp. `Xn` bao gồm thời gian khóa `a = 3 × 10^-9` giây và thời gian chờ bổ sung `Yn` cho đến phân rã tiếp theo. Nhờ tính chất không nhớ của phân phối mũ, `Yn` cũng tuân theo phân phối mũ với tốc độ `λ`.
    *   **Bước 4: Giải mô hình**: Kỳ vọng của `Yn` là `E[Yn] = 1/λ`. Do đó, `E[Xn] = a + 1/λ`.
        Theo luật số lớn, tổng trung bình của các quan sát `(X1 + ... + Xn)/n` sẽ tiến đến `a + 1/λ` khi `n → ∞`, nghĩa là `Tn/n → a + 1/λ`.
        Giải cho `λ`, ta được công thức: `λ = n / (Tn - na)`.
    *   **Bước 5: Trả lời câu hỏi**: Công thức đã tìm được cho phép điều chỉnh tốc độ phân rã để tính đến các phân rã bị bỏ lỡ khi bộ đếm bị khóa. Chỉ cần ghi lại tổng thời gian quan sát và số lượng phân rã được ghi lại.

### c. Chuỗi Markov (Markov chain)

*   **Ví dụ: Bài toán cửa hàng bán bể cá**
    *   **Vấn đề**: Một cửa hàng bán bể cá 20 gallon. Cuối mỗi tuần, quản lý kiểm kê và đặt hàng. Chính sách là đặt 3 bể mới nếu tất cả hàng tồn kho đã bán hết. Nếu còn dù chỉ một bể, không đặt hàng. Chính sách này dựa trên quan sát cửa hàng chỉ bán trung bình một bể mỗi tuần. Chính sách này có đủ để chống lại việc mất doanh số do khách hàng yêu cầu khi hết hàng không?
    *   **Bước 1: Đặt câu hỏi**:
        *   **Các biến**:
            *   `Sn` = nguồn cung bể cá vào đầu tuần `n`
            *   `Dn` = nhu cầu bể cá trong tuần `n`
        *   **Các giả định**:
            *   Nếu `Dn-1 < Sn-1`, thì `Sn = Sn-1 - Dn-1`
            *   Nếu `Dn-1 ≥ Sn-1`, thì `Sn = 3`
            *   Số lượng người mua tiềm năng trong một tuần có phân phối Poisson với trung bình một.
        *   **Mục tiêu**: Tính `Pr{Dn > Sn}` (xác suất nhu cầu vượt cung).
    *   **Bước 2: Chọn phương pháp mô hình hóa**: Sử dụng mô hình chuỗi Markov. Một chuỗi Markov là một mô hình ngẫu nhiên thời gian rời rạc, được mô tả như một chuỗi các bước nhảy ngẫu nhiên giữa các trạng thái.
    *   **Bước 3: Xây dựng mô hình**:
        *   **Không gian trạng thái**: `Xn = Sn`, số lượng bể cá trong kho vào đầu tuần bán hàng. Các trạng thái khả thi của `Xn` là `{1, 2, 3}`.
        *   **Ma trận chuyển đổi trạng thái (P)**: Được xây dựng dựa trên phân phối Poisson của nhu cầu `Dn` và chính sách đặt hàng của cửa hàng. (Ví dụ, nếu đang ở trạng thái 1 bể cá, và nhu cầu là 1 hoặc hơn, thì sẽ hết hàng và đặt 3 bể, chuyển sang trạng thái 3).
    *   **Bước 4: Giải mô hình**: Mục tiêu là tính xác suất `Pr(Dn > Sn)`. Để tìm xác suất này trong dài hạn, cần tìm phân phối trạng thái ổn định `π` của `Xn`. Phân phối trạng thái ổn định được xác định bởi phương trình `π = πP` và điều kiện tổng các xác suất bằng 1 (`∑πi = 1`).
        Giải hệ phương trình này, ta được `π = (0.285, 0.263, 0.452)` (đại diện cho xác suất có 1, 2, hoặc 3 bể cá trong kho ở trạng thái ổn định).
    *   **Bước 5: Trả lời câu hỏi**: Trong dài hạn, nhu cầu sẽ vượt cung khoảng 10% thời gian. Chính sách kiểm kê hiện tại dẫn đến mất doanh số khoảng 10% thời gian.

### d. Quy trình Markov (Markov process)

*   **Ví dụ: Bài toán bảo trì xe nâng hàng**
    *   **Vấn đề**: Một thợ cơ khí chịu trách nhiệm sửa chữa xe nâng hàng. Xe nâng hỏng được đưa đến cơ sở sửa chữa và được phục vụ theo thứ tự đến. Cơ sở có chỗ cho 27 xe. Xe nâng đến sửa chữa với tốc độ 4.5 xe/tháng. Tốc độ sửa chữa tối đa là 7.3 xe/tháng. Cần tìm số lượng xe trung bình đang sửa chữa và tỷ lệ thời gian thợ cơ khí bận sửa chữa?
    *   **Bước 1: Đặt câu hỏi**:
        *   **Các biến**: `Xt` = số lượng xe nâng trong cửa hàng sửa chữa tại thời điểm `t`.
        *   **Các giả định**:
            *   Xe nâng đến sửa chữa với tốc độ `λ = 4.5` xe/tháng.
            *   Tốc độ sửa chữa tối đa là `μ = 7.3` xe/tháng.
        *   **Mục tiêu**: Tính `E[Xt]` (số lượng xe trung bình đang sửa chữa) và `Pr{Xt > 0}` (tỷ lệ thời gian thợ cơ khí bận, tức là có xe trong xưởng).
    *   **Bước 2: Chọn phương pháp mô hình hóa**: Mô hình hóa cơ sở sửa chữa bằng một quy trình Markov. Một quy trình Markov là mô hình tương tự thời gian liên tục của chuỗi Markov. Đặc trưng bởi tính chất không nhớ.
    *   **Bước 3: Xây dựng mô hình**: `Xt` là số xe nâng đang sửa chữa. Vì cơ sở chỉ có thể chứa 27 xe, không gian trạng thái là `Xt ∈ {0, 1, 2, ..., 27}`. Các chuyển đổi được phép là từ `Xt = i` sang `Xt+1 = i + 1` (xe mới đến) hoặc `i - 1` (xe sửa xong). Các phương trình trạng thái ổn định được lấy từ biểu đồ tốc độ bằng nguyên tắc "Tốc độ ra = Tốc độ vào".
    *   **Bước 4: Giải mô hình**: Giải hệ phương trình trạng thái ổn định với điều kiện tổng các xác suất bằng 1 (`∑pi = 1`) để tìm `Pr{Xt = i}`. Xác suất `Pn = (λ/μ)^n P0` cho tất cả `n = 1, ..., 27`. Khi đó, `P0 = (1-α)/(1-α^28)` với `α = λ/μ`.
        Thay các giá trị `λ` và `μ` vào, ta tính được `Pr{Xt > 0} = 1 - P0 ≈ 0.616`.
        Kỳ vọng `E[Xt] = ∑iPi` được tính là `1.607`.
    *   **Bước 5: Trả lời câu hỏi**: Thợ cơ khí bận sửa chữa xe nâng khoảng 60% thời gian. Trung bình, có khoảng 1.6 xe trong cơ sở sửa chữa tại bất kỳ thời điểm nào.

### e. Mô phỏng Monte Carlo (Monte Carlo simulation)

*   **Ví dụ: Bài toán kỳ nghỉ (xác suất ngày mưa)**
    *   **Vấn đề**: Dự báo thời tiết địa phương cho biết 50% khả năng mưa mỗi ngày trong tuần. Xác suất có 3 ngày mưa liên tiếp là bao nhiêu?
    *   **Bước 1: Đặt câu hỏi**:
        *   **Các biến**: `Xt` = `0` nếu không mưa, `1` nếu mưa vào ngày `t`.
        *   **Các giả định**:
            *   `X1, X2, ..., X7` là độc lập
            *   `Pr{Xt = 0} = Pr{Xt = 1} = 1/2`
        *   **Mục tiêu**: Xác định xác suất `Xt = Xt+1 = Xt+2 = 1` cho một số `t = 1, 2, 3, 4` hoặc `5`.
    *   **Bước 2: Chọn phương pháp mô hình hóa**: Sử dụng mô phỏng Monte Carlo. Đây là một kỹ thuật tổng quát, tạo các giá trị ngẫu nhiên cho các biến theo phân phối xác suất của chúng và lặp lại nhiều lần để xác định kết quả trung bình.
    *   **Bước 3: Xây dựng mô hình**:
        *   **Thuật toán mô phỏng ngày mưa**:
            *   **Các biến**: `p` = xác suất một ngày mưa; `X(t)` = `1` nếu mưa vào ngày `t`, `0` nếu không; `Y` = `1` nếu có ít nhất 3 ngày mưa liên tiếp, `0` nếu không.
            *   **Đầu vào**: `p`.
            *   (Thuật toán sẽ bao gồm việc tạo một chuỗi 7 ngày (từ `X1` đến `X7`) với xác suất mưa 50% cho mỗi ngày, sau đó kiểm tra xem có chuỗi 3 ngày mưa liên tiếp nào không. Quá trình này được lặp lại nhiều lần).
    *   **Bước 4: Giải mô hình**: Chạy một chương trình máy tính thực hiện thuật toán với `p = 0.5` và `n = 100` lần lặp. Mô phỏng đếm được 43 tuần có mưa (có ít nhất 3 ngày mưa liên tiếp) trong 100 tuần. Các lần chạy bổ sung cũng cho kết quả tương tự, khoảng 40 tuần mưa trong 100.
    *   **Bước 5: Trả lời câu hỏi**: Nếu dự báo thời tiết là đúng, có khoảng 40% khả năng sẽ có ít nhất 3 ngày mưa liên tiếp trong tuần này. Kết quả tương tự cũng áp dụng cho những ngày nắng.
```