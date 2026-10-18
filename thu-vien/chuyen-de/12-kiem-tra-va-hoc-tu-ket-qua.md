# QC — Kiểm tra và học từ kết quả

Phiên bản 1.3.0. Duyệt, thử có kiểm soát, quản lý phiên bản và nâng kiến thức đúng phạm vi.

[Mục lục](../README.md) · [Chuẩn ra quyết định](../03_RA_QUYET_DINH.md)

Mỗi mục dưới là hướng dẫn có điều kiện. Tác dụng cảm xúc là giả thuyết thiết kế; chưa có thử tạo video hoặc kiểm nghiệm khán giả cho các ví dụ mới. Thuật ngữ xem [từ điển](../TU_DIEN.md).

| Mã | Quyết định | Mức |
| --- | --- | --- |
| [QC-001](#qc-001) | Duyệt theo mục tiêu và lỗi chặn sử dụng | co_ban |
| [QC-002](#qc-002) | Chẩn đoán lỗi trước khi viết lại | trung_cap |
| [QC-003](#qc-003) | Thử có kiểm soát và nhật ký kết quả | nang_cao |
| [QC-004](#qc-004) | Cập nhật tại chỗ, bản hiện hành và lịch sử Git | nang_cao |
| [QC-005](#qc-005) | Dự toán bằng sản phẩm dùng được | trung_cap |
| [QC-006](#qc-006) | Từ ví dụ ngách tới kiến thức chung | nang_cao |
| [QC-007](#qc-007) | Duyệt theo công đoạn để không hoàn thiện một cấu trúc còn sai | trung_cap |
| [QC-008](#qc-008) | Chuyển mục tiêu thành tiêu chí kiểm và giữ giới hạn kết luận | nang_cao |
| [QC-009](#qc-009) | Chọn phương án theo nhiều mục tiêu và ngân sách rủi ro | nang_cao |
| [QC-010](#qc-010) | Ổn định theo thời gian và đúng hành động là hai phép duyệt riêng | nang_cao |

<a id="qc-001"></a>
## QC-001 — Duyệt theo mục tiêu và lỗi chặn sử dụng

**Phiên bản mục:** 1.3.0

**Câu hỏi quyết định:** Clip đạt ở những tiêu chí nào và còn lỗi gì?

**Dùng khi:** Khi nhận đầu ra hoặc xuất bản dựng cuối.

**Nguyên lý thực hành:** Duyệt nội dung, hiểu mạch, hình, chuyển động, liên tục, âm và định dạng. Lỗi chặn dùng phụ thuộc bản yêu cầu, không chỉ vẻ đẹp một khung.

**Cách làm:**

1. Đặt tiêu chí trước khi xem bản đẹp nhất.
2. Xem trọn, rồi rà các mốc tiếp xúc/đổi góc/biến đổi.
3. Ghi đạt, chưa đạt hoặc chưa kiểm cùng bằng chứng.
4. Duyệt ở ba quy mô: take riêng, chuỗi điểm nối và toàn phim. Các take đều đạt riêng chưa xác nhận liên tục, nhịp, giá trị kết hoặc sự mệt do lặp trong phim dài.
5. Tách lỗi chặn dùng theo brief, lỗi cần sửa nhưng có thể khắc phục và lựa chọn thẩm mỹ còn tranh luận. Một điểm đẹp không bù việc sai người, sai thao tác hoặc mất bằng chứng bắt buộc.
6. Với chuỗi xử lý AI/hậu kỳ, so nguồn với bản sau xử lý và mở lại tệp xuất. Ghi nguyên nhân/độ phủ khi chưa xác minh được.

**Đánh đổi:** Danh sách quá dài có thể làm chậm; ưu tiên lỗi ảnh hưởng hiểu và trải nghiệm.

**Kiểm tra:**

- Không báo đã kiểm âm nếu chỉ xem hình.
- Tệp xuất cuối được mở lại để kiểm thật.

**Ví dụ tự biên soạn:** Một cảnh đẹp nhưng tay xuyên bát ở mốc chính chưa đạt cảnh thao tác.

**Phản ví dụ / giới hạn:** Một chi tiết nhỏ ngoài vùng nhìn có thể được chấp nhận nếu không phá mục tiêu và phù hợp mức lỗi đã chốt.

**Liên quan:** [ED-008](../kien-thuc/ED-008.json), [SO-008](../kien-thuc/SO-008.json), [EV-004](../kien-thuc/EV-004.json), [QC-010](../kien-thuc/QC-010.json), [YT-012](../kien-thuc/YT-012.json), [QC-007](../kien-thuc/QC-007.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Đạt tại đơn vị nhỏ không tự cộng thành đạt ở quy mô lớn. Cần duyệt các quan hệ và sự tích lũy chỉ xuất hiện khi các clip đứng cạnh nhau.

**Tình huống:** Bốn take xếp đồ đều đẹp, nhưng vật thay số lượng ở cut và đoạn kết không thấy việc đã xong.

**Phần phải giữ:** Nhận diện đã duyệt Hành động chính Kết quả cần đọc

| Phương án | Thực hiện |
| --- | --- |
| A | Chọn từng take đẹp nhất rồi duyệt bằng ảnh đại diện. |
| B | Duyệt take, dựng liền theo trạng thái, kiểm toàn chuỗi và dấu kết; sửa đúng take hoặc khoảng lược. |

**Cách chọn:** Chọn B khi cần sản phẩm dùng được; việc đạt schema/tệp không thay duyệt nội dung.

**Dấu hiệu kiểm trong ca:**

- Có kết quả kiểm cho từng quy mô
- Lỗi chặn dùng không bị bù bằng tổng điểm
- Tệp giao được xem/nghe lại

**Nếu gặp:** Điểm trung bình cao nhưng phim vẫn sai công việc hoặc không liền.

Có thể do: Chấm ảnh riêng Gộp tiêu chí bắt buộc với sở thích

Thử tiếp: Rà một lượt liền theo chức năng câu chuyện, sau đó quay lại đúng mốc lỗi; không tự chấm phần chưa xem.
**Nguồn đối chiếu:** [B022](../../bai-hoc/022-veo-tu-co-ban-den-quy-trinh/README.md), [B033](../../bai-hoc/033-sua-prompt-bi-bo-qua/README.md)

[Bản JSON chuẩn](../kien-thuc/QC-001.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="qc-002"></a>
## QC-002 — Chẩn đoán lỗi trước khi viết lại

**Phiên bản mục:** 1.0.0

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

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Điều gì trong thay đổi có thể giải thích kết quả?

**Dùng khi:** Khi so prompt, đầu vào, model hoặc cách dựng.

**Nguyên lý thực hành:** Giữ các biến có thể giữ, ghi những biến không kiểm soát và lặp theo nhu cầu. Không gọi một cặp đổi nhiều yếu tố là thử một biến. Nguồn ngẫu nhiên, model thay phiên bản, khán giả và phân phối có thể cùng đổi. Phân biệt thử kỹ thuật có kiểm, A/B nền tảng và so quan sát tuần tự.

**Cách làm:**

1. Lưu phiên bản đầu vào, câu lệnh, thiết lập, model và kết quả.
2. Đặt tiêu chí chấm trước; thay một yếu tố từ bản mốc.
3. Ghi số lần thử, số clip dùng được và lỗi mới, kể cả thất bại.
4. Nêu câu hỏi, đầu vào/cấu hình, biến đổi, tiêu chí đặt trước và biến không kiểm được. Khi có ngẫu nhiên đáng kể, đừng kết luận tỷ lệ đạt từ một take.

**Đánh đổi:** Lặp nhiều tốn chi phí; số mẫu nên theo quyết định cần đưa ra và độ biến thiên.

**Kiểm tra:**

- Không suy tỷ lệ thành công từ một clip được chọn đẹp.
- Chi phí được tính trên kết quả sử dụng được, không chỉ giá mỗi lần tạo.
- Kết quả không dùng ngôn ngữ nhân quả mạnh hơn thiết kế và dữ liệu cho phép.

**Ví dụ tự biên soạn:** Giữ ảnh và hành động, chỉ đổi máy tĩnh sang tiến nhẹ; ghi việc model vẫn có ngẫu nhiên.

**Phản ví dụ / giới hạn:** Giữ seed nếu có không tự bảo đảm mọi điều khác không đổi giữa phiên bản/chế độ.

**Liên quan:** [AU-006](../kien-thuc/AU-006.json), [AI-007](../kien-thuc/AI-007.json), [QC-005](../kien-thuc/QC-005.json), [EV-007](../kien-thuc/EV-007.json), [QC-008](../kien-thuc/QC-008.json), [AI-013](../kien-thuc/AI-013.json), [YT-009](../kien-thuc/YT-009.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Giữ một biến là cách làm rõ thử nghiệm, chưa tự bảo đảm nhân quả trong mọi điều kiện.

**Tình huống:** Hai prompt tạo hai clip khác nhau trên một chế độ có ngẫu nhiên.

**Phần phải giữ:** Mục tiêu và các phần đã duyệt trong tình huống.

| Phương án | Thực hiện |
| --- | --- |
| A | Lấy take đẹp hơn làm bằng chứng prompt luôn tốt hơn. |
| B | Báo so take trong điều kiện đã ghi và thử thêm đúng câu hỏi nếu quyết định cần độ tin cao. |

**Cách chọn:** Chọn B; chưa đo nhiều lần thì không có tỷ lệ đạt đáng tin.

**Dấu hiệu kiểm trong ca:**

- Kết quả không dùng ngôn ngữ nhân quả mạnh hơn thiết kế và dữ liệu cho phép.

**Nếu gặp:** Mỗi lần thử đều “thắng” khác nhau.

Có thể do: Ngẫu nhiên hoặc biến cấu hình/đầu vào chưa được giữ.

Thử tiếp: Kiểm nhật ký cấu hình và tiêu chí, rồi chọn thử đủ cho quyết định thay vì khẳng định xu hướng từ một mẫu.

**Phát biểu được đối chiếu:** Thử đồng thời và đổi tuần tự khác thiết kế; kết quả có thể chưa phân định. Nguồn: [SRC-YT-ABTEST](https://support.google.com/youtube/answer/16391400?hl=en).

**Giới hạn nguồn:** Chưa chạy thử trên tài khoản người dùng. Không chứng minh một ảnh luôn thắng hoặc tách được tác dụng từng biến khi đổi cả tổ hợp.
**Nguồn đối chiếu:** [B007](../../bai-hoc/007-muoi-cong-cu-video-ai/README.md), [B023](../../bai-hoc/023-negative-prompt/README.md), [B033](../../bai-hoc/033-sua-prompt-bi-bo-qua/README.md), [SRC-YT-ABTEST](https://support.google.com/youtube/answer/16391400?hl=en)

[Bản JSON chuẩn](../kien-thuc/QC-003.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="qc-004"></a>
## QC-004 — Cập nhật tại chỗ, bản hiện hành và lịch sử Git

**Phiên bản mục:** 1.2.0

**Câu hỏi quyết định:** Đâu là bản hiện hành và thay đổi ảnh hưởng những gì?

**Dùng khi:** Khi nhiều AI hoặc nhiều ngách dùng chung kho.

**Nguyên lý thực hành:** Mỗi mục có một mã và đường dẫn hiện hành. Sửa trực tiếp tệp đó, cập nhật version khi nội dung đổi và ghi một nhật ký thay đổi chung; Git giữ các bản trước. Nhánh ngách đọc core hiện hành, kiểm tác động đến các mã đang dùng và giữ lựa chọn sáng tạo đã chốt.

**Cách làm:**

1. Đọc manifest và mục lục hiện hành trên main; ghi ID@version thực dùng trong kết quả.
2. Sửa JSON chuẩn tại chỗ, xuất lại Markdown/gói ở đường dẫn cố định; không tạo bản sao theo version hoặc ngày.
3. Ghi thay đổi, lý do, mã/tệp bị tác động và trạng thái kiểm trong CHANGELOG.md chung; dùng git diff/commit để xem trước–sau.
4. Đối chiếu phụ thuộc ngách với core hiện hành; cập nhật metadata và liên kết khi đã kiểm. Nguồn quan sát vẫn giữ dấu vết riêng. Thay đổi đảo nguyên tắc sáng tạo phải trình rõ trước áp dụng rộng.

**Đánh đổi:** Đường dẫn luôn cho bản mới nhất nên khi cần tái hiện một kết quả cũ phải dùng commit đã ghi; không đọc main rồi gọi đó là nội dung lịch sử.

**Kiểm tra:**

- Mỗi mã và mỗi gói chỉ có một tệp hiện hành đúng định dạng; không có tệp sao theo version.
- Version, mục lục, liên kết và gói xuất khớp nội dung hiện hành.
- Nhật ký nằm một chỗ; có thể truy vết nội dung cũ bằng Git mà không giữ bản sao trong main.

**Ví dụ tự biên soạn:** Khi bổ sung QC-004, sửa đúng kien-thuc/QC-004.json rồi xuất lại chuyên đề; không tạo QC-004-v2 hoặc một chuyên đề mới chỉ để ghi bản sửa.

**Phản ví dụ / giới hạn:** Hai video nguồn khác nhau cần hai asset ID; đó là hai nguồn thật, không phải lý do giữ hai bản v1/v2 của cùng một tài liệu đang dùng.

**Liên quan:** [EV-002](../kien-thuc/EV-002.json), [EV-006](../kien-thuc/EV-006.json), [QC-006](../kien-thuc/QC-006.json), [QC-007](../kien-thuc/QC-007.json), [AI-010](../kien-thuc/AI-010.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Mã và đường dẫn cố định cho AI biết tài liệu cần đọc; metadata ghi bản hiện hành, Git và một nhật ký chung đảm nhiệm lịch sử.

**Tình huống:** Người dùng bổ sung điều kiện cho một mục đang được Farm tham chiếu.

**Phần phải giữ:** Mã kiến thức và đường dẫn đã dùng. Nguồn quan sát và quyết định sáng tạo hiện hành.

| Phương án | Thực hiện |
| --- | --- |
| A | Tạo một gói mới có hậu tố version và giữ gói cũ cạnh nó để các AI tự chọn. |
| B | Sửa mục hiện hành, kiểm các tham chiếu, xuất đè gói cố định và ghi thay đổi vào CHANGELOG.md. |

**Cách chọn:** Chọn B theo chính sách người dùng; khi cần đối chiếu bản trước, mở commit của Git.

**Dấu hiệu kiểm trong ca:**

- Chỉ có một tệp hiện hành cho mỗi mã/định dạng.
- Farm đọc manifest hiện hành; nội dung nguồn và lựa chọn đã duyệt không bị đổi ngoài phạm vi.

**Nếu gặp:** Hai AI đọc hai tệp tên gần nhau rồi dùng hai nguyên tắc khác nhau.

Có thể do: Còn bản sao theo version ở main. Liên kết làm việc trỏ commit cũ hoặc gói cũ.

Thử tiếp: Kiểm manifest, đường dẫn và liên kết; hợp nhất vào tệp hiện hành, xem lịch sử bằng Git và xuất lại gói.
**Nguồn đối chiếu:** [B019](../../bai-hoc/019-banh-da-hoc-tap-ai/README.md)

[Bản JSON chuẩn](../kien-thuc/QC-004.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="qc-005"></a>
## QC-005 — Dự toán bằng sản phẩm dùng được

**Phiên bản mục:** 1.3.0

**Câu hỏi quyết định:** Tốn bao nhiêu để có một đoạn hoàn chỉnh đạt yêu cầu?

**Dùng khi:** Khi chọn quy trình, số job hoặc ngân sách.

**Nguyên lý thực hành:** Tách chi phí tiền kỳ, sinh thử, tạo lại, hậu kỳ và thời gian duyệt. Ước lượng bằng tỷ lệ dùng được đo từ dự án, kèm khoảng chưa chắc.

**Cách làm:**

1. Ghi độ dài thật dùng trong dựng từ mỗi job.
2. Tính số job cần theo phần sử dụng và số lần thử quan sát được.
3. So phương án ít sinh hơn, cảnh đơn giản hơn hoặc xử lý hậu kỳ.
4. Chi phí mỗi giây dùng thực = tổng chi phí của toàn take thử/sinh/sửa chia cho số giây riêng biệt thực được chấp nhận trong bản dựng. Không cộng các take thay thế cùng một vị trí thành nhiều giây thành phẩm.
5. Tách nhóm shot theo độ khó; ghi riêng sửa âm, ghép, kiểm và chi phí tài sản tái dùng. Tỷ lệ mẫu nhỏ hoặc thử lặp cùng lỗi không bảo đảm giữ nguyên khi mở rộng.

**Đánh đổi:** Chọn giá/lần thấp có thể tăng tổng công sửa; chất lượng vượt nhu cầu cũng có thể lãng phí.

**Kiểm tra:**

- Không lấy 600/8 làm số lần tạo chắc chắn cho phim 10 phút.
- Không đưa giá hiện tại vào nguyên lý khi thiếu nguồn/ngày/điều kiện.
- Dự toán ghi rõ chi phí nào đã/chưa tính và mẫu số giây thuộc bản dựng nào.

**Ví dụ tự biên soạn:** Một job dài nhưng chỉ dùng đoạn ngắn phải tính theo đoạn đạt đã chọn.

**Phản ví dụ / giới hạn:** Một lần thử rẻ chưa chứng minh quy trình rẻ khi nhân lên nhiều shot.

**Liên quan:** [AI-004](../kien-thuc/AI-004.json), [QC-003](../kien-thuc/QC-003.json), [ED-008](../kien-thuc/ED-008.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Đơn vị có ích là phần hoàn chỉnh được dùng. Độ dài được sinh hoặc giá một job chỉ là đầu vào; tỷ lệ được dùng còn phụ thuộc dựng, liên tục và công sửa.

**Tình huống:** Ví dụ tính tự biên soạn: 10 job, mỗi job 5 giây, giá giả định 5 đơn vị/job; bản dựng chỉ dùng 20 giây riêng biệt.

**Phần phải giữ:** Số liệu chỉ là ví dụ, không là giá dịch vụ Không đếm chồng các take thay thế

| Phương án | Thực hiện |
| --- | --- |
| A | Chia 50 đơn vị cho 50 giây sinh và báo 1 đơn vị/giây thành phẩm. |
| B | Chia 50 đơn vị cho 20 giây thật dùng: 2,5 đơn vị/giây, trước nhân công/hậu kỳ chưa tính. |

**Cách chọn:** Dùng B cho đúng mẫu số. Chưa ngoại suy cố định cả phim; đo nhóm shot khó và dự phòng phần chưa biết.

**Dấu hiệu kiểm trong ca:**

- Phép chia và đơn vị rõ
- Có số giây dùng thực
- Chi phí bỏ/thử nằm trong tử số
- Chưa biến số ví dụ thành báo giá

**Nếu gặp:** Dự toán rẻ nhưng hoàn tất phim vượt xa mức dự kiến.

Có thể do: Đếm giây sinh thay giây dùng Bỏ take hỏng và công sửa Gộp shot dễ/khó vào mẫu không tương ứng

Thử tiếp: Lấy một đoạn đã dựng, đối chiếu toàn job và công sửa phục vụ nó; cập nhật theo từng nhóm độ khó.
**Nguồn đối chiếu:** [B007](../../bai-hoc/007-muoi-cong-cu-video-ai/README.md), [B022](../../bai-hoc/022-veo-tu-co-ban-den-quy-trinh/README.md), [B024](../../bai-hoc/024-xau-chuoi-canh/README.md)

[Bản JSON chuẩn](../kien-thuc/QC-005.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="qc-006"></a>
## QC-006 — Từ ví dụ ngách tới kiến thức chung

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Phần nào của quan sát có thể chuyển sang bối cảnh khác?

**Dùng khi:** Sau một lượt phân tích nhiều video hoặc kết quả sản xuất.

**Nguyên lý thực hành:** Ghi mẫu, cơ chế được đề xuất, điều kiện và phản ví dụ. Lặp lại không tự chứng minh nhân quả; nguồn trùng không tăng sức bằng chứng. Chức năng có thể chuyển giao qua nhiều thủ pháp, còn tỷ lệ/cỡ/nhịp thường phụ thuộc lời hứa và tệp. Nguồn nghiên cứu hẹp không tự chứng minh hiệu quả trên YouTube.

**Cách làm:**

1. Tạo ứng viên kiến thức với liên kết đến các quan sát.
2. Thử giải thích mẫu trong một ngách khác và tìm trường hợp ngược.
3. Phân loại bổ sung, sửa điều kiện hay đảo nguyên tắc; trình loại đảo trước áp dụng rộng.
4. Mỗi ứng viên core có điều kiện, bằng chứng thuận/trái, lý giải chức năng, phương án khác và phép thử; sửa đảo nguyên tắc vẫn giữ proposed_reversal.

**Đánh đổi:** Khái quát quá sớm dễ mang gu tác giả thành luật; giữ quá riêng làm khó chuyển giao.

**Kiểm tra:**

- Không dùng số video cố định như điều kiện đủ tự động nâng lên core.
- Nguồn bất đồng và kết quả thử trái ý đồ được giữ.
- Không gọi kiến thức được xác nhận rộng khi mới có các ví dụ cùng tác giả hoặc một thử mô hình.

**Ví dụ tự biên soạn:** Từ chuỗi món ăn hoàn tất đề xuất nguyên lý cho người xem nhận ra kết quả; không nâng tỷ lệ cận của một phim thành chuẩn chung.

**Phản ví dụ / giới hạn:** Cùng thủ pháp có thể phục vụ căng thẳng ở ngách khác; nguyên lý nên giữ điều kiện thay vì đổi tên cảm xúc.

**Liên quan:** [EV-006](../kien-thuc/EV-006.json), [AU-006](../kien-thuc/AU-006.json), [QC-004](../kien-thuc/QC-004.json), [EV-007](../kien-thuc/EV-007.json), [EV-008](../kien-thuc/EV-008.json), [YT-010](../kien-thuc/YT-010.json), [QC-008](../kien-thuc/QC-008.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Nâng kiến thức cần xét chức năng và phản chứng chứ không cộng số video như số phiếu bầu.

**Tình huống:** Một nhóm phim đều có khoảng kết quả sau thao tác.

**Phần phải giữ:** Mục tiêu và các phần đã duyệt trong tình huống.

| Phương án | Thực hiện |
| --- | --- |
| A | Chốt mọi shot kết quả phải dài tám giây. |
| B | Nêu chức năng xác nhận thành quả, giữ thời lượng theo thông tin và tệp. |

**Cách chọn:** Chọn B để chuyển giao; thời lượng mẫu giữ ở báo cáo/ngách tương ứng.

**Dấu hiệu kiểm trong ca:**

- Không gọi kiến thức được xác nhận rộng khi mới có các ví dụ cùng tác giả hoặc một thử mô hình.

**Nếu gặp:** Core dần biến thành công thức của một kênh.

Có thể do: Không tách chức năng khỏi biểu hiện phong cách.

Thử tiếp: Viết phản ví dụ ở một ngách khác và kiểm điều kiện của nguyên lý đề xuất.
**Nguồn đối chiếu:** [B019](../../bai-hoc/019-banh-da-hoc-tap-ai/README.md), [B033](../../bai-hoc/033-sua-prompt-bi-bo-qua/README.md), [SRC-PERCEPTION-EVENTS](https://pmc.ncbi.nlm.nih.gov/articles/PMC3208769/)

[Bản JSON chuẩn](../kien-thuc/QC-006.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="qc-007"></a>
## QC-007 — Duyệt theo công đoạn để không hoàn thiện một cấu trúc còn sai

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Bằng chứng nào đủ để chuyển sang công đoạn tiếp theo?

**Dùng khi:** Sản xuất nhiều shot, nhiều người/AI hoặc liên tục phải quay lại sửa việc đã hoàn thiện.

**Nguyên lý thực hành:** Đặt điểm duyệt theo loại rủi ro: yêu cầu→kịch bản→bản sơ→tài sản/shot khó→take→bản dựng→âm/màu→bản giao. Duyệt đúng thứ cần chứng minh ở mỗi điểm; một ảnh đẹp không xác nhận chuyển động, một bản đúng schema không xác nhận chất lượng phim.

**Cách làm:**

1. Ghi đầu vào, đầu ra và tiêu chí đạt cho từng công đoạn; phần thiếu quan trọng có thể giữ trạng thái tạm để thử, không giả hoàn tất.
2. Kiểm rủi ro khó sửa muộn trước: lời hứa/cấu trúc, nhận diện, hành động then chốt. Có thể tiến song song các phần độc lập nhưng phải giữ phiên bản.
3. Khi một thay đổi quay ngược, chỉ mở lại các phần phụ thuộc; ghi quyết định, lý do và phần vẫn được duyệt.

**Đánh đổi:** Quá nhiều điểm duyệt làm chậm; phim đơn giản có thể gộp công đoạn nhưng vẫn cần phân biệt bằng chứng.

**Kiểm tra:**

- Mỗi kết luận đạt nêu được đã kiểm điều gì và chưa kiểm điều gì.
- Không làm màu/âm tỉ mỉ cho shot có khả năng bị bỏ vì sai cấu trúc chưa giải quyết.

**Ví dụ tự biên soạn:** Trước tạo hàng chục cảnh, duyệt bản sơ hiểu được tiến trình và một thử tiếp xúc khó; chỉ sau đó mở rộng bộ tài sản.

**Phản ví dụ / giới hạn:** Duyệt không buộc khóa sáng tạo vĩnh viễn; phát hiện mới có thể yêu cầu quay lại với tác động được ghi rõ.

**Liên quan:** [AI-009](../kien-thuc/AI-009.json), [QC-001](../kien-thuc/QC-001.json), [QC-004](../kien-thuc/QC-004.json), [QC-005](../kien-thuc/QC-005.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Loại lỗi được phát hiện sớm bằng dạng đầu ra phù hợp thường ít làm mất công đã hoàn thiện. Đây là cách tổ chức công việc, không là chứng nhận hiệu quả đã đo cho dự án.

**Tình huống:** Trước tạo hàng chục cảnh, duyệt bản sơ hiểu được tiến trình và một thử tiếp xúc khó; chỉ sau đó mở rộng bộ tài sản.

**Phần phải giữ:** Mạch đã duyệt và phạm vi bằng chứng từng bước.

| Phương án | Thực hiện |
| --- | --- |
| A | Tạo xong, grade và mix mọi shot rồi mới duyệt kịch bản. |
| B | Duyệt mạch bằng bản sơ, thử rủi ro tạo, sau đó hoàn thiện những take phục vụ bản dựng. |

**Cách chọn:** Chọn B khi thay đổi cấu trúc còn khả năng lớn; A chỉ hợp khi cấu trúc đã được kiểm ở công đoạn khác.

**Dấu hiệu kiểm trong ca:**

- Mỗi kết luận đạt nêu được đã kiểm điều gì và chưa kiểm điều gì.
- Không làm màu/âm tỉ mỉ cho shot có khả năng bị bỏ vì sai cấu trúc chưa giải quyết.

**Nếu gặp:** Mỗi lần sửa kịch bản kéo theo sinh lại và làm màu toàn bộ.

Có thể do: Không có phiên bản duyệt. Rủi ro cấu trúc được để quá muộn.

Thử tiếp: Lập danh sách phụ thuộc của một thay đổi; tách phần buộc sửa khỏi phần có thể giữ.
**Nguồn đối chiếu:** [SRC-YALE-EDIT](https://filmanalysis.yale.edu/editing/)

[Bản JSON chuẩn](../kien-thuc/QC-007.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="qc-008"></a>
## QC-008 — Chuyển mục tiêu thành tiêu chí kiểm và giữ giới hạn kết luận

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Bằng chứng nào thực sự trả lời câu hỏi đang muốn biết?

**Dùng khi:** Duyệt “điện ảnh”, “êm”, “cuốn”, “rõ”, so phiên bản hoặc tổng kết dữ liệu người xem.

**Nguyên lý thực hành:** Mỗi mục tiêu cần tiêu chí tương ứng: hình/âm kiểm tính thực hiện, người xem kiểm khả năng hiểu/cảm nhận, Analytics mô tả hành vi trong hoàn cảnh phân phối. Một phép đo không tự thay thế tất cả mục tiêu.

**Cách làm:**

1. Viết bảng mục tiêu→dấu hiệu→cách thu→giới hạn: “rõ thao tác” kiểm người xem kể bước; “nhất quán vật” kiểm trạng thái; “êm” cần phản hồi phù hợp, không suy riêng từ thời lượng shot.
2. Đặt tiêu chí trước khi nhìn kết quả, ghi tệp người xem/cỡ mẫu/cách chọn/thời điểm và các biến đổi cùng lúc. Mẫu nhỏ hữu ích tìm lỗi nhưng cần giữ giới hạn suy rộng.
3. So phiên bản cùng điều kiện khi có thể; nếu không ngẫu nhiên hoặc không kiểm biến, báo quan sát và giả thuyết. Không biến điểm tự chấm của AI thành hài lòng của khán giả.

**Đánh đổi:** Đo đầy đủ tốn công; ưu tiên câu hỏi quyết định bước tiếp theo, tránh gom nhiều chỉ số nhưng không biết sẽ sửa gì.

**Kiểm tra:**

- Mỗi kết luận dẫn về đúng loại bằng chứng.
- Chỉ số, ý đồ và phản hồi người xem không bị trộn trong cùng một nhãn đạt.

**Ví dụ tự biên soạn:** Bản B làm người thử kể đúng các bước hơn nhưng chưa có dữ liệu xem toàn phim: có thể báo cải thiện khả năng hiểu trong mẫu đó, chưa báo tăng retention hoặc view.

**Phản ví dụ / giới hạn:** Không cần một thử nghiệm thống kê cho mọi lựa chọn thẩm mỹ nhỏ; vẫn có thể quyết định theo mục tiêu, kinh nghiệm và ghi phần chưa được kiểm.

**Liên quan:** [AU-004](../kien-thuc/AU-004.json), [AU-006](../kien-thuc/AU-006.json), [EV-008](../kien-thuc/EV-008.json), [QC-003](../kien-thuc/QC-003.json), [YT-007](../kien-thuc/YT-007.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Kết luận mạnh đến đâu phụ thuộc phép đo trả lời được đến đó. Gắn tiêu chí với quyết định giúp dùng dữ liệu mà không đánh đồng tương quan, tuân thủ kỹ thuật và tác dụng khán giả.

**Tình huống:** Bản B làm người thử kể đúng các bước hơn nhưng chưa có dữ liệu xem toàn phim: có thể báo cải thiện khả năng hiểu trong mẫu đó, chưa báo tăng retention hoặc view.

**Phần phải giữ:** Mục tiêu khả năng hiểu, không đổi thành tăng view.

| Phương án | Thực hiện |
| --- | --- |
| A | AI tự cho điểm 9/10 rồi ghi phim đã được khán giả thích. |
| B | Dùng kiểm chuyên môn cho lỗi thực hiện, hỏi người xem phù hợp cho trải nghiệm và giữ Analytics thành dữ liệu hành vi. |

**Cách chọn:** Chọn B khi đánh giá hiệu quả; điểm chuyên môn có ích nhưng không phải phản ứng của người xem.

**Dấu hiệu kiểm trong ca:**

- Mỗi kết luận dẫn về đúng loại bằng chứng.
- Chỉ số, ý đồ và phản hồi người xem không bị trộn trong cùng một nhãn đạt.

**Nếu gặp:** Báo cáo nhiều điểm đẹp nhưng không giải thích vì sao khán giả chưa thích.

Có thể do: Tiêu chí đo không khớp mục tiêu. Tệp người thử khác tệp cần phục vụ.

Thử tiếp: Chọn một mục tiêu còn thiếu bằng chứng và thu đúng loại phản hồi; đừng chỉ thêm điểm số tự chấm.
**Nguồn đối chiếu:** [SRC-YT-RETENTION](https://support.google.com/youtube/answer/9314415?hl=en), [SRC-YT-CTR](https://support.google.com/youtube/answer/7628154?hl=en), [SRC-YT-PERFORMANCE](https://support.google.com/youtube/answer/16559650)

[Bản JSON chuẩn](../kien-thuc/QC-008.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="qc-009"></a>
## QC-009 — Chọn phương án theo nhiều mục tiêu và ngân sách rủi ro

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Nên đầu tư thử và sửa vào phần nào có ảnh hưởng lớn nhất?

**Dùng khi:** Cân chất lượng, độ tin, cảm xúc, chi phí, thời gian và năng lực công cụ.

**Nguyên lý thực hành:** Chọn theo ràng buộc bắt buộc trước, rồi so các đánh đổi còn lại. Dành thử nghiệm cho lỗi có hậu quả lớn, khó sửa muộn hoặc chưa biết khả năng làm; không cần mọi shot đạt cùng mức phức tạp.

**Cách làm:**

1. Liệt kê điều bắt buộc: đúng hành động/thông tin, phần đã duyệt, thông số giao và ngân sách. Loại phương án không đáp ứng trước khi cộng điểm thẩm mỹ.
2. Với từng rủi ro ghi khả năng chưa chắc, hậu quả nếu lỗi, cách phát hiện sớm và phương án dự phòng. Đây là ước lượng lập kế hoạch, không là xác suất đã đo.
3. Ưu tiên thử cảnh then chốt, giữ cảnh đơn giản đủ tốt và tính chi phí trên take/giây thực dùng cộng công hậu kỳ. Chỉ lặp khi còn một giả thuyết sửa có ý nghĩa.

**Đánh đổi:** Thử quá ít tăng nguy cơ hỏng muộn; thử mọi thứ ở mức cao nhất có thể tiêu hết ngân sách trước khi cấu trúc thành hình.

**Kiểm tra:**

- Phương án chọn giải thích được vì sao phù hợp yêu cầu.
- Không chấm một tổng điểm che việc vi phạm điều bắt buộc hoặc gọi ước lượng là tỷ lệ đạt thật.

**Ví dụ tự biên soạn:** Shot trao vật quyết định kết nên thử tiếp xúc trước; ba shot không gian tĩnh có thể dùng cách tạo đơn giản hơn, vẫn kiểm nhận diện và màu.

**Phản ví dụ / giới hạn:** Không phải cảnh phức tạp hoặc model đắt hơn sẽ phục vụ tốt hơn; cảnh cần thông tin rõ có thể hưởng lợi từ một khung đơn giản.

**Liên quan:** [QC-003](../kien-thuc/QC-003.json), [QC-005](../kien-thuc/QC-005.json), [AI-012](../kien-thuc/AI-012.json), [AI-013](../kien-thuc/AI-013.json), [DR-006](../kien-thuc/DR-006.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Ngân sách và thời gian có hạn; giá trị thử nằm ở việc giảm bất định cho quyết định quan trọng. Cân nhiều mục tiêu làm rõ hy sinh thay vì giấu trong một nhãn “chất lượng”.

**Tình huống:** Shot trao vật quyết định kết nên thử tiếp xúc trước; ba shot không gian tĩnh có thể dùng cách tạo đơn giản hơn, vẫn kiểm nhận diện và màu.

**Phần phải giữ:** Cảnh trao vật then chốt. Ngân sách và phần dự phòng.

| Phương án | Thực hiện |
| --- | --- |
| A | Đầu tư mọi shot cùng số lần tạo lại, bất kể vai trò. |
| B | Thử rủi ro then chốt trước, dùng tiêu chí tối thiểu cho phần phụ và giữ dự phòng có chức năng. |

**Cách chọn:** Chọn B khi rủi ro không đều; số lần thử không có định mức chung bảo đảm chất lượng.

**Dấu hiệu kiểm trong ca:**

- Phương án chọn giải thích được vì sao phù hợp yêu cầu.
- Không chấm một tổng điểm che việc vi phạm điều bắt buộc hoặc gọi ước lượng là tỷ lệ đạt thật.

**Nếu gặp:** Cạn ngân sách khi cảnh chính vẫn chưa làm được.

Có thể do: Chi phí tập trung vào cảnh dễ đẹp. Không có kiểm khả thi hoặc phương án dự phòng.

Thử tiếp: Xếp lại các cảnh theo hậu quả nếu thất bại; thử hoặc đơn giản hóa cảnh chặn cấu trúc trước.
**Nguồn đối chiếu:** [SRC-GOOGLE-I2V](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/best-practice), [SRC-YALE-EDIT](https://filmanalysis.yale.edu/editing/)

[Bản JSON chuẩn](../kien-thuc/QC-009.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="qc-010"></a>
## QC-010 — Ổn định theo thời gian và đúng hành động là hai phép duyệt riêng

**Phiên bản mục:** 1.3.0

**Câu hỏi quyết định:** Clip đẹp từng frame có giữ được vật, trạng thái và hành động qua thời gian không?

**Dùng khi:** Clip đẹp từng frame có giữ được vật, trạng thái và hành động qua thời gian không?

**Nguyên lý thực hành:** Tách vẻ hình từng frame, ổn định nhận diện/nền, nhịp chuyển động và đúng quan hệ vật lý/hành động. Hình mượt vẫn có thể sai việc; hình gần đứng yên ít nhấp nháy vẫn có thể không thực hiện yêu cầu. Kiểm theo mục tiêu thật, không thay bằng một điểm tổng.

**Cách làm:**

1. Xem toàn clip ở tốc độ phát thật, đánh dấu mốc lỗi rồi mới rà frame quanh mốc. Ghi tệp, khoảng xem, vật mốc và mức ảnh hưởng; chưa xem thì để chưa kiểm.
2. Rà theo nhóm: mặt/trang phục/số lượng; hình học/vân/nhãn; nền/bóng/phản chiếu; chuyển động/quỹ đạo/pha chạm; vật bị che rồi lộ và các biến đổi phải có tác nhân.
3. So với yêu cầu hành động và sổ trạng thái, không chỉ độ giống hai frame. Phân biệt rung sáng có nguyên nhân với flicker vô cớ, chuyển động tự nhiên của vật liệu với vân bị trôi.
4. Sau nội suy, upscale, ổn định, sửa vùng hoặc ghép, xem lại vùng biên và toàn clip liên quan. Sau đó dựng liền để kiểm điểm nối theo QC-001.
5. Chọn sửa vùng, cắt, thay take hay tạo lại theo thông tin phải giữ; không giấu mất bằng chứng bắt buộc chỉ để hết nhìn thấy lỗi.

**Đánh đổi:** Ưu tiên theo brief và lỗi ảnh hưởng trải nghiệm; không có ngưỡng điểm chung thay duyệt sản phẩm thực tế.

**Kiểm tra:**

- Số lượng/trạng thái không tự đổi khi che lộ
- Hành động yêu cầu thực sự xảy ra theo thứ tự đúng
- Không gọi rà ảnh mẫu là duyệt toàn chuyển động
- Điểm benchmark nếu có ghi đúng công cụ/phạm vi, tách khỏi hài lòng khán giả

**Ví dụ tự biên soạn:** Một hộp đi sau cánh tay rồi xuất hiện với khóa khác: frame đầu/cuối đều đẹp nhưng nhận diện không ổn định. Một take khác giữ hộp hoàn hảo nhưng không mở nắp cũng chưa đạt yêu cầu mở.

**Phản ví dụ / giới hạn:** Hơi nước, lá, ánh phản chiếu và vật bị biến đổi có thể thay đổi hợp lý; không yêu cầu mọi pixel hoặc trạng thái đứng yên. Phim cách điệu áp quy luật đã chọn của nó.

**Liên quan:** [EV-004](../kien-thuc/EV-004.json), [AI-010](../kien-thuc/AI-010.json), [DR-008](../kien-thuc/DR-008.json), [CO-004](../kien-thuc/CO-004.json), [MO-007](../kien-thuc/MO-007.json), [QC-001](../kien-thuc/QC-001.json), [AI-012](../kien-thuc/AI-012.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Các chiều chất lượng độc lập giúp xác định đúng công đoạn sửa. Chọn theo brief rồi mới đo; kiểm thủ công này không phải đã chạy VBench.

**Tình huống:** Clip giả định mở hộp có mặt đúng, chuyển động êm, nhưng vật bên trong tự nhân đôi khi nắp che khung.

**Phần phải giữ:** Một hộp Một vật bên trong Hành động mở nắp Nhịp thời gian đã duyệt

| Phương án | Thực hiện |
| --- | --- |
| A | Thêm nhòe/nội suy cho mượt và chấm cao theo vẻ chung. |
| B | Rà đoạn che lộ, đối chiếu số lượng/trạng thái rồi sửa take hoặc ghép có kiểm; xem lại hành động và bản dựng. |

**Cách chọn:** Chọn B cho lỗi số lượng. Chỉ sửa độ mượt nếu đó cũng là lỗi được quan sát, không coi mượt là thay thế đúng vật.

**Dấu hiệu kiểm trong ca:**

- Một vật trước/sau che lộ
- Nắp mở thật
- Không sinh lỗi mới quanh vùng sửa

**Nếu gặp:** Clip được đánh giá đẹp/mượt nhưng không dùng được trong chuỗi.

Có thể do: Tiêu chí chỉ nhìn từng ảnh Chưa tách nhận diện, vật lý và yêu cầu hành động

Thử tiếp: Xem toàn take theo từng nhóm tiêu chí và đối chiếu sổ trạng thái; ghi khoảng lỗi trước khi chọn công đoạn sửa.

**Phát biểu được đối chiếu:** VBench tách nhiều chiều gồm nhất quán chủ thể, nhấp nháy theo thời gian và chuyển động. Nguồn: [SRC-VBENCH](https://vchitect.github.io/VBench-project/).

**Giới hạn nguồn:** Bộ rà thủ công của thư viện không phải kết quả chạy VBench hoặc chứng nhận cảm xúc.

**Phát biểu được đối chiếu:** VBench-2.0 mở đánh giá sang vật lý, lẽ thường, cơ thể và khả năng điều khiển. Nguồn: [SRC-VBENCH-2](https://arxiv.org/abs/2503.21755v2).

**Giới hạn nguồn:** Đã đọc tóm tắt, chưa triển khai bộ đo; không dùng kết quả benchmark làm chứng cứ mọi clip của một model đều đúng.
**Nguồn đối chiếu:** [SRC-VBENCH](https://vchitect.github.io/VBench-project/), [SRC-VBENCH-2](https://arxiv.org/abs/2503.21755v2)

[Bản JSON chuẩn](../kien-thuc/QC-010.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).
