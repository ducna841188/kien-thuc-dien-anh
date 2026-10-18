# Viết yêu cầu tạo ảnh/video

Tác vụ: write_generation_prompts. Core release 1.2.1; dẫn version của từng mục thực dùng.

[Mục lục](../README.md) · [Chuẩn quyết định](../03_RA_QUYET_DINH.md)

**Đầu vào:** Kế hoạch shot, tài sản được duyệt, model/chế độ/dịch vụ thực và những điều cần giữ.

## Cách thực hiện

1. Đọc hồ sơ model đúng phiên bản; thiếu thì ghi unknown.
2. Phân quyền tham chiếu cho mặt, thân, áo, cảnh, vật và chuyển động.
3. Tách điều ảnh đã cho khỏi diễn tiến chữ cần yêu cầu.
4. Viết hành động có đối tượng, trạng thái và đường máy; chỉ thêm thuộc tính có chức năng.
5. Đặt thông số ở nơi thực hỗ trợ; dùng negative theo đúng hướng dẫn chế độ nếu có.
6. Trả câu lệnh, cách nhập, phần chưa xác minh và tiêu chí xem lại; không tự chạy dịch vụ trả phí.

## Đầu ra

[Schema đầu ra](../schema/generation-request.schema.json) · [Mẫu hiện hành](../mau/yeu-cau-tao.json)

Kết quả kèm mã kiến thức, phiên bản, giả định và trạng thái kiểm nghiệm. Các mẫu chưa điền không phải sản phẩm đã phân tích.

## Tiêu chí duyệt

- Không bịa tham số khóa hoặc năng lực công cụ.
- Câu lệnh phục vụ đúng job và tài sản.
- Ghi tested=false khi chưa có lần chạy.

Mã trọng tâm: [AI-001](../kien-thuc/AI-001.json), [AI-002](../kien-thuc/AI-002.json), [AI-003](../kien-thuc/AI-003.json), [AI-004](../kien-thuc/AI-004.json), [AI-007](../kien-thuc/AI-007.json)

## Áp dụng và kiểm tra

Kiểm khả thi ảnh đầu theo AI-011 và sổ trạng thái theo AI-010. Tách ý đồ, tham chiếu và thiết lập thật của model/chế độ theo AI-013. Chuẩn bị tiêu chí toàn clip và mốc rủi ro; không coi từ khóa lens/fps/8K hoặc seed là khóa tuyệt đối. AI-012 giúp giao phần chính xác sang hậu kỳ khi có cách làm phù hợp. Chưa sinh đầu ra thì giữ trạng thái yêu cầu/đề xuất.
