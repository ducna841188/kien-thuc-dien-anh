# ST — Kịch bản và cấu trúc

Phiên bản 1.0.0. Xây thay đổi từ đơn vị hành động đến toàn phim; chọn điều cần kể bằng hình/tiếng.

[Mục lục](../README.md) · [Chuẩn ra quyết định](../03_RA_QUYET_DINH.md)

Mỗi mục dưới là hướng dẫn có điều kiện. Tác dụng cảm xúc là giả thuyết thiết kế; chưa có thử tạo video hoặc kiểm nghiệm khán giả cho các ví dụ mới. Thuật ngữ xem [từ điển](../TU_DIEN.md).

| Mã | Quyết định | Mức |
| --- | --- | --- |
| [ST-001](#st-001) | Chủ đề, lời hứa và trục thay đổi | co_ban |
| [ST-002](#st-002) | Mục tiêu, trở ngại và lựa chọn | co_ban |
| [ST-003](#st-003) | Nhịp diễn biến và bước ngoặt trong cảnh | trung_cap |
| [ST-004](#st-004) | Chuẩn bị, phát triển và trả kết quả | trung_cap |
| [ST-005](#st-005) | Cấu trúc phân đoạn và chuỗi hành động | trung_cap |
| [ST-006](#st-006) | Điểm nhìn và phân phối thông tin | nang_cao |
| [ST-007](#st-007) | Kịch bản hình–tiếng và lời bổ sung | trung_cap |
| [ST-008](#st-008) | Mở, kết và đời sống tiếp diễn | nang_cao |

<a id="st-001"></a>
## ST-001 — Chủ đề, lời hứa và trục thay đổi

**Câu hỏi quyết định:** Phim này đưa người xem đi qua điều gì?

**Dùng khi:** Khi bắt đầu ý tưởng hoặc rà một bản kịch bản.

**Nguyên lý thực hành:** Chọn một trục tổ chức đủ rõ: hành trình một việc, một câu hỏi, một quan hệ hoặc một trạng thái. Chủ đề cần hiện qua diễn biến cụ thể.

**Cách làm:**

1. Viết một câu về giá trị và thay đổi chính.
2. Liệt kê phần bắt đầu, các bước cần trải qua và trạng thái kết.
3. Rà từng đoạn theo việc nó đóng góp vào trục ấy.

**Đánh đổi:** Trục quá chặt có thể làm mất khoảnh khắc quan sát có giá trị; chừa chỗ có lý do.

**Kiểm tra:**

- Có thể nói đầu–cuối khác nhau ở đâu.
- Các đoạn phụ có vai trò thay vì chỉ tăng độ dài.

**Ví dụ tự biên soạn:** Một vật liệu thô trở thành đồ dùng; hoặc một nơi tưởng an toàn bộc lộ giới hạn của nó.

**Phản ví dụ / giới hạn:** Phim trải nghiệm có thể không có nhân vật theo đuổi mục tiêu, nhưng vẫn cần cách tổ chức sự chú ý.

**Liên quan:** [AU-001](../kien-thuc/AU-001.json), [ST-005](../kien-thuc/ST-005.json), [YT-001](../kien-thuc/YT-001.json)

**Nguồn đối chiếu:** [B002](../../bai-hoc/002-prompt-cau-truc/README.md), [B017](../../bai-hoc/017-mini-story-ba-nhip/README.md)

[Bản JSON chuẩn](../kien-thuc/ST-001.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="st-002"></a>
## ST-002 — Mục tiêu, trở ngại và lựa chọn

**Câu hỏi quyết định:** Điều gì làm hành động đáng theo dõi?

**Dùng khi:** Khi cảnh có người/vật đang cố đạt một kết quả.

**Nguyên lý thực hành:** Mục tiêu tạo hướng; trở ngại tạo nhu cầu thích nghi; lựa chọn làm lộ năng lực hoặc tính cách. Mức trở ngại theo lời hứa trải nghiệm.

**Cách làm:**

1. Nêu mục tiêu có thể nhìn thấy.
2. Chọn trở ngại đúng hoàn cảnh, có thể rất nhỏ.
3. Cho hành động thay đổi trước trở ngại và để lại hệ quả.

**Đánh đổi:** Tăng trở ngại quá mức có thể phá cảm giác an toàn hoặc làm nhân vật kém tin cậy.

**Kiểm tra:**

- Không phải mọi hành động đều là lặp lại không đổi.
- Khán giả hiểu lựa chọn đã tác động kết quả thế nào.

**Ví dụ tự biên soạn:** Người điều chỉnh quai giỏ để mang nặng dễ hơn; ở phim khác đó có thể là lựa chọn đường thoát.

**Phản ví dụ / giới hạn:** Một cảnh ngắm cảnh có thể có giá trị dù không có xung đột; đừng bịa tai nạn để đủ công thức.

**Liên quan:** [DR-001](../kien-thuc/DR-001.json), [AU-003](../kien-thuc/AU-003.json), [ST-004](../kien-thuc/ST-004.json)

**Nguồn đối chiếu:** [B017](../../bai-hoc/017-mini-story-ba-nhip/README.md), [B021](../../bai-hoc/021-lam-chu-cam-xuc/README.md)

[Bản JSON chuẩn](../kien-thuc/ST-002.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="st-003"></a>
## ST-003 — Nhịp diễn biến và bước ngoặt trong cảnh

**Câu hỏi quyết định:** Tại đâu mục tiêu, hiểu biết hoặc quan hệ đổi?

**Dùng khi:** Khi chia một cảnh thành các phần chỉ đạo.

**Nguyên lý thực hành:** Beat là một nhịp diễn biến có thay đổi nhiệm vụ hoặc thông tin. Nó không tự đồng nghĩa một shot, một giây hay một câu thoại.

**Cách làm:**

1. Đánh dấu trạng thái trước mỗi nhịp.
2. Chỉ ra sự kiện khiến nhân vật/người xem đổi cách hiểu.
3. Ghi trạng thái sau và quyết định quay/dựng cần để đọc chuyển biến.

**Đánh đổi:** Tách mọi động tác nhỏ thành nhịp làm kế hoạch nặng mà không thêm giá trị.

**Kiểm tra:**

- Mỗi nhịp có thay đổi nêu được.
- Một nhịp có thể qua nhiều shot hoặc nhiều nhịp ở trong một cú máy.

**Ví dụ tự biên soạn:** Từ đang làm việc sang nhận ra có khách, rồi quyết định dừng tay; mỗi phần có nhiệm vụ khác.

**Phản ví dụ / giới hạn:** Nhấc tay rồi hạ tay không thành bước ngoặt nếu không đổi điều gì đáng kể.

**Liên quan:** [EV-003](../kien-thuc/EV-003.json), [DR-003](../kien-thuc/DR-003.json), [ED-001](../kien-thuc/ED-001.json)

**Nguồn đối chiếu:** [B017](../../bai-hoc/017-mini-story-ba-nhip/README.md), [B021](../../bai-hoc/021-lam-chu-cam-xuc/README.md)

[Bản JSON chuẩn](../kien-thuc/ST-003.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="st-004"></a>
## ST-004 — Chuẩn bị, phát triển và trả kết quả

**Câu hỏi quyết định:** Kết quả có được chuẩn bị đủ và nhìn thấy đủ không?

**Dùng khi:** Khi xây một việc, mối quan hệ hoặc bí mật kéo dài nhiều đoạn.

**Nguyên lý thực hành:** Gieo thông tin để kết quả có nghĩa; phát triển mong chờ; cho dấu hoàn tất phù hợp. Không bắt buộc ba phần dài bằng nhau.

**Cách làm:**

1. Đặt chi tiết cần nhớ ở chỗ dễ đọc.
2. Cho chi tiết trở lại trong hoàn cảnh đã thay đổi.
3. Dành hình/âm hoặc phản ứng để xác nhận kết quả.

**Đánh đổi:** Nhấn đi nhấn lại có thể lộ dụng ý hoặc giảm bất ngờ.

**Kiểm tra:**

- Người xem nhận ra liên hệ mà không phải giải thích lại toàn bộ.
- Kết quả đáp ứng điều phim đã hứa hoặc chủ động thay đổi kỳ vọng có căn cứ.

**Ví dụ tự biên soạn:** Chiếc cốc được làm ở đầu phim quay lại chứa thức uống khi gia đình ngồi cùng nhau.

**Phản ví dụ / giới hạn:** Kết mở có thể chủ ý; cần phân biệt sự bỏ ngỏ có ý nghĩa với công đoạn bị quên.

**Liên quan:** [AU-003](../kien-thuc/AU-003.json), [ST-008](../kien-thuc/ST-008.json), [ED-005](../kien-thuc/ED-005.json)

**Nguồn đối chiếu:** [B017](../../bai-hoc/017-mini-story-ba-nhip/README.md), [B024](../../bai-hoc/024-xau-chuoi-canh/README.md)

[Bản JSON chuẩn](../kien-thuc/ST-004.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="st-005"></a>
## ST-005 — Cấu trúc phân đoạn và chuỗi hành động

**Câu hỏi quyết định:** Các phần phim nối nhau bằng quan hệ nào?

**Dùng khi:** Khi biến nhiều shot đẹp thành một video có mạch.

**Nguyên lý thực hành:** Tổ chức theo nguyên nhân, tiến trình, không gian, thời gian, so sánh hoặc ý tưởng. Ghi quan hệ thật thay vì mặc định mọi shot là trước–sau của cùng một việc.

**Cách làm:**

1. Viết vai trò mỗi phân đoạn trong một dòng.
2. Ghi vật/người/trạng thái nào được mang qua ranh giới.
3. Lược bỏ hoặc chuyển vị trí đoạn không phục vụ quan hệ đã chọn.

**Đánh đổi:** Mạch quá tuyến tính có thể mất sự phong phú; dựng đan xen cần thêm dấu định hướng.

**Kiểm tra:**

- Có lý do cho thứ tự thay vì chỉ theo thứ tự tạo file.
- Không gộp các mẻ, mùa hay loài khác nhau thành một quá trình giả.

**Ví dụ tự biên soạn:** Chuỗi gieo–chăm–thu là tiến trình; hai gia đình cùng ăn có thể là so sánh chứ không cùng thời điểm.

**Phản ví dụ / giới hạn:** Montage có thể liên kết bằng cảm giác hoặc hình khối, nhưng nên ghi rõ đó là liên hệ ý tưởng.

**Liên quan:** [EV-003](../kien-thuc/EV-003.json), [ED-003](../kien-thuc/ED-003.json), [ST-006](../kien-thuc/ST-006.json)

**Nguồn đối chiếu:** [B012](../../bai-hoc/012-cau-truc-camera/README.md), [B024](../../bai-hoc/024-xau-chuoi-canh/README.md)

[Bản JSON chuẩn](../kien-thuc/ST-005.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="st-006"></a>
## ST-006 — Điểm nhìn và phân phối thông tin

**Câu hỏi quyết định:** Người xem biết nhiều hơn, ít hơn hay cùng nhân vật?

**Dùng khi:** Khi thiết kế tò mò, hồi hộp, bất ngờ hoặc quan sát.

**Nguyên lý thực hành:** Chọn ai được biết điều gì và lúc nào. Điểm nhìn kể chuyện rộng hơn một cú POV nhìn qua mắt nhân vật.

**Cách làm:**

1. Lập cột thông tin nhân vật biết và khán giả biết.
2. Chọn thời điểm lộ mỗi thông tin.
3. Kiểm tra nguồn thông tin có hợp lý với thế giới và cách kể.

**Đánh đổi:** Giữ bí mật quá lâu làm khó hiểu; biết trước quá nhiều có thể giảm bất ngờ nhưng tăng mong chờ.

**Kiểm tra:**

- Nhận xét ý đồ thông tin dẫn được đến shot/âm cụ thể.
- Không nhầm POV hình ảnh với toàn bộ điểm nhìn của phim.

**Ví dụ tự biên soạn:** Nghe tiếng người ngoài cửa trước nhân vật tạo khác biệt thông tin; cùng nhìn trong mắt nhân vật là một phương án khác.

**Phản ví dụ / giới hạn:** Phim quy trình có thể cho thấy thành phẩm trước để mời xem cách làm thay vì giấu kết quả.

**Liên quan:** [CA-008](../kien-thuc/CA-008.json), [SO-003](../kien-thuc/SO-003.json), [AU-003](../kien-thuc/AU-003.json)

**Nguồn đối chiếu:** [B005](../../bai-hoc/005-bay-cu-may/README.md), [B021](../../bai-hoc/021-lam-chu-cam-xuc/README.md)

[Bản JSON chuẩn](../kien-thuc/ST-006.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="st-007"></a>
## ST-007 — Kịch bản hình–tiếng và lời bổ sung

**Câu hỏi quyết định:** Thông tin nào cần hình, tiếng hoặc lời kể?

**Dùng khi:** Khi viết kịch bản có thoại/lời bình hoặc phim không thoại.

**Nguyên lý thực hành:** Phân công kênh truyền đạt theo điều mỗi kênh làm tốt. Lời có thể thêm bối cảnh, quy luật, suy nghĩ; hình/tiếng có thể tự cho thấy hành động.

**Cách làm:**

1. Lập cột hình, âm, lời và thông tin mới.
2. Rà câu nào chỉ lặp điều đã quá rõ trong hình.
3. Chừa thời gian để hình/tiếng mang thông tin trước khi thêm lời.

**Đánh đổi:** Bỏ hết lời có thể làm mất bối cảnh khó thấy; nhiều lời có thể che trải nghiệm quan sát.

**Kiểm tra:**

- Mỗi câu có chức năng và vừa thời lượng đọc thực tế.
- Không dùng lời để tuyên bố một hành động mà hình mâu thuẫn.

**Ví dụ tự biên soạn:** Thấy bàn tay nhào bột; lời nếu có nói về thời gian chờ hoặc ký ức, không cần đọc mọi cử động.

**Phản ví dụ / giới hạn:** Video hướng dẫn có thể cần gọi tên thao tác đang thấy để người mới học theo.

**Liên quan:** [SO-002](../kien-thuc/SO-002.json), [SO-007](../kien-thuc/SO-007.json), [AU-005](../kien-thuc/AU-005.json)

**Nguồn đối chiếu:** [B016](../../bai-hoc/016-thiet-ke-am-thanh/README.md), [B032](../../bai-hoc/032-dieu-khien-am-thanh/README.md)

[Bản JSON chuẩn](../kien-thuc/ST-007.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="st-008"></a>
## ST-008 — Mở, kết và đời sống tiếp diễn

**Câu hỏi quyết định:** Đầu phim mời vào bằng gì, cuối phim để lại gì?

**Dùng khi:** Khi thiết kế tập độc lập hoặc loạt có nhân vật quen.

**Nguyên lý thực hành:** Mở xác lập lời hứa và việc đáng theo; kết xác nhận phần đã đi qua và tạo dư âm. Một tập nên hiểu được ngay cả khi người xem chưa xem tập trước.

**Cách làm:**

1. Cho sớm một tín hiệu phù hợp lời hứa.
2. Đóng vòng công việc/câu hỏi chính hoặc đánh dấu lý do giữ mở.
3. Gieo chi tiết đời sống tiếp diễn mà không làm tập hiện tại thiếu phần kết.

**Đánh đổi:** Mở quá giải thích giảm sức vào phim; kết quá nhiều nhiệm vụ làm dư âm loãng.

**Kiểm tra:**

- Người xem mới hiểu việc chính.
- Kết không chỉ hết nhạc hoặc hết clip mà có trạng thái cuối rõ.

**Ví dụ tự biên soạn:** Vườn mới gieo ở tập sau là phần tiếp diễn; tập hiện tại vẫn cho thấy bữa ăn hay việc đã hoàn tất.

**Phản ví dụ / giới hạn:** Một phim thử nghiệm có thể không đóng câu hỏi; đó phải là lựa chọn được nêu trong bản yêu cầu.

**Liên quan:** [YT-001](../kien-thuc/YT-001.json), [ST-004](../kien-thuc/ST-004.json), [ED-008](../kien-thuc/ED-008.json)

**Nguồn đối chiếu:** [B017](../../bai-hoc/017-mini-story-ba-nhip/README.md), [B024](../../bai-hoc/024-xau-chuoi-canh/README.md)

[Bản JSON chuẩn](../kien-thuc/ST-008.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).
