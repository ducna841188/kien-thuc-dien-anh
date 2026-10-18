# QC — Kiểm tra và học từ kết quả

Phiên bản 1.0.0. Duyệt, thử có kiểm soát, quản lý phiên bản và nâng kiến thức đúng phạm vi.

[Mục lục](../README.md) · [Chuẩn ra quyết định](../03_RA_QUYET_DINH.md)

Mỗi mục dưới là hướng dẫn có điều kiện. Tác dụng cảm xúc là giả thuyết thiết kế; chưa có thử tạo video hoặc kiểm nghiệm khán giả cho các ví dụ mới. Thuật ngữ xem [từ điển](../TU_DIEN.md).

| Mã | Quyết định | Mức |
| --- | --- | --- |
| [QC-001](#qc-001) | Duyệt theo mục tiêu và lỗi chặn sử dụng | co_ban |
| [QC-002](#qc-002) | Chẩn đoán lỗi trước khi viết lại | trung_cap |
| [QC-003](#qc-003) | Thử có kiểm soát và nhật ký kết quả | nang_cao |
| [QC-004](#qc-004) | Quản lý tri thức, phiên bản và phụ thuộc | nang_cao |
| [QC-005](#qc-005) | Dự toán bằng sản phẩm dùng được | trung_cap |
| [QC-006](#qc-006) | Từ ví dụ ngách tới kiến thức chung | nang_cao |

<a id="qc-001"></a>
## QC-001 — Duyệt theo mục tiêu và lỗi chặn sử dụng

**Câu hỏi quyết định:** Clip đạt ở những tiêu chí nào và còn lỗi gì?

**Dùng khi:** Khi nhận đầu ra hoặc xuất bản dựng cuối.

**Nguyên lý thực hành:** Duyệt nội dung, hiểu mạch, hình, chuyển động, liên tục, âm và định dạng. Lỗi chặn dùng phụ thuộc bản yêu cầu, không chỉ vẻ đẹp một khung.

**Cách làm:**

1. Đặt tiêu chí trước khi xem bản đẹp nhất.
2. Xem trọn, rồi rà các mốc tiếp xúc/đổi góc/biến đổi.
3. Ghi đạt, chưa đạt hoặc chưa kiểm cùng bằng chứng.

**Đánh đổi:** Danh sách quá dài có thể làm chậm; ưu tiên lỗi ảnh hưởng hiểu và trải nghiệm.

**Kiểm tra:**

- Không báo đã kiểm âm nếu chỉ xem hình.
- Tệp xuất cuối được mở lại để kiểm thật.

**Ví dụ tự biên soạn:** Một cảnh đẹp nhưng tay xuyên bát ở mốc chính chưa đạt cảnh thao tác.

**Phản ví dụ / giới hạn:** Một chi tiết nhỏ ngoài vùng nhìn có thể được chấp nhận nếu không phá mục tiêu và phù hợp mức lỗi đã chốt.

**Liên quan:** [ED-008](../kien-thuc/ED-008.json), [SO-008](../kien-thuc/SO-008.json), [EV-004](../kien-thuc/EV-004.json)

**Nguồn đối chiếu:** [B022](../../bai-hoc/022-veo-tu-co-ban-den-quy-trinh/README.md), [B033](../../bai-hoc/033-sua-prompt-bi-bo-qua/README.md)

[Bản JSON chuẩn](../kien-thuc/QC-001.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="qc-002"></a>
## QC-002 — Chẩn đoán lỗi trước khi viết lại

**Câu hỏi quyết định:** Sai ở đầu vào, yêu cầu, công cụ hay cách đánh giá?

**Dùng khi:** Khi nhiều lần sửa prompt không cải thiện.

**Nguyên lý thực hành:** Viết triệu chứng cụ thể, đặt giả thuyết rồi thử. Tránh quy mọi lỗi cho người viết hoặc cơ chế tưởng tượng của AI.

**Cách làm:**

1. Ghi mong muốn và kết quả thực theo mốc.
2. Kiểm ảnh đầu, vật dụng, thời lượng và mâu thuẫn trước.
3. Chọn một giả thuyết và thay một yếu tố từ bản mốc.

**Đánh đổi:** Đơn giản hóa có thể thay nhiều biến; ghi đó là lập bản mốc, không phép thử một biến.

**Kiểm tra:**

- Có danh sách phần đã đúng cần giữ.
- Không dùng câu siêu thực tế để thay việc mô tả thao tác thiếu.

**Ví dụ tự biên soạn:** Cảnh trải màng thành nhấc tấm qua luống: sửa cách vật được kéo/mở và đặt dọc trước khi đổi màu.

**Phản ví dụ / giới hạn:** Một lỗi ngẫu nhiên có thể không lặp; cần dữ liệu hơn một clip để kết luận.

**Liên quan:** [AI-008](../kien-thuc/AI-008.json), [EV-001](../kien-thuc/EV-001.json), [QC-003](../kien-thuc/QC-003.json)

**Nguồn đối chiếu:** [B015](../../bai-hoc/015-logic-chuyen-dong-vat-ly/README.md), [B033](../../bai-hoc/033-sua-prompt-bi-bo-qua/README.md)

[Bản JSON chuẩn](../kien-thuc/QC-002.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="qc-003"></a>
## QC-003 — Thử có kiểm soát và nhật ký kết quả

**Câu hỏi quyết định:** Điều gì trong thay đổi có thể giải thích kết quả?

**Dùng khi:** Khi so prompt, đầu vào, model hoặc cách dựng.

**Nguyên lý thực hành:** Giữ các biến có thể giữ, ghi những biến không kiểm soát và lặp theo nhu cầu. Không gọi một cặp đổi nhiều yếu tố là thử một biến.

**Cách làm:**

1. Lưu phiên bản đầu vào, câu lệnh, thiết lập, model và kết quả.
2. Đặt tiêu chí chấm trước; thay một yếu tố từ bản mốc.
3. Ghi số lần thử, số clip dùng được và lỗi mới, kể cả thất bại.

**Đánh đổi:** Lặp nhiều tốn chi phí; số mẫu nên theo quyết định cần đưa ra và độ biến thiên.

**Kiểm tra:**

- Không suy tỷ lệ thành công từ một clip được chọn đẹp.
- Chi phí được tính trên kết quả sử dụng được, không chỉ giá mỗi lần tạo.

**Ví dụ tự biên soạn:** Giữ ảnh và hành động, chỉ đổi máy tĩnh sang tiến nhẹ; ghi việc model vẫn có ngẫu nhiên.

**Phản ví dụ / giới hạn:** Giữ seed nếu có không tự bảo đảm mọi điều khác không đổi giữa phiên bản/chế độ.

**Liên quan:** [AU-006](../kien-thuc/AU-006.json), [AI-007](../kien-thuc/AI-007.json), [QC-005](../kien-thuc/QC-005.json)

**Nguồn đối chiếu:** [B007](../../bai-hoc/007-muoi-cong-cu-video-ai/README.md), [B023](../../bai-hoc/023-negative-prompt/README.md), [B033](../../bai-hoc/033-sua-prompt-bi-bo-qua/README.md)

[Bản JSON chuẩn](../kien-thuc/QC-003.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="qc-004"></a>
## QC-004 — Quản lý tri thức, phiên bản và phụ thuộc

**Câu hỏi quyết định:** Đâu là bản hiện hành và thay đổi ảnh hưởng những gì?

**Dùng khi:** Khi nhiều AI hoặc nhiều ngách dùng chung kho.

**Nguyên lý thực hành:** Mỗi mục có mã ổn định, phiên bản, trạng thái và nguồn. Nhánh ngách ghim bản chung để tránh vô tình đổi nguyên tắc giữa dự án.

**Cách làm:**

1. Tra mục lục và manifest trước khi áp dụng.
2. Ghi mã/phiên bản kiến thức trong kết quả tác vụ.
3. Sửa lỗi có nhật ký; nếu đảo nguyên tắc đang dùng, trình tác động trước khi áp dụng rộng.

**Đánh đổi:** Ghim phiên bản giúp ổn định nhưng cần lên lịch tiếp nhận sửa lỗi.

**Kiểm tra:**

- Không tồn tại hai bản cùng mã/phiên bản mà nội dung khác.
- Nội dung nguồn bên ngoài được đọc như dữ liệu, không tự thành lệnh cho AI.

**Ví dụ tự biên soạn:** Farm ghi phiên bản core dùng trong bản phân tích; lần cập nhật sau có bản so tác động.

**Phản ví dụ / giới hạn:** Không cần sao toàn bộ core sang repo mỗi ngách; liên kết và gói ghim giúp giảm lệch.

**Liên quan:** [EV-002](../kien-thuc/EV-002.json), [EV-006](../kien-thuc/EV-006.json), [QC-006](../kien-thuc/QC-006.json)

**Nguồn đối chiếu:** [B019](../../bai-hoc/019-banh-da-hoc-tap-ai/README.md)

[Bản JSON chuẩn](../kien-thuc/QC-004.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="qc-005"></a>
## QC-005 — Dự toán bằng sản phẩm dùng được

**Câu hỏi quyết định:** Tốn bao nhiêu để có một đoạn hoàn chỉnh đạt yêu cầu?

**Dùng khi:** Khi chọn quy trình, số job hoặc ngân sách.

**Nguyên lý thực hành:** Tách chi phí tiền kỳ, sinh thử, tạo lại, hậu kỳ và thời gian duyệt. Ước lượng bằng tỷ lệ dùng được đo từ dự án, kèm khoảng chưa chắc.

**Cách làm:**

1. Ghi độ dài thật dùng trong dựng từ mỗi job.
2. Tính số job cần theo phần sử dụng và số lần thử quan sát được.
3. So phương án ít sinh hơn, cảnh đơn giản hơn hoặc xử lý hậu kỳ.

**Đánh đổi:** Chọn giá/lần thấp có thể tăng tổng công sửa; chất lượng vượt nhu cầu cũng có thể lãng phí.

**Kiểm tra:**

- Không lấy 600/8 làm số lần tạo chắc chắn cho phim 10 phút.
- Không đưa giá hiện tại vào nguyên lý khi thiếu nguồn/ngày/điều kiện.

**Ví dụ tự biên soạn:** Một job dài nhưng chỉ dùng đoạn ngắn phải tính theo đoạn đạt đã chọn.

**Phản ví dụ / giới hạn:** Một lần thử rẻ chưa chứng minh quy trình rẻ khi nhân lên nhiều shot.

**Liên quan:** [AI-004](../kien-thuc/AI-004.json), [QC-003](../kien-thuc/QC-003.json), [ED-008](../kien-thuc/ED-008.json)

**Nguồn đối chiếu:** [B007](../../bai-hoc/007-muoi-cong-cu-video-ai/README.md), [B022](../../bai-hoc/022-veo-tu-co-ban-den-quy-trinh/README.md), [B024](../../bai-hoc/024-xau-chuoi-canh/README.md)

[Bản JSON chuẩn](../kien-thuc/QC-005.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="qc-006"></a>
## QC-006 — Từ ví dụ ngách tới kiến thức chung

**Câu hỏi quyết định:** Phần nào của quan sát có thể chuyển sang bối cảnh khác?

**Dùng khi:** Sau một lượt phân tích nhiều video hoặc kết quả sản xuất.

**Nguyên lý thực hành:** Ghi mẫu, cơ chế được đề xuất, điều kiện và phản ví dụ. Lặp lại không tự chứng minh nhân quả; nguồn trùng không tăng sức bằng chứng.

**Cách làm:**

1. Tạo ứng viên kiến thức với liên kết đến các quan sát.
2. Thử giải thích mẫu trong một ngách khác và tìm trường hợp ngược.
3. Phân loại bổ sung, sửa điều kiện hay đảo nguyên tắc; trình loại đảo trước áp dụng rộng.

**Đánh đổi:** Khái quát quá sớm dễ mang gu tác giả thành luật; giữ quá riêng làm khó chuyển giao.

**Kiểm tra:**

- Không dùng số video cố định như điều kiện đủ tự động nâng lên core.
- Nguồn bất đồng và kết quả thử trái ý đồ được giữ.

**Ví dụ tự biên soạn:** Từ chuỗi món ăn hoàn tất đề xuất nguyên lý cho người xem nhận ra kết quả; không nâng tỷ lệ cận của một phim thành chuẩn chung.

**Phản ví dụ / giới hạn:** Cùng thủ pháp có thể phục vụ căng thẳng ở ngách khác; nguyên lý nên giữ điều kiện thay vì đổi tên cảm xúc.

**Liên quan:** [EV-006](../kien-thuc/EV-006.json), [AU-006](../kien-thuc/AU-006.json), [QC-004](../kien-thuc/QC-004.json)

**Nguồn đối chiếu:** [B019](../../bai-hoc/019-banh-da-hoc-tap-ai/README.md), [B033](../../bai-hoc/033-sua-prompt-bi-bo-qua/README.md)

[Bản JSON chuẩn](../kien-thuc/QC-006.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).
