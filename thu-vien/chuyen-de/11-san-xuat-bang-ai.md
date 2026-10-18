# AI — Sản xuất bằng AI

Phiên bản 1.3.1. Chuyển ý đồ thành đầu vào, kiểm kết quả và chọn cách sửa.

[Mục lục](../README.md) · [Chuẩn ra quyết định](../03_RA_QUYET_DINH.md)

Mỗi mục dưới là hướng dẫn có điều kiện. Tác dụng cảm xúc là giả thuyết thiết kế; chưa có thử tạo video hoặc kiểm nghiệm khán giả cho các ví dụ mới. Thuật ngữ xem [từ điển](../TU_DIEN.md).

| Mã | Quyết định | Mức |
| --- | --- | --- |
| [AI-001](#ai-001) | Chọn chế độ tạo theo thông tin cần giữ | co_ban |
| [AI-002](#ai-002) | Phân quyền tham chiếu và giữ liên tục | trung_cap |
| [AI-003](#ai-003) | Hợp đồng hành động: đầu, tiếp xúc, biến đổi, cuối | trung_cap |
| [AI-004](#ai-004) | Chia nhiệm vụ sinh và dựng phim | trung_cap |
| [AI-005](#ai-005) | Nối dài, ảnh cuối và điểm nối | nang_cao |
| [AI-006](#ai-006) | Thoại và âm AI: kiểm từng loại lỗi | nang_cao |
| [AI-007](#ai-007) | Câu lệnh, thiết lập và hồ sơ năng lực mô hình | trung_cap |
| [AI-008](#ai-008) | Sửa ít nhất, giữ phần đạt và chọn hậu kỳ | nang_cao |
| [AI-009](#ai-009) | Tiền kỳ bằng bản dựng sơ trước khi tạo hàng loạt | trung_cap |
| [AI-010](#ai-010) | Sổ trạng thái và tài sản dùng chung giữa các shot | trung_cap |
| [AI-011](#ai-011) | Kiểm tính khả thi của ảnh tham chiếu trước khi viết thêm prompt | trung_cap |
| [AI-012](#ai-012) | Chia việc giữa sinh hình và hậu kỳ để sửa đúng tầng | nang_cao |
| [AI-013](#ai-013) | Hiệu chỉnh bộ điều khiển theo model, chế độ và phiên bản thực tế | nang_cao |

<a id="ai-001"></a>
## AI-001 — Chọn chế độ tạo theo thông tin cần giữ

**Phiên bản mục:** 1.0.0

**Câu hỏi quyết định:** Đầu vào nào đã đủ quyết định hình, chuyển động và âm?

**Dùng khi:** Trước khi chọn công cụ hoặc viết câu lệnh.

**Nguyên lý thực hành:** Phân biệt tạo từ chữ, ảnh đầu, bộ tham chiếu, video chuyển động, hai khung và chỉnh video. Mỗi chế độ dùng thông tin khác nhau; khả năng phải theo phiên bản/dịch vụ.

**Cách làm:**

1. Lập danh sách điều phải giữ và điều phải tạo mới.
2. Chọn kiểu đầu vào phù hợp, kiểm tính năng thật có.
3. Tách mô tả ý đồ khỏi thông số phải đặt ở giao diện/API.

**Đánh đổi:** Nhiều tham chiếu có thể bổ sung kiểm soát nhưng cũng mang mâu thuẫn.

**Kiểm tra:**

- Không yêu cầu tính năng chưa xác minh có trong tài khoản.
- Ảnh đầu đủ rõ với hành động có thể bắt đầu từ trạng thái đó.

**Ví dụ tự biên soạn:** Đã duyệt ảnh người và bếp: dùng nó làm nền tạo hình, tập trung chữ vào thao tác mới.

**Phản ví dụ / giới hạn:** Tạo từ chữ vẫn phù hợp cảnh không cần nhận diện cố định.

**Liên quan:** [CA-007](../kien-thuc/CA-007.json), [AI-002](../kien-thuc/AI-002.json), [AI-007](../kien-thuc/AI-007.json)

**Nguồn đối chiếu:** [B022](../../bai-hoc/022-veo-tu-co-ban-den-quy-trinh/README.md), [B026](../../bai-hoc/026-nam-tru-cot-prompt/README.md), [SRC-GOOGLE-I2V](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/best-practice)

[Bản JSON chuẩn](../kien-thuc/AI-001.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ai-002"></a>
## AI-002 — Phân quyền tham chiếu và giữ liên tục

**Phiên bản mục:** 1.0.0

**Câu hỏi quyết định:** Ảnh/video nào có quyền quyết định thuộc tính nào?

**Dùng khi:** Khi dùng hồ sơ mặt, vóc dáng, trang phục, cảnh và động tác.

**Nguyên lý thực hành:** Lập bảng quyền tham chiếu để tránh lấy nhầm mặt từ ảnh cảnh hoặc đồ vật từ video dẫn động. Tách điều đã duyệt khỏi biến thể chưa duyệt.

**Cách làm:**

1. Ghi tài sản chuẩn, phiên bản và phạm vi: mặt, thân, áo, cảnh, vật, chuyển động.
2. Giải quyết xung đột tham chiếu trước khi sinh.
3. Lưu ảnh cảnh được duyệt cùng trạng thái người/vật cho các shot liên quan.

**Đánh đổi:** Khóa quá nhiều chi tiết bằng chữ có thể tăng xung đột; vẫn cần xem kết quả.

**Kiểm tra:**

- Một người không thành nhiều bản sao khi đổi vị trí theo thời gian.
- Vật không đổi thiết kế ngoài chủ ý, nhưng được phép đổi ánh sáng/trạng thái vật lý.

**Ví dụ tự biên soạn:** Ảnh hồ sơ quyết định mặt/áo; ảnh cảnh quyết định bàn/bếp; video mẫu chỉ dẫn thao tác.

**Phản ví dụ / giới hạn:** Một ảnh cận mặt không cung cấp đủ mặt sau trang phục hoặc bối cảnh ngoài khung.

**Liên quan:** [DR-005](../kien-thuc/DR-005.json), [LI-005](../kien-thuc/LI-005.json), [CO-005](../kien-thuc/CO-005.json)

**Nguồn đối chiếu:** [B003](../../bai-hoc/003-khoa-thiet-ke-nhan-vat/README.md), [B020](../../bai-hoc/020-nam-chia-khoa-nhat-quan/README.md)

[Bản JSON chuẩn](../kien-thuc/AI-002.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ai-003"></a>
## AI-003 — Hợp đồng hành động: đầu, tiếp xúc, biến đổi, cuối

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** AI phải thể hiện sự thay đổi vật lý nào?

**Dùng khi:** Khi cảnh có tay, dụng cụ, trao vật, đổ/trải/cắt hoặc tác động vật.

**Nguyên lý thực hành:** Viết ai làm gì với vật nào và chuỗi trạng thái cần thấy. Mô tả hành vi có nguyên nhân thay cho nhãn vật lý hoàn hảo. Ghi điều gì đang đỡ/giữ vật và ai có quyền sở hữu ở mỗi pha. Lỗi trạng thái đầu có thể cần sửa ảnh hoặc cách chia shot trước khi sửa câu chữ.

**Cách làm:**

1. Nêu trạng thái đầu và quyền giữ vật.
2. Ghi tiếp xúc, hướng lực hoặc đường đi cần thiết.
3. Nêu trạng thái kết có thể đối chiếu và điều giữ ổn định.
4. Rà tính khả thi ảnh đầu và các mốc tiếp xúc/che lộ; xem tốc độ thường lẫn rà chậm khi tìm lỗi, giữ mục tiêu hành động đã chốt.

**Đánh đổi:** Nhiều tiểu bước có thể quá tải một clip; chia shot khi cần.

**Kiểm tra:**

- Đúng mục tiêu thao tác và không xuyên/nhân đôi/biến mất ở đoạn quan trọng.
- Ghi thiếu dụng cụ hoặc tư thế ngay từ ảnh đầu.
- Vật đổi trạng thái có tác nhân và không có pha treo/xuyên/nhân đôi ngoài ý đồ.

**Ví dụ tự biên soạn:** Gạo rơi từ dụng cụ vào bát và tích trên lớp sẵn có; lượng tăng có nguyên nhân.

**Phản ví dụ / giới hạn:** Một câu một hành động vẫn có thể sai nếu ảnh đầu không có đủ dụng cụ hoặc tư thế.

**Liên quan:** [DR-001](../kien-thuc/DR-001.json), [CO-004](../kien-thuc/CO-004.json), [AI-004](../kien-thuc/AI-004.json), [DR-008](../kien-thuc/DR-008.json), [AI-010](../kien-thuc/AI-010.json), [AI-011](../kien-thuc/AI-011.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Hợp đồng hành động cần trạng thái vào/ra và điểm chuyển lực, không chỉ chuỗi động từ.

**Tình huống:** Người giữ khay hai tay nhưng prompt yêu cầu mở cửa cùng lúc.

**Phần phải giữ:** Mục tiêu và các phần đã duyệt trong tình huống.

| Phương án | Thực hiện |
| --- | --- |
| A | Thêm “chính xác tuyệt đối” nhiều lần. |
| B | Tạo trạng thái có tay rảnh hoặc chia hành động theo kịch bản phù hợp. |

**Cách chọn:** Chọn B khi lỗi thuộc quan hệ đầu; không tự bỏ việc mở cửa nếu đó là mục tiêu.

**Dấu hiệu kiểm trong ca:**

- Vật đổi trạng thái có tác nhân và không có pha treo/xuyên/nhân đôi ngoài ý đồ.

**Nếu gặp:** Tạo nhiều lần vẫn mọc tay hoặc làm đồ biến mất.

Có thể do: Tư thế đầu mâu thuẫn với hành động cần làm.

Thử tiếp: Kiểm điểm đỡ và tay rảnh, thử một thay đổi đầu vào có căn cứ.
**Nguồn đối chiếu:** [B015](../../bai-hoc/015-logic-chuyen-dong-vat-ly/README.md), [B033](../../bai-hoc/033-sua-prompt-bi-bo-qua/README.md), [SRC-GOOGLE-I2V](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/best-practice)

[Bản JSON chuẩn](../kien-thuc/AI-003.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ai-004"></a>
## AI-004 — Chia nhiệm vụ sinh và dựng phim

**Phiên bản mục:** 1.0.0

**Câu hỏi quyết định:** Một lần tạo nên giải quyết phần việc nào?

**Dùng khi:** Khi cảnh phức tạp, nhiều người hoặc nhiều thay đổi.

**Nguyên lý thực hành:** Tách kế hoạch phim khỏi độ dài/chế độ một lần sinh. Chọn đơn vị tạo có mục tiêu kiểm tra được và bộ góc đủ dựng.

**Cách làm:**

1. Lập shot theo chức năng trước khi chia job.
2. Nhóm các hành động liên tục khả thi; tách nhiệm vụ cạnh tranh.
3. Dành phần cắt/nối/nhạc/màu chính xác cho hậu kỳ khi phù hợp.

**Đánh đổi:** Tách nhiều job tăng kiểm soát nhưng tăng công nối và lệch nhận diện.

**Kiểm tra:**

- Mỗi job có tiêu chí đạt và điểm đầu/cuối.
- Không giả định mỗi dòng prompt tự trở thành một shot đúng độ dài.

**Ví dụ tự biên soạn:** Tạo riêng cảnh trung người làm, cận tiếp xúc khó và cảnh kết quả để sửa đúng phần lỗi.

**Phản ví dụ / giới hạn:** Công cụ có thể tạo nhiều shot trong một lần nếu phù hợp; vẫn phải kiểm ranh giới và mạch.

**Liên quan:** [DR-006](../kien-thuc/DR-006.json), [AI-005](../kien-thuc/AI-005.json), [ED-008](../kien-thuc/ED-008.json)

**Nguồn đối chiếu:** [B013](../../bai-hoc/013-tach-shot-hoi-thoai/README.md), [B025](../../bai-hoc/025-dieu-khien-camera/README.md)

[Bản JSON chuẩn](../kien-thuc/AI-004.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ai-005"></a>
## AI-005 — Nối dài, ảnh cuối và điểm nối

**Phiên bản mục:** 1.0.0

**Câu hỏi quyết định:** Cần tiếp tục chuyển động hay chuyển sang một góc/cảnh khác?

**Dùng khi:** Khi làm video dài từ nhiều đoạn.

**Nguyên lý thực hành:** Mở rộng từ video, tạo mới từ ảnh cuối và dựng cut là ba quy trình khác. Ảnh cuối không tự chứa vận tốc hoặc toàn lịch sử chuyển động.

**Cách làm:**

1. Duyệt đoạn gốc và ghi trạng thái cuối.
2. Chọn cách nối theo điều cần bảo toàn và tính năng thật có.
3. Kiểm cả hình, vận tốc, âm và tham chiếu gốc sau mỗi đoạn.

**Đánh đổi:** Nối dài có thể tích lũy lệch; cắt sang góc mới có thể dễ quản lý hơn.

**Kiểm tra:**

- Không có nhảy hình/vận tốc hoặc lặp hành động ngoài ý đồ.
- Không nhân độ dài chuẩn thành số lần sinh chắc chắn dùng được.

**Ví dụ tự biên soạn:** Kết ở tay đang giữ bình thì đoạn sau không được mở bằng bình đã ở bàn nếu không có lược thời gian.

**Phản ví dụ / giới hạn:** Một điểm cắt có chủ ý có thể tốt hơn cố giấu mọi đường nối.

**Liên quan:** [ED-003](../kien-thuc/ED-003.json), [MO-006](../kien-thuc/MO-006.json), [AI-002](../kien-thuc/AI-002.json)

**Nguồn đối chiếu:** [B024](../../bai-hoc/024-xau-chuoi-canh/README.md)

[Bản JSON chuẩn](../kien-thuc/AI-005.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ai-006"></a>
## AI-006 — Thoại và âm AI: kiểm từng loại lỗi

**Phiên bản mục:** 1.3.0

**Câu hỏi quyết định:** Đầu ra sai lời, vai, môi hay âm sự kiện?

**Dùng khi:** Khi clip có âm tích hợp hoặc hội thoại.

**Nguyên lý thực hành:** Chẩn đoán riêng thay vì thêm một khối yêu cầu dài cho mọi lỗi. Giữ hình đạt khi có phương án xử lý âm riêng.

**Cách làm:**

1. Nghe và chép nội dung thực được phát.
2. So vai nói, giọng, môi và sự kiện theo mốc.
3. Chọn sửa lời/giọng/đồng bộ/hậu kỳ hoặc sinh lại đúng shot.
4. Đối chiếu bản âm thật với nội dung mong muốn và lượt nói; nếu thay âm/hậu kỳ, kiểm lại cả hình–âm sau thay, không lấy môi có cử động làm bằng chứng khớp.

**Đánh đổi:** Tạo lại có thể làm mất hình đã đạt; sửa âm có thể khó nếu tách nguồn kém.

**Kiểm tra:**

- Không báo khớp môi chỉ vì người đúng đang mở miệng.
- Không suy có các track riêng khi chỉ nhận một file trộn.

**Ví dụ tự biên soạn:** Mèo và chó bị nhầm lời: xác định vai sai trước; không tự đổi camera đang đúng.

**Phản ví dụ / giới hạn:** Lời kể ngoài khung không cần khớp một miệng đang hiện hình. Với thoại trong hình, đúng chữ và đúng giọng vẫn có thể sai vai hoặc lệch khẩu hình; các tiêu chí ấy cần kiểm riêng.

**Liên quan:** [SO-002](../kien-thuc/SO-002.json), [SO-008](../kien-thuc/SO-008.json), [DR-004](../kien-thuc/DR-004.json)

**Nguồn đối chiếu:** [B027](../../bai-hoc/027-tach-shot-lip-sync/README.md), [B029](../../bai-hoc/029-lip-sync-hoat-hinh/README.md), [B030](../../bai-hoc/030-gan-thoai-dung-nhan-vat/README.md), [B032](../../bai-hoc/032-dieu-khien-am-thanh/README.md)

[Bản JSON chuẩn](../kien-thuc/AI-006.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ai-007"></a>
## AI-007 — Câu lệnh, thiết lập và hồ sơ năng lực mô hình

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Điều gì nên viết, điều gì phải đặt và điều gì chưa biết?

**Dùng khi:** Khi đổi mô hình, dịch vụ hoặc phiên bản.

**Nguyên lý thực hành:** Giữ ý đồ điện ảnh chung, rồi chuyển sang cách nhập đúng công cụ. Mã khóa tự đặt không trở thành tham số kỹ thuật. Tài liệu có ngày và phạm vi chỉ xác nhận cách công cụ được mô tả, chưa chứng minh mức tuân thủ trên bài thực tế. Thông số máy quay trong chữ có thể chỉ là mô tả vẻ hình.

**Cách làm:**

1. Ghi nhà cung cấp, tên/mã mô hình, chế độ và ngày kiểm.
2. Phân loại điều khiển bằng chữ, thiết lập, tham chiếu, hậu kỳ hoặc chưa hỗ trợ.
3. Đối chiếu tài liệu và giao diện khi có khác biệt; để null cho giới hạn chưa rõ.
4. Lưu model/version/chế độ/thiết lập và một thử rủi ro phù hợp trước khi tái dùng adapter cho cả dự án.

**Đánh đổi:** Prompt dùng chung dễ mang cú pháp sai; adapter riêng cần được cập nhật.

**Kiểm tra:**

- Không coi no/don't hoặc negative là cú pháp chung.
- Không dùng HEX, 8K hay 3% rung làm bảo đảm đầu ra.
- Không gán ảnh cuối, seed, tham chiếu hoặc câu phủ định khả năng khóa tuyệt đối chưa được kiểm.

**Ví dụ tự biên soạn:** Veo ở trường negative được tài liệu hướng dẫn liệt kê yếu tố; Gen-4 của Runway khuyên mô tả khẳng định.

**Phản ví dụ / giới hạn:** Có thể giữ cấu trúc lập ý giống nhau nhưng cách nhập của từng chế độ khác.

**Liên quan:** [EV-006](../kien-thuc/EV-006.json), [AI-001](../kien-thuc/AI-001.json), [QC-004](../kien-thuc/QC-004.json), [AI-013](../kien-thuc/AI-013.json), [MO-007](../kien-thuc/MO-007.json), [CA-012](../kien-thuc/CA-012.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Prompt, giao diện dịch vụ và kết quả thực cần ba lớp ghi nhận khác nhau.

**Tình huống:** Dịch vụ có ô seed và ảnh cuối nhưng chưa thử chuyển động.

**Phần phải giữ:** Mục tiêu và các phần đã duyệt trong tình huống.

| Phương án | Thực hiện |
| --- | --- |
| A | Báo nhân vật và quỹ đạo được khóa. |
| B | Ghi điều khiển có thật, thử và báo mức sai lệch của kết quả. |

**Cách chọn:** Chọn B; có nút không đồng nghĩa kiểm soát chính xác mọi biến.

**Dấu hiệu kiểm trong ca:**

- Không gán ảnh cuối, seed, tham chiếu hoặc câu phủ định khả năng khóa tuyệt đối chưa được kiểm.

**Nếu gặp:** Cùng seed nhưng bản sau vẫn đổi chi tiết khi sửa đầu vào.

Có thể do: Seed bị hiểu như khóa mọi yếu tố độc lập.

Thử tiếp: Kiểm cấu hình, thay một biến nếu có thể và so các take theo cùng tiêu chí.
**Nguồn đối chiếu:** [B023](../../bai-hoc/023-negative-prompt/README.md), [B026](../../bai-hoc/026-nam-tru-cot-prompt/README.md), [SRC-GOOGLE-PROMPT](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/video-gen-prompt-guide), [SRC-RUNWAY-GEN4](https://help.runwayml.com/hc/en-us/articles/39789879462419-Gen-4-Video-Prompting-Guide)

[Bản JSON chuẩn](../kien-thuc/AI-007.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ai-008"></a>
## AI-008 — Sửa ít nhất, giữ phần đạt và chọn hậu kỳ

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Cách sửa nào ít làm hỏng phần đang đúng?

**Dùng khi:** Khi user chỉ yêu cầu sửa một lỗi hoặc clip gần đạt.

**Nguyên lý thực hành:** Lưu bản gốc, ghi phần phải giữ và thay đúng nhóm liên quan. Sinh lại là lần tạo mới; không hứa giữ tuyệt đối chi tiết đã duyệt. Khi nhiều lần thử không cải thiện đúng lỗi, xem lại đầu vào, khả năng công cụ và công đoạn sửa; giữ danh sách phần đạt để tránh biến sửa lỗi thành đổi mục tiêu.

**Cách làm:**

1. Phân loại lỗi nội dung, chuyển động, liên tục, âm hoặc đầu ra.
2. Chọn cắt/crop/âm/màu/chỉnh có vùng hoặc tạo lại theo tính năng thật.
3. Ghi khác biệt câu lệnh và xem lại toàn clip sau sửa.
4. Mỗi lượt nêu giả thuyết, biến đổi, tiêu chí giữ/sửa và kết quả; nếu chưa có clip mới chỉ báo đề xuất, không báo đã khắc phục.

**Đánh đổi:** Sửa cục bộ có thể tiết kiệm nhưng để lại dấu; tạo mới có thể sạch hơn nhưng đổi nhiều biến.

**Kiểm tra:**

- Sửa người thừa không tự đổi hành động, thời gian hay phong cách.
- Bản sau được đối chiếu cùng tiêu chí như bản gốc.
- Sau sửa phải kiểm cả lỗi mục tiêu và phần cần bảo vệ trên toàn khoảng liên quan.

**Ví dụ tự biên soạn:** Giữ timelapse đã tốt, chỉ chỉnh mô tả một người và kiểm các đoạn chuyển vị trí.

**Phản ví dụ / giới hạn:** Nếu ảnh đầu sai tư thế khiến thao tác bất khả thi, sửa ảnh đầu có thể cần hơn thêm câu.

**Liên quan:** [QC-002](../kien-thuc/QC-002.json), [AI-003](../kien-thuc/AI-003.json), [MO-006](../kien-thuc/MO-006.json), [AI-011](../kien-thuc/AI-011.json), [AI-012](../kien-thuc/AI-012.json), [AI-013](../kien-thuc/AI-013.json), [QC-009](../kien-thuc/QC-009.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Sửa tối thiểu còn cần điều kiện dừng để tránh lặp vô hạn bằng câu chữ.

**Tình huống:** Clip timelapse tốt nhưng có người thừa.

**Phần phải giữ:** Mục tiêu và các phần đã duyệt trong tình huống.

| Phương án | Thực hiện |
| --- | --- |
| A | Viết lại toàn bộ phong cách và chuyển sang chuyển động chậm. |
| B | Giữ timelapse/hành động, sửa đúng nhận diện/số người; nếu không đạt thì so công cụ sửa khác. |

**Cách chọn:** Chọn B theo yêu cầu hiện hành; số lần thử phụ thuộc giả thuyết và ngân sách, không một định mức cố định.

**Dấu hiệu kiểm trong ca:**

- Sau sửa phải kiểm cả lỗi mục tiêu và phần cần bảo vệ trên toàn khoảng liên quan.

**Nếu gặp:** Sửa lỗi người thừa xong mất động tác đúng.

Có thể do: Prompt bị đổi nhiều biến và không có phiếu phần phải giữ.

Thử tiếp: So bản trước/sau theo hai cột lỗi cần sửa và yếu tố cần bảo vệ.
**Nguồn đối chiếu:** [B004](../../bai-hoc/004-nano-banana-pro/README.md), [B033](../../bai-hoc/033-sua-prompt-bi-bo-qua/README.md)

[Bản JSON chuẩn](../kien-thuc/AI-008.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ai-009"></a>
## AI-009 — Tiền kỳ bằng bản dựng sơ trước khi tạo hàng loạt

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Câu chuyện và thời lượng có hoạt động trước khi đầu tư vào clip đẹp không?

**Dùng khi:** Phim nhiều shot, nhiều model, ngân sách tạo có hạn hoặc kịch bản chưa chắc.

**Nguyên lý thực hành:** Dùng storyboard/bản dựng ảnh có thời gian và âm tạm để kiểm tiến trình, khả năng hiểu và nhịp trước khi sinh hàng loạt. Bản dựng sơ kiểm cấu trúc, không chứng minh chất lượng chuyển động hoặc phản ứng thật của khán giả.

**Cách làm:**

1. Chuyển kịch bản thành các nhịp thay đổi và shot có chức năng, đặt ảnh phác/ảnh giữ chỗ cùng thời lượng dự kiến, lời/âm tạm nếu cần.
2. Kiểm lời hứa–mở–phát triển–kết quả, chỗ thiếu coverage và độ dài đọc/làm việc. Tạo thử shot khó có ảnh hưởng cấu trúc trước, không cần mọi cảnh đẹp mới xem mạch.
3. Sau duyệt sơ, lập danh sách tài sản/job và phần cần dự phòng; cập nhật bản dựng theo take đạt thay vì kéo mọi clip đủ thời lượng sinh sẵn.

**Đánh đổi:** Tiền kỳ thêm công ban đầu nhưng giảm sinh lại; ảnh đứng có thể đánh lừa về tính khả thi của hành động liên tục.

**Kiểm tra:**

- Mỗi shot có chức năng và liên hệ với nhịp.
- Rủi ro chuyển động/tiếp xúc có thử riêng hoặc còn được ghi chưa biết.

**Ví dụ tự biên soạn:** Một phim về sửa đồ được dựng bằng sáu ảnh và âm tạm để kiểm thấy hỏng→thử→sửa→dùng; chỉ sau đó mới quyết định cần bao nhiêu take khó.

**Phản ví dụ / giới hạn:** Một phim ứng tác hoặc quay quan sát có thể phát triển cấu trúc khi dựng; vẫn có thể dùng bản sơ ở giai đoạn phù hợp, không ép khóa trước mọi thứ.

**Liên quan:** [ST-003](../kien-thuc/ST-003.json), [DR-006](../kien-thuc/DR-006.json), [AI-004](../kien-thuc/AI-004.json), [QC-005](../kien-thuc/QC-005.json), [QC-007](../kien-thuc/QC-007.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Tách rủi ro cấu trúc khỏi rủi ro sinh hình giúp phát hiện lỗi bằng cách rẻ hơn. Bản sơ là công cụ ra quyết định, không là mẫu chuyển động đã được kiểm.

**Tình huống:** Một phim về sửa đồ được dựng bằng sáu ảnh và âm tạm để kiểm thấy hỏng→thử→sửa→dùng; chỉ sau đó mới quyết định cần bao nhiêu take khó.

**Phần phải giữ:** Trục hỏng→thử→sửa→dùng. Chưa gán chuyển động đạt từ ảnh sơ.

| Phương án | Thực hiện |
| --- | --- |
| A | Tạo hết các shot ở chất lượng cao rồi mới ghép lần đầu. |
| B | Dựng sơ bằng ảnh/âm tạm, thử hành động khó trước, rồi tạo theo danh sách có mục tiêu. |

**Cách chọn:** Chọn B khi cấu trúc còn chưa rõ hoặc chi phí sinh đáng kể; A chỉ hợp khi cấu trúc đã được kiểm bằng đầu vào khác.

**Dấu hiệu kiểm trong ca:**

- Mỗi shot có chức năng và liên hệ với nhịp.
- Rủi ro chuyển động/tiếp xúc có thử riêng hoặc còn được ghi chưa biết.

**Nếu gặp:** Có nhiều clip đẹp nhưng thiếu cảnh nối và phải tạo lại nhiều.

Có thể do: Chưa kiểm mạch toàn phim. Danh sách tạo không gắn với bằng chứng cần cho nhịp.

Thử tiếp: Ghép bản sơ từ tài sản có sẵn; đánh dấu thiếu thông tin trước khi đặt thêm job.
**Nguồn đối chiếu:** [SRC-YALE-EDIT](https://filmanalysis.yale.edu/editing/), [SRC-GOOGLE-I2V](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/best-practice)

[Bản JSON chuẩn](../kien-thuc/AI-009.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ai-010"></a>
## AI-010 — Sổ trạng thái và tài sản dùng chung giữa các shot

**Phiên bản mục:** 1.3.0

**Câu hỏi quyết định:** Điều gì phải ổn định, điều gì được phép thay đổi ở lần xuất hiện tiếp theo?

**Dùng khi:** Nhân vật/đồ vật/bối cảnh trở lại, đổi góc hoặc nối nhiều công đoạn.

**Nguyên lý thực hành:** Quản lý nhận diện và trạng thái theo sự kiện, không khóa mọi thứ bất biến. Thiết kế có thể giữ ổn định trong khi mức đầy, độ ướt, vị trí, người giữ và ánh sáng thay đổi có nguyên nhân.

**Cách làm:**

1. Cấp mã tài sản và chọn tham chiếu có thẩm quyền cho mặt/đồ/không gian. Ghi phiên bản, vai trò tham chiếu và những thuộc tính phải giữ.
2. Cho mỗi shot ghi trạng thái vào, hành động đổi trạng thái, trạng thái ra và shot phụ thuộc; lưu người giữ, vị trí, lượng tương đối, dấu sử dụng và những phần chưa biết.
3. Khi đổi take hoặc sửa một tài sản, kiểm các shot liên quan thay vì tự cập nhật toàn bộ ngách. Dùng hình mốc được duyệt khi công cụ thật hỗ trợ.
4. Theo dõi cả trong shot: vật đi sau tay/vật cản phải trở lại với nhận diện và trạng thái còn hợp lý. Che khuất không tự là hành động đổi vật, làm đầy hoặc chuyển chủ.
5. Ghi thay đổi có chủ đích cùng tác nhân hoặc khoảng lược: đừng coi mọi khác biệt pixel là lỗi, cũng đừng lấy từ “cinematic” để bỏ qua đổi số lượng/vật thể.

**Đánh đổi:** Ghi quá chi tiết tăng công và có thể gây ràng buộc sai; ưu tiên thuộc tính khán giả dùng để hiểu mạch hoặc nhận diện.

**Kiểm tra:**

- Không có vật tự đầy/sạch/đổi chủ ngoài hành động hoặc lược thời gian rõ.
- Phiên bản tài sản thực được dùng có thể truy ngược.

**Ví dụ tự biên soạn:** Chiếc hộp P01: đầu mở và rỗng, sau người đặt vật A vào, cuối đóng và được khách giữ; màu gỗ giữ thiết kế nhưng đổi sáng theo phòng.

**Phản ví dụ / giới hạn:** Không bắt vật ướt phải giữ cùng biểu hiện màu dưới mọi ánh sáng chỉ để “nhất quán”.

**Liên quan:** [AI-002](../kien-thuc/AI-002.json), [AI-003](../kien-thuc/AI-003.json), [ED-003](../kien-thuc/ED-003.json), [CO-005](../kien-thuc/CO-005.json), [QC-004](../kien-thuc/QC-004.json), [QC-010](../kien-thuc/QC-010.json), [CO-004](../kien-thuc/CO-004.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Cùng một vật không có nghĩa cùng trạng thái. Sổ trạng thái nối ý đồ liên tục với đầu vào tạo và giúp phân biệt lệch nhận diện với biến đổi hợp lý.

**Tình huống:** Chiếc hộp P01: đầu mở và rỗng, sau người đặt vật A vào, cuối đóng và được khách giữ; màu gỗ giữ thiết kế nhưng đổi sáng theo phòng.

**Phần phải giữ:** Mã hộp P01, vật A và người giữ. Thay đổi trạng thái có tác nhân.

| Phương án | Thực hiện |
| --- | --- |
| A | Sao chép một đoạn mô tả dài vào mọi prompt và hy vọng tự khớp. |
| B | Ghi tài sản có mã cùng trạng thái vào/ra theo shot; chọn ảnh tham chiếu đúng vai trò. |

**Cách chọn:** Chọn B khi có chuỗi liên tục; chữ giống nhau không chứng minh kết quả giống nhau.

**Dấu hiệu kiểm trong ca:**

- Không có vật tự đầy/sạch/đổi chủ ngoài hành động hoặc lược thời gian rõ.
- Phiên bản tài sản thực được dùng có thể truy ngược.

**Nếu gặp:** Cảnh sau nhận đúng nhân vật nhưng sai vật hoặc mức hoàn tất.

Có thể do: Chỉ khóa nhận diện, thiếu trạng thái. Take được thay mà không cập nhật phụ thuộc.

Thử tiếp: So chuỗi trạng thái vào/ra của các shot liên quan; sửa đúng take hoặc dấu lược thời gian.
**Nguồn đối chiếu:** [SRC-GOOGLE-I2V](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/best-practice), [SRC-YALE-EDIT](https://filmanalysis.yale.edu/editing/)

[Bản JSON chuẩn](../kien-thuc/AI-010.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ai-011"></a>
## AI-011 — Kiểm tính khả thi của ảnh tham chiếu trước khi viết thêm prompt

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Hành động mong muốn có thể bắt đầu từ tư thế và quan hệ trong ảnh này không?

**Dùng khi:** Image-to-video liên tục lỗi tay, trao vật, mở cửa, đi qua hoặc xoay đồ.

**Nguyên lý thực hành:** Ảnh tham chiếu vừa cung cấp nhận diện vừa đặt trạng thái ban đầu. Nếu điểm đỡ, tay, dụng cụ, khoảng trống hoặc che khuất mâu thuẫn với hành động, thêm chữ có thể không giải được; cần sửa đầu vào hoặc đổi cách chia shot.

**Cách làm:**

1. Kiểm các điểm bắt đầu: tay nào rảnh/giữ gì, dụng cụ thật ở đâu, vật có đường đi không, cửa có khớp quay, khớp người có tư thế khả thi không.
2. Chọn một hành động chính đủ rõ cho job. Nếu ảnh đầu không phù hợp, chuẩn bị ảnh khác/sửa hình bằng công cụ có khả năng hoặc bắt đầu ở pha khác, bảo vệ phần đã duyệt.
3. Thử đoạn khó trước; xem toàn pha che/lộ và tiếp xúc. Nếu lỗi không ổn định, so dàn cảnh khác hoặc tách góc có chức năng thay vì chỉ kéo prompt dài.

**Đánh đổi:** Sửa ảnh có thể lệch nhận diện; đổi góc có thể mất cảm giác liên tục. Cần so chi phí và điều khán giả nhất thiết phải thấy.

**Kiểm tra:**

- Không yêu cầu tay đang ôm đồ thực hiện thêm thao tác bất khả thi.
- Ảnh chỉnh hoặc shot tách vẫn giữ mục tiêu hành động và trạng thái đã chốt.

**Ví dụ tự biên soạn:** Ảnh người giữ khay bằng cả hai tay nhưng cần mở cửa: có thể đặt khay trước, nhờ người khác mở hoặc chuẩn bị tư thế có tay rảnh tùy kịch bản.

**Phản ví dụ / giới hạn:** Model có thể tự bịa một lối giải không có trong ảnh; điều đó không chứng minh đã giữ đúng yêu cầu của dự án.

**Liên quan:** [AI-001](../kien-thuc/AI-001.json), [AI-003](../kien-thuc/AI-003.json), [DR-002](../kien-thuc/DR-002.json), [DR-008](../kien-thuc/DR-008.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Lỗi đầu vào khác lỗi cách diễn đạt. Khi trạng thái đầu không chứa một lối hành động hợp lý, tăng độ chi tiết câu lệnh có thể chỉ thêm mâu thuẫn.

**Tình huống:** Ảnh người giữ khay bằng cả hai tay nhưng cần mở cửa: có thể đặt khay trước, nhờ người khác mở hoặc chuẩn bị tư thế có tay rảnh tùy kịch bản.

**Phần phải giữ:** Việc mang khay và mở cửa theo kịch bản. Nhận diện và tư thế đã duyệt ở phần không sửa.

| Phương án | Thực hiện |
| --- | --- |
| A | Thêm “tay chính xác, vật lý hoàn hảo” nhiều lần. |
| B | Kiểm và sửa tư thế/đường đi hoặc chia nhịp để có tay rảnh trước khi mở. |

**Cách chọn:** Chọn B khi lỗi xuất phát từ quan hệ đầu; A không cung cấp trạng thái còn thiếu.

**Dấu hiệu kiểm trong ca:**

- Không yêu cầu tay đang ôm đồ thực hiện thêm thao tác bất khả thi.
- Ảnh chỉnh hoặc shot tách vẫn giữ mục tiêu hành động và trạng thái đã chốt.

**Nếu gặp:** Mỗi lần tạo lại model mọc tay hoặc làm khay biến mất.

Có thể do: Không có tay rảnh. Vật bị che hoặc không có đường di chuyển.

Thử tiếp: Vẽ lại chuỗi trạng thái đơn giản, thay một điều kiện đầu và kiểm đúng tiếp xúc khó trước.
**Nguồn đối chiếu:** [SRC-GOOGLE-I2V](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/best-practice), [SRC-RUNWAY-GEN4](https://help.runwayml.com/hc/en-us/articles/39789879462419-Gen-4-Video-Prompting-Guide)

[Bản JSON chuẩn](../kien-thuc/AI-011.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ai-012"></a>
## AI-012 — Chia việc giữa sinh hình và hậu kỳ để sửa đúng tầng

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Lỗi này nên tạo lại, sửa vùng, dựng, ghép hay thay âm?

**Dùng khi:** Clip gần đạt, nhiều công cụ hoặc model không làm tốt một chi tiết chính xác.

**Nguyên lý thực hành:** Sản xuất AI là một chuỗi công việc có thể kết hợp sinh, dựng, compositing, màu và âm. Chọn công đoạn sửa theo lỗi và phần cần giữ; khả năng chỉnh cụ thể phải được xác minh trong công cụ thực tế.

**Cách làm:**

1. Phân loại lỗi: cấu trúc, nhận diện, hình học/tiếp xúc, chuyển động, chữ/đồ họa, sáng/màu hoặc âm; xác định lỗi nằm cả shot hay một khoảng/vùng.
2. So phương án theo độ đúng mục tiêu, phần dễ hỏng và chi phí toàn chuỗi. Chữ cần chính xác có thể thêm ở hậu kỳ; âm lệch có thể thay riêng nếu nguồn/công cụ cho phép.
3. Khi ghép/sửa vùng, kiểm mép, che khuất, hướng sáng, bóng, hạt, nhòe và ổn định theo thời gian; xem bản xuất đầy đủ trước khi báo đạt.

**Đánh đổi:** Sửa cục bộ có thể tiết kiệm nhưng tăng công tracking/che mép; tạo lại có thể sạch hơn nhưng làm mất phần hình đã tốt.

**Kiểm tra:**

- Phương án bảo vệ rõ phần đã được duyệt.
- Không tuyên bố có mask/track/stem/inpaint chỉ dựa trên tên model.

**Ví dụ tự biên soạn:** Biển chữ cần đúng trong cảnh đã đẹp: so thêm chữ bằng đồ họa có phối cảnh với sinh lại toàn shot; kiểm chữ có bị vật đi qua che đúng không.

**Phản ví dụ / giới hạn:** Lỗi tiếp xúc mang toàn chuỗi không luôn sửa bằng một frame; vá ảnh đứng có thể tạo nhấp nháy trong video.

**Liên quan:** [AI-008](../kien-thuc/AI-008.json), [SO-008](../kien-thuc/SO-008.json), [CO-006](../kien-thuc/CO-006.json), [QC-002](../kien-thuc/QC-002.json), [QC-005](../kien-thuc/QC-005.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Mỗi công đoạn có khả năng kiểm soát khác nhau. Chọn đúng tầng giảm việc nhờ một model giải mọi vấn đề bằng một lần sinh.

**Tình huống:** Biển chữ cần đúng trong cảnh đã đẹp: so thêm chữ bằng đồ họa có phối cảnh với sinh lại toàn shot; kiểm chữ có bị vật đi qua che đúng không.

**Phần phải giữ:** Hình đạt. Thời điểm và ý nghĩa âm cần thay.

| Phương án | Thực hiện |
| --- | --- |
| A | Sinh lại clip đã đạt chỉ vì một tiếng cửa bị lệch. |
| B | Giữ hình, sửa thời điểm/nguồn âm và duyệt lại quan hệ hình–âm nếu công cụ cho phép. |

**Cách chọn:** Chọn B khi lỗi độc lập ở âm; tạo lại chỉ khi sửa riêng không đạt hoặc có lỗi hình liên quan.

**Dấu hiệu kiểm trong ca:**

- Phương án bảo vệ rõ phần đã được duyệt.
- Không tuyên bố có mask/track/stem/inpaint chỉ dựa trên tên model.

**Nếu gặp:** Sửa một lỗi nhỏ xong xuất hiện nhiều lỗi mới.

Có thể do: Tạo lại toàn bộ mà không cần. Sửa vùng không theo chuyển động/che khuất.

Thử tiếp: So một phương án sửa cục bộ với chi phí/rủi ro tạo lại; đánh giá cả phần được giữ và vùng mới sửa.
**Nguồn đối chiếu:** [SRC-BMD-TRAINING](https://www.blackmagicdesign.com/products/davinciresolve/training), [SRC-GOOGLE-I2V](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/best-practice)

[Bản JSON chuẩn](../kien-thuc/AI-012.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ai-013"></a>
## AI-013 — Hiệu chỉnh bộ điều khiển theo model, chế độ và phiên bản thực tế

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Công cụ nào thật sự điều khiển được yêu cầu này, với mức sai lệch nào?

**Dùng khi:** Đổi model/dịch vụ, cần đường máy/nhân vật/khung cuối chính xác hoặc chuẩn bị sản xuất dài.

**Nguyên lý thực hành:** Tách ý đồ điện ảnh, đầu vào tham chiếu, thiết lập dịch vụ và kết quả đo. Tên model hoặc tài liệu quảng bá không đủ xác nhận một ràng buộc được giữ; cần hồ sơ khả năng theo đúng chế độ và các thử nghiệm nhỏ có ghi nhận.

**Cách làm:**

1. Ghi model/version, nhà cung cấp/chế độ, ngày dùng, đầu vào, thiết lập có thật và đầu ra; không tự coi seed hay ảnh cuối là khóa tuyệt đối.
2. Chọn thử cho rủi ro quan trọng của dự án: nhận diện qua góc, tay chạm, quỹ đạo, che/lộ, chữ hoặc âm. Giữ các biến khác khi điều kiện cho phép và ghi phần không kiểm soát được.
3. Duyệt cả video tốc độ thường, khoảng rủi ro ở tốc độ chậm và tệp xuất. Lưu take không đạt cùng lý do; dùng kết quả để chọn cách chia việc thay vì xếp hạng model chung chung.

**Đánh đổi:** Thử nhiều tiêu chí tốn chi phí; kiểm theo rủi ro dự án, không cần mọi model làm mọi loại bài.

**Kiểm tra:**

- Không biến công bố năng lực thành kết quả thử của tài khoản.
- Một take đẹp không được ghi là tỷ lệ đạt chắc chắn; cả clip được xem trước kết luận chuyển động.

**Ví dụ tự biên soạn:** Cần trao hộp và giữ mặt: thử cùng đầu vào ở chế độ đã xác minh, ghi rõ lỗi chạm và lệch mặt; chọn phương án tạo riêng cận tay nếu cần.

**Phản ví dụ / giới hạn:** Kết quả trên một model/version không tự chuyển sang model mới hoặc dịch vụ trung gian khác.

**Liên quan:** [AI-007](../kien-thuc/AI-007.json), [EV-004](../kien-thuc/EV-004.json), [QC-003](../kien-thuc/QC-003.json), [QC-005](../kien-thuc/QC-005.json), [QC-009](../kien-thuc/QC-009.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Các ràng buộc điện ảnh không luôn trùng với nút điều khiển có trong công cụ. Hồ sơ theo phiên bản nối ý đồ với điều đã thực sự làm được và giữ phần chưa biết.

**Tình huống:** Cần trao hộp và giữ mặt: thử cùng đầu vào ở chế độ đã xác minh, ghi rõ lỗi chạm và lệch mặt; chọn phương án tạo riêng cận tay nếu cần.

**Phần phải giữ:** Cùng bài trao hộp khi so. Đúng model/chế độ và nhật ký đầu vào.

| Phương án | Thực hiện |
| --- | --- |
| A | Chọn model từ bảng xếp hạng rồi mặc định nó làm chính xác mọi shot. |
| B | Thử hành động rủi ro của dự án, ghi sai lệch và chọn công đoạn phù hợp. |

**Cách chọn:** Chọn B khi yêu cầu có tính đặc thù; bảng so sánh chỉ là đầu mối chọn thử, không thay kết quả trên bài thực tế.

**Dấu hiệu kiểm trong ca:**

- Không biến công bố năng lực thành kết quả thử của tài khoản.
- Một take đẹp không được ghi là tỷ lệ đạt chắc chắn; cả clip được xem trước kết luận chuyển động.

**Nếu gặp:** Model được quảng bá tốt nhưng liên tục không đạt cảnh cụ thể.

Có thể do: Chế độ/tính năng khác tài liệu. Bài thử không giống rủi ro đang gặp. Đầu vào không khả thi.

Thử tiếp: Kiểm cấu hình trước, rồi thử một thay đổi đúng nguyên nhân; giữ nhật ký phiên bản và các take dùng/loại.
**Nguồn đối chiếu:** [SRC-GOOGLE-PROMPT](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/video-gen-prompt-guide), [SRC-RUNWAY-GEN4](https://help.runwayml.com/hc/en-us/articles/39789879462419-Gen-4-Video-Prompting-Guide), [SRC-SEEDANCE-25](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)

[Bản JSON chuẩn](../kien-thuc/AI-013.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).
