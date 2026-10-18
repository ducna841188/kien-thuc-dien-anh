# DR — Đạo diễn, diễn xuất và dàn cảnh

Phiên bản 1.0.0. Tổ chức người, vật, không gian và hành vi có mục tiêu.

[Mục lục](../README.md) · [Chuẩn ra quyết định](../03_RA_QUYET_DINH.md)

Mỗi mục dưới là hướng dẫn có điều kiện. Tác dụng cảm xúc là giả thuyết thiết kế; chưa có thử tạo video hoặc kiểm nghiệm khán giả cho các ví dụ mới. Thuật ngữ xem [từ điển](../TU_DIEN.md).

| Mã | Quyết định | Mức |
| --- | --- | --- |
| [DR-001](#dr-001) | Chỉ đạo bằng mục tiêu và hành vi | co_ban |
| [DR-002](#dr-002) | Dàn cảnh người–vật–không gian | co_ban |
| [DR-003](#dr-003) | Nhịp phản ứng và khoảng dừng | trung_cap |
| [DR-004](#dr-004) | Chỉ đạo tương tác nhiều nhân vật | trung_cap |
| [DR-005](#dr-005) | Chi tiết đời sống và thiết kế sản xuất | trung_cap |
| [DR-006](#dr-006) | Thiết kế đủ góc để dựng và phương án tiết kiệm | nang_cao |

<a id="dr-001"></a>
## DR-001 — Chỉ đạo bằng mục tiêu và hành vi

**Câu hỏi quyết định:** Nhân vật đang cố làm gì với ai hoặc vật nào?

**Dùng khi:** Khi chỉ đạo người thật hoặc nhân vật AI.

**Nguyên lý thực hành:** Chuyển nhãn cảm xúc thành hành vi có đối tượng và nguyên nhân. Một hành vi có thể biểu đạt nhiều cảm xúc tùy ngữ cảnh.

**Cách làm:**

1. Ghi mục tiêu hiện tại của nhân vật.
2. Chọn động từ và đối tượng tác động.
3. Thêm phản ứng vừa đủ khi mục tiêu thành/bại.

**Đánh đổi:** Mô tả quá nhiều dấu hiệu có thể khiến diễn xuất cường điệu hoặc AI quá tải.

**Kiểm tra:**

- Hành vi nhìn/nghe được và nối với sự kiện.
- Không dùng nước mắt, run hoặc cười làm điều kiện bắt buộc.

**Ví dụ tự biên soạn:** Người kiểm tra miệng giỏ, chỉnh một sợi rồi mới trao; cho thấy sự quan tâm qua việc làm.

**Phản ví dụ / giới hạn:** Nhân vật có thể giấu cảm xúc; lời nói và hành vi không cần đồng nhất hoàn toàn.

**Liên quan:** [ST-002](../kien-thuc/ST-002.json), [DR-003](../kien-thuc/DR-003.json), [AI-003](../kien-thuc/AI-003.json)

**Nguồn đối chiếu:** [B021](../../bai-hoc/021-lam-chu-cam-xuc/README.md), [B033](../../bai-hoc/033-sua-prompt-bi-bo-qua/README.md)

[Bản JSON chuẩn](../kien-thuc/DR-001.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="dr-002"></a>
## DR-002 — Dàn cảnh người–vật–không gian

**Câu hỏi quyết định:** Bố trí nào làm quan hệ và hành động dễ đọc?

**Dùng khi:** Trước khi chọn góc máy hoặc tạo ảnh bối cảnh.

**Nguyên lý thực hành:** Blocking là bố trí vị trí và di chuyển của người/vật trong cảnh. Máy quay được chọn trong quan hệ với cách dàn cảnh đó.

**Cách làm:**

1. Vẽ vị trí đầu, đích đến, lối đi và vật cần chạm.
2. Kiểm tay thuận, tầm với, vật che và khoảng thao tác.
3. Đặt máy để thấy thông tin quan trọng hoặc chủ động giấu có lý do.

**Đánh đổi:** Bố trí tối ưu cho một góc có thể khó nối góc khác; cần kế hoạch vùng quay.

**Kiểm tra:**

- Người/vật không tự đổi vị trí giữa góc.
- Hành động có không gian để thực hiện và không bị che ngoài ý đồ.

**Ví dụ tự biên soạn:** Bát nằm gần tay đang cầm muôi; người ngồi không phải xuyên qua bàn để lấy.

**Phản ví dụ / giới hạn:** Một cảnh muốn tạo cảm giác bị cản có thể chủ động che một phần nhưng vẫn cần điều khiển thông tin.

**Liên quan:** [CA-004](../kien-thuc/CA-004.json), [CA-006](../kien-thuc/CA-006.json), [AI-002](../kien-thuc/AI-002.json)

**Nguồn đối chiếu:** [SRC-ASC-KAUFMAN](https://theasc.com/article/filming-12-angry-men/), [B015](../../bai-hoc/015-logic-chuyen-dong-vat-ly/README.md)

[Bản JSON chuẩn](../kien-thuc/DR-002.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="dr-003"></a>
## DR-003 — Nhịp phản ứng và khoảng dừng

**Câu hỏi quyết định:** Nhân vật nhận biết, xử lý rồi phản ứng ở lúc nào?

**Dùng khi:** Khi cảnh cần cảm xúc tinh tế hoặc tương tác.

**Nguyên lý thực hành:** Để phản ứng có tác nhân, độ trễ và mức độ phù hợp. Khoảng dừng có thể chứa suy nghĩ hoặc quan sát, không mặc định là khoảng chết.

**Cách làm:**

1. Xác định sự kiện nhân vật nhận được.
2. Chọn một chuyển biến cơ thể/ánh mắt chính.
3. Xác định lúc bắt đầu, phát triển và kết thúc phản ứng.

**Đánh đổi:** Giữ quá lâu có thể trống; cắt quá sớm có thể mất ý nghĩa lựa chọn.

**Kiểm tra:**

- Phản ứng không đến trước tác nhân ngoài chủ ý.
- Người xem có cơ hội đọc thay đổi mà không cần phóng đại.

**Ví dụ tự biên soạn:** Nghe tiếng bà gọi, bàn tay dừng một nhịp rồi người quay nhìn và mỉm cười nhẹ.

**Phản ví dụ / giới hạn:** Phản ứng đồng thời với hành động có thể hợp lệ khi nhân vật đã biết điều sắp đến.

**Liên quan:** [AU-004](../kien-thuc/AU-004.json), [ST-003](../kien-thuc/ST-003.json), [ED-002](../kien-thuc/ED-002.json)

**Nguồn đối chiếu:** [B021](../../bai-hoc/021-lam-chu-cam-xuc/README.md), [B029](../../bai-hoc/029-lip-sync-hoat-hinh/README.md)

[Bản JSON chuẩn](../kien-thuc/DR-003.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="dr-004"></a>
## DR-004 — Chỉ đạo tương tác nhiều nhân vật

**Câu hỏi quyết định:** Ai khởi xướng, ai đáp lại và trọng tâm chuyển khi nào?

**Dùng khi:** Khi có hội thoại, trao vật hoặc cùng làm việc.

**Nguyên lý thực hành:** Phân vai hành động, lời và phản ứng. Người nghe vẫn có đời sống; không cần mọi người cùng biểu diễn ở một mức.

**Cách làm:**

1. Lập vị trí, hướng nhìn và lượt tương tác.
2. Gắn câu thoại hoặc hành động với đúng người.
3. Chọn lúc thấy chung và lúc tách để đọc người nói/người nghe.

**Đánh đổi:** Tách mọi lượt thành một shot có thể mất quan hệ trong cùng không gian.

**Kiểm tra:**

- Người nói, giọng và môi được kiểm riêng.
- Trao vật có chuyển quyền sở hữu rõ, không nhân đôi.

**Ví dụ tự biên soạn:** Cô đưa bát, bà nhận rồi nếm; phản ứng của người đưa có thể quan trọng hơn người đang nói.

**Phản ví dụ / giới hạn:** Hai người có thể cùng thoại chồng chủ ý; cần kế hoạch nghe rõ thay vì cấm mọi chồng lấn.

**Liên quan:** [CA-006](../kien-thuc/CA-006.json), [SO-002](../kien-thuc/SO-002.json), [AI-006](../kien-thuc/AI-006.json)

**Nguồn đối chiếu:** [B013](../../bai-hoc/013-tach-shot-hoi-thoai/README.md), [B027](../../bai-hoc/027-tach-shot-lip-sync/README.md), [B030](../../bai-hoc/030-gan-thoai-dung-nhan-vat/README.md)

[Bản JSON chuẩn](../kien-thuc/DR-004.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="dr-005"></a>
## DR-005 — Chi tiết đời sống và thiết kế sản xuất

**Câu hỏi quyết định:** Chi tiết nào làm thế giới có lịch sử và chức năng?

**Dùng khi:** Khi thiết kế bối cảnh, phục trang, vật liệu và sinh hoạt.

**Nguyên lý thực hành:** Chọn chi tiết theo cách sống, thời tiết, công việc và nhân vật. Cảm giác chân thực đến từ quan hệ hoạt động, không chỉ thêm bụi hoặc khuyết điểm.

**Cách làm:**

1. Ghi công dụng và trạng thái từng đạo cụ quan trọng.
2. Giữ dấu sử dụng có nguyên nhân và mức nhất quán.
3. Rà chi tiết văn hóa, mùa vụ hoặc kỹ thuật cần nguồn chuyên ngành.

**Đánh đổi:** Quá nhiều trang trí có thể che thao tác và gây trôi vật thể khi tạo AI.

**Kiểm tra:**

- Đồ vật có vị trí/công dụng đọc được.
- Không suy văn hóa hoặc tên nguyên liệu vượt bằng chứng.

**Ví dụ tự biên soạn:** Giỏ có chỗ để, được mang ra dùng và trở về với mức đầy đã đổi.

**Phản ví dụ / giới hạn:** Phong cách cách điệu có thể dùng vật liệu phi hiện thực nếu thống nhất quy tắc của thế giới.

**Liên quan:** [CO-002](../kien-thuc/CO-002.json), [AI-002](../kien-thuc/AI-002.json), [QC-002](../kien-thuc/QC-002.json)

**Nguồn đối chiếu:** [B002](../../bai-hoc/002-prompt-cau-truc/README.md), [B003](../../bai-hoc/003-khoa-thiet-ke-nhan-vat/README.md)

[Bản JSON chuẩn](../kien-thuc/DR-005.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="dr-006"></a>
## DR-006 — Thiết kế đủ góc để dựng và phương án tiết kiệm

**Câu hỏi quyết định:** Cần những bằng chứng hình nào để cảnh dựng được?

**Dùng khi:** Khi lập danh sách shot hoặc chi phí tạo cảnh cao.

**Nguyên lý thực hành:** Coverage là bộ góc/chi tiết cho người dựng lựa chọn. Chọn theo điểm kể chuyện và hành động; không mặc định quay mọi cỡ ở mọi cảnh.

**Cách làm:**

1. Bắt đầu bằng góc thấy quan hệ chính.
2. Bổ sung chi tiết, phản ứng và trạng thái kết cần thiết.
3. Lập phương án tối thiểu và góc dự phòng cho lỗi dễ xảy ra.

**Đánh đổi:** Nhiều góc tăng lựa chọn nhưng tốn thời gian và dễ lệch liên tục.

**Kiểm tra:**

- Có thể dựng hiểu việc bằng bộ góc tối thiểu.
- Góc dự phòng có mục đích, không chỉ lặp thông tin.

**Ví dụ tự biên soạn:** Nếu AI khó tạo cả thao tác và mặt cùng lúc, dùng cảnh trung xác lập rồi cận tay và cận kết quả.

**Phản ví dụ / giới hạn:** Một cú máy liên tục có thể đủ; không phải lúc nào cắt nhiều cũng dễ hiểu hơn.

**Liên quan:** [ED-003](../kien-thuc/ED-003.json), [AI-004](../kien-thuc/AI-004.json), [QC-001](../kien-thuc/QC-001.json)

**Nguồn đối chiếu:** [B012](../../bai-hoc/012-cau-truc-camera/README.md), [B013](../../bai-hoc/013-tach-shot-hoi-thoai/README.md), [B024](../../bai-hoc/024-xau-chuoi-canh/README.md)

[Bản JSON chuẩn](../kien-thuc/DR-006.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).
