# Bài 011 — Ánh sáng, bokeh và nhịp chậm: ôn tập qua bộ ảnh trùng B008

Đã mở trực tiếp 18 ảnh của B011. Đối chiếu SHA-256 cho thấy 18/18 tệp trùng từng byte với ảnh B008, dù tên thư mục khác. Vì vậy đây là cùng bộ mười cụm prompt; bài giữ bản đọc và nguồn riêng, liên kết bài cũ, bổ sung bài tập chọn vùng nét và nhịp cho cảnh thao tác nông thôn.

**Nguồn:** [Bí Mật Cinematic Với Prompt Veo3.1- Dùng Golden Hour, Bokeh và Slow Motion Để Tạo Ra Video AI Chuẩn Hollywood](https://drive.google.com/drive/folders/1BwpHpUkcMaVEYLEZKiPSXNTDTq2S7I15). Đã đọc **18/18 ảnh**. Ngày biên soạn: 17/10/2026.

[Đọc từng ảnh](doc-anh.md) · [Bài thực hành](thuc-hanh.md) · [Nguồn và mã kiểm tra](nguon.json) · [Danh mục toàn bộ](../../DANH-MUC-BAI-HOC.md)

**Quy ước:** phần “Nguồn” diễn đạt ý trong bộ ảnh. Phần “Phân tích và áp dụng” do người biên soạn bổ sung. Hiệu quả của câu lệnh chưa được kiểm nghiệm bằng lần tạo video trong đợt này.

## Những điều cần học

| Nội dung | Mã ảnh nguồn |
| --- | --- |
| Bảng tra đủ mười cụm | B011-04, B011-05, B011-06, B011-08, B011-09, B011-10, B011-12, B011-13, B011-14, B011-15, B011-17 |
| Thiết kế ánh sáng có nguồn và hướng | B011-03, B011-04, B011-05, B011-06 |
| Chuyển động máy và vùng nét dẫn chú ý | B011-07, B011-08, B011-09, B011-10 |
| Màu, tốc độ và âm thanh hoàn thiện ý đồ | B011-11, B011-12, B011-13, B011-14, B011-15 |
| Chọn bokeh và nhịp chậm cho thao tác có ý nghĩa | B011-10, B011-13 |

## 1. Bảng tra đủ mười cụm

**Nguồn:** Bộ ảnh gọi đây là mười cú pháp để nâng chất lượng hình ảnh.

**Phân tích và áp dụng:** Đây là các cụm mô tả bằng ngôn ngữ tự nhiên. Có thể viết bằng lời rõ hơn để phục vụ shot. Không có bằng chứng chúng là lệnh khóa hoặc luôn được thực hiện chính xác.

| Cụm trong nguồn | Nghĩa | Cách kiểm |
| --- | --- | --- |
| golden hour lighting | Ánh sáng giờ vàng | Nắng thấp có hướng; giữ chi tiết mặt. |
| soft rim light behind the subject | Viền sáng mềm từ phía sau | Tóc/vai có viền theo đúng phía nguồn sáng. |
| soft fog + volumetric light beams | Sương nhẹ và chùm sáng trong không khí | Tia đi từ nguồn hợp lý, không che mất hành động. |
| wide shot, slow dolly-in | Toàn cảnh, máy tiến chậm | Máy thực sự tiến tới; nền đổi tương quan phối cảnh. |
| tracking shot following the character from behind | Máy bám theo phía sau | Khoảng cách và hướng đi ổn định. |
| shallow depth of field, creamy bokeh | Vùng nét nông, nền mờ mịn | Chi tiết kể chuyện còn ở vùng nét. |
| cinematic color grading, warm tones + teal shadows | Chỉnh màu với tông ấm và bóng xanh ngả lục | Màu da và tính liên tục vẫn hợp ý đồ. |
| slow motion 30% | Chuyển động chậm, mục tiêu tốc độ 30% | Kiểm thời gian; cần chính xác thì chỉnh tốc độ ở khâu dựng. |
| soft ambient wind + natural ambience | Gió nền nhẹ và tiếng môi trường tự nhiên | Nguồn tiếng, mức âm và thời điểm hợp cảnh. |
| Negative: no flicker, no jitter, no distortion | Loại trừ nhấp nháy, giật và biến dạng | Chuyển sang cú pháp được công cụ hỗ trợ; xem toàn clip. |

**Ví dụ cho cảnh nông thôn:** Cảnh cơm chiều chỉ cần ánh nắng thấp, trung cảnh máy đứng và tiếng chén bát; không nhất thiết thêm sương, tracking hay bóng xanh.

**Kiểm tra kết quả:** Mỗi cụm thêm vào phải tạo một đặc điểm có thể quan sát hoặc nghe được.

## 2. Thiết kế ánh sáng có nguồn và hướng

**Nguồn:** Giờ vàng, viền sáng và sương/tia giúp tạo không khí và tách lớp.

**Phân tích và áp dụng:** Nêu vị trí cửa, mặt trời hoặc đèn; xác định mặt sáng, mặt tối và nền. Haze/sương vừa đủ làm rõ tia nhưng có thể làm giảm tương phản nếu quá dày. Giữ hướng sáng xuyên shot.

**Ví dụ cho cảnh nông thôn:** Mặt trời thấp phía sân trái tạo viền tóc Lan, ánh hắt từ tường sáng giữ chi tiết mặt; không thêm tia sáng từ bức tường kín.

**Kiểm tra kết quả:** Bóng và viền sáng cùng chỉ về nguồn hợp lý; mặt đọc được, không bị cháy viền.

![Minh họa nguồn B011-06](anh-goc/06.jpg)

## 3. Chuyển động máy và vùng nét dẫn chú ý

**Nguồn:** Máy tiến, máy bám và nền mờ tập trung người xem vào chủ thể.

**Phân tích và áp dụng:** Ghi điểm đầu/cuối, phía máy và khoảng cách cần giữ. Độ sâu trường ảnh nông chỉ có ích khi không che thông tin quan trọng. Phân biệt nền mờ do mất nét với nhòe chuyển động hoặc hiệu ứng kéo hướng tâm.

**Ví dụ cho cảnh nông thôn:** Máy bám sau Lan vào hiên; khi cô dừng, dùng cận mặt riêng để thấy phản ứng, thay vì vừa bám vừa tiến vừa đổi nét phức tạp.

**Kiểm tra kết quả:** Không nhảy cỡ cảnh; mắt hoặc đạo cụ mục tiêu luôn nét đúng lúc; nền không chảy.

![Minh họa nguồn B011-09](anh-goc/09.jpg)

## 4. Màu, tốc độ và âm thanh hoàn thiện ý đồ

**Nguồn:** Nguồn đề xuất màu ấm/bóng xanh, slow motion, âm thanh nền và loại trừ lỗi.

**Phân tích và áp dụng:** Chọn bảng màu theo tâm trạng. Slow motion thay nhịp thời gian, khác người tự di chuyển chậm. Nếu cần tốc độ đúng 30% so với thời gian thực, đo và xử lý trong dựng. Âm thanh môi trường cần vị trí, cường độ và nhịp; phần loại trừ tham khảo bài 006.

**Ví dụ cho cảnh nông thôn:** Giữ màu da tự nhiên trong bữa cơm; tiếng gió ngoài sân thấp hơn tiếng rổ chạm bàn, không dùng slow motion cho mọi động tác.

**Kiểm tra kết quả:** Xem liền với shot trước/sau; màu và nhịp hỗ trợ câu chuyện, âm không lấn hành động.

![Minh họa nguồn B011-12](anh-goc/12.jpg)

## 5. Chọn bokeh và nhịp chậm cho thao tác có ý nghĩa

**Nguồn:** Nguồn khuyên nền mờ và slow motion để tăng chú ý vào chủ thể, chi tiết.

**Phân tích và áp dụng:** Xem [bài 008](../008-muoi-cu-phap-veo/README.md) cho bảng tra gốc. Phần bổ sung ở đây: với thao tác thủ công, vùng nét phải chứa cả ngón tay, dụng cụ và điểm tiếp xúc. Nền mờ chỉ giảm nhiễu; không làm mờ hành động cần chứng minh. Nhịp chậm dùng cho khoảnh khắc đáng quan sát; timelapse (nén thời gian) là lựa chọn ngược lại và không nên ghép vô điều kiện.

**Ví dụ cho cảnh nông thôn:** Cận tay cô gái tách sợi tre: giữ lưỡi dụng cụ và bề mặt tre rõ nét, vườn phía sau mềm; động tác chạy ở tốc độ thật trước khi cân nhắc bản chậm.

**Kiểm tra kết quả:** Theo dõi điểm chạm từ đầu tới cuối; dụng cụ không xuyên tay, tre không tự mọc hoặc đổi hình. Nêu rõ tốc độ mong muốn và kiểm trong clip.

![Minh họa nguồn B011-10](anh-goc/10.jpg)

## Điểm cần hiểu có điều kiện

- B011 trùng 18/18 tệp ảnh với B008 theo SHA-256 và cùng thứ tự. Số ảnh đã đọc trong danh mục là lượt tệp theo thư mục, không phải số hình hoặc kỹ thuật độc nhất.
- Câu chỉ do ngôn ngữ mà video kém bỏ qua giới hạn công cụ, đầu vào và khâu chọn/dựng.
- Các cặp ảnh thay đổi nhiều yếu tố; không đủ kết luận thêm một cụm gây cải thiện trong mọi video.
- Rim light không tự tách chủ thể hoàn toàn; bokeh và sương cũng không luôn tăng chất lượng.
- Ảnh tĩnh không chứng minh dolly, tracking, slow motion, âm thanh hoặc giảm flicker/jitter.
- slow motion 30% là mô tả mục tiêu, không phải tham số bảo đảm tỉ lệ thời gian.
- Màu ấm/bóng xanh là một kiểu tạo hình, không đồng nghĩa điện ảnh hoặc Hollywood.
- Đối với Veo có trường negative, hướng dẫn Google khuyên liệt kê yếu tố không mong muốn thay vì nhiều câu no.

## Cách đưa vào quy trình sản xuất

Chọn thông tin và cảm xúc shot → thiết kế ánh sáng → chọn một đường máy hoặc máy đứng → quyết định vùng nét → hoàn thiện màu, nhịp, âm thanh → thử và kiểm toàn clip. Mỗi lần sửa ưu tiên một nhóm để biết điều gì thay đổi.

## Tự kiểm tra kiến thức

- Ảnh gần hơn có đủ chứng minh máy dolly-in không?
- Khi nào nền mờ làm mất thông tin cần thiết?
- Tốc độ 30% và 30 fps khác nhau ở đâu?

## Nguồn đối chiếu bổ sung

- [Google — Video generation prompt guide](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/video-gen-prompt-guide): Đối chiếu cách mô tả ánh sáng, vùng nét, thời gian, âm và nội dung loại trừ.

**Giới hạn:** đây là tài liệu học từ ảnh. Không dùng một hình minh họa để xác nhận chuyển động, thời lượng, độ chính xác thao tác hay khả năng hiện tại của một sản phẩm. Những phần chưa kiểm chứng được ghi rõ trong bản đọc ảnh.
