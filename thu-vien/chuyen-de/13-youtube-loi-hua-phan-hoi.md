# YT — YouTube: lời hứa và phản hồi

Phiên bản 1.0.0. Kết nối cách giới thiệu phim, trải nghiệm xem và dữ liệu khán giả.

[Mục lục](../README.md) · [Chuẩn ra quyết định](../03_RA_QUYET_DINH.md)

Mỗi mục dưới là hướng dẫn có điều kiện. Tác dụng cảm xúc là giả thuyết thiết kế; chưa có thử tạo video hoặc kiểm nghiệm khán giả cho các ví dụ mới. Thuật ngữ xem [từ điển](../TU_DIEN.md).

| Mã | Quyết định | Mức |
| --- | --- | --- |
| [YT-001](#yt-001) | Lời hứa ảnh thu nhỏ, tiêu đề và mở đầu | co_ban |
| [YT-002](#yt-002) | Tỷ lệ nhấp và bối cảnh phân phối | trung_cap |
| [YT-003](#yt-003) | Giữ chân theo đoạn và giả thuyết sửa | trung_cap |
| [YT-004](#yt-004) | Tính mới, sự quen thuộc và giá trị trở lại | trung_cap |
| [YT-005](#yt-005) | Phản hồi trải nghiệm và nhóm người xem | nang_cao |
| [YT-006](#yt-006) | Vòng học từ xuất bản về quyết định sáng tạo | nang_cao |

<a id="yt-001"></a>
## YT-001 — Lời hứa ảnh thu nhỏ, tiêu đề và mở đầu

**Câu hỏi quyết định:** Điều người xem bấm vào có được phim thực hiện không?

**Dùng khi:** Khi giới thiệu hoặc mở một video YouTube.

**Nguyên lý thực hành:** Xác lập giá trị/thông tin thật của phim và sớm cho tín hiệu phù hợp. Không có một kiểu mở đầu bắt buộc cho mọi tệp xem.

**Cách làm:**

1. Viết lời hứa trong một câu.
2. Chọn hình/chi tiết mở giúp nhận ra giá trị ấy.
3. Ghi nơi phim thực sự trả lời hứa; rà sự chênh giữa giới thiệu và nội dung.

**Đánh đổi:** Lộ kết quả sớm có thể giảm bí mật nhưng tăng rõ lợi ích; chọn theo lời hứa.

**Kiểm tra:**

- Không hứa thu hoạch một thứ rồi toàn phim chủ yếu việc khác không liên quan.
- Không dùng yếu tố sốc trái trải nghiệm đã chốt chỉ để kéo nhấp.

**Ví dụ tự biên soạn:** Video thư giãn có thể mở bằng nơi chốn và việc dễ hiểu; phim điều tra có thể mở bằng câu hỏi.

**Phản ví dụ / giới hạn:** Không phải mọi video phải mở bằng thành phẩm hoặc cao trào.

**Liên quan:** [ST-008](../kien-thuc/ST-008.json), [AU-001](../kien-thuc/AU-001.json), [YT-002](../kien-thuc/YT-002.json)

**Nguồn đối chiếu:** [SRC-YT-RETENTION](https://support.google.com/youtube/answer/9314415?hl=en)

[Bản JSON chuẩn](../kien-thuc/YT-001.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="yt-002"></a>
## YT-002 — Tỷ lệ nhấp và bối cảnh phân phối

**Câu hỏi quyết định:** Tỷ lệ nhấp đang được so trong điều kiện nào?

**Dùng khi:** Khi đánh giá thumbnail/tiêu đề.

**Nguyên lý thực hành:** CTR là tỷ lệ nhấp theo lượt hiển thị được nền tảng tính. Khán giả và nguồn lưu lượng có thể thay đổi nên không quy mọi chênh lệch cho ảnh/tiêu đề.

**Cách làm:**

1. Ghi khoảng thời gian, số hiển thị và nguồn truy cập.
2. So các trường hợp đủ tương đồng và đủ dữ liệu cho quyết định.
3. Đọc cùng trải nghiệm sau nhấp và mục tiêu kênh.

**Đánh đổi:** Một chỉ số dễ theo dõi nhưng có thể làm bỏ qua giá trị người xem thực nhận.

**Kiểm tra:**

- Không chia tổng view cho mọi impression rồi coi đó luôn là CTR báo cáo.
- Không lấy một ngưỡng chung làm chứng nhận tốt/xấu.

**Ví dụ tự biên soạn:** Hai video có nguồn tìm kiếm và trang chủ khác nhau cần xét phân phối trước khi đổi gu thiết kế.

**Phản ví dụ / giới hạn:** Một tỷ lệ thấp hơn khi tiếp cận rộng hơn không tự chứng minh ảnh kém.

**Liên quan:** [YT-001](../kien-thuc/YT-001.json), [YT-003](../kien-thuc/YT-003.json), [AU-006](../kien-thuc/AU-006.json)

**Nguồn đối chiếu:** [SRC-YT-CTR](https://support.google.com/youtube/answer/7628154?hl=en)

[Bản JSON chuẩn](../kien-thuc/YT-002.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="yt-003"></a>
## YT-003 — Giữ chân theo đoạn và giả thuyết sửa

**Câu hỏi quyết định:** Ở mốc nào hành vi xem thay đổi, và có những giải thích nào?

**Dùng khi:** Khi có dữ liệu giữ chân của video thực.

**Nguyên lý thực hành:** Đỉnh/hõm là dấu để xem lại, không phải kết luận nguyên nhân. Liên kết biểu đồ với diễn tiến và hoàn cảnh khán giả.

**Cách làm:**

1. Gắn đoạn biến đổi vào shot/chuỗi cụ thể.
2. Đưa ít nhất hai cách giải thích hợp lý trước khi sửa.
3. So phản hồi, nguồn truy cập và các video liên quan khi có.

**Đánh đổi:** Sửa theo mọi gợn nhỏ có thể làm mất phong cách vì dữ liệu nhiễu.

**Kiểm tra:**

- Không gọi đỉnh là chắc chắn thích nhất hoặc thư giãn nhất.
- Không suy một cảnh gây rời nếu nhiều thứ cùng đổi ở điểm đó.

**Ví dụ tự biên soạn:** Đỉnh xem lại có thể do thao tác đẹp hoặc do chưa rõ; hai nguyên nhân dẫn tới hai cách sửa khác.

**Phản ví dụ / giới hạn:** Người xem để nền có thể có hành vi khác người theo dõi từng thao tác.

**Liên quan:** [AU-006](../kien-thuc/AU-006.json), [ED-001](../kien-thuc/ED-001.json), [QC-003](../kien-thuc/QC-003.json)

**Nguồn đối chiếu:** [SRC-YT-RETENTION](https://support.google.com/youtube/answer/9314415?hl=en)

[Bản JSON chuẩn](../kien-thuc/YT-003.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="yt-004"></a>
## YT-004 — Tính mới, sự quen thuộc và giá trị trở lại

**Câu hỏi quyết định:** Tập mới cho người xem điều quen và điều mới nào?

**Dùng khi:** Khi xây loạt video hoặc thế giới nhân vật tiếp diễn.

**Nguyên lý thực hành:** Giữ lời hứa và những điểm nhận diện có giá trị, thay đổi công việc, mùa, quan hệ hoặc cách khám phá. Không đồng nhất nhất quán với sao chép nguyên tập.

**Cách làm:**

1. Ghi điều cần giữ xuyên tập và phần có thể biến.
2. Cho người mới hiểu tập hiện tại mà không cần lịch sử.
3. Theo dõi lý do người xem quay lại khi có dữ liệu.

**Đánh đổi:** Đổi nhiều mất nhận diện; lặp nhiều dễ thiếu khám phá.

**Kiểm tra:**

- Không gán lý do quay lại chỉ từ số người trở lại.
- Tập độc lập vẫn có kết quả đáng nhận.

**Ví dụ tự biên soạn:** Cùng căn nhà và nhân vật nhưng mùa vụ/món ăn thay đổi.

**Phản ví dụ / giới hạn:** Kênh khám phá có thể cần độ mới cao hơn kênh tìm cảm giác quen; phải theo hồ sơ ngách.

**Liên quan:** [ST-008](../kien-thuc/ST-008.json), [AI-002](../kien-thuc/AI-002.json), [AU-001](../kien-thuc/AU-001.json)

**Nguồn đối chiếu:** [B003](../../bai-hoc/003-khoa-thiet-ke-nhan-vat/README.md), [B024](../../bai-hoc/024-xau-chuoi-canh/README.md)

[Bản JSON chuẩn](../kien-thuc/YT-004.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="yt-005"></a>
## YT-005 — Phản hồi trải nghiệm và nhóm người xem

**Câu hỏi quyết định:** Ai được phục vụ tốt và ai thấy khác với ý đồ?

**Dùng khi:** Khi đọc bình luận, khảo sát hoặc nhóm thử.

**Nguyên lý thực hành:** Ghi lời phản hồi cùng đoạn, hoàn cảnh và cách thu; tách thích, hiểu, tò mò, thư giãn, buồn và khó chịu khi cần.

**Cách làm:**

1. Hỏi mở trước rồi mới hỏi mục tiêu cụ thể.
2. Giữ phản hồi tiêu cực/trái dự đoán.
3. Tổng hợp theo bằng chứng, không tự suy đặc điểm sức khỏe hay nhân khẩu học.

**Đánh đổi:** Người chịu trả lời có thể khác người không trả lời; kết quả không tự đại diện toàn kênh.

**Kiểm tra:**

- Không biến cảm giác tự báo thành chẩn đoán hoặc hiệu quả điều trị.
- Không gọi mọi phản hồi ấm áp là thư giãn.

**Ví dụ tự biên soạn:** Người nói cảnh gia đình làm nhớ nhà: hỏi là dễ chịu hay buồn trước khi coi đó là hiệu quả đạt.

**Phản ví dụ / giới hạn:** Một video giữ chân tốt vẫn có thể gây mệt; cần hỏi đúng trải nghiệm.

**Liên quan:** [AU-006](../kien-thuc/AU-006.json), [YT-003](../kien-thuc/YT-003.json), [QC-006](../kien-thuc/QC-006.json)

**Nguồn đối chiếu:** [SRC-YT-RETENTION](https://support.google.com/youtube/answer/9314415?hl=en)

[Bản JSON chuẩn](../kien-thuc/YT-005.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="yt-006"></a>
## YT-006 — Vòng học từ xuất bản về quyết định sáng tạo

**Câu hỏi quyết định:** Dữ liệu sau đăng sẽ thay đổi quyết định nào ở tập tới?

**Dùng khi:** Khi hoàn thành một nhóm video và rà hướng kênh.

**Nguyên lý thực hành:** Đặt giả thuyết, thay có chủ đích, đọc kết quả rồi cập nhật điều kiện dùng. Không thay toàn bộ định vị sau một lần dữ liệu trái mong đợi.

**Cách làm:**

1. Chọn một vấn đề có ý nghĩa với lời hứa.
2. Ghi phương án, điều giữ, dữ liệu cần và cách kết luận trước.
3. Cập nhật hồ sơ ngách; chỉ đề xuất core nếu điều kiện khái quát được nêu.

**Đánh đổi:** Học quá chậm có thể lặp lỗi; đổi quá nhanh khó biết nguyên nhân.

**Kiểm tra:**

- Có nhật ký quyết định tiếp theo thay vì chỉ báo chỉ số.
- Không tuyên bố phiên bản thắng khi dữ liệu chưa đủ hoặc khác đối tượng.

**Ví dụ tự biên soạn:** Thử cách làm rõ kết quả công việc và hỏi khả năng theo dõi, thay vì chỉ thêm nhạc ở mọi tập.

**Phản ví dụ / giới hạn:** Một thay đổi cần nhiều quan sát mới kết luận; chưa biết cũng là kết quả hợp lệ.

**Liên quan:** [QC-003](../kien-thuc/QC-003.json), [QC-006](../kien-thuc/QC-006.json), [AU-001](../kien-thuc/AU-001.json)

**Nguồn đối chiếu:** [SRC-YT-CTR](https://support.google.com/youtube/answer/7628154?hl=en), [SRC-YT-RETENTION](https://support.google.com/youtube/answer/9314415?hl=en)

[Bản JSON chuẩn](../kien-thuc/YT-006.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).
