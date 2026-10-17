# Lưu ý về nguồn và cách hiểu kết quả

[Về trang đầu](README.md) · [Hướng dẫn học](HUONG-DAN-HOC.md) · [Danh mục](DANH-MUC-BAI-HOC.md)

## Phạm vi đã hoàn thành

Đã đọc và biên soạn 33 thư mục bài học, gồm 444 tệp ảnh trong danh mục Drive. Mỗi bài có ảnh gốc, bản đọc ảnh, phân tích và thực hành; `nguon.json` lưu mã tệp Drive, thứ tự, kích thước và SHA-256 để đối chiếu. Ảnh không được chỉnh sửa; tên tệp lưu trong kho được chuẩn hóa và vẫn truy ngược được tên gốc.

444 là số tệp nguồn, bao gồm ảnh trùng. So sánh SHA-256 của toàn bộ tệp cho kết quả **374 chuỗi byte khác nhau**, với 70 bản sao ngoài bản đầu tiên. Con số 374 không phải số ý tưởng độc lập: ảnh khác byte vẫn có thể trình bày cùng nội dung.

## Những nhóm trùng đã xác nhận bằng mã băm

| Nhóm | Kết quả đối chiếu |
| --- | --- |
| B008 và B011 | 18 cặp ảnh trùng byte theo cùng thứ tự |
| B003 và B020 | 10 cặp ảnh trùng byte theo cùng thứ tự |
| B001 và B028 | 12 ảnh đầu của B028 trùng byte với 12 ảnh B001; B028 còn ảnh số 12 riêng |
| B013 và B027 | 15 ảnh B027 đều có bản trùng byte trong B013; B013 có 16 tệp vì hai tệp nội bộ cùng nội dung |
| B018 và B031 | 12 cặp ảnh trùng byte theo cùng thứ tự |
| B006 nội bộ | B006-00 và B006-14 trùng byte |
| B013 nội bộ | B013-10 và B013-11 trùng byte |
| B025 nội bộ | B025-10 và B025-11 trùng byte; ứng với tên gốc 011 và 012 |

Các bản sao vẫn được giữ để bảo toàn nguồn gốc từng thư mục. Không xem việc một ý xuất hiện ở nhiều thư mục là nhiều bằng chứng độc lập.

B030 có 12 ảnh trình bày cùng nội dung với B029-01 đến B029-12 khi quan sát trực tiếp, nhưng mã băm khác nhau. Vì vậy chỉ ghi nhận sự lặp nội dung nhìn thấy, không xếp chúng vào bảng trùng byte trên. B030 bổ sung cách lập phiếu phân vai để luyện lại ứng dụng.

## Tên tệp, tên bài và vùng chữ có vấn đề

| Vị trí | Lưu ý |
| --- | --- |
| B021 | Có 15 tệp; dãy tên không có số 012. Không suy ra có một trang thất lạc chỉ từ tên nhảy số. |
| B025 | Có 15 tệp; tên số 10 vắng, hai tệp 011 và 012 trùng byte. |
| B031 | Có 12 tệp; tên số 10 vắng. |
| B028 | Tên thư mục nhấn vào slow push-in, nhưng bộ ảnh bàn về bốn cấu trúc camera; nội dung được tổng kết theo ảnh thực tế. |
| B033-04 | Một vùng chữ ở phía trên bên phải bị lỗi/nghĩa không rõ. Bản đọc đánh dấu thay vì tự khôi phục câu; phần hướng dẫn rõ ở dưới được dùng để diễn giải. |

Đây là các điểm cần chú ý đã ghi nhận, không phải khẳng định mọi bộ ảnh có cách đánh số liên tục. Thứ tự lưu đọc từng bài và tên gốc đều nằm trong `nguon.json`.

## Tách nguồn, phân tích và kiểm nghiệm

- **Nội dung nguồn:** diễn đạt lại những gì đọc thấy trong ảnh, không phải bản chép nguyên văn toàn bộ.
- **Quan sát hình:** mô tả bố cục, ví dụ và minh họa tĩnh. Một ảnh không chứng minh được chuyển động camera, đồng bộ khẩu hình hay thời điểm âm thanh.
- **Phân tích bổ sung:** giải thích, sửa cách hiểu quá tuyệt đối và ví dụ ứng dụng do người biên soạn thêm.
- **Thực hành:** câu lệnh và tiêu chí tự kiểm tra; chưa chạy tạo video trong quá trình biên soạn kho này.

Các tỷ lệ thành công, mức tăng cảm xúc hoặc chất lượng như “90%”, “100%”, “gấp 5”, “1000%” trong nguồn không có dữ liệu thử nghiệm kèm theo. Không dùng chúng làm xác suất bảo đảm. Các tiêu đề nhấn mạnh được giữ để truy nguồn; phần học tập có chú giải điều kiện áp dụng.

Khả năng, giao diện, số ảnh tham chiếu, thời lượng, giá và gói dịch vụ phụ thuộc phiên bản/chế độ/công cụ. Bảng trong ảnh là nội dung tại thời điểm nguồn được làm, không tự trở thành thông số hiện hành. Những chỗ cần thiết có liên kết tài liệu chính thức trong từng bài. Không có hoạt động mua dịch vụ hay tạo video nào được thực hiện trong đợt này.

Ảnh có dấu tên như Vienhn, NotebookLM hoặc tên công cụ được giữ nguyên. Dấu tên nhìn thấy không tự xác minh tác giả, chuyên môn, xuất xứ mọi phát biểu hoặc việc công cụ bảo chứng nội dung.

## Cách dùng kho khi cần sửa lỗi thực tế

Gửi mã bài, mã ảnh nguồn, công cụ/phiên bản/chế độ, câu lệnh đã dùng và video kết quả. Ghi rõ phần nào đã đạt để giữ nguyên. Chọn một lỗi có mốc giây, thử một thay đổi rồi đối chiếu lại. Kết quả có thể phụ thuộc cả câu lệnh, ảnh đầu vào, thiết lập và giới hạn mô hình; không quy mọi lỗi cho người viết câu lệnh.
