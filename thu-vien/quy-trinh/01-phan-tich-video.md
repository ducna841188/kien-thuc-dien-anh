# Phân tích video

Tác vụ: analyze_video. Core 1.0.0.

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

analysis.schema.json; mau/phan-tich-video.json

Kết quả kèm mã kiến thức, phiên bản, giả định và trạng thái kiểm nghiệm. Các mẫu chưa điền không phải sản phẩm đã phân tích.

## Tiêu chí duyệt

- Mỗi kết luận tìm lại được nguồn/mốc.
- Báo cáo tổng hợp không vượt độ phủ.
- Không thống kê nhãn chưa kiểm như sự thật video.

Mã trọng tâm: [EV-001](../kien-thuc/EV-001.json), [EV-003](../kien-thuc/EV-003.json), [EV-004](../kien-thuc/EV-004.json), [EV-005](../kien-thuc/EV-005.json), [ED-001](../kien-thuc/ED-001.json), [AU-004](../kien-thuc/AU-004.json)
