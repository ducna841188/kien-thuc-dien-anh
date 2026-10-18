# Phân tích video

Tác vụ: analyze_video. Core release 1.2.1; dẫn version của từng mục thực dùng.

[Mục lục](../README.md) · [Chuẩn quyết định](../03_RA_QUYET_DINH.md)

**Đầu vào:** Tệp/đoạn video, nguồn và mục tiêu nghiên cứu; hồ sơ ngách nếu có. Bảng shot cũ là nguồn thuật lại, chưa thay việc xem.

## Cách thực hiện

1. Kiểm asset, độ dài, audio và offset; khai báo phạm vi có thể xem/nghe.
2. Đọc toàn phim để xác định trục thay đổi, các phần và lời hứa.
3. Lập ranh giới shot theo bằng chứng; ghi sự kiện dưới một giây nếu cần.
4. Điền 25 thuộc tính với trạng thái bằng chứng, không đoán phần thiếu.
5. Xem các tiếp xúc, ranh giới hình/âm và sự liên tục.
6. Tổng hợp chức năng chuỗi, lượng thông tin, mong chờ và nhịp–cảm xúc dự kiến.
7. Tách bài học có điều kiện, đề xuất tái dựng và câu hỏi cần xem lại.

## Đầu ra

[Schema đầu ra](../schema/analysis.schema.json) · [Mẫu hiện hành](../mau/phan-tich-video.json)

Kết quả kèm mã kiến thức, phiên bản, giả định và trạng thái kiểm nghiệm. Các mẫu chưa điền không phải sản phẩm đã phân tích.

## Tiêu chí duyệt

- Mỗi kết luận tìm lại được nguồn/mốc.
- Báo cáo tổng hợp không vượt độ phủ.
- Không thống kê nhãn chưa kiểm như sự thật video.

Mã trọng tâm: [EV-001](../kien-thuc/EV-001.json), [EV-003](../kien-thuc/EV-003.json), [EV-004](../kien-thuc/EV-004.json), [EV-005](../kien-thuc/EV-005.json), [ED-001](../kien-thuc/ED-001.json), [AU-004](../kien-thuc/AU-004.json)

## Áp dụng và kiểm tra

Trước gắn nhãn hàng loạt, lập sổ định nghĩa và mẫu số theo EV-008. Gắn riêng cut, sự kiện và âm; rà chuyển lực/tiếp xúc, điểm nhìn qua cut và chức năng thời gian. Khi rút bài học từ phim nổi bật, giữ thiên lệch mẫu và điều kiện theo EV-007, YT-010. Đối chiếu kết luận với 07_KIEM_TRA_TRAI_NGHIEM trước khi viết tác dụng khán giả.
