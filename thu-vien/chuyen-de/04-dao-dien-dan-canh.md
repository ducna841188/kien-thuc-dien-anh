# DR — Đạo diễn, diễn xuất và dàn cảnh

Phiên bản 1.2.0. Tổ chức người, vật, không gian và hành vi có mục tiêu.

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
| [DR-007](#dr-007) | Chỉ đạo mục tiêu, chiến thuật và điều nhân vật không nói ra | trung_cap |
| [DR-008](#dr-008) | Trọng lượng, thăng bằng và chuỗi tiếp xúc đáng tin | trung_cap |
| [DR-009](#dr-009) | Chi tiết đời sống có chức năng và mức hoàn hảo phù hợp | trung_cap |

<a id="dr-001"></a>
## DR-001 — Chỉ đạo bằng mục tiêu và hành vi

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Nhân vật đang cố làm gì với ai hoặc vật nào?

**Dùng khi:** Khi chỉ đạo người thật hoặc nhân vật AI.

**Nguyên lý thực hành:** Chuyển nhãn cảm xúc thành hành vi có đối tượng và nguyên nhân. Một hành vi có thể biểu đạt nhiều cảm xúc tùy ngữ cảnh. Hành vi rõ hơn khi có đối tượng và tác nhân; không suy nội tâm chắc chắn chỉ vì một cử chỉ.

**Cách làm:**

1. Ghi mục tiêu hiện tại của nhân vật.
2. Chọn động từ và đối tượng tác động.
3. Thêm phản ứng vừa đủ khi mục tiêu thành/bại.
4. Thêm mục tiêu tác động, một hành động và phản ứng sau tác nhân; tách chỉ đạo sáng tạo khỏi diễn giải khi phân tích phim nguồn.

**Đánh đổi:** Mô tả quá nhiều dấu hiệu có thể khiến diễn xuất cường điệu hoặc AI quá tải.

**Kiểm tra:**

- Hành vi nhìn/nghe được và nối với sự kiện.
- Không dùng nước mắt, run hoặc cười làm điều kiện bắt buộc.
- Có thể chỉ ra nhân vật đang cố đạt điều gì và điều nào làm họ đổi cách làm.

**Ví dụ tự biên soạn:** Người kiểm tra miệng giỏ, chỉnh một sợi rồi mới trao; cho thấy sự quan tâm qua việc làm.

**Phản ví dụ / giới hạn:** Nhân vật có thể giấu cảm xúc; lời nói và hành vi không cần đồng nhất hoàn toàn.

**Liên quan:** [ST-002](../kien-thuc/ST-002.json), [DR-003](../kien-thuc/DR-003.json), [AI-003](../kien-thuc/AI-003.json), [DR-007](../kien-thuc/DR-007.json), [DR-008](../kien-thuc/DR-008.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Tính quan sát được phải nối với mục tiêu và phản ứng, tránh ra lệnh diễn bằng danh sách nét mặt.

**Tình huống:** Người do dự khi nhận một món đồ.

**Phần phải giữ:** Mục tiêu và các phần đã duyệt trong tình huống.

| Phương án | Thực hiện |
| --- | --- |
| A | Yêu cầu buồn, xúc động, vui và lo cùng lúc. |
| B | Cho tay chậm nhận, nhìn người trao rồi lựa chọn nhận theo bối cảnh. |

**Cách chọn:** Chọn B khi cần biểu hiện qua quan hệ; mức diễn phải được kiểm ở cỡ phát thật.

**Dấu hiệu kiểm trong ca:**

- Có thể chỉ ra nhân vật đang cố đạt điều gì và điều nào làm họ đổi cách làm.

**Nếu gặp:** Biểu cảm nhiều nhưng hành vi vô cớ.

Có thể do: Không có mục tiêu hoặc tác nhân được thiết lập.

Thử tiếp: Giảm chỉ dẫn nét mặt, giữ một mục tiêu và hành động hướng tới đối tượng.
**Nguồn đối chiếu:** [B021](../../bai-hoc/021-lam-chu-cam-xuc/README.md), [B033](../../bai-hoc/033-sua-prompt-bi-bo-qua/README.md)

[Bản JSON chuẩn](../kien-thuc/DR-001.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="dr-002"></a>
## DR-002 — Dàn cảnh người–vật–không gian

**Phiên bản mục:** 1.0.0

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

**Phiên bản mục:** 1.0.0

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

**Phiên bản mục:** 1.0.0

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

**Phiên bản mục:** 1.0.0

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

**Phiên bản mục:** 1.0.0

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

<a id="dr-007"></a>
## DR-007 — Chỉ đạo mục tiêu, chiến thuật và điều nhân vật không nói ra

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Nhân vật đang cố tác động điều gì, bằng hành vi nào?

**Dùng khi:** Diễn xuất chỉ có nhãn vui/buồn, đối thoại phẳng hoặc biểu cảm quá mức.

**Nguyên lý thực hành:** Chỉ đạo diễn xuất bằng mục tiêu ngay lúc này, hành động hướng tới người/vật và phản ứng với điều vừa nhận. Nội tâm có thể thể hiện qua chênh lệch giữa lời và việc; không cần một biểu cảm mạnh ở mọi nhịp.

**Cách làm:**

1. Viết động từ tác động được: trấn an, thăm dò, né tránh, hướng dẫn, giấu hoặc mời; ghi đối tượng và tác nhân làm đổi chiến thuật.
2. Chọn một vài dấu hành vi quan sát được: nhường chỗ, chậm trao vật, nhìn kiểm tra phản ứng rồi mới nói; tránh cùng lúc ép mắt, môi, tay và thở diễn mọi cảm xúc.
3. Cho phản ứng người nghe và khoảng trước/sau câu nếu nó đổi quan hệ. Trong AI, thử từng hành vi rõ trước khi tăng lớp diễn xuất.

**Đánh đổi:** Hành vi quá tinh có thể không đọc trên màn hình nhỏ; tăng rõ bằng cỡ cảnh hoặc ngữ cảnh trước khi phóng đại nét mặt.

**Kiểm tra:**

- Hành vi có đối tượng và lý do theo cảnh.
- Không gán nội tâm chắc chắn khi chỉ phân tích cử chỉ không đủ bối cảnh.

**Ví dụ tự biên soạn:** Người muốn mời khách ở lại nhưng ngại nói: đặt thêm cốc và kéo ghế; lời vẫn chỉ là hỏi khách có khát không.

**Phản ví dụ / giới hạn:** Phim hướng dẫn thao tác có thể không cần tầng ý ngầm; sự rõ ràng có thể phục vụ lời hứa tốt hơn.

**Liên quan:** [DR-001](../kien-thuc/DR-001.json), [DR-003](../kien-thuc/DR-003.json), [DR-004](../kien-thuc/DR-004.json), [ST-006](../kien-thuc/ST-006.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Mục tiêu và chiến thuật gắn biểu cảm với sự kiện và quan hệ. Đây là phương pháp chỉ đạo để thử, không là quy tắc đọc tâm trí từ một dấu cơ thể.

**Tình huống:** Người muốn mời khách ở lại nhưng ngại nói: đặt thêm cốc và kéo ghế; lời vẫn chỉ là hỏi khách có khát không.

**Phần phải giữ:** Mục tiêu mời khách ở lại. Mức biểu lộ dè dặt của cảnh.

| Phương án | Thực hiện |
| --- | --- |
| A | Yêu cầu “rất xúc động, mắt rưng rưng” cho mọi lượt lời. |
| B | Mô tả việc nhân vật muốn người kia ở lại và một hành động nhỏ thể hiện lời mời. |

**Cách chọn:** Chọn B nếu cảnh cần sự dè dặt; A chỉ xét khi mức biểu lộ đó hợp bối cảnh và đã duyệt.

**Dấu hiệu kiểm trong ca:**

- Hành vi có đối tượng và lý do theo cảnh.
- Không gán nội tâm chắc chắn khi chỉ phân tích cử chỉ không đủ bối cảnh.

**Nếu gặp:** Diễn xuất giống trình diễn cảm xúc hơn là đang sống trong cảnh.

Có thể do: Không có mục tiêu tác động. Quá nhiều chỉ dẫn vi biểu cảm mâu thuẫn.

Thử tiếp: Bỏ nhãn cảm xúc khỏi một bản thử, giữ mục tiêu và hành động; so độ đọc được của quan hệ.
**Nguồn đối chiếu:** [SRC-YALE-STAGING](https://filmanalysis.yale.edu/mise-en-scene/)

[Bản JSON chuẩn](../kien-thuc/DR-007.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="dr-008"></a>
## DR-008 — Trọng lượng, thăng bằng và chuỗi tiếp xúc đáng tin

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Hành động này có cho thấy vật được đỡ, chịu lực và đổi trạng thái đúng lúc không?

**Dùng khi:** Chỉ đạo mang/vác/đổ/trao/đặt vật; sửa nhân vật AI trượt chân hoặc tay xuyên đồ.

**Nguyên lý thực hành:** Làm rõ chuỗi chuẩn bị→chạm/giữ→tác động→vật phản ứng→nhả/ổn định theo hành động thực tế. Trọng lượng được thể hiện bằng tư thế, gia tốc, điểm đỡ, biến dạng và tiếng phù hợp; không chỉ bằng một từ “nặng”.

**Cách làm:**

1. Xác định vật được đỡ bởi gì ở từng thời điểm; đánh dấu lúc chuyển quyền giữ và lúc vật có thể tự đứng. Chọn cỡ/góc thấy được bằng chứng thiết yếu.
2. Chỉ đạo chuẩn bị tư thế, đổi trọng tâm hoặc điều chỉnh tay khi cần; không thêm động tác thừa cho vật nhẹ hoặc phong cách đã cách điệu.
3. Với AI, kiểm ảnh đầu có đủ tay/dụng cụ/khoảng trống. Tách tiếp xúc khó thành shot riêng nếu model không giữ được chuỗi; xem chuyển động đầy đủ quanh lúc chạm và nhả.

**Đánh đổi:** Chi tiết tiếp xúc tăng độ tin nhưng cũng tăng độ khó tạo. Che một phần có thể hợp dàn cảnh, nhưng không dùng che để làm mất bằng chứng khán giả cần.

**Kiểm tra:**

- Vật không có lúc treo không nguyên nhân hoặc xuyên điểm đỡ.
- Âm tiếp xúc không đến trước chạm; bước chân không trượt ngoài chủ ý.

**Ví dụ tự biên soạn:** Đặt thùng xuống: người hạ thùng, đáy chạm sàn, cơ thể giảm tải rồi tay rời; tiếng chạm thuộc thời điểm đáy gặp sàn.

**Phản ví dụ / giới hạn:** Phim hoạt hình cách điệu có thể chủ ý vượt vật lý; phải giữ quy luật nội tại thay vì tự sửa thành hiện thực.

**Liên quan:** [DR-002](../kien-thuc/DR-002.json), [AI-003](../kien-thuc/AI-003.json), [AI-011](../kien-thuc/AI-011.json), [SO-008](../kien-thuc/SO-008.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Người xem có nhiều dấu hình/âm để đọc một lực tác động. Phiếu kiểm ở đây là phương pháp thực hành theo trạng thái, không là mô phỏng động lực học định lượng.

**Tình huống:** Đặt thùng xuống: người hạ thùng, đáy chạm sàn, cơ thể giảm tải rồi tay rời; tiếng chạm thuộc thời điểm đáy gặp sàn.

**Phần phải giữ:** Đúng một chuỗi đặt thùng. Điểm đỡ trước khi tay nhả.

| Phương án | Thực hiện |
| --- | --- |
| A | Tăng mô tả cơ bắp và độ nặng nhưng không chỉ rõ điểm thùng chạm. |
| B | Chọn khung thấy đáy thùng và thời điểm nhả; giữ nguyên hình nhân vật đã duyệt. |

**Cách chọn:** Chọn B khi vấn đề nằm ở chuỗi lực/tiếp xúc; tăng nét mặt không sửa quan hệ hình học.

**Dấu hiệu kiểm trong ca:**

- Vật không có lúc treo không nguyên nhân hoặc xuyên điểm đỡ.
- Âm tiếp xúc không đến trước chạm; bước chân không trượt ngoài chủ ý.

**Nếu gặp:** Vật trông không có trọng lượng dù hình từng frame đẹp.

Có thể do: Thiếu đổi tư thế hoặc gia tốc. Nhả trước khi có điểm đỡ. Âm không gắn với tiếp xúc.

Thử tiếp: Xem chậm quanh điểm chuyển lực để tìm lỗi, sau đó xem lại tốc độ thường để duyệt cảm nhận chuyển động.
**Nguồn đối chiếu:** [SRC-YALE-STAGING](https://filmanalysis.yale.edu/mise-en-scene/)

[Bản JSON chuẩn](../kien-thuc/DR-008.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="dr-009"></a>
## DR-009 — Chi tiết đời sống có chức năng và mức hoàn hảo phù hợp

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Điều gì khiến cảnh giống một hoạt động đang diễn ra thay vì một ảnh quảng bá?

**Dùng khi:** Thế giới AI quá sạch, cử chỉ máy móc, đồ vật chỉ làm nền hoặc ai cũng nhìn máy.

**Nguyên lý thực hành:** Tạo cảm giác sống bằng mục đích sử dụng, dấu thời gian và phản ứng với môi trường. Chọn sự không đều có nguyên nhân; không đồng nhất tự nhiên với bẩn, lỗi hình hoặc rung máy.

**Cách làm:**

1. Gắn đạo cụ và dấu sử dụng với công việc thật của cảnh: vật cần lấy, chỗ đặt, trạng thái đã dùng và đường đi hợp lý.
2. Cho nhân vật chú ý vào nhiệm vụ/người kia, có điều chỉnh nhỏ do vật và không gian; chỉ thêm khi diễn tiến vẫn rõ và phù hợp năng lực tạo.
3. Lập giới hạn phong cách: mức gọn gàng, hao mòn, đối xứng và biểu diễn; so toàn chuỗi để dấu sử dụng không tự mất/nhân lên.

**Đánh đổi:** Nhiều chi tiết tăng công giữ liên tục và có thể hút mắt khỏi việc chính; phim cách điệu có thể cần sự hoàn hảo rõ ràng.

**Kiểm tra:**

- Mỗi dấu đời sống có lý do trong thế giới cảnh.
- Nhân vật không nhìn thẳng máy nếu không thuộc quan hệ đã chốt.

**Ví dụ tự biên soạn:** Người soạn bàn dành chỗ cho khay sắp tới và gạt nhẹ một vật cản; chi tiết xuất phát từ nhiệm vụ, không cần thêm cả phòng bừa bộn.

**Phản ví dụ / giới hạn:** Vết bẩn ngẫu nhiên hoặc mọi vật cũ kỹ không chứng nhận tính chân thực của một bối cảnh cụ thể.

**Liên quan:** [DR-005](../kien-thuc/DR-005.json), [CO-004](../kien-thuc/CO-004.json), [AI-010](../kien-thuc/AI-010.json), [AU-002](../kien-thuc/AU-002.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Chức năng và hệ quả nối đồ vật với hành động. Dấu không đều chỉ hữu ích nếu có quan hệ với việc, người và thời gian; đây là lựa chọn thiết kế được kiểm theo mục tiêu.

**Tình huống:** Người soạn bàn dành chỗ cho khay sắp tới và gạt nhẹ một vật cản; chi tiết xuất phát từ nhiệm vụ, không cần thêm cả phòng bừa bộn.

**Phần phải giữ:** Công năng bàn và khay. Mức gọn gàng đúng phong cách.

| Phương án | Thực hiện |
| --- | --- |
| A | Thêm hạt phim, rung và bụi cho toàn cảnh. |
| B | Chọn một dấu sử dụng và một điều chỉnh hành vi liên quan trực tiếp đến nhiệm vụ. |

**Cách chọn:** Chọn B nếu hình đang vô hồn do thiếu công năng; A chỉ xét như lớp phong cách sau khi quan hệ cảnh đã rõ.

**Dấu hiệu kiểm trong ca:**

- Mỗi dấu đời sống có lý do trong thế giới cảnh.
- Nhân vật không nhìn thẳng máy nếu không thuộc quan hệ đã chốt.

**Nếu gặp:** Đã có nhiều texture nhưng cảnh vẫn giống ảnh dàn dựng.

Có thể do: Mọi người chờ máy hơn là làm việc. Đạo cụ không được sử dụng hoặc không để lại hệ quả.

Thử tiếp: Xem cảnh không lời và hỏi từng hành vi đang phục vụ việc gì; bỏ trang trí không có chức năng.
**Nguồn đối chiếu:** [SRC-YALE-STAGING](https://filmanalysis.yale.edu/mise-en-scene/)

[Bản JSON chuẩn](../kien-thuc/DR-009.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).
