# SO — Âm thanh, nhạc và lời kể

Phiên bản 1.0.0. Gắn tiếng với không gian, sự kiện và ưu tiên cảm nhận.

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

<a id="so-001"></a>
## SO-001 — Bản đồ nguồn âm và lớp âm

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

**Câu hỏi quyết định:** Người xem nghe được điều gì trước ở mức âm thoải mái?

**Dùng khi:** Khi các lớp tranh nhau hoặc cảnh quá chói/gắt.

**Nguyên lý thực hành:** Chọn ưu tiên cảm nhận rồi cân mức, phổ tần và thời điểm. Không đặt một mức dB/LUFS chung cho mọi loại nội dung và thiết bị khi chưa có yêu cầu xuất.

**Cách làm:**

1. Cân lời/âm chính trước nền và nhạc.
2. Rà điểm đỉnh, tiếng sắc và thay đổi mức giữa cảnh.
3. Nghe nhỏ, nghe tai nghe và thiết bị mục tiêu nếu có; kiểm đỉnh kỹ thuật.

**Đánh đổi:** Nén nhiều có thể giảm khác biệt mạnh–nhẹ; giữ động quá rộng có thể khó nghe trên thiết bị nhỏ.

**Kiểm tra:**

- Âm chính rõ mà không phải tăng giảm liên tục.
- Không méo/clipping hoặc âm đột ngột ngoài ý đồ.

**Ví dụ tự biên soạn:** Giảm nhạc quanh tiếng chạm quan trọng, rồi trả nền khi thao tác kết.

**Phản ví dụ / giới hạn:** Một cảnh cần choáng ngợp có thể có khoảng động lớn nhưng phải nằm trong bản yêu cầu.

**Liên quan:** [SO-001](../kien-thuc/SO-001.json), [SO-008](../kien-thuc/SO-008.json), [QC-001](../kien-thuc/QC-001.json)

**Nguồn đối chiếu:** [B016](../../bai-hoc/016-thiet-ke-am-thanh/README.md), [SRC-BMD-TRAINING](https://www.blackmagicdesign.com/products/davinciresolve/training)

[Bản JSON chuẩn](../kien-thuc/SO-005.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="so-006"></a>
## SO-006 — Nhạc: chức năng, tương phản và im lặng

**Câu hỏi quyết định:** Nhạc đang thêm điều gì mà hình/âm khác chưa làm?

**Dùng khi:** Khi chọn nhạc có sẵn hoặc tạo nhạc bằng AI.

**Nguyên lý thực hành:** Chọn vai trò trước thể loại: nâng đỡ, tạo mong chờ, nối thời gian, tương phản hoặc để trống. Tempo nhạc không tự xác định tốc độ hành động hay cảm xúc.

**Cách làm:**

1. Ghi đoạn nào cần nhạc và đoạn nào cần nghe đời sống.
2. Chọn mật độ, nhạc cụ, năng lượng và điểm chuyển phù hợp.
3. Thử bản không nhạc để biết nhạc đang hỗ trợ hay che vấn đề.

**Đánh đổi:** Nhạc có thể kéo cảm xúc quá mức hoặc làm mọi đoạn giống nhau.

**Kiểm tra:**

- Không cắt theo mọi nhịp chỉ vì có beat.
- Khoảng lặng được định nghĩa: không nhạc, nền thưa hay im hoàn toàn.

**Ví dụ tự biên soạn:** Để tiếng gió và dụng cụ dẫn một đoạn, thêm nhạc nhẹ khi chuỗi thời gian mở rộng.

**Phản ví dụ / giới hạn:** Nhạc dịu vẫn có thể làm người xem khó chịu nếu lặp, quá lớn hoặc trái cảnh.

**Liên quan:** [ED-005](../kien-thuc/ED-005.json), [AU-004](../kien-thuc/AU-004.json), [SO-001](../kien-thuc/SO-001.json)

**Nguồn đối chiếu:** [B016](../../bai-hoc/016-thiet-ke-am-thanh/README.md), [B032](../../bai-hoc/032-dieu-khien-am-thanh/README.md)

[Bản JSON chuẩn](../kien-thuc/SO-006.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="so-007"></a>
## SO-007 — Lời kể và khoảng thở

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
