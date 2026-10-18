# Thiết kế danh sách shot

Tác vụ: design_shots. Core 1.0.0.

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

shot-plan.schema.json; mau/danh-sach-shot.json

Kết quả kèm mã kiến thức, phiên bản, giả định và trạng thái kiểm nghiệm. Các mẫu chưa điền không phải sản phẩm đã phân tích.

## Tiêu chí duyệt

- Có thể dựng hiểu việc từ bộ góc.
- Mỗi shot có tiêu chí đạt cụ thể.
- Không nhầm một dòng câu lệnh với một shot chắc chắn sinh ra.

Mã trọng tâm: [DR-002](../kien-thuc/DR-002.json), [DR-006](../kien-thuc/DR-006.json), [CA-001](../kien-thuc/CA-001.json), [CA-004](../kien-thuc/CA-004.json), [MO-001](../kien-thuc/MO-001.json), [AI-003](../kien-thuc/AI-003.json), [ED-003](../kien-thuc/ED-003.json)
