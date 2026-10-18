# Xây và sửa kịch bản

Tác vụ: write_script. Core release 1.2.1; dẫn version của từng mục thực dùng.

[Mục lục](../README.md) · [Chuẩn quyết định](../03_RA_QUYET_DINH.md)

**Đầu vào:** Lời hứa, mục tiêu khán giả, hình thức phim, tài sản và điều đã duyệt. Nếu chưa chọn ngách, ghi phần chung và giả định.

## Cách thực hiện

1. Viết trục thay đổi và trạng thái đầu/cuối.
2. Lập phân đoạn có nhiệm vụ; chọn quan hệ nhân quả, thời gian hoặc ý tưởng.
3. Chia nhịp diễn biến: thông tin mới, hành vi, kết quả và phản ứng.
4. Phân công hình, âm và lời; chừa thời gian nhìn/nghe điều quan trọng.
5. Dự kiến nhịp/cảm xúc có điều kiện và kiểm lời hứa ở đầu/kết.
6. Rà tính khả thi trước khi chuyển sang danh sách shot; giữ các phần đã duyệt khi sửa.

## Đầu ra

[Schema đầu ra](../schema/script.schema.json) · [Mẫu hiện hành](../mau/kich-ban.json)

Kết quả kèm mã kiến thức, phiên bản, giả định và trạng thái kiểm nghiệm. Các mẫu chưa điền không phải sản phẩm đã phân tích.

## Tiêu chí duyệt

- Mỗi phần thay đổi điều gì đó hoặc có chức năng trải nghiệm rõ.
- Không thêm xung đột lớn chỉ để đủ công thức.
- Lời, hình và âm không vô tình mâu thuẫn.

Mã trọng tâm: [AU-001](../kien-thuc/AU-001.json), [ST-001](../kien-thuc/ST-001.json), [ST-003](../kien-thuc/ST-003.json), [ST-005](../kien-thuc/ST-005.json), [ST-007](../kien-thuc/ST-007.json), [ST-008](../kien-thuc/ST-008.json)

## Áp dụng và kiểm tra

Tách chủ đề khỏi góc tiếp cận theo YT-008. Với mỗi nhịp ghi thay đổi, điều đáng quan tâm và bằng chứng cuối nhịp. Dùng ST-009/ST-010/ST-011 để xử lý mạch rời, lặp không tiến và việc nhỏ thiếu giá trị; ST-012 khi cần mô-típ. Dựng sơ theo AI-009 trước tạo hàng loạt, bảo vệ dạng không thoại nếu đã chốt.
