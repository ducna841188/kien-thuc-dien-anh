# AI — Sản xuất bằng AI

Phiên bản 1.0.0. Chuyển ý đồ thành đầu vào, kiểm kết quả và chọn cách sửa.

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

<a id="ai-001"></a>
## AI-001 — Chọn chế độ tạo theo thông tin cần giữ

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

**Câu hỏi quyết định:** AI phải thể hiện sự thay đổi vật lý nào?

**Dùng khi:** Khi cảnh có tay, dụng cụ, trao vật, đổ/trải/cắt hoặc tác động vật.

**Nguyên lý thực hành:** Viết ai làm gì với vật nào và chuỗi trạng thái cần thấy. Mô tả hành vi có nguyên nhân thay cho nhãn vật lý hoàn hảo.

**Cách làm:**

1. Nêu trạng thái đầu và quyền giữ vật.
2. Ghi tiếp xúc, hướng lực hoặc đường đi cần thiết.
3. Nêu trạng thái kết có thể đối chiếu và điều giữ ổn định.

**Đánh đổi:** Nhiều tiểu bước có thể quá tải một clip; chia shot khi cần.

**Kiểm tra:**

- Đúng mục tiêu thao tác và không xuyên/nhân đôi/biến mất ở đoạn quan trọng.
- Ghi thiếu dụng cụ hoặc tư thế ngay từ ảnh đầu.

**Ví dụ tự biên soạn:** Gạo rơi từ dụng cụ vào bát và tích trên lớp sẵn có; lượng tăng có nguyên nhân.

**Phản ví dụ / giới hạn:** Một câu một hành động vẫn có thể sai nếu ảnh đầu không có đủ dụng cụ hoặc tư thế.

**Liên quan:** [DR-001](../kien-thuc/DR-001.json), [CO-004](../kien-thuc/CO-004.json), [AI-004](../kien-thuc/AI-004.json)

**Nguồn đối chiếu:** [B015](../../bai-hoc/015-logic-chuyen-dong-vat-ly/README.md), [B033](../../bai-hoc/033-sua-prompt-bi-bo-qua/README.md)

[Bản JSON chuẩn](../kien-thuc/AI-003.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ai-004"></a>
## AI-004 — Chia nhiệm vụ sinh và dựng phim

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

**Câu hỏi quyết định:** Đầu ra sai lời, vai, môi hay âm sự kiện?

**Dùng khi:** Khi clip có âm tích hợp hoặc hội thoại.

**Nguyên lý thực hành:** Chẩn đoán riêng thay vì thêm một khối yêu cầu dài cho mọi lỗi. Giữ hình đạt khi có phương án xử lý âm riêng.

**Cách làm:**

1. Nghe và chép nội dung thực được phát.
2. So vai nói, giọng, môi và sự kiện theo mốc.
3. Chọn sửa lời/giọng/đồng bộ/hậu kỳ hoặc sinh lại đúng shot.

**Đánh đổi:** Tạo lại có thể làm mất hình đã đạt; sửa âm có thể khó nếu tách nguồn kém.

**Kiểm tra:**

- Không báo khớp môi chỉ vì người đúng đang mở miệng.
- Không suy có các track riêng khi chỉ nhận một file trộn.

**Ví dụ tự biên soạn:** Mèo và chó bị nhầm lời: xác định vai sai trước; không tự đổi camera đang đúng.

**Phản ví dụ / giới hạn:** Không phải mọi tương tác đều cần quay–đảo góc; một khung chung vẫn có thể phù hợp.

**Liên quan:** [SO-002](../kien-thuc/SO-002.json), [SO-008](../kien-thuc/SO-008.json), [DR-004](../kien-thuc/DR-004.json)

**Nguồn đối chiếu:** [B027](../../bai-hoc/027-tach-shot-lip-sync/README.md), [B029](../../bai-hoc/029-lip-sync-hoat-hinh/README.md), [B030](../../bai-hoc/030-gan-thoai-dung-nhan-vat/README.md), [B032](../../bai-hoc/032-dieu-khien-am-thanh/README.md)

[Bản JSON chuẩn](../kien-thuc/AI-006.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ai-007"></a>
## AI-007 — Câu lệnh, thiết lập và hồ sơ năng lực mô hình

**Câu hỏi quyết định:** Điều gì nên viết, điều gì phải đặt và điều gì chưa biết?

**Dùng khi:** Khi đổi mô hình, dịch vụ hoặc phiên bản.

**Nguyên lý thực hành:** Giữ ý đồ điện ảnh chung, rồi chuyển sang cách nhập đúng công cụ. Mã khóa tự đặt không trở thành tham số kỹ thuật.

**Cách làm:**

1. Ghi nhà cung cấp, tên/mã mô hình, chế độ và ngày kiểm.
2. Phân loại điều khiển bằng chữ, thiết lập, tham chiếu, hậu kỳ hoặc chưa hỗ trợ.
3. Đối chiếu tài liệu và giao diện khi có khác biệt; để null cho giới hạn chưa rõ.

**Đánh đổi:** Prompt dùng chung dễ mang cú pháp sai; adapter riêng cần được cập nhật.

**Kiểm tra:**

- Không coi no/don't hoặc negative là cú pháp chung.
- Không dùng HEX, 8K hay 3% rung làm bảo đảm đầu ra.

**Ví dụ tự biên soạn:** Veo ở trường negative được tài liệu hướng dẫn liệt kê yếu tố; Gen-4 của Runway khuyên mô tả khẳng định.

**Phản ví dụ / giới hạn:** Có thể giữ cấu trúc lập ý giống nhau nhưng cách nhập của từng chế độ khác.

**Liên quan:** [EV-006](../kien-thuc/EV-006.json), [AI-001](../kien-thuc/AI-001.json), [QC-004](../kien-thuc/QC-004.json)

**Nguồn đối chiếu:** [B023](../../bai-hoc/023-negative-prompt/README.md), [B026](../../bai-hoc/026-nam-tru-cot-prompt/README.md), [SRC-GOOGLE-PROMPT](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/video-gen-prompt-guide), [SRC-RUNWAY-GEN4](https://help.runwayml.com/hc/en-us/articles/39789879462419-Gen-4-Video-Prompting-Guide)

[Bản JSON chuẩn](../kien-thuc/AI-007.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ai-008"></a>
## AI-008 — Sửa ít nhất, giữ phần đạt và chọn hậu kỳ

**Câu hỏi quyết định:** Cách sửa nào ít làm hỏng phần đang đúng?

**Dùng khi:** Khi user chỉ yêu cầu sửa một lỗi hoặc clip gần đạt.

**Nguyên lý thực hành:** Lưu bản gốc, ghi phần phải giữ và thay đúng nhóm liên quan. Sinh lại là lần tạo mới; không hứa giữ tuyệt đối chi tiết đã duyệt.

**Cách làm:**

1. Phân loại lỗi nội dung, chuyển động, liên tục, âm hoặc đầu ra.
2. Chọn cắt/crop/âm/màu/chỉnh có vùng hoặc tạo lại theo tính năng thật.
3. Ghi khác biệt câu lệnh và xem lại toàn clip sau sửa.

**Đánh đổi:** Sửa cục bộ có thể tiết kiệm nhưng để lại dấu; tạo mới có thể sạch hơn nhưng đổi nhiều biến.

**Kiểm tra:**

- Sửa người thừa không tự đổi hành động, thời gian hay phong cách.
- Bản sau được đối chiếu cùng tiêu chí như bản gốc.

**Ví dụ tự biên soạn:** Giữ timelapse đã tốt, chỉ chỉnh mô tả một người và kiểm các đoạn chuyển vị trí.

**Phản ví dụ / giới hạn:** Nếu ảnh đầu sai tư thế khiến thao tác bất khả thi, sửa ảnh đầu có thể cần hơn thêm câu.

**Liên quan:** [QC-002](../kien-thuc/QC-002.json), [AI-003](../kien-thuc/AI-003.json), [MO-006](../kien-thuc/MO-006.json)

**Nguồn đối chiếu:** [B004](../../bai-hoc/004-nano-banana-pro/README.md), [B033](../../bai-hoc/033-sua-prompt-bi-bo-qua/README.md)

[Bản JSON chuẩn](../kien-thuc/AI-008.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).
