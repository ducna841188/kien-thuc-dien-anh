# Chẩn đoán và sửa lỗi

Tác vụ: diagnose_and_repair. Core 1.0.0.

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

decision.schema.json; vi-du/sua-loi-it-thay-doi.json

Kết quả kèm mã kiến thức, phiên bản, giả định và trạng thái kiểm nghiệm. Các mẫu chưa điền không phải sản phẩm đã phân tích.

## Tiêu chí duyệt

- Giữ hành động, nhịp và hình đã đạt khi chỉ sửa một lỗi.
- Không đổ mọi lỗi cho người dùng hoặc hứa hết lỗi.
- Kiểm lại đầy đủ sau sửa.

Mã trọng tâm: [QC-002](../kien-thuc/QC-002.json), [AI-008](../kien-thuc/AI-008.json), [QC-003](../kien-thuc/QC-003.json), [MO-006](../kien-thuc/MO-006.json), [QC-001](../kien-thuc/QC-001.json)
