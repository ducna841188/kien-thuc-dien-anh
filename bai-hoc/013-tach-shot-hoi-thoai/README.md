# Bài 013 — Tách shot hội thoại và giữ tính liên tục

Bài học từ 16 tệp ảnh (có một cặp trùng) về shot–reverse shot: chia việc cho từng shot, xác định người nói, giữ nhân vật/bối cảnh và ráp nhịp. Có chú giải các tuyên bố tuyệt đối và mẫu thực hành đối thoại ở hiên nhà.

**Nguồn:** [Bí Mật Prompt Veo3.1 - Tách Shot Để AI Bám Lệnh (Hội Thoại Không Quay Bằng Một Shot)](https://drive.google.com/drive/folders/1DcfzftcYU9njo4dJcM3AXgUjWpFPsqMA). Đã đọc **16/16 ảnh**. Ngày biên soạn: 17/10/2026.

[Đọc từng ảnh](doc-anh.md) · [Bài thực hành](thuc-hanh.md) · [Nguồn và mã kiểm tra](nguon.json) · [Danh mục toàn bộ](../../DANH-MUC-BAI-HOC.md)

**Quy ước:** phần “Nguồn” diễn đạt ý trong bộ ảnh. Phần “Phân tích và áp dụng” do người biên soạn bổ sung. Hiệu quả của câu lệnh chưa được kiểm nghiệm bằng lần tạo video trong đợt này.

## Những điều cần học

| Nội dung | Mã ảnh nguồn |
| --- | --- |
| Chia theo nhiệm vụ của shot | B013-00, B013-01, B013-02, B013-04, B013-05 |
| Dựng đối đáp và giữ trục nhìn | B013-03, B013-07, B013-09, B013-10 |
| Giữ bối cảnh và nhận diện | B013-06, B013-07, B013-13 |
| Chỉ rõ lời thoại và phản ứng | B013-08, B013-09, B013-10, B013-13 |
| Chẩn đoán rồi sửa đúng shot | B013-12, B013-13, B013-14, B013-15 |

## 1. Chia theo nhiệm vụ của shot

**Nguồn:** Nguồn đề xuất tách hội thoại thành shot ngắn để tập trung lời, cảm xúc và sửa riêng đoạn lỗi.

**Phân tích và áp dụng:** Shot là đoạn hình liên tục giữa hai lần cắt; scene là cảnh có thể gồm nhiều shot. Trước khi chia, ghi ai muốn gì và thông tin thay đổi ở mỗi lượt. Chỉ cắt khi cần đổi chú ý, phản ứng hoặc nhấn chi tiết. Hội thoại cũng có thể ở two-shot (khung hai người) hay long take (cú máy dài).

**Ví dụ cho cảnh nông thôn:** A hỏi thời điểm gieo, B trả lời rồi nhìn trời. Có thể giữ hai người cùng khung; nếu phản ứng B quan trọng, dùng cận B riêng.

**Kiểm tra kết quả:** Mỗi shot có vai trò kể chuyện, không chỉ đổi góc cho đủ số lượng.

![Minh họa nguồn B013-03](anh-goc/03.jpg)

## 2. Dựng đối đáp và giữ trục nhìn

**Nguồn:** Qua vai B nhìn A rồi qua vai A nhìn B; giữ mô tả chung giữa hai shot.

**Phân tích và áp dụng:** Over-the-shoulder là góc qua vai. Đặt sơ đồ A/B và đường nối họ; giữ các vị trí máy cùng một phía trục 180 độ để hướng nhìn dễ khớp. Ví dụ A nhìn về phải khung, B về trái. 'Reverse' là góc đối đáp, không có nghĩa quay camera sang phía bên kia trục. Quy tắc là công cụ giữ định hướng, có thể phá có chủ ý.

**Ví dụ cho cảnh nông thôn:** A ngồi đầu trái bàn hiên, B ở đầu phải. Shot A qua vai B, A nhìn lệch phải; shot B qua vai A, B nhìn lệch trái. Ấm trà ở cùng vị trí trên bàn.

**Kiểm tra kết quả:** Mắt có vẻ hướng tới nhau; tay, cốc và ghế không đổi chỗ vô cớ.

![Minh họa nguồn B013-10](anh-goc/10.jpg)

## 3. Giữ bối cảnh và nhận diện

**Nguồn:** Khóa địa điểm/ánh sáng, lặp mô tả nhân vật trong mọi prompt, chia storyboard A/B.

**Phân tích và áp dụng:** Lập khối mô tả chung: sơ đồ phòng, nguồn sáng trong thế giới cảnh, giờ/ngày, tóc, trang phục và đạo cụ. Dùng ảnh tham chiếu nhất quán nếu công cụ hỗ trợ. Khi đảo góc, ánh sáng đến từ cùng cửa sổ nên hướng tương đối trên màn hình có thể đổi; đừng ép 'trái khung' cho mọi góc.

**Ví dụ cho cảnh nông thôn:** Cửa sổ ở phía sân chiếu vào hiên từ hướng đông; áo nâu của A và áo xanh xám của B giữ nguyên, kể cả khi đổi góc.

**Kiểm tra kết quả:** Khớp khung đầu/cuối giữa các clip: gương mặt, áo, ánh sáng, vị trí cốc và độ đầy cốc.

![Minh họa nguồn B013-07](anh-goc/07.jpg)

## 4. Chỉ rõ lời thoại và phản ứng

**Nguồn:** Một người nói mỗi shot, người còn lại nghe; câu ngắn và một hành động chính.

**Phân tích và áp dụng:** Gắn từng câu với tên/mô tả người nói. Ghi giọng, tốc độ và ngôn ngữ; mô tả người nghe bằng phản ứng nhỏ. Một người nói là chiến lược giảm độ phức tạp khi thử AI, không phải luật điện ảnh. Cận người nghe có thể đi kèm tiếng người nói ngoài khung nếu dựng chủ ý.

**Ví dụ cho cảnh nông thôn:** A hỏi một câu ngắn; B giữ miệng khép, nhìn A. Sau đó shot B nói một câu, A chỉ gật nhẹ.

**Kiểm tra kết quả:** Đúng nội dung, đúng giọng/người, đúng thời điểm miệng chuyển động; tiếng nền không lấn lời.

![Minh họa nguồn B013-09](anh-goc/09.jpg)

## 5. Chẩn đoán rồi sửa đúng shot

**Nguồn:** Nguồn liệt kê đảo thoại, khẩu hình sai, màu/ánh sáng lệch, bỏ qua chuyển động máy và người xuất hiện thêm.

**Phân tích và áp dụng:** Ghi lỗi theo mốc giây, thử sửa một nhóm yêu cầu. Nếu khẩu hình sai, rút ngắn lời hoặc giảm tác vụ phụ trước khi tăng mô tả. Nếu camera sai, chọn một đường máy rõ. Nếu dựng giật, kiểm tra liên tục và khoảng nghỉ thay vì tạo lại tất cả. Duy trì nền âm phòng qua điểm cắt.

**Ví dụ cho cảnh nông thôn:** Shot B đúng mặt nhưng câu trả lời kéo dài che mất khoảng nghỉ: chỉ sửa lời/nhịp của B, giữ shot A đã đạt.

**Kiểm tra kết quả:** Sửa đoạn có lỗi, so bản mới với tiêu chí ban đầu; nghe cả đường tiếng qua điểm cắt.

![Minh họa nguồn B013-13](anh-goc/13.jpg)

## Điểm cần hiểu có điều kiện

- Không phải mọi lỗi do người viết prompt; mô hình vẫn có giới hạn và tính ngẫu nhiên.
- Hội thoại có thể quay bằng một shot, hai người cùng khung hoặc nhiều dạng dựng khác; shot–reverse shot là lựa chọn.
- Một người nói/shot, camera đặt đầu prompt và mô tả lặp không bảo đảm chính xác tuyệt đối.
- Hai tệp B013-10 và B013-11 có cùng SHA-256; 16 là số tệp nguồn, không phải 16 trang khác nhau.
- Negative prompt của nguồn dùng 'no ...'; hướng dẫn ở trường negative riêng có thể yêu cầu liệt kê yếu tố không muốn. Không coi đó là cú pháp chung cho mọi giao diện.

## Cách đưa vào quy trình sản xuất

Viết đoạn thoại → lập sơ đồ A/B và nguồn sáng → giữ khối nhân vật/bối cảnh chung → thiết kế shot theo ý nghĩa → tạo riêng và kiểm tra hình/âm → sửa shot lỗi → dựng khoảng nghỉ và nền âm liên tục.

## Tự kiểm tra kiến thức

- Vì sao không nên hiểu góc đảo là vượt trục 180 độ?
- Sau khi đổi góc, nguồn sáng cần giữ theo căn phòng hay theo bên trái khung?
- Một shot phản ứng có nhất thiết phải cho người trong khung nói không?

## Nguồn đối chiếu bổ sung

- [Adobe: shot–reverse shot](https://www.adobe.com/creativecloud/video/production/cinematography/camera-shots-and-angles/reverse-shot.html): Đối chiếu cách dựng đối đáp và việc lập kế hoạch trục nhìn.
- [Adobe: quy tắc 180 độ](https://www.adobe.com/creativecloud/video/discover/what-is-the-180-degree-rule.html): Đối chiếu giữ vị trí camera cùng phía trục để bảo toàn hướng nhìn.
- [Google: hướng dẫn prompt video](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/video-gen-prompt-guide): Đối chiếu các thành phần prompt và cách dùng negative prompt theo nền tảng.

**Giới hạn:** đây là tài liệu học từ ảnh. Không dùng một hình minh họa để xác nhận chuyển động, thời lượng, độ chính xác thao tác hay khả năng hiện tại của một sản phẩm. Những phần chưa kiểm chứng được ghi rõ trong bản đọc ảnh.
