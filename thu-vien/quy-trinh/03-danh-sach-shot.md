# Thiết kế danh sách shot

Tác vụ: design_shots. Core release 1.3.1; dẫn version của từng mục thực dùng.

[Mục lục](../README.md) · [Chuẩn quyết định](../03_RA_QUYET_DINH.md)

**Đầu vào:** Kịch bản/nhịp đã duyệt, bộ tham chiếu, ràng buộc công cụ/chi phí và chuẩn hình đích.

## Cách thực hiện

1. Với mỗi nhịp, nêu bằng chứng phải nhìn/nghe.
2. Lập vị trí người/vật và trạng thái đầu–tiếp xúc–kết.
3. Chọn cỡ, góc, bố cục, nét và đường máy theo nhiệm vụ.
4. Ghi sáng/màu/âm và loại nhịp thời gian; đánh dấu phần giữ qua điểm nối.
5. Chọn bộ góc tối thiểu và dự phòng có mục đích.
6. Tách shot dựng với job sinh; thời lượng mục tiêu chưa thành cài đặt hỗ trợ cho tới khi kiểm.

## Đầu ra

[Schema đầu ra](../schema/shot-plan.schema.json) · [Mẫu hiện hành](../mau/danh-sach-shot.json)

Kết quả kèm mã kiến thức, phiên bản, giả định và trạng thái kiểm nghiệm. Các mẫu chưa điền không phải sản phẩm đã phân tích.

## Tiêu chí duyệt

- Có thể dựng hiểu việc từ bộ góc.
- Mỗi shot có tiêu chí đạt cụ thể.
- Không nhầm một dòng câu lệnh với một shot chắc chắn sinh ra.

Mã trọng tâm: [DR-002](../kien-thuc/DR-002.json), [DR-006](../kien-thuc/DR-006.json), [CA-001](../kien-thuc/CA-001.json), [CA-004](../kien-thuc/CA-004.json), [MO-001](../kien-thuc/MO-001.json), [AI-003](../kien-thuc/AI-003.json), [ED-003](../kien-thuc/ED-003.json)

## Áp dụng và kiểm tra

Ghi chức năng và trạng thái vào/ra trước thông số. CA-011/CA-012 giúp bố cục theo thời gian và vùng nét đủ đọc; MO-007/MO-008 cho nhòe, quỹ đạo và nhịp chuyển động; LI-007/LI-008 cho phơi sáng và đường sáng. Với tiếp xúc, xác định điểm đỡ, pha chạm/nhả và cách nối qua ED-009/ED-010. Chỉ nêu số máy quay thật khi có điều kiện, còn AI cần kiểm kết quả.

Lập mặt bằng và bộ góc theo bằng chứng cần dựng, không theo danh sách cỡ máy mặc định. [Mẫu hiện hành](../mau/danh-sach-shot.json) có đủ bốn shot của chuỗi 12 giây giả lập; lượt đặt bát thứ hai được lược tại cut 2→3. Thời gian dùng trong dựng tách khỏi thời lượng job và phần dư.
