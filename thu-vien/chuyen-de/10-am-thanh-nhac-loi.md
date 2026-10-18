# SO — Âm thanh, nhạc và lời kể

Phiên bản 1.2.1. Gắn tiếng với không gian, sự kiện và ưu tiên cảm nhận.

[Mục lục](../README.md) · [Chuẩn ra quyết định](../03_RA_QUYET_DINH.md)

Mỗi mục dưới là hướng dẫn có điều kiện. Tác dụng cảm xúc là giả thuyết thiết kế; chưa có thử tạo video hoặc kiểm nghiệm khán giả cho các ví dụ mới. Thuật ngữ xem [từ điển](../TU_DIEN.md).

| Mã | Quyết định | Mức |
| --- | --- | --- |
| [SO-001](#so-001) | Bản đồ nguồn âm và lớp âm | co_ban |
| [SO-002](#so-002) | Thoại, người nói và khoảng phản ứng | trung_cap |
| [SO-003](#so-003) | Âm ngoài khung và phối cảnh âm | trung_cap |
| [SO-004](#so-004) | Cầu nối âm và điểm vào/ra | trung_cap |
| [SO-005](#so-005) | Thứ tự nghe, độ lớn và khoảng động | nang_cao |
| [SO-006](#so-006) | Nhạc: chức năng, tương phản và im lặng | trung_cap |
| [SO-007](#so-007) | Lời kể và khoảng thở | trung_cap |
| [SO-008](#so-008) | Dựng tiếng và kiểm âm–hình | nang_cao |
| [SO-009](#so-009) | Đỉnh âm, độ động và sự thoải mái khi nghe | trung_cap |
| [SO-010](#so-010) | Phân chia ưu tiên để âm chính không bị che | trung_cap |
| [SO-011](#so-011) | Nhịp âm nhạc, mô-típ và sự liên tục của không gian nghe | nang_cao |

<a id="so-001"></a>
## SO-001 — Bản đồ nguồn âm và lớp âm

**Phiên bản mục:** 1.0.0

**Câu hỏi quyết định:** Điều gì cần nghe, phát từ đâu và làm nhiệm vụ gì?

**Dùng khi:** Khi viết kịch bản âm hoặc rà video AI.

**Nguyên lý thực hành:** Tách thoại, tiếng sự kiện, nền môi trường và nhạc theo nguồn/chức năng. Nhãn văn bản không bảo đảm được xuất thành các track riêng.

**Cách làm:**

1. Ghi nguồn, khoảng cách, vị trí và thời điểm mỗi âm chính.
2. Chọn lớp nổi bật theo mục tiêu cảnh.
3. Chừa nền đủ để không gian không đứt khi đổi góc.

**Đánh đổi:** Nhiều lớp làm thế giới sống hơn nhưng có thể che thao tác hoặc khiến người xem mệt.

**Kiểm tra:**

- Mỗi âm chính có lý do xuất hiện.
- Không nhầm không nhạc với không âm thanh.

**Ví dụ tự biên soạn:** Tiếng bát chạm ở gần, chim xa làm nền, nhạc tùy ý đồ; không cần mọi lớp cùng lớn.

**Phản ví dụ / giới hạn:** Không phải cảnh thật nào cũng cần nghe mọi thứ đúng như thu tại hiện trường.

**Liên quan:** [SO-005](../kien-thuc/SO-005.json), [SO-008](../kien-thuc/SO-008.json), [AI-006](../kien-thuc/AI-006.json)

**Nguồn đối chiếu:** [B016](../../bai-hoc/016-thiet-ke-am-thanh/README.md), [B032](../../bai-hoc/032-dieu-khien-am-thanh/README.md)

[Bản JSON chuẩn](../kien-thuc/SO-001.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="so-002"></a>
## SO-002 — Thoại, người nói và khoảng phản ứng

**Phiên bản mục:** 1.0.0

**Câu hỏi quyết định:** Ai nói câu nào và người xem cần theo ai?

**Dùng khi:** Khi có đối thoại, lời ngoài khung hoặc nhân vật AI.

**Nguyên lý thực hành:** Kiểm riêng nội dung lời, vai nói, giọng và độ khớp môi. Phân câu theo nhịp ý và thời gian đọc thực tế.

**Cách làm:**

1. Gắn mỗi câu với nhân vật/nhận dạng rõ.
2. Đọc thử hoặc đo bản tiếng thật để đặt thời lượng.
3. Giữ phản ứng người nghe khi có giá trị, chọn tách shot khi cần giảm mơ hồ.

**Đánh đổi:** Câu quá ngắn có thể mất tự nhiên; nhiều lời/động tác cùng lúc tăng khó tạo và khó nghe.

**Kiểm tra:**

- Không báo đạt chỉ vì môi có cử động.
- Lời hiểu được và không bị nhạc/âm khác che.

**Ví dụ tự biên soạn:** Một câu ngắn nói khi trao vật, rồi dành nhịp nhìn người nhận.

**Phản ví dụ / giới hạn:** Người nói ngoài khung là lựa chọn hợp lệ; không cần ép miệng luôn hiện hình.

**Liên quan:** [DR-004](../kien-thuc/DR-004.json), [ST-007](../kien-thuc/ST-007.json), [AI-006](../kien-thuc/AI-006.json)

**Nguồn đối chiếu:** [B013](../../bai-hoc/013-tach-shot-hoi-thoai/README.md), [B027](../../bai-hoc/027-tach-shot-lip-sync/README.md), [B029](../../bai-hoc/029-lip-sync-hoat-hinh/README.md), [B030](../../bai-hoc/030-gan-thoai-dung-nhan-vat/README.md)

[Bản JSON chuẩn](../kien-thuc/SO-002.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="so-003"></a>
## SO-003 — Âm ngoài khung và phối cảnh âm

**Phiên bản mục:** 1.0.0

**Câu hỏi quyết định:** Âm cho biết điều gì ngoài phần nhìn thấy?

**Dùng khi:** Khi mở không gian hoặc tạo mong chờ.

**Nguyên lý thực hành:** Khoảng cách, hướng và độ vang gợi nơi phát âm. Âm ngoài khung có thể dẫn chú ý mà không thêm nhân vật vào hình.

**Cách làm:**

1. Chọn nguồn thật/giả định và vị trí tương đối.
2. Giữ mức gần–xa và đặc tính không gian hợp lý qua góc.
3. Ghi khi nào nguồn được lộ hoặc cố ý giữ ngoài khung.

**Đánh đổi:** Âm quá rõ của nguồn xa có thể bị cảm như phóng đại; có thể dùng khi cách điệu chủ ý.

**Kiểm tra:**

- Không gán nhầm tiếng ngoài khung cho vật đang thấy.
- Nguồn không tự đổi bên hoặc đổi phòng ngoài ý đồ.

**Ví dụ tự biên soạn:** Tiếng bước tới trước khi khách xuất hiện làm rõ có người ở gần.

**Phản ví dụ / giới hạn:** Nhạc không thuộc thế giới phim không cần có nguồn vật lý trong cảnh.

**Liên quan:** [CA-005](../kien-thuc/CA-005.json), [ST-006](../kien-thuc/ST-006.json), [SO-004](../kien-thuc/SO-004.json)

**Nguồn đối chiếu:** [B032](../../bai-hoc/032-dieu-khien-am-thanh/README.md), [SRC-YALE-SOUND](https://filmanalysis.yale.edu/sound/)

[Bản JSON chuẩn](../kien-thuc/SO-003.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="so-004"></a>
## SO-004 — Cầu nối âm và điểm vào/ra

**Phiên bản mục:** 1.0.0

**Câu hỏi quyết định:** Âm có thể làm điểm nối hình tự nhiên hoặc có ý nghĩa hơn không?

**Dùng khi:** Khi chuyển cảnh, địa điểm hoặc góc.

**Nguyên lý thực hành:** Âm có thể đến trước hình cảnh sau hoặc kéo qua hình mới. Ghi quan hệ thời gian và nguồn; không tự gọi mọi đoạn có nhạc là cầu nối có chủ ý.

**Cách làm:**

1. Thử để âm kế tiếp dẫn vào hoặc âm cũ lưu lại.
2. Giữ những âm cần liên tục qua góc.
3. Kiểm xem nối âm có khiến hiểu sai nơi/thời điểm không.

**Đánh đổi:** Nối quá dài có thể làm nhầm hai không gian; cắt âm dứt có thể là chủ ý gây ngắt.

**Kiểm tra:**

- Không có bật nền hoặc đuôi âm đứt vô cớ.
- Lựa chọn vào/ra phục vụ mạch thay vì chỉ che cut.

**Ví dụ tự biên soạn:** Tiếng nước của bếp xuất hiện trước khi hình chuyển từ sân vào bếp.

**Phản ví dụ / giới hạn:** Một cú cắt im đột ngột có thể phù hợp bước ngoặt; không bắt mọi nối phải êm.

**Liên quan:** [ED-007](../kien-thuc/ED-007.json), [SO-003](../kien-thuc/SO-003.json), [ED-003](../kien-thuc/ED-003.json)

**Nguồn đối chiếu:** [B024](../../bai-hoc/024-xau-chuoi-canh/README.md), [SRC-YALE-SOUND](https://filmanalysis.yale.edu/sound/)

[Bản JSON chuẩn](../kien-thuc/SO-004.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="so-005"></a>
## SO-005 — Thứ tự nghe, độ lớn và khoảng động

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Người xem nghe được điều gì trước ở mức âm thoải mái?

**Dùng khi:** Khi các lớp tranh nhau hoặc cảnh quá chói/gắt.

**Nguyên lý thực hành:** Chọn ưu tiên cảm nhận rồi cân mức, phổ tần và thời điểm. Không đặt một mức dB/LUFS chung cho mọi loại nội dung và thiết bị khi chưa có yêu cầu xuất. Mức trung bình, đỉnh và độ động phản ánh các thuộc tính khác nhau. Một mục tiêu giao tệp cụ thể cần được ghi riêng khỏi nguyên lý chọn quan hệ âm.

**Cách làm:**

1. Cân lời/âm chính trước nền và nhạc.
2. Rà điểm đỉnh, tiếng sắc và thay đổi mức giữa cảnh.
3. Nghe nhỏ, nghe tai nghe và thiết bị mục tiêu nếu có; kiểm đỉnh kỹ thuật.
4. Kiểm gain/automation theo sự kiện trước khi nén tổng; so bypass ở mức tương đương và nghe toàn mix sau xuất.

**Đánh đổi:** Nén nhiều có thể giảm khác biệt mạnh–nhẹ; giữ động quá rộng có thể khó nghe trên thiết bị nhỏ.

**Kiểm tra:**

- Âm chính rõ mà không phải tăng giảm liên tục.
- Không méo/clipping hoặc âm đột ngột ngoài ý đồ.
- Không lấy một số LUFS hoặc một limiter cuối chuỗi làm chứng nhận âm phù hợp.

**Ví dụ tự biên soạn:** Giảm nhạc quanh tiếng chạm quan trọng, rồi trả nền khi thao tác kết.

**Phản ví dụ / giới hạn:** Một cảnh cần choáng ngợp có thể có khoảng động lớn nhưng phải nằm trong bản yêu cầu.

**Liên quan:** [SO-001](../kien-thuc/SO-001.json), [SO-008](../kien-thuc/SO-008.json), [QC-001](../kien-thuc/QC-001.json), [SO-009](../kien-thuc/SO-009.json), [SO-010](../kien-thuc/SO-010.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Đủ lớn, rõ lời và thoải mái là ba câu hỏi có thể cần cách sửa khác nhau.

**Tình huống:** Lời đủ mức nhưng nhạc và một tiếng chạm đang lấn.

**Phần phải giữ:** Mục tiêu và các phần đã duyệt trong tình huống.

| Phương án | Thực hiện |
| --- | --- |
| A | Nâng toàn mix. |
| B | Hạ cạnh tranh theo mốc và xử lý riêng tiếng chạm. |

**Cách chọn:** Chọn B khi lỗi là quan hệ các lớp; tăng tổng không giải phần che nhau.

**Dấu hiệu kiểm trong ca:**

- Không lấy một số LUFS hoặc một limiter cuối chuỗi làm chứng nhận âm phù hợp.

**Nếu gặp:** Lớn hơn nhưng vẫn không rõ.

Có thể do: Mức chung bị dùng thay cho ưu tiên trong mix.

Thử tiếp: Tạm tắt lớp cạnh tranh để tìm nguồn che, rồi so bản sửa trong toàn mix.
**Nguồn đối chiếu:** [B016](../../bai-hoc/016-thiet-ke-am-thanh/README.md), [SRC-BMD-TRAINING](https://www.blackmagicdesign.com/products/davinciresolve/training), [SRC-ADOBE-SOUND](https://helpx.adobe.com/audition/desktop/kb/editing-using-essential-sound-panel-audition.html)

[Bản JSON chuẩn](../kien-thuc/SO-005.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="so-006"></a>
## SO-006 — Nhạc: chức năng, tương phản và im lặng

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Nhạc đang thêm điều gì mà hình/âm khác chưa làm?

**Dùng khi:** Khi chọn nhạc có sẵn hoặc tạo nhạc bằng AI.

**Nguyên lý thực hành:** Chọn vai trò trước thể loại: nâng đỡ, tạo mong chờ, nối thời gian, tương phản hoặc để trống. Tempo nhạc không tự xác định tốc độ hành động hay cảm xúc. Chọn vị trí vào/ra và biến đổi nhạc theo cấu trúc, có thể giữ âm đời sống dẫn. Chỉ chỉnh độc lập các nhạc cụ khi thực có stem hoặc công cụ tách được kiểm.

**Cách làm:**

1. Ghi đoạn nào cần nhạc và đoạn nào cần nghe đời sống.
2. Chọn mật độ, nhạc cụ, năng lượng và điểm chuyển phù hợp.
3. Thử bản không nhạc để biết nhạc đang hỗ trợ hay che vấn đề.
4. Lập tuyến âm trước/sau biến chuyển; so bản ít nhạc hoặc không nhạc khi cần chẩn đoán nhạc có đang che hành động và đồng đều hóa cảm xúc không.

**Đánh đổi:** Nhạc có thể kéo cảm xúc quá mức hoặc làm mọi đoạn giống nhau.

**Kiểm tra:**

- Không cắt theo mọi nhịp chỉ vì có beat.
- Khoảng lặng được định nghĩa: không nhạc, nền thưa hay im hoàn toàn.
- Nhạc kết theo câu hoặc chủ ý rõ; không bị cắt cụt chỉ vì hình hết.

**Ví dụ tự biên soạn:** Để tiếng gió và dụng cụ dẫn một đoạn, thêm nhạc nhẹ khi chuỗi thời gian mở rộng.

**Phản ví dụ / giới hạn:** Nhạc dịu vẫn có thể làm người xem khó chịu nếu lặp, quá lớn hoặc trái cảnh.

**Liên quan:** [ED-005](../kien-thuc/ED-005.json), [AU-004](../kien-thuc/AU-004.json), [SO-001](../kien-thuc/SO-001.json), [SO-011](../kien-thuc/SO-011.json), [ST-012](../kien-thuc/ST-012.json), [AU-009](../kien-thuc/AU-009.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Nhạc nên có chức năng và phân câu; lời nhắc “thư giãn” không đủ để đặt mọi đoạn cùng một tông.

**Tình huống:** Một bài tạo AI hay nhưng kết đoạn giữa câu và che tiếng dụng cụ.

**Phần phải giữ:** Mục tiêu và các phần đã duyệt trong tình huống.

| Phương án | Thực hiện |
| --- | --- |
| A | Lặp toàn bài ở cùng mức. |
| B | Chọn đoạn/cắt/fade theo chức năng và nhường mốc thao tác quan trọng. |

**Cách chọn:** Chọn B; nếu cần chỉnh nhạc cụ riêng phải xác minh đầu vào thực có.

**Dấu hiệu kiểm trong ca:**

- Nhạc kết theo câu hoặc chủ ý rõ; không bị cắt cụt chỉ vì hình hết.

**Nếu gặp:** Cảnh nào cũng tạo cùng một cảm giác và kết nghe cụt.

Có thể do: Nhạc được dùng như nền phủ, không theo chức năng.

Thử tiếp: Nghe tuyến nhạc riêng và bản bỏ nhạc, đánh dấu chỗ giá trị thay đổi.
**Nguồn đối chiếu:** [B016](../../bai-hoc/016-thiet-ke-am-thanh/README.md), [B032](../../bai-hoc/032-dieu-khien-am-thanh/README.md), [SRC-ADOBE-SOUND](https://helpx.adobe.com/audition/desktop/kb/editing-using-essential-sound-panel-audition.html)

[Bản JSON chuẩn](../kien-thuc/SO-006.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="so-007"></a>
## SO-007 — Lời kể và khoảng thở

**Phiên bản mục:** 1.0.0

**Câu hỏi quyết định:** Khi nào người xem cần lời và khi nào cần tự cảm nhận?

**Dùng khi:** Khi viết voiceover hoặc kiểm nhịp lời–hình.

**Nguyên lý thực hành:** Lời kể có thể bổ sung điều không nhìn thấy; khoảng thở cho hình/âm thời gian mang ý. Đo tốc độ bằng bản đọc thật và ngôn ngữ thực dùng.

**Cách làm:**

1. Gán chức năng cho mỗi câu: bối cảnh, quy luật, ý nghĩ, câu hỏi hoặc kết nối.
2. Chọn vị trí dừng để hình trả thông tin.
3. Rà phát âm, số, tên riêng và độ dài so với cảnh.

**Đánh đổi:** Ít lời quá có thể mất bối cảnh; lời dày làm mất không gian cảm nhận.

**Kiểm tra:**

- Câu không tả lặp mọi chuyển động trừ khi đó là mục tiêu hướng dẫn.
- Không áp một tốc độ từ/phút hoặc khoảng nghỉ cho tất cả ngách.

**Ví dụ tự biên soạn:** Cao trào có thể để hành động tự nói; lời sau đó đặt hệ quả vào bối cảnh.

**Phản ví dụ / giới hạn:** Phim phổ biến kiến thức có thể cần lời dày hơn phim trải nghiệm không thoại.

**Liên quan:** [ST-007](../kien-thuc/ST-007.json), [AU-005](../kien-thuc/AU-005.json), [ED-001](../kien-thuc/ED-001.json)

**Nguồn đối chiếu:** [B016](../../bai-hoc/016-thiet-ke-am-thanh/README.md), [B032](../../bai-hoc/032-dieu-khien-am-thanh/README.md)

[Bản JSON chuẩn](../kien-thuc/SO-007.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="so-008"></a>
## SO-008 — Dựng tiếng và kiểm âm–hình

**Phiên bản mục:** 1.0.0

**Câu hỏi quyết định:** Âm được sinh/thu có đúng sự kiện và dùng được không?

**Dùng khi:** Khi nhận clip AI hoặc ghép nhiều nguồn âm.

**Nguyên lý thực hành:** Kiểm nội dung, nguồn, thời điểm và chất lượng riêng. Có thể thay/đắp lại tiếng sai thay vì tạo lại hình đã đạt.

**Cách làm:**

1. Lập spotting list: sự kiện, mốc vào/ra, nguồn âm và vai trò.
2. So tiếp xúc, tiếng bắt đầu và đuôi vang trên toàn clip.
3. Kiểm file xuất có đúng kênh, mức và không mất lớp.

**Đánh đổi:** Thêm tiếng quá sạch hoặc quá gần có thể mất cảm giác không gian.

**Kiểm tra:**

- Không có tiếng bước khi chân không bước ngoài chủ ý.
- Không suy đầu ra nhiều track chỉ từ nhãn prompt.

**Ví dụ tự biên soạn:** Giữ clip đặt bát đẹp, thay tiếng chạm bị lệch bằng âm đúng thời điểm khi công cụ dựng cho phép.

**Phản ví dụ / giới hạn:** Một tiếng cách điệu có thể cố tình không trùng vật lý; phải ghi đó là ý đồ.

**Liên quan:** [AI-006](../kien-thuc/AI-006.json), [QC-001](../kien-thuc/QC-001.json), [SO-005](../kien-thuc/SO-005.json)

**Nguồn đối chiếu:** [B016](../../bai-hoc/016-thiet-ke-am-thanh/README.md), [B032](../../bai-hoc/032-dieu-khien-am-thanh/README.md)

[Bản JSON chuẩn](../kien-thuc/SO-008.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="so-009"></a>
## SO-009 — Đỉnh âm, độ động và sự thoải mái khi nghe

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Lỗi nằm ở mức trung bình, một đỉnh chói hay sự chênh mạnh–nhẹ?

**Dùng khi:** Cảnh yên có tiếng chạm giật mình, lời khó nghe hoặc bản mix bị nén phẳng.

**Nguyên lý thực hành:** Tách độ lớn cảm nhận theo thời gian, đỉnh tín hiệu và độ động. Một giá trị loudness toàn phim không mô tả hết cú chạm ngắn hoặc đoạn lời nhỏ; sửa theo chức năng và kiểm trên thiết bị sử dụng thực tế.

**Cách làm:**

1. Nghe ở mức tham chiếu nhất quán, đánh dấu đỉnh gây khó chịu, lời mất rõ và nền bật đột ngột. Kiểm gain từng clip trước khi thêm xử lý toàn mix.
2. Chọn automation để sửa sự kiện cụ thể, EQ hoặc xử lý động khi phù hợp; cân attack/release theo âm thật, giữ nét cần thiết và nghe bypass có mức tương đương.
3. Kiểm tệp sau xuất về méo, đỉnh và trải nghiệm ở loa/tai nghe sẵn có; ghi tiêu chuẩn giao tệp nếu dự án yêu cầu, không dùng một số LUFS làm quy luật cho mọi ngách.

**Đánh đổi:** Giảm đỉnh quá mạnh làm vật nhẹ và thiếu sức; nén mạnh tăng độ đều nhưng có thể mất tương phản, tiếng thở/nền trồi lên.

**Kiểm tra:**

- Không phải liên tục chỉnh âm lượng để nghe việc chính.
- Tiếng đột ngột có lý do và mức phù hợp lời hứa.

**Ví dụ tự biên soạn:** Tiếng đặt cốc quá chói trong cảnh nhẹ: giảm riêng sự kiện và đuôi cần thiết, giữ nền và hình đã đạt; so lại cảm giác vật liệu.

**Phản ví dụ / giới hạn:** Một đỉnh lớn có thể là ý đồ phim căng thẳng; không tự làm phẳng mọi bản mix.

**Liên quan:** [SO-001](../kien-thuc/SO-001.json), [SO-005](../kien-thuc/SO-005.json), [SO-008](../kien-thuc/SO-008.json), [AU-001](../kien-thuc/AU-001.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Các loại sai khác âm cần công cụ khác nhau. Cách sửa theo từng sự kiện bảo vệ tương phản của toàn phim tốt hơn việc tự hạ tất cả chỉ vì một tiếng chói.

**Tình huống:** Tiếng đặt cốc quá chói trong cảnh nhẹ: giảm riêng sự kiện và đuôi cần thiết, giữ nền và hình đã đạt; so lại cảm giác vật liệu.

**Phần phải giữ:** Chất liệu tiếng cốc. Nền và hình đã duyệt.

| Phương án | Thực hiện |
| --- | --- |
| A | Hạ toàn bộ âm phim vì một tiếng cốc quá lớn. |
| B | Sửa mức và phổ của riêng tiếng cốc, nghe cùng nền và hành động. |

**Cách chọn:** Chọn B nếu chỉ một sự kiện gây lỗi; xử lý tổng chỉ sau khi kiểm quan hệ các lớp.

**Dấu hiệu kiểm trong ca:**

- Không phải liên tục chỉnh âm lượng để nghe việc chính.
- Tiếng đột ngột có lý do và mức phù hợp lời hứa.

**Nếu gặp:** Lời đã đủ mức nhưng tiếng chạm vẫn gây giật mình.

Có thể do: Đỉnh/transient quá nổi. Tiếng được đặt quá gần so với không gian hình.

Thử tiếp: So giảm riêng gain với sửa đặc tính âm/không gian; nghe ở mức phát thường trước khi chốt.
**Nguồn đối chiếu:** [SRC-ADOBE-SOUND](https://helpx.adobe.com/audition/desktop/kb/editing-using-essential-sound-panel-audition.html)

[Bản JSON chuẩn](../kien-thuc/SO-009.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="so-010"></a>
## SO-010 — Phân chia ưu tiên để âm chính không bị che

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Âm nào cần rõ ở thời điểm này, và lớp nào đang cạnh tranh với nó?

**Dùng khi:** Lời lẫn nhạc, thao tác khó nghe, nhiều nền/SFX cùng lớn.

**Nguyên lý thực hành:** Độ rõ phụ thuộc quan hệ giữa các lớp, không chỉ mức của âm chính. Chọn ưu tiên theo mốc sự kiện; có thể giảm, dời, thưa hoặc thay âm cạnh tranh trước khi tăng mạnh âm cần nghe.

**Cách làm:**

1. Đánh dấu mốc phải hiểu lời hoặc nghe tiếp xúc; solo để tìm vấn đề nhưng luôn quyết định trong toàn mix.
2. Thử giảm/automation lớp cạnh tranh, thay phối khí, EQ có mục đích hoặc để khoảng trống; với ducking kiểm vào/ra để tránh âm nền bơm theo từng khe thở.
3. So ở mức nghe tương đương và thiết bị nhỏ nếu đó là cách khán giả dùng. Không cho mọi nguồn cùng ở gần hoặc cùng phủ đầy phổ chỉ để âm “dày”.

**Đánh đổi:** Dọn quá nhiều làm không gian rỗng; tăng rõ bằng xử lý mạnh có thể làm tiếng nhân tạo hoặc mệt.

**Kiểm tra:**

- Nghe được nội dung quan trọng ở toàn mix.
- Khi âm chính kết, lớp nền trở lại hợp nhịp và không bật mức vô cớ.

**Ví dụ tự biên soạn:** Cần nghe tiếng khóa cài: giảm nhạc/âm kim loại cạnh tranh quanh thời điểm đó, giữ room tone thay vì kéo tiếng khóa cực lớn.

**Phản ví dụ / giới hạn:** Có thể cố ý để lời bị át trong một cảnh; phải xác định người xem cần hiểu lời hay cảm nhận hoàn cảnh bị lấn.

**Liên quan:** [SO-001](../kien-thuc/SO-001.json), [SO-002](../kien-thuc/SO-002.json), [SO-005](../kien-thuc/SO-005.json), [SO-009](../kien-thuc/SO-009.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Một lớp có thể đủ rõ khi solo nhưng khó nghe trong phối trộn. Phân quyền theo thời điểm nối xử lý âm với mục tiêu thông tin của cảnh.

**Tình huống:** Cần nghe tiếng khóa cài: giảm nhạc/âm kim loại cạnh tranh quanh thời điểm đó, giữ room tone thay vì kéo tiếng khóa cực lớn.

**Phần phải giữ:** Thời điểm khóa cài. Không gian nghe của cảnh.

| Phương án | Thực hiện |
| --- | --- |
| A | Tăng mọi lớp rồi đặt limiter cuối chuỗi. |
| B | Chọn lớp dẫn từng mốc, giảm cạnh tranh và giữ quan hệ không gian. |

**Cách chọn:** Chọn B khi vấn đề là che lẫn; A có thể làm mix đặc hơn mà không thêm độ rõ.

**Dấu hiệu kiểm trong ca:**

- Nghe được nội dung quan trọng ở toàn mix.
- Khi âm chính kết, lớp nền trở lại hợp nhịp và không bật mức vô cớ.

**Nếu gặp:** Nghe có vẻ lớn nhưng không hiểu lời hoặc không nhận ra thao tác.

Có thể do: Lớp cạnh tranh cùng thời điểm. Màu âm hoặc phối khí phủ phần cần nghe.

Thử tiếp: Tạm tắt từng lớp cạnh tranh; xác định lớp nào bỏ ra thì nội dung chính rõ, rồi sửa ít nhất có thể.
**Nguồn đối chiếu:** [SRC-ADOBE-SOUND](https://helpx.adobe.com/audition/desktop/kb/editing-using-essential-sound-panel-audition.html), [SRC-YALE-SOUND](https://filmanalysis.yale.edu/sound/)

[Bản JSON chuẩn](../kien-thuc/SO-010.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="so-011"></a>
## SO-011 — Nhịp âm nhạc, mô-típ và sự liên tục của không gian nghe

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Âm đang dẫn câu chuyện, giữ nơi chốn hay chỉ phủ đều toàn bộ hình?

**Dùng khi:** Dùng nhạc mua/tạo AI, cắt nhạc đột ngột, đoạn nào cũng cùng mức hoặc không gian nghe thay vô cớ.

**Nguyên lý thực hành:** Tổ chức nhạc theo câu và chức năng, đồng thời giữ nền không gian đủ liền khi cần. Có thể nối bằng đuôi âm, room tone hoặc âm nguồn; các lớp không phải lúc nào cũng lên xuống cùng nhau.

**Cách làm:**

1. Đánh dấu vào/ra câu nhạc, thay hòa âm/âm sắc và khoảng thưa; chọn điểm hỗ trợ biến chuyển câu chuyện thay vì cắt hình theo mọi beat.
2. Ghi nguồn âm môi trường và hướng/khoảng cách tương đối qua chuỗi; giữ nền hoặc chuyển nền có lý do khi đổi không gian.
3. Nếu dùng stem, xác minh thực có các lớp tách và nghe lỗi tách. Nếu chỉ có bản trộn, chọn đoạn/cắt/fade phù hợp trong giới hạn đó; không hứa chỉnh độc lập mọi nhạc cụ.

**Đánh đổi:** Nhạc ăn khớp quá mọi động tác có thể lộ thủ pháp; nền quá liền qua đổi nơi có thể làm người xem hiểu nhầm không gian.

**Kiểm tra:**

- Điểm đổi nhạc có quan hệ với chức năng cảnh hoặc chủ ý đối lập.
- Không có đuôi nhạc/room tone đứt ngoài ý đồ; không giả định có stem.

**Ví dụ tự biên soạn:** Chuỗi sửa đồ dùng tiếng dụng cụ dẫn; khi đồ bắt đầu được dùng, một mô-típ nhạc trở lại nhẹ. Tiếng phòng tiếp tục qua hai góc cùng không gian.

**Phản ví dụ / giới hạn:** Không phải mọi phim cần nhạc hoặc mô-típ; im nhạc có thể là lựa chọn hoàn chỉnh nếu âm đời sống đã phục vụ trải nghiệm.

**Liên quan:** [SO-003](../kien-thuc/SO-003.json), [SO-004](../kien-thuc/SO-004.json), [SO-006](../kien-thuc/SO-006.json), [ST-012](../kien-thuc/ST-012.json), [ED-011](../kien-thuc/ED-011.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Nhạc có cấu trúc riêng; không gian nghe có tính liên tục riêng. Quyết định theo hai lớp tránh dùng nhạc để che mọi lỗi dựng hoặc làm thế giới âm biến mất khi nhạc dừng.

**Tình huống:** Chuỗi sửa đồ dùng tiếng dụng cụ dẫn; khi đồ bắt đầu được dùng, một mô-típ nhạc trở lại nhẹ. Tiếng phòng tiếp tục qua hai góc cùng không gian.

**Phần phải giữ:** Âm thao tác dẫn chuỗi sửa. Tiếng phòng liên tục qua cùng không gian.

| Phương án | Thực hiện |
| --- | --- |
| A | Kéo một bài lặp từ đầu tới cuối và cắt ngang ở frame cuối. |
| B | Chọn đoạn và điểm kết câu phù hợp, bố trí lúc nhạc lùi để âm sự kiện được dẫn. |

**Cách chọn:** Chọn theo trải nghiệm cần có; B hữu ích khi nhạc đang đồng đều hóa những đoạn có chức năng khác nhau.

**Dấu hiệu kiểm trong ca:**

- Điểm đổi nhạc có quan hệ với chức năng cảnh hoặc chủ ý đối lập.
- Không có đuôi nhạc/room tone đứt ngoài ý đồ; không giả định có stem.

**Nếu gặp:** Mọi phân đoạn giống nhau hoặc kết phim bị cụt dù hình đã hoàn tất.

Có thể do: Nhạc không có phân câu theo chức năng. Âm nền/đuôi âm bị cắt theo hình.

Thử tiếp: Nghe riêng tuyến âm toàn đoạn, đánh dấu chỗ cần chuyển nhạc và chỗ chỉ cần giữ không gian.
**Nguồn đối chiếu:** [SRC-YALE-SOUND](https://filmanalysis.yale.edu/sound/), [SRC-ADOBE-SOUND](https://helpx.adobe.com/audition/desktop/kb/editing-using-essential-sound-panel-audition.html)

[Bản JSON chuẩn](../kien-thuc/SO-011.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).
