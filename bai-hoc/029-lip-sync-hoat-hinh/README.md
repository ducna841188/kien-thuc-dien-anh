# Bài 029 — Thoại hoạt hình: sáu cách giảm nhầm vai và kiểm tra khớp môi

Sáu chiến lược trong nguồn là làm nổi người nói, chỉ rõ vai phát âm, tách lượt, rút câu, thêm cử chỉ nhỏ và giảm nhân vật cạnh tranh. Chuyển chúng thành các phương án thử có tiêu chí; phân biệt gán đúng vai, giọng đúng, lời đúng và môi khớp.

**Nguồn:** [Trị Bệnh Chó Nói Thoại Của Mèo - 6 Bí Quyết Lip-Sync Hoạt Hình AI Hoàn Hảo](https://drive.google.com/drive/folders/1JJGBH0ew1DF-EjXmZR-TA_rZJ_FLsOdv). Đã đọc **13/13 ảnh**. Ngày biên soạn: 18/10/2026.

[Đọc từng ảnh](doc-anh.md) · [Bài thực hành](thuc-hanh.md) · [Nguồn và mã kiểm tra](nguon.json) · [Danh mục toàn bộ](../../DANH-MUC-BAI-HOC.md)

**Quy ước:** phần “Nguồn” diễn đạt ý trong bộ ảnh. Phần “Phân tích và áp dụng” do người biên soạn bổ sung. Hiệu quả của câu lệnh chưa được kiểm nghiệm bằng lần tạo video trong đợt này.

## Những điều cần học

| Nội dung | Mã ảnh nguồn |
| --- | --- |
| Phân loại lỗi trước khi sửa | B029-00, B029-01, B029-02, B029-03, B029-04 |
| Làm người nói dễ nhận diện | B029-05, B029-10 |
| Gắn từng câu với vai cụ thể | B029-06, B029-07 |
| Câu vừa thời gian, cử chỉ vừa nhiệm vụ | B029-08, B029-09 |
| Duyệt bằng nghe–xem và có phương án dựng | B029-11, B029-12 |

## 1. Phân loại lỗi trước khi sửa

**Nguồn:** Nguồn gộp nhiều biểu hiện dưới tên lip-sync (khớp chuyển động môi với tiếng).

**Phân tích và áp dụng:** Chấm riêng: đúng người phát lời, đúng loại giọng/tiếng, đúng câu, môi đúng nhịp, máy giữ đúng chủ thể. Câu có thể đúng vai nhưng môi lệch; đổi bố cục không chắc sửa giọng. Không lấy giải thích 'chỉ nhìn ảnh' làm sự thật về kiến trúc mô hình.

**Ví dụ cho cảnh nông thôn:** Cô gái nói đúng câu nhưng giọng bà là lỗi giọng; bà ngoài khung nhép theo là lỗi vai; miệng đi trước tiếng là lỗi đồng bộ.

**Kiểm tra kết quả:** Nhật ký ghi tên lỗi và mốc giây, không chỉ ghi 'thoại hỏng'.

![Minh họa nguồn B029-01](anh-goc/01.jpg)

## 2. Làm người nói dễ nhận diện

**Nguồn:** Nguồn giảm số mặt cạnh tranh và tăng độ nổi chủ thể nói.

**Phân tích và áp dụng:** Duyệt ảnh một người nói rõ mặt, không bị che miệng, người nghe có thể ngoài khung hoặc chỉ lộ vai. Không bó buộc tỷ lệ 60–80%; bố cục vẫn phải hợp hướng nhìn và cảnh. Với nhân vật hoạt hình, dùng đặc điểm đã duyệt, không đổi màu để chữa lỗi nếu làm mất thiết kế.

**Ví dụ cho cảnh nông thôn:** Cận vừa cô gái ở hiên; bà chỉ lộ vai tiền cảnh. Mặt cô rõ và đủ chỗ nhìn về bà, không bắt buộc đặt chính giữa.

**Kiểm tra kết quả:** Đúng một mặt cần theo dõi khớp môi; không che miệng hoặc đổi thiết kế.

![Minh họa nguồn B029-05](anh-goc/05.jpg)

## 3. Gắn từng câu với vai cụ thể

**Nguồn:** Nguồn dùng nhãn khóa và tách từng lượt.

**Phân tích và áp dụng:** Viết tên kèm nhận dạng ngắn, lời nguyên văn và trạng thái người nghe. Dùng một lượt cho mỗi lần thử khi đang xử lý nhầm vai. Nhãn 'Lip-Sync Lock' có thể dùng để tổ chức, nhưng chính câu chỉ đạo và đầu vào mới cần rõ. Không đưa câu đáp khác vào phần bối cảnh của cùng lần thử.

**Ví dụ cho cảnh nông thôn:** Chỉ cô gái áo theo mẫu nói: 'Con đã đan xong chiếc giỏ rồi.' Bà nghe ngoài khung; không có câu của bà trong yêu cầu này.

**Kiểm tra kết quả:** Không đổi vai giữa câu, không tự thêm câu; người nghe giữ môi nghỉ.

![Minh họa nguồn B029-06](anh-goc/06.jpg)

## 4. Câu vừa thời gian, cử chỉ vừa nhiệm vụ

**Nguồn:** Nguồn khuyên câu đơn giản và cử chỉ nhỏ trong lúc nói.

**Phân tích và áp dụng:** Đọc thử câu với nhịp đích trước khi tạo; dành khoảng đầu/cuối và hơi thở. Với tiếng Việt, số từ theo khoảng trắng không tương đương thời gian phát âm ở mọi câu. Chọn một gật hoặc một động tác tay nhỏ; không vừa thoại vừa đổi cảnh hay làm thao tác tay phức tạp.

**Ví dụ cho cảnh nông thôn:** Cô nói một câu ngắn rồi gật nhẹ. Việc chuyển giỏ sang tay bà thực hiện thành cảnh khác.

**Kiểm tra kết quả:** Lời không bị nuốt hoặc tăng tốc để nhét vừa; cử chỉ không phá mặt và tay.

![Minh họa nguồn B029-08](anh-goc/08.jpg)

## 5. Duyệt bằng nghe–xem và có phương án dựng

**Nguồn:** Nguồn tổng hợp sáu điểm và hứa tăng độ chính xác.

**Phân tích và áp dụng:** Duyệt từng bản có âm thanh, xem toàn câu ở tốc độ thường rồi soi chỗ lệch. So từng thay đổi với bản cơ sở. Nếu sinh thoại tích hợp vẫn thất bại, thử quy trình âm thanh riêng và khớp môi/hậu kỳ bằng công cụ hỗ trợ; đây là phương án cần thử riêng, không thành quả đã thực hiện.

**Ví dụ cho cảnh nông thôn:** Giữ ảnh và camera, lần lượt thử câu ngắn hơn hoặc người nghe ngoài khung. Nếu chỉ sai vài đoạn, sửa đúng đoạn thay vì thay mọi thiết lập.

**Kiểm tra kết quả:** Có phiên bản, đầu vào, lỗi và phần dùng được; không lấy tỷ lệ nguồn làm tỷ lệ của dự án.

![Minh họa nguồn B029-11](anh-goc/11.jpg)

## Điểm cần hiểu có điều kiện

- Không có bằng chứng trong bộ ảnh cho 60%, 90%, 96%, 'đã kiểm chứng', 'gần hoàn hảo' hoặc 'toàn quyền'.
- Tuyên bố Veo không đọc tên và chỉ nhìn ảnh là quá mức; tên cần nối rõ với nhận dạng, không thay bằng một giả thuyết cơ chế.
- Lip-Sync Lock là tiêu đề khối chỉ đạo của tác giả, không tham số hay tính năng khóa cứng được xác nhận.
- 60–80% khung, 16–18 từ và một–hai người là các gợi ý, không ngưỡng bắt buộc.
- Một scene trong nguồn được dùng gần nghĩa đoạn tạo/cú máy; cảnh điện ảnh có thể gồm nhiều góc và lượt.
- Để người nghe im không đồng nghĩa cấm mọi chuyển động tự nhiên của miệng/mặt. Dấu NotebookLM trong ảnh được giữ nguyên, không coi là nguồn nghiên cứu chứng minh hiệu quả.

## Cách đưa vào quy trình sản xuất

Định danh nhân vật → viết một câu ngắn phù hợp thời gian → duyệt ảnh góc một người nói → chỉ định lời và người nghe → tạo → phân loại lỗi vai/giọng/lời/môi/máy → thay một yếu tố → dựng chuỗi và nghe lại. Đối chiếu B027 về hướng nhìn và liên tục giữa các góc.

## Tự kiểm tra kiến thức

- Đúng người nói nhưng sai giọng là lỗi nào?
- Vì sao nhãn khóa không chứng minh đã cố định người phát âm?
- Có cần nhân vật luôn chính giữa và chiếm đúng 80% khung không?

**Giới hạn:** đây là tài liệu học từ ảnh. Không dùng một hình minh họa để xác nhận chuyển động, thời lượng, độ chính xác thao tác hay khả năng hiện tại của một sản phẩm. Những phần chưa kiểm chứng được ghi rõ trong bản đọc ảnh.
