# Bài 027 — Tách lượt thoại: đúng người nói, liền mạch khi dựng

Shot–reverse shot (quay–đảo góc) chia hội thoại thành các góc tập trung từng người. Với AI, đây là cách giảm số nhiệm vụ mỗi lần tạo và sửa riêng cảnh lỗi. Cần giữ danh tính, không gian, hướng nhìn, giọng nói và nhịp phản ứng; tách cảnh hỗ trợ kiểm soát nhưng không bảo đảm hết lỗi khớp môi.

**Nguồn:** [Tại sao video AI của bạn bị lỗi lip-sync? Cách khắc phục triệt để bằng phương pháp tách shot đơn giản](https://drive.google.com/drive/folders/1_cyMghOhl8O241qxJWE9pdcpu7x_NGBP). Đã đọc **15/15 ảnh**. Ngày biên soạn: 18/10/2026.

[Đọc từng ảnh](doc-anh.md) · [Bài thực hành](thuc-hanh.md) · [Nguồn và mã kiểm tra](nguon.json) · [Danh mục toàn bộ](../../DANH-MUC-BAI-HOC.md)

**Quy ước:** phần “Nguồn” diễn đạt ý trong bộ ảnh. Phần “Phân tích và áp dụng” do người biên soạn bổ sung. Hiệu quả của câu lệnh chưa được kiểm nghiệm bằng lần tạo video trong đợt này.

## Những điều cần học

| Nội dung | Mã ảnh nguồn |
| --- | --- |
| Tách theo lượt và nhu cầu phản ứng | B027-00, B027-01, B027-02, B027-03, B027-04, B027-05 |
| Duyệt vị trí và hướng nhìn trước | B027-06, B027-07, B027-10 |
| Xác định người nói bằng tên và lời cụ thể | B027-08, B027-09, B027-10 |
| Giảm thao tác phụ, giữ nguồn sáng và âm nền | B027-08, B027-12, B027-13 |
| Chấm riêng bốn lỗi và sửa đúng cảnh | B027-11, B027-12, B027-13, B027-14 |

## 1. Tách theo lượt và nhu cầu phản ứng

**Nguồn:** Nguồn tập trung từng lượt nói thay vì nhồi hội thoại phức tạp.

**Phân tích và áp dụng:** Lập bảng ai nói câu nào, ai nghe, cần nhìn gì. Mỗi yêu cầu tạo chỉ mang một lượt ngắn khi đang xử lý lỗi gán thoại. Chèn cảnh phản ứng nếu nó có thông tin, không cắt máy móc sau mọi câu.

**Ví dụ cho cảnh nông thôn:** Bà hỏi về chiếc giỏ, cô gái đáp ngắn; sau đó giữ một khoảng cô nhìn giỏ, thay vì cả hai liên tục nói và đưa vật trong một clip.

**Kiểm tra kết quả:** Đúng lời và đúng người; có khoảng nghe; cảnh tĩnh không bị loại chỉ vì không chuyển máy.

![Minh họa nguồn B027-03](anh-goc/03.jpg)

## 2. Duyệt vị trí và hướng nhìn trước

**Nguồn:** Nguồn giữ địa điểm/nhân vật và đổi góc qua vai.

**Phân tích và áp dụng:** Lập vị trí hai người và đường nối giữa họ. Khi dựng theo quy ước giữ trục, hai máy cùng một phía đường đó, người A nhìn về phía B và B nhìn ngược lại. Không lật gương để giả góc đảo vì tóc, trang phục và vật có thể đảo theo. Duyệt riêng hai ảnh góc A/B.

**Ví dụ cho cảnh nông thôn:** Bà ngồi bên trái bàn, cô gái bên phải. Ở góc bà, vai cô chỉ lộ tiền cảnh; ở góc cô, vai bà ở phía đối ứng, cùng hiên và nguồn sáng.

**Kiểm tra kết quả:** Hai góc cho cảm giác họ đối diện nhau; vị trí giỏ và tay không đổi vô cớ.

![Minh họa nguồn B027-07](anh-goc/07.jpg)

## 3. Xác định người nói bằng tên và lời cụ thể

**Nguồn:** Nguồn viết A nói, B im và tách dòng âm thanh.

**Phân tích và áp dụng:** Mỗi nhân vật có mô tả phân biệt ổn định và lời đặt ngay cạnh chủ thể. Chọn một kiểu máy cụ thể. Với người nghe, yêu cầu phản ứng kín đáo, môi nghỉ tự nhiên; không yêu cầu miệng kẹp bất động. Rút câu để đủ thời gian nói và nghỉ, kiểm tra bằng nghe thật.

**Ví dụ cho cảnh nông thôn:** Chỉ bà nói: 'Chiếc giỏ này con đan à?' Cô gái nhìn bà, chớp nhẹ, giữ miệng nghỉ; không đưa cả câu đáp của cô vào cùng yêu cầu thử.

**Kiểm tra kết quả:** Đúng nguyên văn, không thêm câu, giọng không đổi; môi người nghe không nhép lại lời.

![Minh họa nguồn B027-09](anh-goc/09.jpg)

## 4. Giảm thao tác phụ, giữ nguồn sáng và âm nền

**Nguồn:** Nguồn giới hạn hành động và dùng nguồn sáng có lý do, một chuyển động máy rõ.

**Phân tích và áp dụng:** Thử máy tĩnh trước khi thêm tiến nhẹ. Nếu vừa thoại vừa trao vật gây lỗi, tạo thao tác thành cảnh riêng. Hướng sáng cần gắn với không gian thật, không cố cùng một phía màn hình ở hai góc đối nhau. Giữ lớp môi trường liên tục khi dựng.

**Ví dụ cho cảnh nông thôn:** Bà nói dưới hiên sáng trời; cô chỉ nghe. Cận tay đưa giỏ được tạo riêng. Tiếng sân nhỏ nối qua hai góc, không đột ngột đổi thành tiếng phòng kín.

**Kiểm tra kết quả:** Không vỡ mặt hoặc tay khi nói; ánh sáng hợp vị trí; âm nền không bật/tắt ở cắt.

![Minh họa nguồn B027-12](anh-goc/12.jpg)

## 5. Chấm riêng bốn lỗi và sửa đúng cảnh

**Nguồn:** Nguồn dành phần hỏi đáp để sửa gán thoại, môi, màu/sáng, máy và người thừa.

**Phân tích và áp dụng:** Xem có âm thanh để tách sai người, sai lời, lệch thời điểm môi và sai cảm xúc. Duyệt từng cảnh rồi xem cả chuỗi. Nếu vẫn lỗi, có thể dùng thoại thu riêng và xử lý khớp môi/hậu kỳ trong công cụ phù hợp; phương án này cần kiểm tra riêng, chưa thử ở đây.

**Ví dụ cho cảnh nông thôn:** Cảnh A đạt thì giữ; chỉ tạo lại cảnh B sai môi. Đừng thay cả nhân vật và ánh sáng để chữa một câu đáp.

**Kiểm tra kết quả:** Có mốc giây lỗi, phiên bản được giữ và bản sửa; không kết luận từ ảnh tĩnh.

![Minh họa nguồn B027-13](anh-goc/13.jpg)

## Điểm cần hiểu có điều kiện

- Không đúng khi nói mọi lỗi đều do người ra lệnh; mô hình và giao diện cũng có giới hạn.
- Hội thoại có thể quay trong một cú máy. Quay–đảo góc là lựa chọn phổ biến, không độc quyền.
- Tách lượt giảm mơ hồ nhưng không bảo đảm khớp môi tuyệt đối, giọng ổn định hoặc hết nhầm.
- Máy tĩnh không đồng nghĩa nghiệp dư; chọn theo chức năng cảnh.
- Các nhãn Character Lock/Speaker Lock (giữ nhận dạng/xác định người nói) là mô tả ý đồ, không tính năng khóa cứng đã xác nhận.
- Mẫu loại trừ dùng 'no...' cần điều chỉnh theo công cụ; xem hướng dẫn cú pháp ở B023. Không dùng yêu cầu loại trừ để tẩy tên tác giả trên ảnh nguồn.

## Cách đưa vào quy trình sản xuất

Viết hội thoại ngắn → phân vai → duyệt nhân vật và sơ đồ vị trí → duyệt hai ảnh góc → tạo từng lượt với một người nói → nghe và xem môi → sửa cảnh lỗi → tạo cảnh tay/phản ứng riêng nếu cần → dựng giữ trục, nhịp nghỉ và âm nền → xem toàn chuỗi.

## Tự kiểm tra kiến thức

- Vì sao đảo góc không đồng nghĩa lật gương ảnh?
- Lỗi gán người nói khác lệch khớp môi thế nào?
- Khi chỉ B lỗi, cần giữ những phần nào của A?

**Giới hạn:** đây là tài liệu học từ ảnh. Không dùng một hình minh họa để xác nhận chuyển động, thời lượng, độ chính xác thao tác hay khả năng hiện tại của một sản phẩm. Những phần chưa kiểm chứng được ghi rõ trong bản đọc ảnh.
