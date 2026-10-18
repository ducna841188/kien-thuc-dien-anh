# MO — Chuyển động và thời gian

Phiên bản 1.3.0. Phân biệt máy/người/môi trường, chỉ đạo quỹ đạo và loại nhịp thời gian.

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
| [MO-007](#mo-007) | Tốc độ khung, thời gian phơi sáng và nhòe chuyển động | trung_cap |
| [MO-008](#mo-008) | Quỹ đạo, gia tốc và phối hợp máy–chủ thể | trung_cap |

<a id="mo-001"></a>
## MO-001 — Ba lớp chuyển động độc lập

**Phiên bản mục:** 1.0.0

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

**Phiên bản mục:** 1.0.0

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

**Phiên bản mục:** 1.0.0

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

**Phiên bản mục:** 1.0.0

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

**Phiên bản mục:** 1.0.0

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

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Thời gian trên màn hình quan hệ thế nào với thời gian sự việc?

**Dùng khi:** Khi dựng quá trình dài hoặc sửa yêu cầu timelapse.

**Nguyên lý thực hành:** Tách chuyển động chậm, tăng tốc liên tục, timelapse lấy mẫu theo thời gian và dựng lược qua các trạng thái. FPS đầu ra không tự cho biết tốc độ sự việc. Slow motion có thể cần nguồn tốc độ cao phát chậm; nội suy có thể tạo frame mới và lỗi. Timelapse, tua nhanh và lược thời gian không chứng minh cùng quá trình đã diễn ra liên tục.

**Cách làm:**

1. Ghi loại nhịp thời gian đã chốt.
2. Chọn dấu tiến triển cần nhìn thấy và bước có thể lược.
3. Kiểm chuyển động/nhòe/liên tục sau xử lý; giữ âm theo ý đồ thời gian.
4. Ghi thời gian trong thế giới, cách xử lý hình và thời lượng phát nếu biết; không đổi timelapse đã duyệt thành real time chỉ để dễ tạo.

**Đánh đổi:** Nén mạnh có thể làm mất kỹ thuật thao tác; kéo chậm có thể tạo cảm giác nặng hoặc giả.

**Kiểm tra:**

- Sửa lỗi số người không tự đổi timelapse thành thời gian thực.
- Thông số tệp và loại chuyển động được kiểm riêng.
- Không suy fps gốc hoặc thời gian thực của quá trình từ nhãn phong cách.

**Ví dụ tự biên soạn:** Phủ đất cả buổi được nén nhưng phải vẫn thấy kéo/trải đúng vật, không thành chuyển tấm phủ qua luống khác.

**Phản ví dụ / giới hạn:** Chuỗi mầm–cây–quả có thể là dựng lược, không đủ bằng chứng gọi timelapse chỉ từ ảnh tĩnh.

**Liên quan:** [EV-005](../kien-thuc/EV-005.json), [AI-005](../kien-thuc/AI-005.json), [ED-004](../kien-thuc/ED-004.json), [MO-007](../kien-thuc/MO-007.json), [AI-008](../kien-thuc/AI-008.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Thời gian kể chuyện và cách lấy mẫu/đổi tốc cần được ghi riêng.

**Tình huống:** Đoạn timelapse làm việc đạt nhưng có người thừa.

**Phần phải giữ:** Mục tiêu và các phần đã duyệt trong tình huống.

| Phương án | Thực hiện |
| --- | --- |
| A | Đổi sang cảnh chậm để model dễ làm. |
| B | Giữ loại thời gian, sửa nhận diện/số người và kiểm toàn pha. |

**Cách chọn:** Chọn B theo yêu cầu; chỉ đổi nhịp khi ràng buộc được xét lại rõ.

**Dấu hiệu kiểm trong ca:**

- Không suy fps gốc hoặc thời gian thực của quá trình từ nhãn phong cách.

**Nếu gặp:** Sửa lỗi hình nhưng video không còn trải nghiệm đã chốt.

Có thể do: Biến điều kiện thuận tiện của model thành thay đổi mục tiêu.

Thử tiếp: So bản sửa với danh sách phải giữ trước khi đánh giá riêng lỗi mới sửa.
**Nguồn đối chiếu:** [B011](../../bai-hoc/011-anh-sang-bo-nen-nhip-cham/README.md), [B015](../../bai-hoc/015-logic-chuyen-dong-vat-ly/README.md), [B033](../../bai-hoc/033-sua-prompt-bi-bo-qua/README.md), [SRC-YT-ENCODE](https://support.google.com/youtube/answer/1722171)

[Bản JSON chuẩn](../kien-thuc/MO-006.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="mo-007"></a>
## MO-007 — Tốc độ khung, thời gian phơi sáng và nhòe chuyển động

**Phiên bản mục:** 1.3.0

**Câu hỏi quyết định:** Độ nhòe và cách chuyển động được lấy mẫu có phù hợp ý đồ không?

**Dùng khi:** Thiết lập quay/xuất, chẩn đoán chuyển động giật hoặc mô tả motion blur cho AI.

**Nguyên lý thực hành:** Tốc độ khung quy định mật độ mẫu theo thời gian; thời gian phơi sáng góp phần tạo nhòe trong mỗi mẫu. Ở mô hình màn trập thông thường, t = góc/(360 × fps): 24 fps với 180° tương ứng khoảng 1/48 giây. Đây là ví dụ tính, không phải chuẩn bắt buộc để có điện ảnh.

**Cách làm:**

1. Chọn fps theo trải nghiệm chuyển động và quy trình phát; phân biệt quay tốc độ cao rồi phát chậm với đổi nhãn fps hoặc nội suy.
2. Với quay thật cân độ nhòe với tốc độ chủ thể/lia máy, phơi sáng và điều kiện đèn. Với AI kiểm fps tệp và nhòe thực, tách mô tả hình khỏi thiết lập mà dịch vụ thật hỗ trợ.
3. Khi đổi fps trong dựng, ghi cách xử lý: bỏ/lặp frame, nội suy hay đổi tốc độ. Duyệt chuyển động sau xuất, không chỉ xem timeline.
4. Kiểm riêng trước và sau nội suy/ổn định/đổi tốc: pha tiếp xúc, hình học tay/vật và nhịp dừng có còn đúng không. Chuyển động êm hơn không tự là hành động đúng hơn.

**Đánh đổi:** Phơi ngắn làm rõ pha nhanh nhưng có thể cho cảm giác giật; phơi dài làm mềm chuyển động nhưng có thể mất chi tiết tiếp xúc.

**Kiểm tra:**

- Không coi 24 fps hoặc 180° là bằng chứng chất lượng tự động.
- Không lấy upscale/nội suy làm bằng chứng phục hồi chuyển động thật.
- Bản xử lý không tạo frame trung gian làm đổi thứ tự chạm–nhả hoặc nhân đôi vật.

**Ví dụ tự biên soạn:** Động tác xoay bánh nhanh bị nhòe đến mất chốt: thử giảm độ nhòe hoặc giảm tốc hành động; vẫn giữ nhịp câu chuyện đã chọn.

**Phản ví dụ / giới hạn:** Ghi “1/48s” trong prompt không xác nhận model dùng thời gian phơi thật; 60 fps phát bình thường không tự là slow motion.

**Liên quan:** [MO-005](../kien-thuc/MO-005.json), [MO-006](../kien-thuc/MO-006.json), [LI-007](../kien-thuc/LI-007.json), [QC-001](../kien-thuc/QC-001.json), [QC-010](../kien-thuc/QC-010.json), [DR-008](../kien-thuc/DR-008.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Độ nhòe hình thành trong khoảng ghi mỗi frame, còn khoảng cách thời gian giữa frame quyết định lấy mẫu. Hai biến có liên hệ nhưng không thay thế nhau; còn phải kiểm tốc độ/độ lớn chuyển động trên màn hình.

**Tình huống:** Động tác xoay bánh nhanh bị nhòe đến mất chốt: thử giảm độ nhòe hoặc giảm tốc hành động; vẫn giữ nhịp câu chuyện đã chọn.

**Phần phải giữ:** Hành động xoay bánh và chốt cần đọc. Nhịp kể đã chọn.

| Phương án | Thực hiện |
| --- | --- |
| A | Đổi mọi clip sang 24 fps bằng thiết lập xuất rồi coi đã sửa giật. |
| B | Kiểm fps nguồn, nhịp frame, nhòe và cách chuyển đổi; sửa biến gây lỗi cụ thể. |

**Cách chọn:** Chọn B khi có lỗi chuyển động; A chỉ là thay thông số xuất và có thể sinh lỗi mới.

**Dấu hiệu kiểm trong ca:**

- Không coi 24 fps hoặc 180° là bằng chứng chất lượng tự động.
- Không lấy upscale/nội suy làm bằng chứng phục hồi chuyển động thật.

**Nếu gặp:** Chuyển động có nhịp khựng định kỳ dù ảnh sắc nét.

Có thể do: Chuyển fps bằng lặp/bỏ frame. Nguồn hoặc nội suy có frame lặp/biến dạng.

Thử tiếp: Xem nguồn và bản xuất ở tốc độ thường, rồi kiểm frame quanh chỗ khựng; so một bản không chuyển fps không cần thiết.

**Phát biểu được đối chiếu:** Theo mô hình màn trập mô tả, 24 fps và góc 180° cho khoảng phơi 1/48 giây. Nguồn: [SRC-RED-SHUTTER](https://www.reddigitalcinema.com/red-101/shutter-angle-tutorial).

**Giới hạn nguồn:** Không chứng minh 180° tối ưu cho mọi cảnh hoặc một model AI mô phỏng thông số máy quay thật.
**Nguồn đối chiếu:** [SRC-RED-SHUTTER](https://www.reddigitalcinema.com/red-101/shutter-angle-tutorial), [SRC-YT-ENCODE](https://support.google.com/youtube/answer/1722171)

[Bản JSON chuẩn](../kien-thuc/MO-007.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="mo-008"></a>
## MO-008 — Quỹ đạo, gia tốc và phối hợp máy–chủ thể

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Chuyển động này bắt đầu vì sao, đổi tốc ở đâu và kết vào thông tin nào?

**Dùng khi:** Chỉ đạo tracking/orbit hoặc sửa máy AI trôi, tăng tốc vô cớ và mất điểm quan trọng.

**Nguyên lý thực hành:** Một đường đi cần mốc không gian và mốc sự kiện, không chỉ tên động tác. Chọn quan hệ giữa máy và chủ thể, pha bắt đầu/tiếp diễn/dừng và thông tin ở khung cuối; nhịp chuyển động có thể tạo ý nghĩa ngay khi không cắt.

**Cách làm:**

1. Ghi máy bắt đầu ở đâu, chủ thể ở đâu, yếu tố nào đứng yên, vật mốc nào cho thấy thị sai và điểm nhìn kết thúc.
2. Nối tăng/giảm tốc với hành động hoặc hé lộ nếu phù hợp. Nếu cần tốc độ đều, nêu điều đó và kiểm lại; đừng đồng thời yêu cầu vừa khóa vị trí vừa bay vòng.
3. Với AI thử một chuyển động chính trước, xác định mức sai lệch chấp nhận; khi đường phức tạp lỗi hãy so phương án dàn cảnh hoặc cắt thay thế.

**Đánh đổi:** Chuyển động phối hợp có thể giàu thông tin nhưng tăng công kiểm hình học và đồng bộ; máy đứng yên vẫn có thể phục vụ cảnh tốt.

**Kiểm tra:**

- Khung cuối có chức năng cụ thể.
- Không có trôi/đổi tốc hoặc lặp chuyển động ngoài ý đồ ở các pha nối.

**Ví dụ tự biên soạn:** Máy đi ngang cùng người mang hộp, chậm lại khi người đặt hộp để điểm tiếp xúc ở trong khung; giữ bức tường như mốc không gian.

**Phản ví dụ / giới hạn:** Chuyển động tốc độ đều có thể là phong cách chủ ý; không áp đường cong tăng giảm tốc cho mọi shot.

**Liên quan:** [MO-001](../kien-thuc/MO-001.json), [MO-003](../kien-thuc/MO-003.json), [MO-005](../kien-thuc/MO-005.json), [CA-011](../kien-thuc/CA-011.json), [AI-013](../kien-thuc/AI-013.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Mốc không gian cho phép kiểm đường đi; mốc sự kiện cho phép kiểm lý do và thời điểm. Chúng biến tên chuyển động thành yêu cầu có thể duyệt.

**Tình huống:** Máy đi ngang cùng người mang hộp, chậm lại khi người đặt hộp để điểm tiếp xúc ở trong khung; giữ bức tường như mốc không gian.

**Phần phải giữ:** Đường người mang hộp. Điểm đặt hộp không ra ngoài khung.

| Phương án | Thực hiện |
| --- | --- |
| A | Yêu cầu orbit, zoom, pan và theo người cùng lúc mà không có thứ tự. |
| B | Chọn tracking ngang theo một hành động, điểm dừng gắn với lúc đặt hộp. |

**Cách chọn:** Chọn B khi mục tiêu là đọc hành động; thêm chuyển động chỉ khi có thông tin cụ thể cần nó.

**Dấu hiệu kiểm trong ca:**

- Khung cuối có chức năng cụ thể.
- Không có trôi/đổi tốc hoặc lặp chuyển động ngoài ý đồ ở các pha nối.

**Nếu gặp:** Máy đi đẹp nhưng sự kiện quan trọng ra ngoài khung.

Có thể do: Không có mốc cuối. Vận tốc máy và chủ thể không được phối hợp.

Thử tiếp: Dựng sơ bằng khung mốc, kiểm vùng thao tác trước khi sinh lại toàn shot.
**Nguồn đối chiếu:** [SRC-YALE-CAMERA](https://filmanalysis.yale.edu/cinematography/), [SRC-GOOGLE-PROMPT](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/video-gen-prompt-guide)

[Bản JSON chuẩn](../kien-thuc/MO-008.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).
