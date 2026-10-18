# CO — Màu sắc và thiết kế hình ảnh

Phiên bản 1.3.0. Tổ chức màu từ vật liệu đến hậu kỳ; giữ quan hệ màu qua chuỗi.

[Mục lục](../README.md) · [Chuẩn ra quyết định](../03_RA_QUYET_DINH.md)

Mỗi mục dưới là hướng dẫn có điều kiện. Tác dụng cảm xúc là giả thuyết thiết kế; chưa có thử tạo video hoặc kiểm nghiệm khán giả cho các ví dụ mới. Thuật ngữ xem [từ điển](../TU_DIEN.md).

| Mã | Quyết định | Mức |
| --- | --- | --- |
| [CO-001](#co-001) | Sắc, độ bão hòa và độ sáng là ba lựa chọn | co_ban |
| [CO-002](#co-002) | Bảng màu từ thế giới, nhân vật và vật liệu | trung_cap |
| [CO-003](#co-003) | Tách chủ thể và phân cấp bằng màu/độ sáng | trung_cap |
| [CO-004](#co-004) | Chất liệu và dấu biến đổi | trung_cap |
| [CO-005](#co-005) | Màu liên tục và chuyển biến có mục đích | nang_cao |
| [CO-006](#co-006) | Quản lý màu, sửa cân bằng và tạo phong cách | nang_cao |
| [CO-007](#co-007) | Cân bằng trắng, ám xanh–hồng và nguồn sáng pha trộn | trung_cap |
| [CO-008](#co-008) | Khớp shot trước, tạo phong cách sau và kiểm bằng mắt lẫn công cụ | trung_cap |
| [CO-009](#co-009) | Dữ liệu theo cảnh và hình đã hiển thị: tránh gán nhầm Log/RAW cho AI | nang_cao |

<a id="co-001"></a>
## CO-001 — Sắc, độ bão hòa và độ sáng là ba lựa chọn

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Điều gì của màu đang phục vụ cảnh?

**Dùng khi:** Khi chọn bảng màu hoặc nhận xét tông hình.

**Nguyên lý thực hành:** Tách tên sắc, mức rực và quan hệ sáng–tối. Ý nghĩa màu phụ thuộc văn hóa, vật thể, lịch sử trong phim và bối cảnh; không dùng bảng màu như luật cảm xúc. Các hệ màu dùng lightness/luma/luminance và saturation/chroma khác nhau; khi đo cần ghi hệ/công cụ thay vì coi các thuật ngữ là một phép đo giống hệt.

**Cách làm:**

1. Chọn quan hệ màu quan trọng thay vì một tên mood chung.
2. Ghi mục tiêu độ sáng và mức bão hòa tương đối.
3. Kiểm màu cùng nội dung và các cảnh lân cận.
4. Nếu màu không truyền đạt đúng, kiểm độ tách sáng và vật liệu trước; dùng lời mô tả quan hệ và bản tham chiếu thay một mã HEX đơn lẻ.

**Đánh đổi:** Giảm rực có thể mất sinh khí; tăng rực có thể làm vật liệu giả hoặc che điểm nhấn.

**Kiểm tra:**

- Nhận xét cảm xúc có điều kiện thay vì đỏ luôn giận/xanh luôn buồn.
- Chi tiết thiết yếu vẫn đọc khi xem hình gần như đen trắng.
- Bảng màu không làm mất nhận diện hoặc điểm tiếp xúc khi xem ở đầu ra thật.

**Ví dụ tự biên soạn:** Lam–xám sương và hồng hoa có thể yên bình; đỏ có thể là thức ăn ấm áp hoặc tín hiệu nguy hiểm.

**Phản ví dụ / giới hạn:** Một bảng màu hài hòa không tự làm câu chuyện dễ hiểu.

**Liên quan:** [AU-004](../kien-thuc/AU-004.json), [CO-003](../kien-thuc/CO-003.json), [LI-003](../kien-thuc/LI-003.json), [CO-007](../kien-thuc/CO-007.json), [CO-008](../kien-thuc/CO-008.json), [CO-009](../kien-thuc/CO-009.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Màu dùng được ngay phải giữ quan hệ độ sáng, vật liệu và bối cảnh, không gán bảng cảm xúc tuyệt đối.

**Tình huống:** Một món đồ đỏ không nổi vì nền sáng hơn và chuyển động nền mạnh.

**Phần phải giữ:** Mục tiêu và các phần đã duyệt trong tình huống.

| Phương án | Thực hiện |
| --- | --- |
| A | Tăng đỏ đến khi clipping. |
| B | Sửa quan hệ độ sáng/nền, giữ màu và vật liệu có lý do. |

**Cách chọn:** Chọn B nếu vấn đề là phân cấp; saturation không phải cách duy nhất.

**Dấu hiệu kiểm trong ca:**

- Bảng màu không làm mất nhận diện hoặc điểm tiếp xúc khi xem ở đầu ra thật.

**Nếu gặp:** Màu càng rực càng giả nhưng trọng tâm vẫn yếu.

Có thể do: Sai chẩn đoán giữa độ nổi và độ bão hòa.

Thử tiếp: So bản giảm cạnh tranh nền và bản tăng màu ở mức tương đương; kiểm vật liệu và thông tin.
**Nguồn đối chiếu:** [B008](../../bai-hoc/008-muoi-cu-phap-veo/README.md), [B009](../../bai-hoc/009-nang-cap-ngon-ngu-dien-anh/README.md), [SRC-YALE-CAMERA](https://filmanalysis.yale.edu/cinematography/), [SRC-ACES-WORKFLOW](https://docs.acescentral.com/background/overview/)

[Bản JSON chuẩn](../kien-thuc/CO-001.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="co-002"></a>
## CO-002 — Bảng màu từ thế giới, nhân vật và vật liệu

**Phiên bản mục:** 1.0.0

**Câu hỏi quyết định:** Màu nào có lý do tồn tại trong cảnh?

**Dùng khi:** Khi tiền kỳ hoặc thiết kế một chuỗi/tập.

**Nguyên lý thực hành:** Chọn bảng màu từ bối cảnh, phục trang, đạo cụ và thời điểm. Phân vai màu nền, màu chủ thể và điểm nhấn; không phụ thuộc hoàn toàn vào chỉnh màu sau.

**Cách làm:**

1. Ghi nguồn vật lý của từng màu chủ đạo.
2. Chọn mức lặp và những màu cần hạn chế vì cạnh tranh.
3. So phục trang/đạo cụ trên nền và dưới ánh sáng dự kiến.

**Đánh đổi:** Bảng quá đồng nhất có thể làm chủ thể hòa lẫn hoặc thế giới đơn điệu.

**Kiểm tra:**

- Điểm nhấn có chức năng và đọc được qua chuỗi.
- Màu không chỉ được ghi bằng HEX mà có vật liệu và ánh sáng đi kèm.

**Ví dụ tự biên soạn:** Áo chàm, đất nâu và cây xanh giúp cảnh có hệ màu; món tím có thể là điểm nhấn lặp.

**Phản ví dụ / giới hạn:** Một cảnh tương phản mạnh có thể phù hợp bước ngoặt, dù khác bảng chủ đạo.

**Liên quan:** [DR-005](../kien-thuc/DR-005.json), [CO-003](../kien-thuc/CO-003.json), [AI-002](../kien-thuc/AI-002.json)

**Nguồn đối chiếu:** [B003](../../bai-hoc/003-khoa-thiet-ke-nhan-vat/README.md), [B020](../../bai-hoc/020-nam-chia-khoa-nhat-quan/README.md)

[Bản JSON chuẩn](../kien-thuc/CO-002.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="co-003"></a>
## CO-003 — Tách chủ thể và phân cấp bằng màu/độ sáng

**Phiên bản mục:** 1.0.0

**Câu hỏi quyết định:** Người xem cần tìm điều gì trong một nền nhiều chi tiết?

**Dùng khi:** Khi chủ thể chìm hoặc nhiều màu tranh nhau.

**Nguyên lý thực hành:** Dùng chênh tương đối về sáng, sắc hoặc bão hòa. Không cần mọi yếu tố đều tương phản tối đa.

**Cách làm:**

1. So chủ thể với vùng nền ngay sát nó.
2. Chọn một kiểu chênh đủ dùng và giảm màu cạnh tranh.
3. Xem ở kích thước nhỏ và theo chuyển động thực.

**Đánh đổi:** Tách mạnh quá có thể giống ghép lớp; tương phản màu mất tác dụng nếu độ sáng quá giống trên thiết bị khác.

**Kiểm tra:**

- Điểm chính tìm được nhanh nhưng vẫn thuộc không gian.
- Không phải làm da sáng/rực hơn mọi thứ trong mọi cảnh.

**Ví dụ tự biên soạn:** Bát sáng trên bàn tối giúp đọc đường gạo rơi; đổi nền có thể tốt hơn tăng sáng toàn ảnh.

**Phản ví dụ / giới hạn:** Cảnh muốn nhân vật hòa vào môi trường có thể chủ động giảm tách.

**Liên quan:** [AU-002](../kien-thuc/AU-002.json), [CA-003](../kien-thuc/CA-003.json), [LI-006](../kien-thuc/LI-006.json)

**Nguồn đối chiếu:** [B003](../../bai-hoc/003-khoa-thiet-ke-nhan-vat/README.md), [B025](../../bai-hoc/025-dieu-khien-camera/README.md)

[Bản JSON chuẩn](../kien-thuc/CO-003.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="co-004"></a>
## CO-004 — Chất liệu và dấu biến đổi

**Phiên bản mục:** 1.3.0

**Câu hỏi quyết định:** Hình có cho thấy vật được làm, chạm và thay đổi không?

**Dùng khi:** Khi kể quy trình, đồ ăn, thủ công hoặc thế giới giả tưởng.

**Nguyên lý thực hành:** Ghi bề mặt, trọng lượng, độ ẩm, phản chiếu và trạng thái trước–sau có liên quan. Chi tiết hỗ trợ hiểu vật, không chỉ tăng độ sắc.

**Cách làm:**

1. Chọn dấu vật liệu cần người xem nhận ra.
2. Gắn thay đổi với thao tác hoặc môi trường gây ra nó.
3. Kiểm vùng tiếp xúc và sự ổn định của chất liệu qua thời gian.
4. Chọn dấu bề mặt gắn với vật để theo dõi qua chuyển động/che lộ; phân biệt vân vật bị trôi với phản chiếu, hơi nước hoặc hạt đang thay đổi hợp lý.
5. Đối chiếu lượng/trạng thái trước–sau theo công đoạn. Không tạo cảm giác tiến triển bằng cách tự đổi vật liệu hay thành phẩm giữa hai cận.

**Đánh đổi:** Chi tiết quá mức có thể gây cảm giác giả hoặc mất trọng tâm.

**Kiểm tra:**

- Vật không tự sạch/chín/đầy khi chưa có nguyên nhân hoặc lược thời gian rõ.
- Không dùng quá sắc và hạt phim để che lỗi hình học.
- Vân, nhãn và hình học gắn với vật khi cần giữ nhận diện; phần động tự nhiên không bị khóa thành ảnh đứng.

**Ví dụ tự biên soạn:** Đất khô trở ẩm khi nước đến; một bề mặt ướt có phản chiếu đổi hợp lý.

**Phản ví dụ / giới hạn:** Hoạt hình có thể giản lược vật liệu nhưng vẫn cần quy luật biến đổi nội tại.

**Liên quan:** [DR-005](../kien-thuc/DR-005.json), [AI-003](../kien-thuc/AI-003.json), [LI-006](../kien-thuc/LI-006.json), [QC-010](../kien-thuc/QC-010.json), [AI-010](../kien-thuc/AI-010.json)

**Nguồn đối chiếu:** [B015](../../bai-hoc/015-logic-chuyen-dong-vat-ly/README.md), [B023](../../bai-hoc/023-negative-prompt/README.md)

[Bản JSON chuẩn](../kien-thuc/CO-004.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="co-005"></a>
## CO-005 — Màu liên tục và chuyển biến có mục đích

**Phiên bản mục:** 1.0.0

**Câu hỏi quyết định:** Màu đổi vì điều kiện cảnh hay vì lỗi?

**Dùng khi:** Khi nối góc, đổi thời điểm hoặc làm chuỗi tập.

**Nguyên lý thực hành:** Giữ thiết kế nhận diện nhưng cho phép màu nhìn thấy đổi theo nguồn sáng, phơi sáng và vật liệu. Phân biệt giữ vật thật với giữ pixel cùng mã.

**Cách làm:**

1. Chọn vật chuẩn và ảnh tham chiếu trong từng điều kiện.
2. So các shot gần nhau trước khi chỉnh tổng thể.
3. Đánh dấu chuyển màu phục vụ thời gian/câu chuyện thay vì sửa phẳng.

**Đánh đổi:** Ép một màu tuyệt đối dưới mọi nguồn sáng có thể phá cảm giác vật lý.

**Kiểm tra:**

- Áo vẫn nhận ra đúng thiết kế dù sáng/tối thay đổi hợp lý.
- Không có cú nhảy tông vô cớ ở điểm cắt hoặc trong shot.

**Ví dụ tự biên soạn:** Cùng áo ở sân nắng và trong bếp có biểu hiện khác nhưng không thành áo mới.

**Phản ví dụ / giới hạn:** Thay đổi bảng màu có thể là dụng ý chuyển trạng thái nếu được tổ chức rõ.

**Liên quan:** [LI-005](../kien-thuc/LI-005.json), [CO-006](../kien-thuc/CO-006.json), [QC-001](../kien-thuc/QC-001.json)

**Nguồn đối chiếu:** [B003](../../bai-hoc/003-khoa-thiet-ke-nhan-vat/README.md), [B020](../../bai-hoc/020-nam-chia-khoa-nhat-quan/README.md), [B023](../../bai-hoc/023-negative-prompt/README.md)

[Bản JSON chuẩn](../kien-thuc/CO-005.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="co-006"></a>
## CO-006 — Quản lý màu, sửa cân bằng và tạo phong cách

**Phiên bản mục:** 1.2.1

**Câu hỏi quyết định:** Tệp và hệ hiển thị đang được diễn giải đúng chưa?

**Dùng khi:** Chọn và kiểm quy trình màu tổng thể khi ghép nguồn hoặc xuất khác bản duyệt; miền dữ liệu xem CO-009, thao tác khớp shot xem CO-008.

**Nguyên lý thực hành:** Tách ba công việc: hiểu đúng dữ liệu đầu vào/đầu ra, cân khớp kỹ thuật và tạo phong cách. Ghi chuỗi biến đổi, tránh gán Log/HDR/LUT theo vẻ hình hoặc áp lặp; kiểm tệp xuất trong điều kiện xem dự kiến.

**Cách làm:**

1. Ghi metadata/tài liệu nguồn và điều chưa biết; dùng CO-009 nếu chưa xác định miền dữ liệu.
2. Chọn chuỗi đầu vào→không gian làm việc→look→đầu ra phù hợp phần mềm; ghi từng biến đổi có thật.
3. Cân khớp qua CO-008 rồi tạo phong cách; mở lại bản xuất và đối chiếu bản duyệt.

**Đánh đổi:** Biến đổi lặp hoặc LUT sai đầu vào có thể làm sai tương phản và màu.

**Kiểm tra:**

- Tệp xuất được mở lại để so với bản duyệt.
- Không hứa LUT hay từ khóa 8K sửa mọi lỗi hoặc tạo thêm chi tiết thật.
- Có thể truy ngược mỗi transform/LUT và không bị áp hai lần.

**Ví dụ tự biên soạn:** Hai clip khác nguồn cần kiểm cách phần mềm hiểu màu trước khi kéo thanh cho giống.

**Phản ví dụ / giới hạn:** Một LUT sáng tạo có thể hữu ích nếu đúng đầu vào, nhưng không thay cân từng shot.

**Liên quan:** [AI-007](../kien-thuc/AI-007.json), [QC-001](../kien-thuc/QC-001.json), [LI-004](../kien-thuc/LI-004.json), [CO-007](../kien-thuc/CO-007.json), [CO-008](../kien-thuc/CO-008.json), [CO-009](../kien-thuc/CO-009.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Nguồn AI khác quay thật ở dữ liệu có thể còn lại, nên không mặc định quy trình camera Log.

**Tình huống:** Clip AI và clip quay thật có vẻ đều phẳng nhưng tài liệu đầu vào khác nhau.

**Phần phải giữ:** Mục tiêu và các phần đã duyệt trong tình huống.

| Phương án | Thực hiện |
| --- | --- |
| A | Áp cùng camera LUT vì cả hai trông phẳng. |
| B | Xác minh từng encoding rồi chọn biến đổi đúng trước khi cân. |

**Cách chọn:** Chọn B; vẻ phẳng không xác nhận Log.

**Dấu hiệu kiểm trong ca:**

- Có thể truy ngược mỗi transform/LUT và không bị áp hai lần.

**Nếu gặp:** LUT khiến hình vỡ vùng sáng và quá tương phản.

Có thể do: Sai miền đầu vào hoặc biến đổi lặp.

Thử tiếp: Tắt từng bước, đối chiếu metadata/tài liệu nguồn và so ở môi trường xem kiểm soát.

**Phát biểu được đối chiếu:** Biến đổi màu có vai trò đầu vào/đầu ra khác nhau, không áp tùy ý cho mọi encoding. Nguồn: [SRC-ACES-WORKFLOW](https://docs.acescentral.com/background/overview/).

**Giới hạn nguồn:** Không chứng minh một clip AI là Log/RAW/ACES, không phục hồi dữ liệu đã mất và không buộc mọi dự án dùng ACES.
**Nguồn đối chiếu:** [B022](../../bai-hoc/022-veo-tu-co-ban-den-quy-trinh/README.md), [SRC-BMD-TRAINING](https://www.blackmagicdesign.com/products/davinciresolve/training), [SRC-ACES-WORKFLOW](https://docs.acescentral.com/background/overview/), [SRC-YT-ENCODE](https://support.google.com/youtube/answer/1722171)

[Bản JSON chuẩn](../kien-thuc/CO-006.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="co-007"></a>
## CO-007 — Cân bằng trắng, ám xanh–hồng và nguồn sáng pha trộn

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Sai màu này thuộc nhận diện nguồn, cân bằng trắng hay một lựa chọn tạo hình?

**Dùng khi:** Nối clip khác nguồn, da/vật đổi màu vô cớ, hai phía khuôn mặt chịu ánh khác nhau.

**Nguyên lý thực hành:** Cân bằng trắng liên quan cách hệ thống diễn giải màu ánh sáng; trục nhiệt màu không mô tả hết mọi ám màu, còn có trục xanh lá–hồng tím. Nguồn pha trộn có thể chiếu các vùng khác nhau; một thao tác toàn ảnh không luôn sửa được mọi vùng cùng lúc.

**Cách làm:**

1. Ghi nguồn chính, nguồn phụ, bề mặt hắt và màu cần nhận diện. Chọn giữ cảm giác ấm/lạnh có chủ ý thay vì tự trung hòa tất cả.
2. Với quay thật, kiểm vật trung tính và ánh sáng ở vị trí sử dụng; với clip AI giữ một mốc nhận diện và phân biệt màu vật với màu chiếu lên vật.
3. Sửa nhận diện/thiết lập đầu vào trước, rồi cân toàn ảnh và vùng cục bộ nếu cần. Kiểm liên tục trong shot, tránh tự cân theo từng frame làm màu bơm nhấp nháy.

**Đánh đổi:** Trung hòa mọi nguồn có thể mất cảm giác nơi chốn; giữ màu pha có thể khó nối hoặc ảnh hưởng khả năng đọc vật.

**Kiểm tra:**

- Vật vẫn nhận ra đúng thiết kế dưới điều kiện sáng đã thiết lập.
- Không dùng một số Kelvin làm bảo đảm da hoặc nguyên liệu chính xác.

**Ví dụ tự biên soạn:** Ánh cửa sổ mát và đèn bàn ấm cùng hiện diện: giữ quan hệ nếu có lý do; sửa ám lục bất thường riêng thay vì kéo toàn cảnh về cam.

**Phản ví dụ / giới hạn:** Không thể suy chính xác nhiệt màu nguồn hoặc cân bằng trắng máy từ một ảnh đã qua tạo màu.

**Liên quan:** [CO-005](../kien-thuc/CO-005.json), [CO-006](../kien-thuc/CO-006.json), [LI-001](../kien-thuc/LI-001.json), [LI-005](../kien-thuc/LI-005.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Cảm giác màu là quan hệ nguồn–vật–xử lý–màn hình. Chẩn đoán đúng tầng giúp tránh sửa màu vật thể để bù một lỗi biến đổi hoặc ánh sáng.

**Tình huống:** Ánh cửa sổ mát và đèn bàn ấm cùng hiện diện: giữ quan hệ nếu có lý do; sửa ám lục bất thường riêng thay vì kéo toàn cảnh về cam.

**Phần phải giữ:** Quan hệ cửa sổ mát và đèn ấm nếu đã duyệt. Nhận diện màu vật.

| Phương án | Thực hiện |
| --- | --- |
| A | Áp cùng Kelvin/LUT lên mọi clip và coi đã khớp. |
| B | Xác định quan hệ sáng cần giữ, kiểm đầu vào rồi cân clip theo mốc phù hợp. |

**Cách chọn:** Chọn B khi các clip đến từ nhiều nguồn; số giống nhau không chứng minh hình hiển thị giống nhau.

**Dấu hiệu kiểm trong ca:**

- Vật vẫn nhận ra đúng thiết kế dưới điều kiện sáng đã thiết lập.
- Không dùng một số Kelvin làm bảo đảm da hoặc nguyên liệu chính xác.

**Nếu gặp:** Sửa phía mặt này thì phía kia sai hoặc màu nhấp nháy.

Có thể do: Nguồn pha trộn. Tự cân theo thời gian. Biến đổi màu đầu vào sai.

Thử tiếp: Khóa một mốc kiểm, so từng vùng và đường thời gian; kiểm cách phần mềm hiểu tệp trước khi tăng chỉnh sáng tạo.

**Phát biểu được đối chiếu:** Manual mô tả hai trục tinh chỉnh trắng: amber–blue và green–magenta. Nguồn: [SRC-NIKON-WB](https://www.nikonusa.com/pdf/manuals/dslr/D600_EN.pdf).

**Giới hạn nguồn:** Không chứng minh một giá trị Kelvin sửa mọi nguồn pha trộn hoặc là số đo của clip đã qua grade.
**Nguồn đối chiếu:** [SRC-NIKON-WB](https://www.nikonusa.com/pdf/manuals/dslr/D600_EN.pdf), [SRC-ACES-WORKFLOW](https://docs.acescentral.com/background/overview/)

[Bản JSON chuẩn](../kien-thuc/CO-007.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="co-008"></a>
## CO-008 — Khớp shot trước, tạo phong cách sau và kiểm bằng mắt lẫn công cụ

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Cần sửa chênh giữa các clip hay tạo một vẻ chung cho phim?

**Dùng khi:** Phim nhiều clip AI khác nguồn, màu không liền hoặc một LUT làm mất chi tiết.

**Nguyên lý thực hành:** Tách việc hiểu đúng dữ liệu, cân và khớp các shot khỏi việc tạo phong cách. Dùng waveform, RGB parade, vectorscope theo đúng thiết lập để kiểm tín hiệu; công cụ không tự quyết định cảm xúc hoặc mức đẹp.

**Cách làm:**

1. Xác minh đầu vào/đầu ra và tránh biến đổi lặp. Chọn shot tham chiếu phù hợp điều kiện sáng, không nhất thiết ép mọi cảnh về cùng một shot.
2. Cân mức sáng/đen và quan hệ màu cần nhận diện; kiểm cạnh điểm cắt, vùng sáng/tối quan trọng và thời gian trong clip trước khi thêm look.
3. Thêm phong cách ở mức bảo vệ vật liệu và thông tin chính; so bypass ở độ sáng cảm nhận tương đương, xuất thử và mở lại đúng môi trường.

**Đánh đổi:** Khớp tuyệt đối có thể xóa thay đổi ngày/đêm hoặc nguồn sáng có ý nghĩa; cần nhất quán quan hệ chứ không đồng nhất mọi pixel.

**Kiểm tra:**

- Không có bước nhảy sáng/màu ngoài ý đồ ở điểm cắt.
- Look không làm mất điểm tiếp xúc, vật liệu hoặc dấu kết quả cần xem.

**Ví dụ tự biên soạn:** Hai góc của cùng căn phòng lệch xanh: kiểm cách đọc màu và cân shot trước; sau đó mới thêm bảng màu ấm chung ở mức vừa đủ.

**Phản ví dụ / giới hạn:** Đường da trên vectorscope là điểm tham khảo tín hiệu, không là một góc bắt buộc cho mọi màu da, ánh sáng và phong cách.

**Liên quan:** [CO-003](../kien-thuc/CO-003.json), [CO-005](../kien-thuc/CO-005.json), [CO-006](../kien-thuc/CO-006.json), [CO-009](../kien-thuc/CO-009.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Nếu sai khác kỹ thuật chưa được sửa, một look chung có thể khuếch đại sai khác. Thứ tự kiểm giúp phân biệt lỗi tín hiệu với chủ ý thẩm mỹ.

**Tình huống:** Hai góc của cùng căn phòng lệch xanh: kiểm cách đọc màu và cân shot trước; sau đó mới thêm bảng màu ấm chung ở mức vừa đủ.

**Phần phải giữ:** Cùng điều kiện xem hai góc. Chi tiết vật liệu và điểm tiếp xúc.

| Phương án | Thực hiện |
| --- | --- |
| A | Tăng saturation cho cả phim để che hai shot lệch nhau. |
| B | Khớp hai shot trong điều kiện xem thống nhất rồi thử phong cách chung. |

**Cách chọn:** Chọn B nếu lỗi là lệch liên tục; A chỉ xét khi mức bão hòa là ý đồ đã duyệt sau bước cân.

**Dấu hiệu kiểm trong ca:**

- Không có bước nhảy sáng/màu ngoài ý đồ ở điểm cắt.
- Look không làm mất điểm tiếp xúc, vật liệu hoặc dấu kết quả cần xem.

**Nếu gặp:** Clip riêng đẹp nhưng khi cắt nối thì rất gắt.

Có thể do: Chênh mức sáng hoặc trung tính. Biến đổi khác nhau. Look làm lệch vật liệu giữa shot.

Thử tiếp: So cặp frame ở điểm cắt và xem lại chuyển động; tạm tắt look để tìm tầng xuất hiện chênh.
**Nguồn đối chiếu:** [SRC-ACES-WORKFLOW](https://docs.acescentral.com/background/overview/), [SRC-BMD-TRAINING](https://www.blackmagicdesign.com/products/davinciresolve/training)

[Bản JSON chuẩn](../kien-thuc/CO-008.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="co-009"></a>
## CO-009 — Dữ liệu theo cảnh và hình đã hiển thị: tránh gán nhầm Log/RAW cho AI

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Tệp này còn mang dữ liệu theo cảnh hay đã được dựng vẻ để hiển thị?

**Dùng khi:** Dùng ACES, LUT, nhiều nguồn AI/quay thật/CGI hoặc xuất SDR/HDR.

**Nguyên lý thực hành:** Quy trình màu cần nhận diện đúng dữ liệu đầu vào, không đoán theo vẻ phẳng hoặc chữ “cinematic”. ACES dùng biến đổi đầu vào và đầu ra trong một hệ quản lý; nó không tự biến clip AI đã hoàn thiện thành dữ liệu máy quay gốc hay khôi phục phần đã mất.

**Cách làm:**

1. Lập danh sách cho từng nguồn: container/codec, tag màu, tài liệu xuất và những điều chưa biết. Vẻ hình chỉ là manh mối, không thay metadata và nguồn cung cấp.
2. Chọn quy trình đủ dùng và ghi chuỗi biến đổi. Clip đã mang look hiển thị không tự nhận camera Log transform chỉ vì muốn grade sâu.
3. Khi cần giao nhiều chuẩn hiển thị, kiểm cả biến đổi đầu ra và bản xem lại; với YouTube SDR đối chiếu hướng dẫn đầu ra hiện hành và không gắn nhãn HDR cho nội dung chỉ được tăng sáng.

**Đánh đổi:** Quy trình quản lý đầy đủ tăng khả năng kiểm nhưng có thể quá phức tạp cho nguồn đơn giản; sai transform có thể tệ hơn việc grade trong một quy trình SDR rõ ràng.

**Kiểm tra:**

- Mỗi biến đổi có đầu vào/đầu ra được ghi.
- Không áp trùng LUT/transform hoặc báo “phục hồi RAW” khi chỉ có clip đã xuất.

**Ví dụ tự biên soạn:** Một clip AI SDR và một clip quay Log: xác minh từng nguồn, đưa qua cách xử lý phù hợp rồi mới cân khớp; không dùng cùng LUT máy quay cho cả hai.

**Phản ví dụ / giới hạn:** Thiếu metadata phải ghi chưa chắc và thử có đối chiếu; không tự suy model sinh video xuất ACES hay Log.

**Liên quan:** [CO-006](../kien-thuc/CO-006.json), [CO-007](../kien-thuc/CO-007.json), [CO-008](../kien-thuc/CO-008.json), [AI-013](../kien-thuc/AI-013.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Biến đổi kỹ thuật có miền đầu vào. Dùng sai miền có thể đổi tương phản/màu theo cách không mong muốn; cảm giác chuyên nghiệp đến từ quy trình đúng và kiểm đầu ra, không từ tên hệ màu.

**Tình huống:** Một clip AI SDR và một clip quay Log: xác minh từng nguồn, đưa qua cách xử lý phù hợp rồi mới cân khớp; không dùng cùng LUT máy quay cho cả hai.

**Phần phải giữ:** Bản gốc và metadata từng nguồn. Chuỗi biến đổi có thể truy lại.

| Phương án | Thực hiện |
| --- | --- |
| A | Gán camera Log cho clip phẳng rồi thêm LUT chuyển Rec.709. |
| B | Kiểm thông tin nguồn; nếu là hình đã render thì dùng cách quản lý phù hợp và ghi giới hạn dữ liệu. |

**Cách chọn:** Chọn B khi không có bằng chứng về encoding theo máy quay; chỉ dùng A khi định dạng đó được xác minh.

**Dấu hiệu kiểm trong ca:**

- Mỗi biến đổi có đầu vào/đầu ra được ghi.
- Không áp trùng LUT/transform hoặc báo “phục hồi RAW” khi chỉ có clip đã xuất.

**Nếu gặp:** Hình bị tương phản hoặc saturation quá mạnh ngay khi bật transform.

Có thể do: Gán nhầm đầu vào. Biến đổi lặp. Tag đầu ra/ứng dụng xem khác nhau.

Thử tiếp: Tạm bỏ từng biến đổi theo chuỗi, so với tệp nguồn ở môi trường được kiểm và ghi điểm bắt đầu sai.

**Phát biểu được đối chiếu:** Hệ ACES có các biến đổi phù hợp miền đầu vào và chuẩn bị đầu ra hiển thị. Nguồn: [SRC-ACES-WORKFLOW](https://docs.acescentral.com/background/overview/).

**Giới hạn nguồn:** Không chứng minh một clip AI là Log/RAW/ACES, không phục hồi dữ liệu đã mất và không buộc mọi dự án dùng ACES.
**Nguồn đối chiếu:** [SRC-ACES-WORKFLOW](https://docs.acescentral.com/background/overview/), [SRC-YT-ENCODE](https://support.google.com/youtube/answer/1722171)

[Bản JSON chuẩn](../kien-thuc/CO-009.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).
