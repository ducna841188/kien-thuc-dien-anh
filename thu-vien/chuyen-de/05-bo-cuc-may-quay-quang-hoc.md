# CA — Bố cục, máy quay và quang học

Phiên bản 1.0.0. Chọn thông tin trong khung, góc nhìn, khoảng cách và vùng nét.

[Mục lục](../README.md) · [Chuẩn ra quyết định](../03_RA_QUYET_DINH.md)

Mỗi mục dưới là hướng dẫn có điều kiện. Tác dụng cảm xúc là giả thuyết thiết kế; chưa có thử tạo video hoặc kiểm nghiệm khán giả cho các ví dụ mới. Thuật ngữ xem [từ điển](../TU_DIEN.md).

| Mã | Quyết định | Mức |
| --- | --- | --- |
| [CA-001](#ca-001) | Cỡ cảnh theo thông tin phải thấy | co_ban |
| [CA-002](#ca-002) | Độ cao, góc nhìn và độ nghiêng | co_ban |
| [CA-003](#ca-003) | Bố cục và trọng tâm theo thời gian | trung_cap |
| [CA-004](#ca-004) | Địa lý màn hình và hướng liên tục | trung_cap |
| [CA-005](#ca-005) | Chiều sâu và không gian ngoài khung | trung_cap |
| [CA-006](#ca-006) | Quan hệ máy với nhân vật: qua vai, hai người, điểm nhìn | trung_cap |
| [CA-007](#ca-007) | Nét, vùng nét và chuyển sự chú ý | trung_cap |
| [CA-008](#ca-008) | Tiêu cự, khoảng cách và phối cảnh | nang_cao |
| [CA-009](#ca-009) | Khung hình và cách xem thực tế | trung_cap |
| [CA-010](#ca-010) | Cú máy dài và thiết kế thay đổi trong khung | nang_cao |

<a id="ca-001"></a>
## CA-001 — Cỡ cảnh theo thông tin phải thấy

**Câu hỏi quyết định:** Khán giả cần thấy quan hệ không gian hay chi tiết nào?

**Dùng khi:** Khi chọn khung cho một nhiệm vụ kể chuyện.

**Nguyên lý thực hành:** Toàn, trung, cận và đặc tả mô tả lượng chủ thể/không gian trong khung. Cỡ cảnh không tự xác định tiêu cự, góc hoặc cảm xúc.

**Cách làm:**

1. Chỉ ra bằng chứng bắt buộc phải nằm trong khung.
2. Chọn cỡ đủ để đọc bằng chứng trên màn hình xem thực tế.
3. Ghi phần cơ thể/vật thể được thấy thay vì chỉ viết chữ viết tắt.

**Đánh đổi:** Khung gần làm rõ chi tiết nhưng có thể mất hướng và quy mô.

**Kiểm tra:**

- Không cắt mất điểm tiếp xúc cần xem.
- Tên cỡ và nội dung khung không mâu thuẫn.

**Ví dụ tự biên soạn:** Toàn cho thấy khoảng cách hai người; cận cho thấy một bàn tay vừa siết chặt.

**Phản ví dụ / giới hạn:** Cận mặt không bắt buộc giàu cảm xúc hơn toàn thân trong mọi cảnh.

**Liên quan:** [AU-002](../kien-thuc/AU-002.json), [CA-003](../kien-thuc/CA-003.json), [DR-006](../kien-thuc/DR-006.json)

**Nguồn đối chiếu:** [B005](../../bai-hoc/005-bay-cu-may/README.md), [B010](../../bai-hoc/010-lam-chu-ngon-ngu-dien-anh/README.md)

[Bản JSON chuẩn](../kien-thuc/CA-001.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ca-002"></a>
## CA-002 — Độ cao, góc nhìn và độ nghiêng

**Câu hỏi quyết định:** Máy ở đâu và nhìn theo hướng nào?

**Dùng khi:** Khi viết góc máy hoặc phân tích một hình.

**Nguyên lý thực hành:** Tách độ cao đặt máy, hướng ngẩng/cúi và độ nghiêng chân trời. Tác dụng quan hệ nhìn phụ thuộc cảnh và điểm nhìn được chọn.

**Cách làm:**

1. Ghi vị trí máy so với chủ thể/vật mốc.
2. Ghi hướng nhìn và phần cần thấy từ trên/dưới.
3. Chỉ dùng nghiêng chân trời khi có lý do; kiểm đường thẳng làm mốc.

**Đánh đổi:** Góc nổi bật có thể gây chú ý vào thủ pháp thay vì việc đang xảy ra.

**Kiểm tra:**

- Không gọi máy thấp là góc ngẩng nếu hướng nhìn gần ngang.
- Dutch angle là khung nghiêng; tilt là ngẩng/cúi, hai khái niệm được tách.

**Ví dụ tự biên soạn:** Đặt máy ngang đầu con chó để thấy quan hệ với người; góc cao trên bàn để đọc bố trí.

**Phản ví dụ / giới hạn:** Góc cao có thể giải thích công việc, không tự làm nhân vật yếu.

**Liên quan:** [MO-002](../kien-thuc/MO-002.json), [ST-006](../kien-thuc/ST-006.json), [CA-004](../kien-thuc/CA-004.json)

**Nguồn đối chiếu:** [B010](../../bai-hoc/010-lam-chu-ngon-ngu-dien-anh/README.md), [B018](../../bai-hoc/018-dolly-pan-tilt/README.md), [B031](../../bai-hoc/031-tu-mo-ta-den-dao-dien/README.md)

[Bản JSON chuẩn](../kien-thuc/CA-002.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ca-003"></a>
## CA-003 — Bố cục và trọng tâm theo thời gian

**Câu hỏi quyết định:** Điều gì được ưu tiên ở đầu và cuối khung?

**Dùng khi:** Khi hình nhiều chi tiết hoặc trọng tâm chuyển.

**Nguyên lý thực hành:** Bố cục gồm vị trí, khoảng trống, đường nét, tương phản và chuyển động. Quy tắc chia ba/đối xứng là phương án, không tiêu chuẩn chất lượng duy nhất.

**Cách làm:**

1. Đặt trọng tâm chính và phần thông tin hỗ trợ.
2. Rà vật ở mép, vật cắt thân và đường dẫn mắt cạnh tranh.
3. Xem khung đầu–giữa–cuối vì bố cục thay đổi cùng hành động.

**Đánh đổi:** Bố cục quá hoàn hảo có thể mất tự nhiên; lệch khung có thể có dụng ý.

**Kiểm tra:**

- Mắt người xem tìm được việc chính đúng lúc.
- Không có yếu tố nền vô tình nổi hơn bằng chứng cần thấy.

**Ví dụ tự biên soạn:** Một khoảng trống bên phía nhân vật nhìn có thể dành chỗ cho điều sắp xuất hiện.

**Phản ví dụ / giới hạn:** Đặt giữa khung vẫn phù hợp nghi lễ, đồ vật hoặc thiết kế đối xứng.

**Liên quan:** [AU-002](../kien-thuc/AU-002.json), [CA-005](../kien-thuc/CA-005.json), [CO-003](../kien-thuc/CO-003.json)

**Nguồn đối chiếu:** [B005](../../bai-hoc/005-bay-cu-may/README.md), [B025](../../bai-hoc/025-dieu-khien-camera/README.md)

[Bản JSON chuẩn](../kien-thuc/CA-003.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ca-004"></a>
## CA-004 — Địa lý màn hình và hướng liên tục

**Câu hỏi quyết định:** Qua điểm cắt, người xem có giữ được ai ở đâu không?

**Dùng khi:** Khi có nhiều góc, người di chuyển hoặc hội thoại.

**Nguyên lý thực hành:** Duy trì hoặc chủ động thay đổi quan hệ trái–phải, hướng đi và hướng nhìn. Trục 180 độ là công cụ định hướng, không luật cấm phá.

**Cách làm:**

1. Vẽ trục hành động và vị trí các góc dự định.
2. Kiểm hướng nhìn/đi và vị trí vật qua cut.
3. Khi đổi bên trục, dùng tín hiệu tái định hướng hoặc mục đích rõ.

**Đánh đổi:** Giữ trục cứng có thể hạn chế góc hữu ích; đổi trục không báo dễ gây lạc hướng.

**Kiểm tra:**

- Người xem xác định được quan hệ không cần nhìn lại.
- Chủ ý gây mất định hướng được ghi trong bản yêu cầu.

**Ví dụ tự biên soạn:** Người nhìn ra cửa ở bên phải; góc tiếp cho thấy cửa phù hợp quan hệ đã thiết lập.

**Phản ví dụ / giới hạn:** Cảnh nhìn thẳng theo trục hoặc chuyển máy liên tục có thể giúp đổi bên dễ hiểu.

**Liên quan:** [DR-002](../kien-thuc/DR-002.json), [ED-003](../kien-thuc/ED-003.json), [EV-004](../kien-thuc/EV-004.json)

**Nguồn đối chiếu:** [B013](../../bai-hoc/013-tach-shot-hoi-thoai/README.md), [B027](../../bai-hoc/027-tach-shot-lip-sync/README.md)

[Bản JSON chuẩn](../kien-thuc/CA-004.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ca-005"></a>
## CA-005 — Chiều sâu và không gian ngoài khung

**Câu hỏi quyết định:** Quan hệ gần–xa và phần chưa thấy đóng vai trò gì?

**Dùng khi:** Khi tạo cảm giác nơi chốn, quy mô hoặc thông tin giấu.

**Nguyên lý thực hành:** Dùng lớp gần–giữa–xa, che khuất, tỷ lệ và đường không gian để làm rõ quan hệ. Phần ngoài khung có thể được gợi bằng nhìn hoặc tiếng.

**Cách làm:**

1. Chọn vật mốc gần/xa có liên quan cảnh.
2. Giữ chủ thể và hành động đọc được qua lớp che.
3. Ghi điều ngoài khung đang được gợi và lúc nào sẽ/không được lộ.

**Đánh đổi:** Nhiều lớp tăng chiều sâu nhưng có thể làm hình rối và AI biến hình khi máy đi.

**Kiểm tra:**

- Lớp gần không che mất thao tác ngoài ý đồ.
- Thị sai và che khuất hợp lý khi vị trí máy thay đổi.

**Ví dụ tự biên soạn:** Khung cửa làm lớp gần khi người ở sân; một tiếng gọi gợi người chưa xuất hiện.

**Phản ví dụ / giới hạn:** Một khung phẳng có thể phù hợp đồ họa hoặc ý đồ cô lập, không tự kém điện ảnh.

**Liên quan:** [SO-003](../kien-thuc/SO-003.json), [MO-003](../kien-thuc/MO-003.json), [ST-006](../kien-thuc/ST-006.json)

**Nguồn đối chiếu:** [B001](../../bai-hoc/001-bon-cau-truc-camera/README.md), [B012](../../bai-hoc/012-cau-truc-camera/README.md)

[Bản JSON chuẩn](../kien-thuc/CA-005.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ca-006"></a>
## CA-006 — Quan hệ máy với nhân vật: qua vai, hai người, điểm nhìn

**Câu hỏi quyết định:** Người xem được đặt vào quan hệ với ai?

**Dùng khi:** Khi quay tương tác, quan sát hoặc chủ quan.

**Nguyên lý thực hành:** Tách số người trong khung, vị trí qua vai và POV. Chọn dựa trên cần thấy quan hệ chung hay trải nghiệm riêng.

**Cách làm:**

1. Chọn người/điểm quan sát gắn với shot.
2. Ghi ai thấy rõ, ai ở tiền cảnh hoặc ngoài khung.
3. Kiểm hướng mắt và vật được nhìn trong shot kế.

**Đánh đổi:** Qua vai giúp quan hệ nhưng có thể che thao tác hoặc tăng khó tạo AI hai người.

**Kiểm tra:**

- Người nói/người nghe không bị gán lẫn.
- POV phù hợp độ cao, vị trí và vật cản của nhân vật nếu muốn chủ quan thực.

**Ví dụ tự biên soạn:** Hai người cùng khung cho thấy trao bát; cận người nhận cho thấy phản ứng; POV cho thấy món họ nhìn.

**Phản ví dụ / giới hạn:** Một máy gần mặt không tự là POV; máy vẫn có thể quan sát người đó từ ngoài.

**Liên quan:** [DR-004](../kien-thuc/DR-004.json), [CA-004](../kien-thuc/CA-004.json), [SO-002](../kien-thuc/SO-002.json)

**Nguồn đối chiếu:** [B005](../../bai-hoc/005-bay-cu-may/README.md), [B013](../../bai-hoc/013-tach-shot-hoi-thoai/README.md), [B029](../../bai-hoc/029-lip-sync-hoat-hinh/README.md)

[Bản JSON chuẩn](../kien-thuc/CA-006.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ca-007"></a>
## CA-007 — Nét, vùng nét và chuyển sự chú ý

**Câu hỏi quyết định:** Những mặt phẳng nào cần đọc rõ và ở thời điểm nào?

**Dùng khi:** Khi nền mờ hoặc chuyển nét ảnh hưởng hiểu cảnh.

**Nguyên lý thực hành:** Focus là mặt phẳng lấy nét; depth of field là vùng độ sâu được xem đủ nét trong điều kiện hiển thị. Rack focus là đổi mặt phẳng nét, không phải đường máy.

**Cách làm:**

1. Chọn đích nét theo bằng chứng cần đọc.
2. Giữ đủ độ sâu cho nhiều phần thao tác nếu cần.
3. Nếu chuyển nét, ghi từ vật nào sang vật nào và tác nhân chuyển.

**Đánh đổi:** Vùng nét nông có thể tách chủ thể nhưng làm tay/vật quan trọng mất rõ.

**Kiểm tra:**

- Mắt hoặc điểm tiếp xúc quan trọng rõ đúng lúc.
- Không dùng bokeh như yêu cầu mặc định cho mọi cảnh.

**Ví dụ tự biên soạn:** Khi luồn kim, tay và lỗ kim đều cần đọc; khi nhận ra người ngoài cửa có thể chuyển nét tới cửa.

**Phản ví dụ / giới hạn:** Cảnh sâu nhiều lớp có thể cần đọc đồng thời thay vì làm nền mờ.

**Liên quan:** [AU-002](../kien-thuc/AU-002.json), [LI-004](../kien-thuc/LI-004.json), [AI-001](../kien-thuc/AI-001.json)

**Nguồn đối chiếu:** [B008](../../bai-hoc/008-muoi-cu-phap-veo/README.md), [B011](../../bai-hoc/011-anh-sang-bo-nen-nhip-cham/README.md), [SRC-YALE-CAMERA](https://filmanalysis.yale.edu/cinematography/)

[Bản JSON chuẩn](../kien-thuc/CA-007.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ca-008"></a>
## CA-008 — Tiêu cự, khoảng cách và phối cảnh

**Câu hỏi quyết định:** Cảm giác gần–xa đến từ vị trí máy hay góc nhìn ống kính?

**Dùng khi:** Khi mô tả tạo hình, chọn ống hoặc phân tích hình bị méo.

**Nguyên lý thực hành:** Khoảng cách và vị trí nhìn quyết định quan hệ phối cảnh; tiêu cự cùng định dạng ảnh quyết định góc nhìn. Đổi ống rồi lùi máy để giữ cỡ đã đổi cả vị trí nhìn.

**Cách làm:**

1. Chọn cỡ cảnh và khoảng cách mong muốn trước.
2. Ghi cách nền/tiền cảnh nên quan hệ với chủ thể.
3. Nếu dùng số mm, ghi định dạng tham chiếu hoặc coi đó là ý đồ chưa đo.

**Đánh đổi:** Ống rộng ở gần có thể nhấn chênh khoảng cách; đứng xa hơn có thể làm các lớp có vẻ sát nhau.

**Kiểm tra:**

- Không quy mọi méo mặt cho một số mm.
- Không suy chính xác tiêu cự hoặc máy từ một khung thiếu metadata.

**Ví dụ tự biên soạn:** Muốn thấy người cùng căn bếp, chọn vị trí đủ đọc không gian; muốn nền như gần hơn thì xét góc nhìn và khoảng cách cùng nhau.

**Phản ví dụ / giới hạn:** Một cận góc rộng có thể là chủ ý biểu cảm; không phải lỗi bắt buộc sửa.

**Liên quan:** [CA-001](../kien-thuc/CA-001.json), [MO-004](../kien-thuc/MO-004.json), [EV-004](../kien-thuc/EV-004.json)

**Nguồn đối chiếu:** [B021](../../bai-hoc/021-lam-chu-cam-xuc/README.md), [SRC-ARRI-FORMAT](https://www.arri.com/en/learn/camera-systems/frequently-asked-questions/alexa-lf-faq)

[Bản JSON chuẩn](../kien-thuc/CA-008.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ca-009"></a>
## CA-009 — Khung hình và cách xem thực tế

**Câu hỏi quyết định:** Bố cục có sống được ở nơi khán giả xem không?

**Dùng khi:** Khi chọn tỷ lệ ngang/dọc, chữ, chi tiết nhỏ hoặc cắt lại định dạng.

**Nguyên lý thực hành:** Tỷ lệ khung và kích thước hiển thị ảnh hưởng lượng thông tin đọc được. Thiết kế vùng quan trọng trước khi xuất nhiều định dạng.

**Cách làm:**

1. Chọn định dạng chính theo nơi xuất bản.
2. Thử cảnh ở kích thước điện thoại và màn hình lớn nếu có.
3. Nếu cần bản dọc/ngang, lập phương án bố cục riêng cho vùng bị mất.

**Đánh đổi:** Khung an toàn chung cho mọi tỷ lệ có thể làm bố cục chính yếu đi.

**Kiểm tra:**

- Tay/vật/chi tiết thiết yếu không bị cắt khi xuất đúng bản.
- Tỷ lệ thực của tệp khớp thiết lập, không chỉ câu lệnh.

**Ví dụ tự biên soạn:** Cảnh hai người ở hai mép khung ngang có thể cần dựng lại khi chuyển dọc.

**Phản ví dụ / giới hạn:** Không phải mọi cảnh ngang nên crop thẳng thành dọc.

**Liên quan:** [AI-007](../kien-thuc/AI-007.json), [QC-001](../kien-thuc/QC-001.json), [YT-001](../kien-thuc/YT-001.json)

**Nguồn đối chiếu:** [B022](../../bai-hoc/022-veo-tu-co-ban-den-quy-trinh/README.md), [B026](../../bai-hoc/026-nam-tru-cot-prompt/README.md)

[Bản JSON chuẩn](../kien-thuc/CA-009.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ca-010"></a>
## CA-010 — Cú máy dài và thiết kế thay đổi trong khung

**Câu hỏi quyết định:** Vì sao cần giữ liên tục thay vì cắt?

**Dùng khi:** Khi muốn hiện diện, theo dõi hành động hoặc tránh đứt quan hệ.

**Nguyên lý thực hành:** Một cú máy có thể chứa thay đổi bố cục, khoảng cách, hành vi và thông tin. Độ dài phải theo nhiệm vụ, không theo nhãn nghệ thuật.

**Cách làm:**

1. Vẽ các điểm chuyển trọng tâm trong một đường liên tục.
2. Chọn đường đi/điểm dừng và những gì phải giữ nhìn được.
3. Đặt phương án cắt dự phòng nếu diễn tiến không đọc được.

**Đánh đổi:** Giữ liên tục tăng yêu cầu dàn cảnh và nhất quán; cắt có thể truyền đạt tốt hơn.

**Kiểm tra:**

- Không có quãng chỉ kéo dài để đủ thời lượng.
- Thông tin phát triển trong khung và hành động quan trọng không mất.

**Ví dụ tự biên soạn:** Theo một người từ lấy khay đến đặt bàn nếu đường đi làm rõ quan hệ nơi chốn.

**Phản ví dụ / giới hạn:** Một shot tĩnh dài có thể chứa thay đổi mạnh; một shot ngắn cũng có thể rất yên.

**Liên quan:** [DR-006](../kien-thuc/DR-006.json), [MO-003](../kien-thuc/MO-003.json), [ED-001](../kien-thuc/ED-001.json)

**Nguồn đối chiếu:** [B024](../../bai-hoc/024-xau-chuoi-canh/README.md), [SRC-YALE-EDIT](https://filmanalysis.yale.edu/editing/)

[Bản JSON chuẩn](../kien-thuc/CA-010.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).
