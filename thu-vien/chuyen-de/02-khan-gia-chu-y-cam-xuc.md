# AU — Khán giả, chú ý và cảm xúc

Phiên bản 1.0.0. Chọn nhu cầu, lượng thông tin, mức mong chờ và trải nghiệm cần kiểm.

[Mục lục](../README.md) · [Chuẩn ra quyết định](../03_RA_QUYET_DINH.md)

Mỗi mục dưới là hướng dẫn có điều kiện. Tác dụng cảm xúc là giả thuyết thiết kế; chưa có thử tạo video hoặc kiểm nghiệm khán giả cho các ví dụ mới. Thuật ngữ xem [từ điển](../TU_DIEN.md).

| Mã | Quyết định | Mức |
| --- | --- | --- |
| [AU-001](#au-001) | Bản yêu cầu trải nghiệm của khán giả | co_ban |
| [AU-002](#au-002) | Dẫn chú ý bằng một trọng tâm đọc được | co_ban |
| [AU-003](#au-003) | Thiết kế mong chờ và trả kết quả | trung_cap |
| [AU-004](#au-004) | Cảm xúc là diễn biến nhiều biến | trung_cap |
| [AU-005](#au-005) | Mật độ thông tin và công sức theo dõi | nang_cao |
| [AU-006](#au-006) | Phản hồi khán giả và giới hạn suy nhân quả | nang_cao |

<a id="au-001"></a>
## AU-001 — Bản yêu cầu trải nghiệm của khán giả

**Câu hỏi quyết định:** Người xem đến đây để nhận điều gì?

**Dùng khi:** Trước khi chọn thủ pháp hoặc đánh giá một phim.

**Nguyên lý thực hành:** Mô tả hoàn cảnh xem, nhu cầu, lời hứa và điều cần tránh. Nhân khẩu học là một phần; không tự suy sở thích từng người từ tuổi/giới.

**Cách làm:**

1. Viết một câu về giá trị khán giả muốn nhận.
2. Chọn trải nghiệm chính và trải nghiệm phụ có thể cùng tồn tại.
3. Phân biệt dữ liệu người xem thực tế với tệp mục tiêu giả định.

**Đánh đổi:** Chọn rõ trải nghiệm có thể giới hạn một số cách gây chú ý ngắn hạn.

**Kiểm tra:**

- Mọi quyết định lớn giải thích được quan hệ với lời hứa.
- Không tự chuyển mục tiêu thư giãn thành bắt buộc không có tò mò.

**Ví dụ tự biên soạn:** Cùng cảnh chờ nước sôi có thể phục vụ nghỉ ngơi, học kỹ thuật hoặc hồi hộp tùy lời hứa.

**Phản ví dụ / giới hạn:** Một người thuộc nhóm tuổi mục tiêu vẫn có thể không thích phong cách của video.

**Liên quan:** [YT-001](../kien-thuc/YT-001.json), [AU-005](../kien-thuc/AU-005.json), [ST-001](../kien-thuc/ST-001.json)

**Nguồn đối chiếu:** [B002](../../bai-hoc/002-prompt-cau-truc/README.md), [B014](../../bai-hoc/014-dao-dien-bang-yeu-cau-ro/README.md)

[Bản JSON chuẩn](../kien-thuc/AU-001.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="au-002"></a>
## AU-002 — Dẫn chú ý bằng một trọng tâm đọc được

**Câu hỏi quyết định:** Ở thời điểm này khán giả cần nhìn/nghe gì trước?

**Dùng khi:** Khi khung có nhiều vật, hành động hoặc lớp âm cạnh tranh.

**Nguyên lý thực hành:** Tổ chức ưu tiên thay vì làm mọi thứ nổi bật. Trọng tâm có thể chuyển qua diễn tiến; phải cho người xem cơ hội theo được.

**Cách làm:**

1. Chỉ ra chi tiết thiết yếu cho hiểu việc hoặc cảm xúc.
2. Chọn vị trí, tương phản, nét, chuyển động hoặc âm để làm rõ nó.
3. Giảm yếu tố cạnh tranh không phục vụ cảnh, rồi thử xem lại ở kích thước nhỏ.

**Đánh đổi:** Cô lập quá mạnh có thể làm mất không gian và quan hệ nhân–quả.

**Kiểm tra:**

- Người xem thử chỉ đúng điều quan trọng mà không được chỉ trước.
- Thông tin nền cần thiết vẫn có thể đọc ở thời điểm phù hợp.

**Ví dụ tự biên soạn:** Tiếng chốt bật và cận tay làm rõ cửa được mở; trong cảnh khác, toàn thân cho thấy người đang do dự.

**Phản ví dụ / giới hạn:** Vật sáng nhất không luôn là ý đồ chú ý; khuôn mặt hoặc chuyển động có thể hút mắt hơn.

**Liên quan:** [CA-003](../kien-thuc/CA-003.json), [CA-007](../kien-thuc/CA-007.json), [SO-005](../kien-thuc/SO-005.json)

**Nguồn đối chiếu:** [B005](../../bai-hoc/005-bay-cu-may/README.md), [B021](../../bai-hoc/021-lam-chu-cam-xuc/README.md)

[Bản JSON chuẩn](../kien-thuc/AU-002.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="au-003"></a>
## AU-003 — Thiết kế mong chờ và trả kết quả

**Câu hỏi quyết định:** Khán giả đang đợi biết hoặc thấy điều gì?

**Dùng khi:** Khi xây mở đầu, quá trình và đoạn kết của một việc.

**Nguyên lý thực hành:** Đặt câu hỏi hoặc khoảng thiếu thông tin đủ hiểu, tiến triển nó rồi cho kết quả tương xứng. Đây là lựa chọn kể chuyện cần kiểm với người xem.

**Cách làm:**

1. Cho biết mục tiêu hoặc vật đang thay đổi.
2. Tạo dấu tiến triển thay vì chỉ kéo dài chờ.
3. Đặt kết quả ở chỗ người xem có thể nhận ra, rồi cân nhắc dư âm.

**Đánh đổi:** Giấu quá lâu có thể gây khó hiểu; lộ hết sớm có thể giảm mong chờ.

**Kiểm tra:**

- Nêu được câu hỏi trước và điều đã được trả sau.
- Không hứa một kết quả rồi bỏ qua việc xác nhận nó.

**Ví dụ tự biên soạn:** Thấy khối bột rời, công đoạn tạo hình rồi chiếc bánh giữ được hình; không phải mọi phim cần bí mật lớn.

**Phản ví dụ / giới hạn:** Phim quan sát có thể tạo hấp dẫn bằng hiện diện và chất liệu mà không giấu đáp án.

**Liên quan:** [ST-002](../kien-thuc/ST-002.json), [ST-004](../kien-thuc/ST-004.json), [ED-005](../kien-thuc/ED-005.json)

**Nguồn đối chiếu:** [B017](../../bai-hoc/017-mini-story-ba-nhip/README.md), [B024](../../bai-hoc/024-xau-chuoi-canh/README.md)

[Bản JSON chuẩn](../kien-thuc/AU-003.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="au-004"></a>
## AU-004 — Cảm xúc là diễn biến nhiều biến

**Câu hỏi quyết định:** Trải nghiệm thay đổi thế nào theo thời gian?

**Dùng khi:** Khi chỉ đạo cảm xúc hoặc lập bản đồ nhịp toàn phim.

**Nguyên lý thực hành:** Tách cảm xúc nhân vật, ý đồ đạo diễn và phản ứng khán giả. Theo dõi mức kích thích, dễ chịu/khó chịu, chắc chắn và gần gũi bằng mô tả có căn cứ.

**Cách làm:**

1. Ghi trạng thái mong muốn ở đầu, chỗ chuyển và cuối.
2. Liên kết mỗi chuyển với thông tin/hành vi/hình/tiếng cụ thể.
3. Đặt cách hỏi người xem và giữ khả năng phản ứng khác ý đồ.

**Đánh đổi:** Một điểm số cảm xúc dễ so nhưng có thể che nhiều trải nghiệm khác nhau.

**Kiểm tra:**

- Không dùng một nụ cười để chứng nhận khán giả thư giãn.
- Các nhịp thay đổi có tác nhân đọc được; mức số nếu dùng phải có định nghĩa.

**Ví dụ tự biên soạn:** Cảnh người lạ xuất hiện có thể tạo tò mò hoặc bất an; tiếng và bối cảnh quyết định cách đọc.

**Phản ví dụ / giới hạn:** Xanh lạnh có thể yên bình; vàng ấm có thể ngột ngạt trong hoàn cảnh khác.

**Liên quan:** [DR-003](../kien-thuc/DR-003.json), [CO-001](../kien-thuc/CO-001.json), [SO-006](../kien-thuc/SO-006.json)

**Nguồn đối chiếu:** [B010](../../bai-hoc/010-lam-chu-ngon-ngu-dien-anh/README.md), [B021](../../bai-hoc/021-lam-chu-cam-xuc/README.md)

[Bản JSON chuẩn](../kien-thuc/AU-004.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="au-005"></a>
## AU-005 — Mật độ thông tin và công sức theo dõi

**Câu hỏi quyết định:** Người xem phải nhớ, đoán và tìm lại bao nhiêu?

**Dùng khi:** Khi nhiều nhân vật, công đoạn hoặc địa điểm làm mạch khó theo.

**Nguyên lý thực hành:** Đánh giá số quan hệ mới và điều khán giả cần giữ trong đầu; nhịp chậm không tự giảm khó hiểu. Đây là phép rà thực hành, không thang đo tâm lý chuẩn hóa.

**Cách làm:**

1. Đặt mốc người, vật, mục tiêu và nơi trước chi tiết khó.
2. Mỗi lần đổi lớn cần một tín hiệu đủ rõ.
3. Cắt thông tin dư nhưng giữ bước nối cần cho hiểu nguyên nhân.

**Đánh đổi:** Giải thích quá rõ có thể mất tinh tế; cần cân bằng theo người xem mục tiêu.

**Kiểm tra:**

- Người xem thử kể được việc đang làm và điều vừa thay đổi.
- Không phải nhìn lại chỉ để biết ai đang cầm vật gì.

**Ví dụ tự biên soạn:** Sau đổi phòng, một khung trung cho thấy người và chiếc khay trước khi cắt vào tay.

**Phản ví dụ / giới hạn:** Dựng nhanh có thể dễ hiểu nếu mỗi khung bổ sung một thông tin rõ và quan hệ giữ ổn.

**Liên quan:** [EV-003](../kien-thuc/EV-003.json), [ED-003](../kien-thuc/ED-003.json), [ST-005](../kien-thuc/ST-005.json)

**Nguồn đối chiếu:** [B012](../../bai-hoc/012-cau-truc-camera/README.md), [B017](../../bai-hoc/017-mini-story-ba-nhip/README.md)

[Bản JSON chuẩn](../kien-thuc/AU-005.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="au-006"></a>
## AU-006 — Phản hồi khán giả và giới hạn suy nhân quả

**Câu hỏi quyết định:** Có bằng chứng người xem nhận được trải nghiệm mong muốn không?

**Dùng khi:** Khi đánh giá phản hồi nhóm thử hoặc số liệu sau xuất bản.

**Nguyên lý thực hành:** Ghi tách ý đồ, hành vi xem và lời tự báo cảm xúc. Một chỉ số không đủ chứng minh tác dụng nghệ thuật hoặc nguyên nhân.

**Cách làm:**

1. Hỏi cụ thể về đoạn/mốc thay vì gợi câu trả lời tốt.
2. So kết quả giữa nhóm và hoàn cảnh tương đồng khi có thể.
3. Ghi cả phản ứng ngoài ý đồ và các yếu tố khác đã đổi.

**Đánh đổi:** Dữ liệu nhỏ giúp phát hiện vấn đề, chưa đủ kết luận cho cả thị trường.

**Kiểm tra:**

- Không đổi giữ chân cao thành bằng chứng thư giãn.
- Không suy chẩn đoán cá nhân từ bình luận hoặc cách xem.

**Ví dụ tự biên soạn:** Một đoạn được xem lại: hỏi vì đẹp, muốn học thao tác hay vì chưa hiểu trước khi chỉnh nhịp.

**Phản ví dụ / giới hạn:** Người im lặng không đồng nghĩa hài lòng; bình luận công khai không đại diện mọi người xem.

**Liên quan:** [YT-003](../kien-thuc/YT-003.json), [YT-005](../kien-thuc/YT-005.json), [QC-003](../kien-thuc/QC-003.json)

**Nguồn đối chiếu:** [SRC-YT-RETENTION](https://support.google.com/youtube/answer/9314415?hl=en)

[Bản JSON chuẩn](../kien-thuc/AU-006.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).
