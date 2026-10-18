# ST — Kịch bản và cấu trúc

Phiên bản 1.1.0. Xây thay đổi từ đơn vị hành động đến toàn phim; chọn điều cần kể bằng hình/tiếng.

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
| [ST-009](#st-009) | Tạo mạch nguyên nhân hoặc liên tưởng có chủ đích | trung_cap |
| [ST-010](#st-010) | Lặp có biến đổi để tạo tiến triển và nhận diện | trung_cap |
| [ST-011](#st-011) | Tạo điều đáng quan tâm mà không cần phóng đại nguy hiểm | co_ban |
| [ST-012](#st-012) | Mô-típ hình và âm trở lại với nghĩa đã thay đổi | nang_cao |

<a id="st-001"></a>
## ST-001 — Chủ đề, lời hứa và trục thay đổi

**Phiên bản mục:** 1.0.0

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

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Điều gì làm hành động đáng theo dõi?

**Dùng khi:** Khi cảnh có người/vật đang cố đạt một kết quả.

**Nguyên lý thực hành:** Mục tiêu tạo hướng; trở ngại tạo nhu cầu thích nghi; lựa chọn làm lộ năng lực hoặc tính cách. Mức trở ngại theo lời hứa trải nghiệm. Trở ngại không bắt buộc là đối đầu hay nguy hiểm; điều đáng quan tâm có thể là hoàn tất, chăm sóc, khám phá hoặc làm đúng một việc.

**Cách làm:**

1. Nêu mục tiêu có thể nhìn thấy.
2. Chọn trở ngại đúng hoàn cảnh, có thể rất nhỏ.
3. Cho hành động thay đổi trước trở ngại và để lại hệ quả.
4. Ghi giá trị của kết quả và cách lựa chọn tác động nó; nếu cảnh không cần trở ngại, dùng tiến triển hoặc khám phá phù hợp lời hứa.

**Đánh đổi:** Tăng trở ngại quá mức có thể phá cảm giác an toàn hoặc làm nhân vật kém tin cậy.

**Kiểm tra:**

- Không phải mọi hành động đều là lặp lại không đổi.
- Khán giả hiểu lựa chọn đã tác động kết quả thế nào.
- Không tự thêm tai nạn hoặc căng thẳng trái mục tiêu để thỏa một mẫu cấu trúc.

**Ví dụ tự biên soạn:** Người điều chỉnh quai giỏ để mang nặng dễ hơn; ở phim khác đó có thể là lựa chọn đường thoát.

**Phản ví dụ / giới hạn:** Một cảnh ngắm cảnh có thể có giá trị dù không có xung đột; đừng bịa tai nạn để đủ công thức.

**Liên quan:** [DR-001](../kien-thuc/DR-001.json), [AU-003](../kien-thuc/AU-003.json), [ST-004](../kien-thuc/ST-004.json), [ST-011](../kien-thuc/ST-011.json), [YT-008](../kien-thuc/YT-008.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Một mục tiêu nhỏ có thể tạo lực theo dõi nếu giá trị và lựa chọn đọc được.

**Tình huống:** Người chuẩn bị một chỗ ngồi cho khách trong phim yên.

**Phần phải giữ:** Mục tiêu và các phần đã duyệt trong tình huống.

| Phương án | Thực hiện |
| --- | --- |
| A | Thêm ghế sắp gãy để có nguy hiểm. |
| B | Giữ mục tiêu tiếp đón, cho thao tác sửa và hành vi sử dụng xác nhận. |

**Cách chọn:** Chọn B nếu sự chăm sóc là giá trị chính.

**Dấu hiệu kiểm trong ca:**

- Không tự thêm tai nạn hoặc căng thẳng trái mục tiêu để thỏa một mẫu cấu trúc.

**Nếu gặp:** Câu chuyện trở nên giật gân khi chuyển kịch bản sang shot.

Có thể do: Nhầm có lực theo dõi với phải có hiểm nguy.

Thử tiếp: Viết lại mục tiêu và giá trị của kết quả trước khi thiết kế trở ngại.
**Nguồn đối chiếu:** [B017](../../bai-hoc/017-mini-story-ba-nhip/README.md), [B021](../../bai-hoc/021-lam-chu-cam-xuc/README.md)

[Bản JSON chuẩn](../kien-thuc/ST-002.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="st-003"></a>
## ST-003 — Nhịp diễn biến và bước ngoặt trong cảnh

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Tại đâu mục tiêu, hiểu biết hoặc quan hệ đổi?

**Dùng khi:** Khi chia một cảnh thành các phần chỉ đạo.

**Nguyên lý thực hành:** Beat là một nhịp diễn biến có thay đổi nhiệm vụ hoặc thông tin. Nó không tự đồng nghĩa một shot, một giây hay một câu thoại. Thay đổi có thể thuộc trạng thái vật, quyết định, thông tin hoặc quan hệ; một nhịp không buộc trùng một shot hay một job tạo.

**Cách làm:**

1. Đánh dấu trạng thái trước mỗi nhịp.
2. Chỉ ra sự kiện khiến nhân vật/người xem đổi cách hiểu.
3. Ghi trạng thái sau và quyết định quay/dựng cần để đọc chuyển biến.
4. Viết đầu–cuối của nhịp và bằng chứng làm nhận ra đổi; chỉ tách nhịp khi có ích cho quyết định cấu trúc hoặc coverage.

**Đánh đổi:** Tách mọi động tác nhỏ thành nhịp làm kế hoạch nặng mà không thêm giá trị.

**Kiểm tra:**

- Mỗi nhịp có thay đổi nêu được.
- Một nhịp có thể qua nhiều shot hoặc nhiều nhịp ở trong một cú máy.
- Có thể bỏ tên cỡ cảnh mà vẫn hiểu nhịp làm thay đổi điều gì.

**Ví dụ tự biên soạn:** Từ đang làm việc sang nhận ra có khách, rồi quyết định dừng tay; mỗi phần có nhiệm vụ khác.

**Phản ví dụ / giới hạn:** Nhấc tay rồi hạ tay không thành bước ngoặt nếu không đổi điều gì đáng kể.

**Liên quan:** [EV-003](../kien-thuc/EV-003.json), [DR-003](../kien-thuc/DR-003.json), [ED-001](../kien-thuc/ED-001.json), [AU-007](../kien-thuc/AU-007.json), [AI-009](../kien-thuc/AI-009.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Nhịp cần đo bằng thay đổi có chức năng thay vì mỗi dòng một động tác.

**Tình huống:** Một người đang làm rồi nhận ra khách và quyết định dừng.

**Phần phải giữ:** Mục tiêu và các phần đã duyệt trong tình huống.

| Phương án | Thực hiện |
| --- | --- |
| A | Chia thành ba nhịp chỉ vì có ba góc. |
| B | Đặt nhịp theo nhận ra và quyết định; chọn số góc sau. |

**Cách chọn:** Chọn B khi lập cấu trúc; ba góc có thể phục vụ cùng một nhịp.

**Dấu hiệu kiểm trong ca:**

- Có thể bỏ tên cỡ cảnh mà vẫn hiểu nhịp làm thay đổi điều gì.

**Nếu gặp:** Kịch bản dài nhiều dòng nhưng ít thay đổi.

Có thể do: Nhịp bị đồng nhất với shot hoặc động tác vụn.

Thử tiếp: Gộp các dòng không đổi thông tin/trạng thái và kiểm lại tiến trình.

**Phát biểu được đối chiếu:** Ranh giới cắt và ranh giới sự kiện được nghiên cứu như các biến khác nhau. Nguồn: [SRC-PERCEPTION-EVENTS](https://pmc.ncbi.nlm.nih.gov/articles/PMC3208769/).

**Giới hạn nguồn:** Không có tỷ lệ cắt tối ưu, phép đo hài lòng khán giả kênh này hoặc quy luật mọi thể loại. Ứng dụng dựng trong kho là đề xuất cần kiểm.
**Nguồn đối chiếu:** [B017](../../bai-hoc/017-mini-story-ba-nhip/README.md), [B021](../../bai-hoc/021-lam-chu-cam-xuc/README.md), [SRC-PERCEPTION-EVENTS](https://pmc.ncbi.nlm.nih.gov/articles/PMC3208769/)

[Bản JSON chuẩn](../kien-thuc/ST-003.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="st-004"></a>
## ST-004 — Chuẩn bị, phát triển và trả kết quả

**Phiên bản mục:** 1.0.0

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

**Phiên bản mục:** 1.0.0

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

**Phiên bản mục:** 1.0.0

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

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Thông tin nào cần hình, tiếng hoặc lời kể?

**Dùng khi:** Khi viết kịch bản có thoại/lời bình hoặc phim không thoại.

**Nguyên lý thực hành:** Phân công kênh truyền đạt theo điều mỗi kênh làm tốt. Lời có thể thêm bối cảnh, quy luật, suy nghĩ; hình/tiếng có thể tự cho thấy hành động. Thiết lập mục tiêu, tác động và hệ quả có thể đọc qua hành động/hình–âm; lời vẫn có ích cho bối cảnh không thể thấy khi dạng phim cho phép.

**Cách làm:**

1. Lập cột hình, âm, lời và thông tin mới.
2. Rà câu nào chỉ lặp điều đã quá rõ trong hình.
3. Chừa thời gian để hình/tiếng mang thông tin trước khi thêm lời.
4. Làm bản sơ chỉ bằng hình–âm để tìm chỗ người mới hiểu sai; sửa đúng dấu thiếu, bảo vệ lựa chọn không thoại nếu đã chốt.

**Đánh đổi:** Bỏ hết lời có thể làm mất bối cảnh khó thấy; nhiều lời có thể che trải nghiệm quan sát.

**Kiểm tra:**

- Mỗi câu có chức năng và vừa thời lượng đọc thực tế.
- Không dùng lời để tuyên bố một hành động mà hình mâu thuẫn.
- Người xem có thể kể tiến trình chính mà không cần biết trước bản thuyết minh của tác giả.

**Ví dụ tự biên soạn:** Thấy bàn tay nhào bột; lời nếu có nói về thời gian chờ hoặc ký ức, không cần đọc mọi cử động.

**Phản ví dụ / giới hạn:** Video hướng dẫn có thể cần gọi tên thao tác đang thấy để người mới học theo.

**Liên quan:** [SO-002](../kien-thuc/SO-002.json), [SO-007](../kien-thuc/SO-007.json), [AU-005](../kien-thuc/AU-005.json), [ST-009](../kien-thuc/ST-009.json), [ST-011](../kien-thuc/ST-011.json), [YT-011](../kien-thuc/YT-011.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Kể không lời cần bằng chứng và quan hệ, không phải chỉ bỏ voiceover.

**Tình huống:** Một vật được sửa nhưng nguồn không có thoại.

**Phần phải giữ:** Mục tiêu và các phần đã duyệt trong tình huống.

| Phương án | Thực hiện |
| --- | --- |
| A | Bổ sung lời tuyên bố vật đã hoạt động. |
| B | Thêm hoặc chọn hành động sử dụng chứng minh chức năng. |

**Cách chọn:** Chọn B khi phải giữ không thoại; lời chỉ xem xét nếu cần bối cảnh và được cho phép.

**Dấu hiệu kiểm trong ca:**

- Người xem có thể kể tiến trình chính mà không cần biết trước bản thuyết minh của tác giả.

**Nếu gặp:** Bỏ lời xong phim không còn hiểu được.

Có thể do: Thông tin thiết yếu chỉ tồn tại trong bản thuyết minh.

Thử tiếp: Lập danh sách thông tin đó và tìm bằng chứng hình–âm khả thi cho từng mục.
**Nguồn đối chiếu:** [B016](../../bai-hoc/016-thiet-ke-am-thanh/README.md), [B032](../../bai-hoc/032-dieu-khien-am-thanh/README.md)

[Bản JSON chuẩn](../kien-thuc/ST-007.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="st-008"></a>
## ST-008 — Mở, kết và đời sống tiếp diễn

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Đầu phim mời vào bằng gì, cuối phim để lại gì?

**Dùng khi:** Khi thiết kế tập độc lập hoặc loạt có nhân vật quen.

**Nguyên lý thực hành:** Mở xác lập lời hứa và việc đáng theo; kết xác nhận phần đã đi qua và tạo dư âm. Một tập nên hiểu được ngay cả khi người xem chưa xem tập trước. Mở có thể vào trực tiếp một việc, một nơi chốn hoặc câu hỏi; cần cho người phù hợp nhận ra giá trị sớm. Kết cần xác nhận giá trị hoặc lựa chọn kết mở có lý do.

**Cách làm:**

1. Cho sớm một tín hiệu phù hợp lời hứa.
2. Đóng vòng công việc/câu hỏi chính hoặc đánh dấu lý do giữ mở.
3. Gieo chi tiết đời sống tiếp diễn mà không làm tập hiện tại thiếu phần kết.
4. So chính xác điều tiêu đề/ảnh/mở hứa với bằng chứng ở kết; không dùng teaser hoặc lời kêu gọi thay phần trả giá trị.

**Đánh đổi:** Mở quá giải thích giảm sức vào phim; kết quá nhiều nhiệm vụ làm dư âm loãng.

**Kiểm tra:**

- Người xem mới hiểu việc chính.
- Kết không chỉ hết nhạc hoặc hết clip mà có trạng thái cuối rõ.
- Không áp thời hạn ba giây, ba mươi giây hoặc một tỷ lệ hồi như luật chung.

**Ví dụ tự biên soạn:** Vườn mới gieo ở tập sau là phần tiếp diễn; tập hiện tại vẫn cho thấy bữa ăn hay việc đã hoàn tất.

**Phản ví dụ / giới hạn:** Một phim thử nghiệm có thể không đóng câu hỏi; đó phải là lựa chọn được nêu trong bản yêu cầu.

**Liên quan:** [YT-001](../kien-thuc/YT-001.json), [ST-004](../kien-thuc/ST-004.json), [ED-008](../kien-thuc/ED-008.json), [YT-008](../kien-thuc/YT-008.json), [ST-011](../kien-thuc/ST-011.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Mở và kết phải cùng trả một lời hứa nhưng không cần cùng một công thức.

**Tình huống:** Video hứa trải nghiệm một buổi sửa đồ không lời.

**Phần phải giữ:** Mục tiêu và các phần đã duyệt trong tình huống.

| Phương án | Thực hiện |
| --- | --- |
| A | Mở bằng tình huống sốc không xuất hiện lại. |
| B | Vào việc rõ và cho thấy hướng giá trị phù hợp tông phim. |

**Cách chọn:** Chọn B; tốc độ mở tùy thông tin và tệp, không tùy một số giây duy nhất.

**Dấu hiệu kiểm trong ca:**

- Không áp thời hạn ba giây, ba mươi giây hoặc một tỷ lệ hồi như luật chung.

**Nếu gặp:** Mở kéo được nhấp nhưng khán giả nói nội dung khác kỳ vọng.

Có thể do: Lời hứa không khớp trải nghiệm thật.

Thử tiếp: Đối chiếu lời hứa với đoạn đầu và phần trả giá trị, sửa chỗ lệch cụ thể.
**Nguồn đối chiếu:** [B017](../../bai-hoc/017-mini-story-ba-nhip/README.md), [B024](../../bai-hoc/024-xau-chuoi-canh/README.md), [SRC-YT-PERFORMANCE](https://support.google.com/youtube/answer/16559650)

[Bản JSON chuẩn](../kien-thuc/ST-008.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="st-009"></a>
## ST-009 — Tạo mạch nguyên nhân hoặc liên tưởng có chủ đích

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Vì sao cảnh kế tiếp phải có mặt sau cảnh này?

**Dùng khi:** Kịch bản thành danh sách cảnh đẹp, trình tự công đoạn hoặc montage thiếu trục.

**Nguyên lý thực hành:** Một chuỗi có thể nối bằng nguyên nhân, thời gian, câu hỏi–lời giải, không gian hoặc liên tưởng. Chọn quan hệ chính và làm người xem đọc được; không bắt mọi phim thành chuỗi xung đột.

**Cách làm:**

1. Viết bên cạnh mỗi nối cảnh một từ chỉ quan hệ: vì vậy, nhưng, sau đó, đồng thời, tương phản hoặc gợi nhớ; nếu không xác định được thì xem lại chức năng.
2. Đối với tiến trình, cho thấy điều kiện đầu, hành động đổi trạng thái và hệ quả cần cho bước sau. Với liên tưởng, giữ dấu hình/âm/ý nghĩa đủ nhận ra.
3. Loại hoặc chuyển vị trí cảnh đẹp nếu không bổ sung trải nghiệm, thông tin hoặc khoảng nghỉ có mục đích.

**Đánh đổi:** Giải thích mọi quan hệ có thể làm phim khô; có thể để người xem tự nối khi bằng chứng đủ.

**Kiểm tra:**

- Đảo thứ tự hai cảnh làm thay đổi nghĩa hoặc nhịp theo cách nêu được.
- Không tạo nhân quả giả khi chỉ có quan hệ cắt xen.

**Ví dụ tự biên soạn:** Chốt cửa kẹt→người kiểm khe→tháo vật cản→cửa mở. Một phim quan sát khác có thể nối các cánh cửa bằng tương đồng hình để nói về nơi chốn.

**Phản ví dụ / giới hạn:** Các cảnh có chung tông màu không tự tạo tiến trình; nhưng phim mang mục tiêu chiêm ngắm có thể chủ động dùng quan hệ thị giác làm trục.

**Liên quan:** [ST-001](../kien-thuc/ST-001.json), [ST-003](../kien-thuc/ST-003.json), [ST-005](../kien-thuc/ST-005.json), [ED-006](../kien-thuc/ED-006.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Nêu quan hệ buộc người dựng xác định đóng góp của mỗi đoạn. Đây là công cụ biên tập, không yêu cầu mọi cú nối phải được khán giả diễn đạt thành lời.

**Tình huống:** Chốt cửa kẹt→người kiểm khe→tháo vật cản→cửa mở. Một phim quan sát khác có thể nối các cánh cửa bằng tương đồng hình để nói về nơi chốn.

**Phần phải giữ:** Quan hệ cửa kẹt, kiểm tra và khắc phục.

| Phương án | Thực hiện |
| --- | --- |
| A | Giữ tất cả cảnh đã tạo vì mỗi cảnh đều đẹp. |
| B | Lập bản dựng theo các bước thay đổi chính, rồi chèn cảnh quan sát ở chỗ chúng có tác dụng cụ thể. |

**Cách chọn:** Chọn theo lời hứa; khi người xem đang lạc tiến trình, thử B trước khi tạo thêm hình.

**Dấu hiệu kiểm trong ca:**

- Đảo thứ tự hai cảnh làm thay đổi nghĩa hoặc nhịp theo cách nêu được.
- Không tạo nhân quả giả khi chỉ có quan hệ cắt xen.

**Nếu gặp:** Phim có nhiều công đoạn nhưng không thấy việc tiến tới đâu.

Có thể do: Thiếu kết quả trung gian. Cảnh lặp chức năng hoặc thứ tự theo ngày sinh file.

Thử tiếp: Tóm tắt mỗi cảnh bằng một thay đổi; thử bỏ một cảnh và xem quan hệ nào bị mất.
**Nguồn đối chiếu:** [SRC-YALE-EDIT](https://filmanalysis.yale.edu/editing/)

[Bản JSON chuẩn](../kien-thuc/ST-009.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="st-010"></a>
## ST-010 — Lặp có biến đổi để tạo tiến triển và nhận diện

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Lần lặp này đem đến điều mới gì?

**Dùng khi:** Cảnh công việc lặp, series, nghi thức, âm thanh hoặc động tác trở lại nhiều lần.

**Nguyên lý thực hành:** Sự lặp có thể giúp nhận diện, so sánh, học thao tác hoặc thưởng thức nhịp. Để tạo tiến triển, thay đổi ít nhất một yếu tố có ý nghĩa thay vì chỉ đổi góc quay.

**Cách làm:**

1. Xác định điều cố định để người xem nhận ra và điều thay đổi: độ thuần thục, vật liệu, quy mô, quan hệ, trạng thái hoàn thành hoặc kết quả.
2. Cho lần đầu đủ rõ để thiết lập; những lần sau chọn dấu khác biệt cần thiết. Có thể nén khi người xem đã hiểu thao tác.
3. Giữ nguyên một lần lặp dài nếu giá trị nằm ở trải nghiệm quan sát; ghi đó là lựa chọn theo tệp, không mặc định là cảnh thừa.

**Đánh đổi:** Nén quá mức mất cảm giác công sức; giữ mọi lần lặp đầy đủ có thể kéo dài mà không thêm giá trị.

**Kiểm tra:**

- Mỗi lần trở lại có vai trò hoặc thay đổi gọi tên được.
- Không đo sự mới chỉ bằng số cỡ cảnh khác nhau.

**Ví dụ tự biên soạn:** Ba lượt thử một bánh xe: lần đầu còn đảo, lần hai được chỉnh, lần ba lăn thẳng. Cùng góc máy có thể làm sự thay đổi rõ hơn ba góc đẹp khác nhau.

**Phản ví dụ / giới hạn:** Lặp âm nước hoặc động tác đều không luôn gây chán; nội dung nghe/ngắm cần kiểm theo nhu cầu đã chốt.

**Liên quan:** [ST-003](../kien-thuc/ST-003.json), [ST-004](../kien-thuc/ST-004.json), [ED-011](../kien-thuc/ED-011.json), [YT-004](../kien-thuc/YT-004.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Phần ổn định tạo mốc so sánh; phần thay đổi truyền tiến độ. Chức năng này khác với việc thêm chuyển động máy để tạo cảm giác mới bề mặt.

**Tình huống:** Ba lượt thử một bánh xe: lần đầu còn đảo, lần hai được chỉnh, lần ba lăn thẳng. Cùng góc máy có thể làm sự thay đổi rõ hơn ba góc đẹp khác nhau.

**Phần phải giữ:** Điều kiện so ba lượt bánh xe. Tiến triển từ đảo sang lăn thẳng.

| Phương án | Thực hiện |
| --- | --- |
| A | Đổi góc cho từng lượt nhưng vật và kết quả không thay đổi. |
| B | Giữ góc so sánh và chỉ giữ những lượt cho thấy tiến triển hoặc giá trị quan sát. |

**Cách chọn:** Chọn B nếu cần thấy quá trình cải thiện; A phù hợp khi mục tiêu chính là khám phá hình dạng từ nhiều phía.

**Dấu hiệu kiểm trong ca:**

- Mỗi lần trở lại có vai trò hoặc thay đổi gọi tên được.
- Không đo sự mới chỉ bằng số cỡ cảnh khác nhau.

**Nếu gặp:** Video dài hơn nhưng khán giả không nhận ra tiến độ.

Có thể do: Mọi công đoạn được đối xử ngang nhau. Dấu kết quả quá nhỏ hoặc không cùng điều kiện so sánh.

Thử tiếp: Dùng cùng mốc hình để so trạng thái trước/sau; hỏi người xem điều gì vừa cải thiện.
**Nguồn đối chiếu:** [SRC-YALE-EDIT](https://filmanalysis.yale.edu/editing/), [SRC-YT-RECOMMENDATIONS](https://support.google.com/youtube/answer/16533387?hl=en)

[Bản JSON chuẩn](../kien-thuc/ST-010.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="st-011"></a>
## ST-011 — Tạo điều đáng quan tâm mà không cần phóng đại nguy hiểm

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Vì sao người xem nên quan tâm kết quả của hành động nhỏ này?

**Dùng khi:** Phim đời sống, thủ công, thiên nhiên, quan sát hoặc câu chuyện ít xung đột.

**Nguyên lý thực hành:** Điều đáng quan tâm có thể là hoàn tất việc, chăm sóc ai đó, khám phá, độ khéo, vẻ đẹp hoặc cảm giác thuộc về. Làm rõ giá trị của kết quả và người/vật chịu tác động; không tự thêm tai nạn để tạo kịch tính.

**Cách làm:**

1. Ghi ai hoặc điều gì được lợi từ việc hoàn tất: một công dụng, một bữa chung, một nơi được chăm hoặc một câu hỏi được trả.
2. Cho một bằng chứng ban đầu khiến kết quả có nghĩa: đồ chưa dùng được, người sẽ nhận, trạng thái đang dở hoặc đặc điểm cần khám phá.
3. Kết bằng hành động sử dụng, kết quả kiểm tra hoặc sự tiếp tục đời sống để xác nhận giá trị; không chỉ dừng ở ảnh sản phẩm.

**Đánh đổi:** Giải thích quá nhiều biến khoảnh khắc tinh tế thành thông điệp lộ; có thể dùng hành động nhỏ và âm thanh thay lời.

**Kiểm tra:**

- Mục tiêu nhỏ vẫn nêu được giá trị với tệp mong muốn.
- Kết quả có dấu sử dụng/tiếp nhận hoặc lý do kết mở rõ.

**Ví dụ tự biên soạn:** Người sửa chiếc ghế cũ để khách có chỗ ngồi; cuối phim người khách ngồi xuống và cuộc trò chuyện tiếp tục.

**Phản ví dụ / giới hạn:** Phim ngắm thiên nhiên có thể không cần nhân vật hoặc một vật được hoàn tất; giá trị khám phá/chiêm ngắm vẫn là một lời hứa hợp lệ.

**Liên quan:** [AU-001](../kien-thuc/AU-001.json), [AU-009](../kien-thuc/AU-009.json), [ST-002](../kien-thuc/ST-002.json), [ST-008](../kien-thuc/ST-008.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Một kết quả có trọng lượng khi đã có mối quan tâm phù hợp trước đó. Quy mô nhỏ không có nghĩa giá trị nhỏ; lựa chọn phụ thuộc nhu cầu người xem, không phải mức hiểm nguy tối đa.

**Tình huống:** Người sửa chiếc ghế cũ để khách có chỗ ngồi; cuối phim người khách ngồi xuống và cuộc trò chuyện tiếp tục.

**Phần phải giữ:** Trải nghiệm yên và sự tiếp đón. Kết quả chiếc ghế được dùng.

| Phương án | Thực hiện |
| --- | --- |
| A | Thêm biến cố chiếc ghế gãy nguy hiểm dù phim đã chốt êm dịu. |
| B | Cho thấy công dụng thiếu trước sửa và dấu người nhận sử dụng sau sửa. |

**Cách chọn:** Chọn B nếu mục tiêu là sự chăm sóc và hoàn tất; A chỉ xét khi đổi trải nghiệm đã được người dùng duyệt.

**Dấu hiệu kiểm trong ca:**

- Mục tiêu nhỏ vẫn nêu được giá trị với tệp mong muốn.
- Kết quả có dấu sử dụng/tiếp nhận hoặc lý do kết mở rõ.

**Nếu gặp:** Cảnh hoàn tất rất đẹp nhưng kết phim nhạt.

Có thể do: Không biết sản phẩm dùng cho ai hoặc việc hoàn thành có ý nghĩa gì. Kết chỉ trưng bày mà thiếu xác nhận chức năng.

Thử tiếp: Thêm một hành vi tiếp nhận phù hợp thay vì tăng nhạc hay tạo nguy hiểm.
**Nguồn đối chiếu:** [SRC-YALE-STAGING](https://filmanalysis.yale.edu/mise-en-scene/), [SRC-YT-PERFORMANCE](https://support.google.com/youtube/answer/16559650)

[Bản JSON chuẩn](../kien-thuc/ST-011.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="st-012"></a>
## ST-012 — Mô-típ hình và âm trở lại với nghĩa đã thay đổi

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Chi tiết lặp này phát triển ý nghĩa hay chỉ trang trí?

**Dùng khi:** Tạo liên kết đầu–cuối, bản sắc series hoặc dư âm không cần lời giải thích.

**Nguyên lý thực hành:** Mô-típ là một chi tiết, hành động, hình hoặc âm có chức năng khi trở lại. Thiết lập đủ nhận ra và thay đổi ngữ cảnh để lần trở lại bổ sung nghĩa; không bắt người xem giải mật mã mới hiểu việc chính.

**Cách làm:**

1. Chọn ít yếu tố dễ nhận, gắn với câu chuyện: âm cửa, bàn tay trao vật, ánh đèn hoặc vật dụng có công năng.
2. Ghi cho mỗi lần xuất hiện: điều ổn định, ngữ cảnh mới và liên hệ dự kiến. Cho dấu biến đổi cụ thể thay vì chỉ lặp cùng stock shot.
3. Kiểm hai lớp: người không nhận ra mô-típ vẫn hiểu mạch; người nhận ra có thêm liên hệ hoặc cảm giác hoàn tất.

**Đánh đổi:** Nhấn quá rõ gây đoán trước; quá kín khiến ý nghĩa chỉ tồn tại trong thuyết minh của tác giả.

**Kiểm tra:**

- Lần trở lại có quan hệ với thay đổi chính.
- Phim vẫn hiểu được khi chưa gọi tên biểu tượng.

**Ví dụ tự biên soạn:** Đầu phim tiếng chốt cửa gắn với căn phòng chưa dùng; cuối phim cùng âm mở ra buổi sinh hoạt. Nguồn âm giống nhưng công năng trong câu chuyện đổi.

**Phản ví dụ / giới hạn:** Một tông cam xuất hiện nhiều lần chưa đủ để kết luận đó là biểu tượng về gia đình của tác giả.

**Liên quan:** [ST-004](../kien-thuc/ST-004.json), [ST-010](../kien-thuc/ST-010.json), [CO-002](../kien-thuc/CO-002.json), [SO-006](../kien-thuc/SO-006.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Mốc quen cho phép so ngữ cảnh trước–sau. Ý nghĩa được đề xuất qua quan hệ trong phim; khi phân tích nguồn, phải tách quan sát lặp khỏi diễn giải biểu tượng.

**Tình huống:** Đầu phim tiếng chốt cửa gắn với căn phòng chưa dùng; cuối phim cùng âm mở ra buổi sinh hoạt. Nguồn âm giống nhưng công năng trong câu chuyện đổi.

**Phần phải giữ:** Nguồn tiếng chốt nhận ra được. Việc chính vẫn hiểu khi chưa nhận ra mô-típ.

| Phương án | Thực hiện |
| --- | --- |
| A | Lặp cận vật ở mọi chương dù không liên quan. |
| B | Giữ hai hoặc vài lần có chức năng rõ và để ngữ cảnh tạo khác biệt. |

**Cách chọn:** Chọn B khi mô-típ đang làm ngắt mạch; tần suất không có ngưỡng chung.

**Dấu hiệu kiểm trong ca:**

- Lần trở lại có quan hệ với thay đổi chính.
- Phim vẫn hiểu được khi chưa gọi tên biểu tượng.

**Nếu gặp:** Chi tiết lặp bị cảm như quảng cáo hoặc cảnh chèn.

Có thể do: Xuất hiện không có tác nhân. Lặp hình nhưng không phát triển công năng/quan hệ.

Thử tiếp: Tạm bỏ một lần lặp; xem câu chuyện hoặc liên hệ có mất điều gì cụ thể không.
**Nguồn đối chiếu:** [SRC-YALE-STAGING](https://filmanalysis.yale.edu/mise-en-scene/), [SRC-YALE-SOUND](https://filmanalysis.yale.edu/sound/)

[Bản JSON chuẩn](../kien-thuc/ST-012.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).
