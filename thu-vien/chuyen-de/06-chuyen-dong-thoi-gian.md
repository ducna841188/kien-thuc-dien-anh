# MO — Chuyển động và thời gian

Phiên bản 1.0.0. Phân biệt máy/người/môi trường, chỉ đạo quỹ đạo và loại nhịp thời gian.

[Mục lục](../README.md) · [Chuẩn ra quyết định](../03_RA_QUYET_DINH.md)

Mỗi mục dưới là hướng dẫn có điều kiện. Tác dụng cảm xúc là giả thuyết thiết kế; chưa có thử tạo video hoặc kiểm nghiệm khán giả cho các ví dụ mới. Thuật ngữ xem [từ điển](../TU_DIEN.md).

| Mã | Quyết định | Mức |
| --- | --- | --- |
| [MO-001](#mo-001) | Ba lớp chuyển động độc lập | co_ban |
| [MO-002](#mo-002) | Pan, tilt và roll: đổi hướng nhìn | co_ban |
| [MO-003](#mo-003) | Dolly, truck, tracking và orbit: đổi vị trí | trung_cap |
| [MO-004](#mo-004) | Tiến máy, zoom và crop | trung_cap |
| [MO-005](#mo-005) | Tốc độ, tăng giảm tốc và điểm dừng | nang_cao |
| [MO-006](#mo-006) | Thời gian thực, chậm, tua nhanh và lược thời gian | trung_cap |

<a id="mo-001"></a>
## MO-001 — Ba lớp chuyển động độc lập

**Câu hỏi quyết định:** Thứ gì đang chuyển động: máy, chủ thể hay môi trường?

**Dùng khi:** Khi mô tả hoặc sửa chuyển động AI.

**Nguyên lý thực hành:** Ghi riêng ba lớp để tránh yêu cầu camera biến thành chủ thể di chuyển. Không cần cả ba cùng hoạt động.

**Cách làm:**

1. Chọn lớp chuyển động chính phục vụ cảnh.
2. Ghi lớp nào giữ ổn định.
3. Thêm phản ứng môi trường có nguyên nhân nếu cần.

**Đánh đổi:** Nhiều chuyển động làm hình giàu năng lượng nhưng có thể khó theo và khó tạo nhất quán.

**Kiểm tra:**

- Máy tĩnh không bị mô tả như nền phải tự di chuyển.
- Gió, bụi, nước phản ứng phù hợp thay vì thêm hiệu ứng vô cớ.

**Ví dụ tự biên soạn:** Người đi ngang trước máy cố định là cảnh hợp lệ; tracking là máy đổi vị trí để theo người.

**Phản ví dụ / giới hạn:** Hình có sức sống vẫn có thể chỉ nhờ một cử động tay nhỏ và âm thanh.

**Liên quan:** [CA-010](../kien-thuc/CA-010.json), [DR-001](../kien-thuc/DR-001.json), [AI-003](../kien-thuc/AI-003.json)

**Nguồn đối chiếu:** [B015](../../bai-hoc/015-logic-chuyen-dong-vat-ly/README.md), [B018](../../bai-hoc/018-dolly-pan-tilt/README.md), [SRC-GOOGLE-I2V](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/best-practice)

[Bản JSON chuẩn](../kien-thuc/MO-001.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="mo-002"></a>
## MO-002 — Pan, tilt và roll: đổi hướng nhìn

**Câu hỏi quyết định:** Máy xoay hướng nào từ vị trí nào?

**Dùng khi:** Khi cần lia, ngẩng/cúi hoặc nghiêng.

**Nguyên lý thực hành:** Pan là xoay hướng ngang; tilt là ngẩng/cúi; roll là xoay quanh trục nhìn. Mô tả vật bắt đầu, vật kết thúc và điểm đặt máy.

**Cách làm:**

1. Nêu máy gần như giữ vị trí hay có dịch đồng thời.
2. Ghi hướng, mục tiêu và lý do đổi hướng nhìn.
3. Chọn điểm bắt đầu/dừng dễ kiểm trong không gian.

**Đánh đổi:** Lia quá nhanh dễ mất chi tiết; lia không có thông tin mới có thể chỉ trang trí.

**Kiểm tra:**

- Không gọi quỹ đạo đi quanh người là pan.
- Tilt không bị dùng để chỉ chân trời nghiêng.

**Ví dụ tự biên soạn:** Lia từ bàn tay làm việc sang người đang chờ giúp chuyển trọng tâm.

**Phản ví dụ / giới hạn:** Pan có thể kết hợp dịch máy, nhưng khi đó cần ghi cả hai lớp thay vì đổi tên tùy ý.

**Liên quan:** [CA-002](../kien-thuc/CA-002.json), [MO-003](../kien-thuc/MO-003.json), [AU-002](../kien-thuc/AU-002.json)

**Nguồn đối chiếu:** [B018](../../bai-hoc/018-dolly-pan-tilt/README.md), [B025](../../bai-hoc/025-dieu-khien-camera/README.md), [B031](../../bai-hoc/031-tu-mo-ta-den-dao-dien/README.md)

[Bản JSON chuẩn](../kien-thuc/MO-002.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="mo-003"></a>
## MO-003 — Dolly, truck, tracking và orbit: đổi vị trí

**Câu hỏi quyết định:** Máy đi theo đường nào và giữ quan hệ gì?

**Dùng khi:** Khi tạo tiến/lùi, ngang, bám hoặc đi vòng.

**Nguyên lý thực hành:** Đường máy cần điểm đầu, quỹ đạo, đích và đối tượng bám. Tracking mô tả quan hệ theo chủ thể, không chỉ một hướng ngang.

**Cách làm:**

1. Ghi mốc đầu và cuối trong cảnh.
2. Ghi máy đi sang phía nào, khoảng cách/độ cao có đổi không.
3. Chọn dấu nền để kiểm thị sai và sự liên tục.

**Đánh đổi:** Đi máy nhiều có thể lộ vùng chưa có tham chiếu, tăng suy diễn và lỗi AI.

**Kiểm tra:**

- Chủ thể không tự xoay hoặc tự chạy sát máy ngoài ý đồ.
- Vật gần–xa dịch tương đối phù hợp đường máy.

**Ví dụ tự biên soạn:** Đi cung ngắn quanh chiếc bình để lộ quai sau, giữ vật đứng yên.

**Phản ví dụ / giới hạn:** Một máy cố định và chủ thể tự xoay có thể đạt nhu cầu giới thiệu vật, nhưng đó là phương án khác.

**Liên quan:** [CA-005](../kien-thuc/CA-005.json), [MO-001](../kien-thuc/MO-001.json), [AI-002](../kien-thuc/AI-002.json)

**Nguồn đối chiếu:** [B001](../../bai-hoc/001-bon-cau-truc-camera/README.md), [B018](../../bai-hoc/018-dolly-pan-tilt/README.md), [B028](../../bai-hoc/028-slow-push-in/README.md)

[Bản JSON chuẩn](../kien-thuc/MO-003.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="mo-004"></a>
## MO-004 — Tiến máy, zoom và crop

**Câu hỏi quyết định:** Muốn thay quan hệ không gian hay chỉ thay vùng nhìn?

**Dùng khi:** Khi cần đến gần hoặc chỉnh khung hậu kỳ.

**Nguyên lý thực hành:** Dolly thay vị trí; zoom thay tiêu cự/góc nhìn quang học; crop/phóng hậu kỳ chọn vùng ảnh. Chúng không mặc định tạo cùng biến đổi phối cảnh.

**Cách làm:**

1. Chọn mục đích: gần gũi, lộ thông tin hay chỉnh khuôn.
2. Ghi thay đổi chủ thể và nền mong muốn.
3. Nếu cần chính xác, kiểm video bằng vật mốc và metadata có sẵn.

**Đánh đổi:** Crop có thể tiết kiệm tạo lại nhưng làm giảm phần thông tin/độ phân giải sử dụng.

**Kiểm tra:**

- Không gọi mọi phóng to là máy tiến.
- Phương án xử lý hậu kỳ có đủ chất lượng ở kích thước xuất.

**Ví dụ tự biên soạn:** Tiến gần bàn tay có thể thay tương quan với nền; crop một khung tĩnh chỉ làm vùng đã có lớn hơn.

**Phản ví dụ / giới hạn:** Zoom là lựa chọn có chủ ý, không phải dấu hiệu AI hiểu sai trong mọi trường hợp.

**Liên quan:** [CA-008](../kien-thuc/CA-008.json), [MO-003](../kien-thuc/MO-003.json), [AI-008](../kien-thuc/AI-008.json)

**Nguồn đối chiếu:** [B001](../../bai-hoc/001-bon-cau-truc-camera/README.md), [B015](../../bai-hoc/015-logic-chuyen-dong-vat-ly/README.md), [B028](../../bai-hoc/028-slow-push-in/README.md)

[Bản JSON chuẩn](../kien-thuc/MO-004.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="mo-005"></a>
## MO-005 — Tốc độ, tăng giảm tốc và điểm dừng

**Câu hỏi quyết định:** Năng lượng chuyển động thay đổi ở đoạn nào?

**Dùng khi:** Khi nhịp máy/hành động cần phục vụ thông tin hoặc cảm xúc.

**Nguyên lý thực hành:** Ngoài nhanh/chậm, mô tả lúc bắt đầu, giữ đều, giảm tốc và dừng. Dừng ở đúng thông tin có thể quan trọng hơn đường đi.

**Cách làm:**

1. Chọn sự kiện bắt đầu và điểm dừng.
2. Mô tả tương quan tốc độ người–máy, không chỉ tính từ.
3. Cho đủ thời gian đọc điều được hé lộ hoặc kết quả thao tác.

**Đánh đổi:** Làm mượt mọi chuyển động có thể mất lực hoặc cảm giác quan sát thật.

**Kiểm tra:**

- Máy không dừng trước khi thông tin chính xuất hiện.
- Tốc độ không làm mất đọc hành động quan trọng.

**Ví dụ tự biên soạn:** Máy theo giỏ được đặt xuống rồi dừng để nhìn mức đầy; hành động tiếp tục bên trong khung.

**Phản ví dụ / giới hạn:** Cú giật hoặc đổi tốc bất ngờ có thể là chủ ý phù hợp một phong cách khác.

**Liên quan:** [ED-002](../kien-thuc/ED-002.json), [AU-004](../kien-thuc/AU-004.json), [CA-010](../kien-thuc/CA-010.json)

**Nguồn đối chiếu:** [B021](../../bai-hoc/021-lam-chu-cam-xuc/README.md), [B025](../../bai-hoc/025-dieu-khien-camera/README.md)

[Bản JSON chuẩn](../kien-thuc/MO-005.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="mo-006"></a>
## MO-006 — Thời gian thực, chậm, tua nhanh và lược thời gian

**Câu hỏi quyết định:** Thời gian trên màn hình quan hệ thế nào với thời gian sự việc?

**Dùng khi:** Khi dựng quá trình dài hoặc sửa yêu cầu timelapse.

**Nguyên lý thực hành:** Tách chuyển động chậm, tăng tốc liên tục, timelapse lấy mẫu theo thời gian và dựng lược qua các trạng thái. FPS đầu ra không tự cho biết tốc độ sự việc.

**Cách làm:**

1. Ghi loại nhịp thời gian đã chốt.
2. Chọn dấu tiến triển cần nhìn thấy và bước có thể lược.
3. Kiểm chuyển động/nhòe/liên tục sau xử lý; giữ âm theo ý đồ thời gian.

**Đánh đổi:** Nén mạnh có thể làm mất kỹ thuật thao tác; kéo chậm có thể tạo cảm giác nặng hoặc giả.

**Kiểm tra:**

- Sửa lỗi số người không tự đổi timelapse thành thời gian thực.
- Thông số tệp và loại chuyển động được kiểm riêng.

**Ví dụ tự biên soạn:** Phủ đất cả buổi được nén nhưng phải vẫn thấy kéo/trải đúng vật, không thành chuyển tấm phủ qua luống khác.

**Phản ví dụ / giới hạn:** Chuỗi mầm–cây–quả có thể là dựng lược, không đủ bằng chứng gọi timelapse chỉ từ ảnh tĩnh.

**Liên quan:** [EV-005](../kien-thuc/EV-005.json), [AI-005](../kien-thuc/AI-005.json), [ED-004](../kien-thuc/ED-004.json)

**Nguồn đối chiếu:** [B011](../../bai-hoc/011-anh-sang-bo-nen-nhip-cham/README.md), [B015](../../bai-hoc/015-logic-chuyen-dong-vat-ly/README.md), [B033](../../bai-hoc/033-sua-prompt-bi-bo-qua/README.md)

[Bản JSON chuẩn](../kien-thuc/MO-006.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).
