# Chẩn đoán và sửa lỗi

Tác vụ: diagnose_and_repair. Core release 1.3.1; dẫn version của từng mục thực dùng.

[Mục lục](../README.md) · [Chuẩn quyết định](../03_RA_QUYET_DINH.md)

**Đầu vào:** Câu lệnh gốc, đầu vào, clip kết quả, model/chế độ, lỗi và phần đã đạt. Thiếu phần thiết yếu thì hỏi đúng phần đó.

## Cách thực hiện

1. Lưu bản gốc và ghi các thuộc tính phải giữ.
2. Tách triệu chứng nội dung, vật lý, camera, nhận diện, âm, điểm nối hoặc xuất.
3. Xác minh lỗi bằng mốc; kiểm đầu vào và mâu thuẫn trước khi thêm chữ.
4. Đặt giả thuyết và chọn sửa nhỏ, hậu kỳ, đổi đầu vào hoặc sinh lại.
5. Cho bản sửa và bản so thay đổi; nếu lập bản tối giản thì ghi đã thay nhiều biến.
6. Xem toàn kết quả theo cùng tiêu chí và ghi lỗi mới; chưa có clip thì chưa báo đã khắc phục.

## Đầu ra

[Schema đầu ra](../schema/decision.schema.json) · [Mẫu hiện hành](../mau/quyet-dinh.json) · [Ví dụ sửa lỗi](../vi-du/sua-loi-it-thay-doi.json)

Kết quả kèm mã kiến thức, phiên bản, giả định và trạng thái kiểm nghiệm. Các mẫu chưa điền không phải sản phẩm đã phân tích.

## Tiêu chí duyệt

- Giữ hành động, nhịp và hình đã đạt khi chỉ sửa một lỗi.
- Không đổ mọi lỗi cho người dùng hoặc hứa hết lỗi.
- Kiểm lại đầy đủ sau sửa.

Mã trọng tâm: [QC-002](../kien-thuc/QC-002.json), [AI-008](../kien-thuc/AI-008.json), [QC-003](../kien-thuc/QC-003.json), [MO-006](../kien-thuc/MO-006.json), [QC-001](../kien-thuc/QC-001.json)

## Áp dụng và kiểm tra

Phân loại lỗi trước: cấu trúc/thông tin, hành vi/tiếp xúc, hình/nhận diện, chuyển động, màu hoặc âm. Dùng phần failure_diagnosis và related_ids của mục liên quan để chọn giả thuyết; QC-008 chọn đúng phép kiểm. Ghi phần phải giữ, thử ít biến có mục đích; AI-012/QC-009 giúp quyết định sửa vùng, dựng, âm, tạo lại hoặc đổi công đoạn. Chưa có kết quả mới không báo đã khắc phục.

Rà riêng vẻ ảnh, ổn định theo thời gian, đúng hành động và điểm nối; QC-010 giúp định vị trước chọn công đoạn sửa. Sau xử lý mượt/sắc hoặc sửa vùng, kiểm lại thứ tự chạm–nhả và nhận diện ở vùng ảnh hưởng.
