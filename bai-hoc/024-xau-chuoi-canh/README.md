# Bài 024 — Xâu chuỗi cảnh: kéo dài hành động và dựng phim có kiểm soát

Bài phân biệt độ dài một lần tạo với độ dài thành phẩm. Giá trị cốt lõi là duyệt cảnh gốc, chỉ đạo phần tiếp diễn, giữ trạng thái nhân vật–vật thể–máy quay và kiểm tra điểm nối. Nối dài một hành động và dựng nhiều cảnh thành phim là hai việc cần kế hoạch khác nhau.

**Nguồn:** [Làm phim chuyên nghiệp với Google Veo 3- Từ Prompt cơ bản đến kỹ thuật Xâu chuỗi (Chaining)](https://drive.google.com/drive/folders/1kgxRLK9WGqrFxDsNpD9umwIIlL8oZUGZ). Đã đọc **15/15 ảnh**. Ngày biên soạn: 18/10/2026.

[Đọc từng ảnh](doc-anh.md) · [Bài thực hành](thuc-hanh.md) · [Nguồn và mã kiểm tra](nguon.json) · [Danh mục toàn bộ](../../DANH-MUC-BAI-HOC.md)

**Quy ước:** phần “Nguồn” diễn đạt ý trong bộ ảnh. Phần “Phân tích và áp dụng” do người biên soạn bổ sung. Hiệu quả của câu lệnh chưa được kiểm nghiệm bằng lần tạo video trong đợt này.

## Những điều cần học

| Nội dung | Mã ảnh nguồn |
| --- | --- |
| Lập phim theo cảnh, không nhân độ dài máy móc | B024-00, B024-01, B024-14 |
| Duyệt điểm bắt đầu trước khi mở rộng | B024-02, B024-03, B024-04 |
| Giữ trạng thái, thêm hành động mới | B024-05, B024-06, B024-11 |
| Nối hình phải khớp cả nhịp và âm thanh | B024-07, B024-08, B024-09, B024-10 |
| Duyệt chuỗi và dừng mở rộng khi lỗi tích lũy | B024-12, B024-13 |

## 1. Lập phim theo cảnh, không nhân độ dài máy móc

**Nguồn:** Nguồn giải thích video dài là kết quả tổ chức đoạn ngắn và biên tập.

**Phân tích và áp dụng:** Lập danh sách cảnh theo mục đích kể chuyện. Dùng nối dài khi hành động thật sự cần tiếp diễn; dùng cắt dựng khi đổi góc, thời gian hoặc thông tin. Số đoạn lý tưởng bằng thời lượng đích chia thời lượng dùng được, còn số lần tạo phụ thuộc tỷ lệ đạt.

**Ví dụ cho cảnh nông thôn:** Quá trình đan rổ gồm toàn cảnh không gian, cận luồn nan, phản ứng nhân vật và thành phẩm. Không cần kéo một góc máy thành cả mười phút.

**Kiểm tra kết quả:** Mỗi đoạn có thông tin mới; có dự phòng hao hụt; không kéo dài chỉ để đủ phút.

![Minh họa nguồn B024-01](anh-goc/01.jpg)

## 2. Duyệt điểm bắt đầu trước khi mở rộng

**Nguồn:** Nguồn lấy clip gốc làm nền rồi chỉ đạo hành động tiếp theo bằng Extend.

**Phân tích và áp dụng:** Hướng dẫn Flow được đối chiếu xác nhận có mở rộng và dựng chuỗi; giao diện minh họa trong bài có thể khác thực tế. Chỉ nối từ trạng thái đúng: mặt, tay, vật và hướng máy còn ổn định. Nếu cuối clip đã hỏng, quay lại điểm sạch hoặc tạo cảnh mới.

**Ví dụ cho cảnh nông thôn:** Đoạn A kết thúc khi tay giữ được nan tre và nan đã luồn nửa đường. Đoạn B tiếp tục kéo chính nan ấy, không mọc thêm nan và không bắt đầu lại thao tác.

**Kiểm tra kết quả:** Xem vài giây trước/sau điểm nối; tay, độ căng, vị trí nan và tốc độ không bật nhảy.

![Minh họa nguồn B024-02](anh-goc/02.jpg)

## 3. Giữ trạng thái, thêm hành động mới

**Nguồn:** Nguồn kết hợp nhân vật cố định, môi trường nhất quán và hành động tiếp diễn.

**Phân tích và áp dụng:** Lập ghi chú trạng thái cuối: tay nào cầm gì, mặt hướng đâu, vật ở trạng thái nào, máy đang đi hướng nào. Giữ phần không đổi và mô tả phần tiếp tục. Không dựa vào câu 'như cảnh trước' khi công cụ không có đầu vào trước.

**Ví dụ cho cảnh nông thôn:** Cô vẫn ngồi cùng ghế, tay trái giữ khung rổ, tay phải kéo nan đang cầm thêm một đoạn rồi miết xuống. Màu áo và hoa cài theo ảnh đã duyệt.

**Kiểm tra kết quả:** Có đầu vào thật và ghi chú cụ thể; động tác không tự khởi động lại.

![Minh họa nguồn B024-05](anh-goc/05.jpg)

## 4. Nối hình phải khớp cả nhịp và âm thanh

**Nguồn:** Nguồn đưa góc, chuyển động, ánh sáng, hiệu ứng và thời gian vào ngôn ngữ chỉ đạo.

**Phân tích và áp dụng:** Chọn một chuyển động phù hợp rồi giữ tốc độ qua chỗ nối. Duy trì hướng sáng và âm nền nếu cùng thời điểm. Khi đổi cảnh bằng cắt, chọn một trạng thái có thể khớp hành động. Không ép zoom chỉ vì nguồn gợi ý; máy tĩnh rất hữu ích để nhìn thao tác.

**Ví dụ cho cảnh nông thôn:** Đoạn A và B đều máy tĩnh nhìn bàn tre; tiếng cọ nan không dừng vô cớ ở đường nối. Đổi sang cận tay bằng cắt khi tay bắt đầu luồn nan mới.

**Kiểm tra kết quả:** Không giật kích thước, đổi hướng hoặc đổi âm phòng; không biến tua nhanh thành thời gian thực giữa chuỗi.

![Minh họa nguồn B024-08](anh-goc/08.jpg)

## 5. Duyệt chuỗi và dừng mở rộng khi lỗi tích lũy

**Nguồn:** Nguồn dành hậu kỳ để chọn, cắt và hoàn thiện.

**Phân tích và áp dụng:** Sau mỗi đoạn, so cả với đoạn trước và ảnh tham chiếu ban đầu để phát hiện mặt hoặc vật liệu trôi dần. Lưu phiên bản được duyệt. Khi lỗi tích lũy, tạo cảnh mới từ nguồn chuẩn; dựng phim không đòi mọi đoạn phải nối vô hình.

**Ví dụ cho cảnh nông thôn:** Sau vài đoạn đan, gương mặt hoặc áo thay đổi thì ngắt chuỗi, quay về ảnh chuẩn để tạo cận vật hoặc cảnh mới có chủ đích.

**Kiểm tra kết quả:** Có bản sạch để quay lại; xuất bản cuối được xem liền cả hình và tiếng.

![Minh họa nguồn B024-13](anh-goc/13.jpg)

## Điểm cần hiểu có điều kiện

- 8 giây trong nguồn không là định luật của mọi mô hình/chế độ; không suy ra mỗi lần mở rộng luôn thêm 8 giây hoặc lặp vô hạn.
- 75 đoạn cho 10 phút chỉ là phép chia với giả định dùng trọn 8 giây mỗi đoạn; không phải dự toán 75 lần tạo.
- Extend từ video, tạo mới từ ảnh cuối và dựng các clip bằng cắt là ba cách khác nhau.
- Đường dẫn nút trong ảnh là giao diện nguồn; tài liệu Flow hiện tại cần được đối chiếu khi thao tác. Không bảo đảm ô câu lệnh trống hợp lệ.
- Lặp mô tả và cùng dùng slow zoom in không bảo đảm danh tính hoặc điểm nối mượt.
- Cinematic (điện ảnh) không bắt buộc tương phản cao, máy luôn chuyển động hay hậu cảnh luôn mờ.

## Cách đưa vào quy trình sản xuất

Lập danh sách cảnh → duyệt ảnh/clip gốc → ghi trạng thái cuối → chọn mở rộng hay cắt sang cảnh mới → tạo một đoạn tiếp → kiểm tra điểm nối và tham chiếu gốc → lưu bản sạch → tiếp tục hoặc dừng chuỗi → dựng và xem toàn bộ. Giữ hình và âm thanh thành hai phần đều cần duyệt.

## Tự kiểm tra kiến thức

- Khi nào nên mở rộng hành động, khi nào nên cắt sang cảnh mới?
- Ảnh cuối có đủ giữ tốc độ chuyển động từ video trước không?
- Cần ghi những trạng thái gì trước khi tạo đoạn B?

## Nguồn đối chiếu bổ sung

- [Google Flow — chỉnh video và dựng cảnh](https://support.google.com/labs/answer/16935718?hl=en): Đối chiếu chức năng mở rộng, lưu khung và sắp xếp/cắt/xem/tải chuỗi. Vị trí nút có thể khác ảnh nguồn.

**Giới hạn:** đây là tài liệu học từ ảnh. Không dùng một hình minh họa để xác nhận chuyển động, thời lượng, độ chính xác thao tác hay khả năng hiện tại của một sản phẩm. Những phần chưa kiểm chứng được ghi rõ trong bản đọc ảnh.
