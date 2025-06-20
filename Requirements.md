# 1. Hiểu yêu cầu: 

1. Notebook LLMs để xem môn này học gì? 

2. Xem presentation của 1 ông đề tài 1 

2. Tôi cần làm gì khi vào Project 5
```bash
**Giới thiệu về Dự Án 5: Basics of Modelling the Pedestrian Flow**

Dự án của bạn tập trung vào việc xây dựng và phân tích các mô hình toán học mô tả dòng người đi bộ (pedestrian flow). Đây là một chủ đề quan trọng trong lĩnh vực toán ứng dụng, đặc biệt liên quan đến an toàn công cộng, thiết kế đô thị, quản lý sự kiện lớn, và nghiên cứu hành vi con người trong các không gian đông đúc. Để chuẩn bị tốt cho project này, bạn cần thực hiện các bước sau:

---

**1. Nắm Vững Yêu Cầu Tổng Quát của Dự Án:**

- **Báo cáo:** Khoảng 10 trang, bao gồm các mục như giới thiệu, phân tích phương pháp mô hình hóa, mô tả chi tiết mô hình, thuật toán giải, kết luận, và bàn luận về độ nhạy cũng như tính ổn định của mô hình.
- **Code:** Viết lại trình mô phỏng đã được giới thiệu trong tài liệu tham khảo, chạy các mô phỏng như trong tài liệu.
- **Tài liệu hỗ trợ:** Có thể là dữ liệu, hình ảnh, hoặc bất kỳ file nào giúp minh họa và hỗ trợ cho báo cáo, mã code.
- **Nộp qua:** Teams, Assignment trước ngày 23/06/2025.

---

**2. Chuẩn Bị Kiến Thức Nền Tảng Cho Chủ Đề Dòng Người Đi Bộ:**

Bạn nên đọc và hiểu các tài liệu tham khảo được cung cấp trên Teams, đồng thời tìm hiểu thêm về các mô hình phổ biến như:

- **Mô hình tế bào tự động (Cellular Automata Model):** Chia không gian thành các ô vuông, mỗi người chiếm một ô và di chuyển theo các quy tắc đơn giản.
- **Mô hình xã hội lực (Social Force Model):** Mô tả chuyển động của mỗi người dưới tác động của các “lực xã hội” như lực hấp dẫn hướng tới mục tiêu, lực đẩy tránh va chạm với người khác và vật cản.
- **Các biến số chính:** Mật độ, vận tốc, hướng di chuyển, tương tác giữa các cá nhân, và ảnh hưởng của môi trường vật lý (tường, cửa, v.v.).

---

**3. Cấu Trúc Báo Cáo Cần Soạn:**

- **Giới thiệu vấn đề:** Trình bày lý do tại sao cần mô hình hóa dòng người đi bộ, các ứng dụng thực tiễn.
- **Phương pháp mô hình hóa:** Giải thích mô hình được tài liệu tham khảo lựa chọn, lý do chọn mô hình đó (ví dụ: ưu điểm về tính thực tế, khả năng mô phỏng đa dạng tình huống,…).
- **Mô tả chi tiết mô hình:** Bao gồm các giả định, biến số, công thức toán học, và các bước xây dựng mô hình.
- **Thuật toán giải:** Trình bày cách giải mô hình (giả sử là mô phỏng bằng máy tính), các bước thực hiện, sơ đồ thuật toán nếu cần.
- **Kết luận theo tài liệu tham khảo:** Tóm tắt kết quả và nhận định chính.
- **Phân tích độ nhạy và độ bền vững:** Xem xét nếu thay đổi các tham số đầu vào (ví dụ: mật độ người, tốc độ di chuyển), kết quả mô hình có ổn định không, mô hình có nhạy cảm với tham số nào không.
- **Thảo luận mở rộng:** Đề xuất hướng cải tiến hoặc nhận xét về giới hạn của mô hình.

---

**4. Chuẩn Bị Code và Chạy Mô Phỏng:**

- **Lựa chọn ngôn ngữ lập trình:** Python là lựa chọn phổ biến nhờ thư viện mạnh cho mô phỏng và trực quan hóa (matplotlib, numpy, v.v.).
- **Cài đặt môi trường:** Đảm bảo bạn có đầy đủ các thư viện cần thiết và môi trường lập trình phù hợp.
- **Viết lại mô phỏng:** Dựa trên mô hình và giải thuật đã mô tả, viết mã mô phỏng dòng người.
- **Chạy các thí nghiệm như trong tài liệu tham khảo:** So sánh kết quả, vẽ đồ thị minh họa.
- **Kiểm tra lại mã nguồn:** Đảm bảo code rõ ràng, dễ chạy, có chú thích.

---

**5. Tài Liệu Hỗ Trợ:**

- **Dữ liệu đầu vào:** Nếu tài liệu tham khảo có sử dụng dữ liệu cụ thể (sơ đồ phòng, vị trí xuất phát, v.v.), chuẩn bị file dữ liệu.
- **Hình ảnh, sơ đồ:** Chụp lại các biểu đồ kết quả, sơ đồ minh họa dòng người, v.v. để đưa vào báo cáo.
- **Tài liệu tham khảo:** Đính kèm file PDF hoặc link tài liệu được sử dụng.

---

**6. Lập Kế Hoạch Thời Gian:**

- **Tuần đầu:** Đọc kỹ tài liệu tham khảo, xác định rõ mô hình, thuật toán.
- **Tuần thứ hai:** Viết báo cáo phần lý thuyết, cài đặt code mô phỏng.
- **Tuần thứ ba:** Hoàn thiện mô phỏng, chạy các thí nghiệm, tạo biểu đồ, hoàn tất báo cáo, chuẩn bị file nộp.

---

**7. Một số lời khuyên thực tế:**

- **Ghi chú cẩn thận khi đọc tài liệu tham khảo.**
- **Liên hệ thầy/cô hoặc các bạn nếu có chỗ không hiểu về mô hình hoặc thuật toán.**
- **Chạy thử code nhiều lần để đảm bảo tính đúng đắn.**
- **Kiểm tra lại toàn bộ các file trước khi nộp.**

---

Chúc bạn hoàn thành tốt project này! Nếu bạn cần hướng dẫn chi tiết về mô hình (ví dụ: mô hình xã hội lực, hoặc code mẫu), hãy hỏi thêm, tôi sẽ hỗ trợ chi tiết hơn.
```

4. thầy cô yêu cầu đọc tài liệu ngoài hay tài liệu thầy cô đã gửi? 
```bash
**Yêu Cầu Về Tài Liệu Tham Khảo:**

Dựa trên thông tin bạn cung cấp, **tài liệu tham khảo chính là tài liệu thầy cô đã gửi trên Teams**. Cụ thể, trong phần hướng dẫn dự án, thầy cô ghi rõ:

> **"References for the topics can be downloaded from the class Teams"**  
> (Các tài liệu tham khảo cho các chủ đề có thể được tải về từ Teams của lớp)

Và trong phần yêu cầu báo cáo có câu:

> **"What is the modeling approach chosen by the reference, and why was that approach selected?"**  
> (Phương pháp mô hình hóa được tài liệu tham khảo lựa chọn là gì, và vì sao lại chọn phương pháp đó?)

Điều này cho thấy **bắt buộc bạn phải sử dụng và phân tích nội dung từ tài liệu mà thầy cô đã cung cấp trên Teams** cho chủ đề "Basics of modelling the pedestrian flow". Toàn bộ cấu trúc báo cáo, mô tả mô hình, thuật toán giải và kết quả mô phỏng đều cần bám sát tài liệu tham khảo này.

---

**Có Cần Đọc Tài Liệu Ngoài Không?**

- **Không bắt buộc:** Thầy cô không yêu cầu phải đọc thêm tài liệu ngoài để hoàn thành báo cáo hay mô phỏng.
- **Có thể bổ sung:** Tuy nhiên, nếu bạn muốn mở rộng phần thảo luận, nhận xét, hoặc muốn hiểu sâu hơn, bạn hoàn toàn có thể đọc thêm các tài liệu ngoài. Điều này sẽ giúp bạn:
  - Hiểu rõ hơn về lý thuyết, các mô hình khác nhau.
  - So sánh, mở rộng, hoặc đề xuất cải tiến mô hình trong phần thảo luận.
  - Thể hiện sự chủ động và sáng tạo, điều này thường được đánh giá cao.

---

**Tóm Lại:**

- **Bắt buộc:** Sử dụng và phân tích kỹ tài liệu thầy cô đã gửi (trên Teams).
- **Không bắt buộc** nhưng **khuyến khích**: Đọc thêm tài liệu ngoài nếu muốn làm phong phú báo cáo.

Nếu bạn chưa tìm thấy tài liệu trên Teams, hãy liên hệ ngay với thầy/cô để được cung cấp lại, hoặc hỏi các bạn trong lớp để đảm bảo không bị thiếu thông tin quan trọng.

---

**Nếu bạn muốn, tôi cũng có thể giúp bạn tìm hiểu các tài liệu ngoài liên quan đến modelling pedestrian flow bằng tiếng Anh hoặc tiếng Việt để bổ sung cho phần thảo luận.**
```

---

# 2. Actions:

### Prompt: 

Đính kèm 2 file: 1 file: project annoucemnent.pdf, 1 file: Basics of modelling the pedestrian flow.pdf
```bash
TÔI ĐƯỢC GIAO ĐỀ TÀI SỐ 5: Với chủ đề bạn được giao là "Basics of modelling the pedestrian flow",

đỌC VÀ LÀM THEO YÊU CẦU NHƯ TRONG THÔNG BÁO: project annoucement.pdf 
-> output 

General requirements
 1. Report
 • Introduction to the problem
 • What is the modeling approach chosen by the reference, and why was that 
approach selected?
 • Detailed description of the mathematical model
 • What is the solving algorithm?
 • What is the conclusion from the reference?
 • Discussion about the sensitivity analysis and robustness of the proposed model
 2. Code
 • Reimplement the simulator introduced in the reference
 • Run some simulations mentioned in the reference
 6
Project allocation

Submission
 • Submission includes 3 files:
 • Report of  approximately 10 pages
 • Code
 • Supported material
 • Submission system: Teams, Assignment
 • Deadline: 23 June 2025
```



### Output

#### Output 1: todo.md
```bash
# TODO for Project: Basics of modelling the pedestrian flow

- [ ] Đọc kỹ yêu cầu từ project annoucement.pdf và bài báo gốc
- [ ] Lập dàn ý chi tiết cho báo cáo (~10 trang)
- [ ] Viết phần Giới thiệu vấn đề
- [ ] Trình bày phương pháp mô hình hóa được chọn và lý do chọn
- [ ] Mô tả chi tiết mô hình toán học
- [ ] Trình bày thuật toán giải quyết mô hình
- [ ] Tổng kết kết quả và kết luận từ bài báo
- [ ] Thảo luận về phân tích độ nhạy và độ vững của mô hình
- [ ] Viết code mô phỏng lại mô hình trong bài báo
- [ ] Chạy các mô phỏng như trong bài báo, lưu kết quả
- [ ] Tổng hợp tài liệu hỗ trợ (hình ảnh, dữ liệu, v.v.)
- [ ] Biên tập, hoàn thiện báo cáo (~10 trang)
- [ ] Đóng gói file nộp: báo cáo, code, tài liệu hỗ trợ

```

#### Output 2: outline.md

```bash
# Dàn ý chi tiết cho báo cáo (~10 trang)

1. Giới thiệu vấn đề
   - Tầm quan trọng của mô hình hóa dòng người đi bộ
   - Ứng dụng thực tiễn: thiết kế lối thoát hiểm, cơ sở hạ tầng, nghiên cứu lý thuyết
   - Các thách thức trong mô hình hóa hành vi tập thể của người đi bộ

2. Phương pháp mô hình hóa được chọn và lý do chọn
   - Tổng quan các phương pháp: mô hình ô-lưới (cellular automata), mô hình liên tục (continuous space)
   - Lý do chọn mô hình lực xã hội (social force model) và biến thể một chiều
   - Ưu điểm của mô hình này trong việc tái hiện các đặc trưng thực nghiệm

3. Mô tả chi tiết mô hình toán học
   - Trình bày phương trình chuyển động cơ bản của mô hình lực xã hội
   - Phân tích các thành phần: lực thúc đẩy, lực đẩy từ xa, độ dài cần thiết phụ thuộc vận tốc
   - Các biến số, tham số và ý nghĩa vật lý
   - So sánh hai biến thể: hard body không có lực từ xa và hard body có lực từ xa

4. Thuật toán giải quyết mô hình
   - Mô tả thuật toán giải tích số (Euler explicit, cập nhật vị trí, vận tốc)
   - Xử lý điều kiện biên tuần hoàn, cập nhật va chạm, dừng chuyển động
   - Đặc điểm riêng của từng biến thể mô hình

5. Kết quả và kết luận từ bài báo
   - So sánh kết quả mô phỏng với dữ liệu thực nghiệm (biểu đồ vận tốc – mật độ)
   - Ảnh hưởng của các tham số lên kết quả
   - Nhận xét về khả năng tái hiện hiện tượng thực tế

6. Thảo luận về phân tích độ nhạy và độ vững của mô hình
   - Phân tích độ nhạy của mô hình với các tham số (a, b, e, f, t)
   - Độ vững của mô hình khi thay đổi điều kiện ban đầu, phân bố vận tốc ý định
   - Hạn chế và hướng phát triển tiếp theo

7. Tài liệu tham khảo
   - Trích dẫn bài báo gốc và các tài liệu liên quan

8. Phụ lục (nếu cần)
   - Mã nguồn mô phỏng, hình ảnh, dữ liệu hỗ trợ
```
