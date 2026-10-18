# EV — Bằng chứng và chuẩn phân tích

Phiên bản 1.0.0. Tách điều quan sát được, suy luận và đề xuất; giữ mốc thời gian và độ phủ.

[Mục lục](../README.md) · [Chuẩn ra quyết định](../03_RA_QUYET_DINH.md)

Mỗi mục dưới là hướng dẫn có điều kiện. Tác dụng cảm xúc là giả thuyết thiết kế; chưa có thử tạo video hoặc kiểm nghiệm khán giả cho các ví dụ mới. Thuật ngữ xem [từ điển](../TU_DIEN.md).

| Mã | Quyết định | Mức |
| --- | --- | --- |
| [EV-001](#ev-001) | Tách quan sát, diễn giải và đề xuất | co_ban |
| [EV-002](#ev-002) | Nguồn, phiên bản và dấu vết | co_ban |
| [EV-003](#ev-003) | Phân tích từ toàn phim đến sự kiện | co_ban |
| [EV-004](#ev-004) | Độ phủ xem và những điều chưa biết | trung_cap |
| [EV-005](#ev-005) | Mốc thời gian, khung hình và ranh giới | trung_cap |
| [EV-006](#ev-006) | Ưu tiên bằng chứng và giữ bất đồng | nang_cao |

<a id="ev-001"></a>
## EV-001 — Tách quan sát, diễn giải và đề xuất

**Câu hỏi quyết định:** Kết luận này dựa trên điều gì?

**Dùng khi:** Khi tiếp nhận video, ảnh, bảng phân tích hoặc bình luận.

**Nguyên lý thực hành:** Một khung đẹp chỉ chứng minh phần nhìn thấy ở khung đó. Ghi loại bằng chứng trước khi đặt tên tác dụng.

**Cách làm:**

1. Ghi mô tả trung tính về điều thấy/nghe và mốc thời gian.
2. Đặt diễn giải về chức năng/cảm xúc ở trường riêng.
3. Gắn đề xuất sản xuất với mục tiêu và điều kiện cần kiểm.

**Đánh đổi:** Viết thận trọng hơn nhưng giúp tránh truyền lỗi nguồn vào các tác vụ sau.

**Kiểm tra:**

- Mọi nhận xét chuyển động có bằng chứng chuyển động hoặc ghi chưa xác minh.
- Mục cảm xúc nói rõ là ý đồ, giả thuyết hay phản hồi thực tế.

**Ví dụ tự biên soạn:** Ảnh bàn tay trên cửa: ghi vị trí tay; việc đang mở cửa chỉ được xác nhận khi có diễn tiến.

**Phản ví dụ / giới hạn:** Bảng nguồn ghi dolly không đủ để khẳng định camera thực sự tiến.

**Liên quan:** [EV-002](../kien-thuc/EV-002.json), [EV-004](../kien-thuc/EV-004.json), [QC-004](../kien-thuc/QC-004.json)

**Nguồn đối chiếu:** [B015](../../bai-hoc/015-logic-chuyen-dong-vat-ly/README.md), [B033](../../bai-hoc/033-sua-prompt-bi-bo-qua/README.md)

[Bản JSON chuẩn](../kien-thuc/EV-001.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ev-002"></a>
## EV-002 — Nguồn, phiên bản và dấu vết

**Câu hỏi quyết định:** Có tìm lại đúng bằng chứng được dùng không?

**Dùng khi:** Khi nhập, sửa hoặc trích kiến thức.

**Nguyên lý thực hành:** Mỗi nguồn có mã, phiên bản, vị trí và phạm vi đã kiểm. Bản biên soạn không thay thế bản gốc.

**Cách làm:**

1. Ghi mã asset, tên gốc, mã kiểm tra nếu có, nguồn và ngày tiếp nhận.
2. Lưu mốc gốc cùng offset của đoạn cắt; liên kết nhận xét tới nguồn.
3. Ghi thay đổi và lý do; giữ bản trước khi sửa nội dung.

**Đánh đổi:** Lưu dấu vết tăng khối lượng dữ liệu; chỉ lưu bản sao khi cần bảo toàn nguồn.

**Kiểm tra:**

- Một nhận xét truy được về đúng video/ảnh và vị trí; không chỉ tới trang chủ.

**Ví dụ tự biên soạn:** Hai thư mục có ảnh trùng vẫn giữ hai nguồn xuất xứ nhưng không tính thành hai bằng chứng độc lập.

**Phản ví dụ / giới hạn:** Hai ảnh nén khác nhau có thể cùng nội dung; mã băm khác không chứng minh ý tưởng khác.

**Liên quan:** [EV-001](../kien-thuc/EV-001.json), [QC-004](../kien-thuc/QC-004.json), [QC-006](../kien-thuc/QC-006.json)

**Nguồn đối chiếu:** [B019](../../bai-hoc/019-banh-da-hoc-tap-ai/README.md), [B020](../../bai-hoc/020-nam-chia-khoa-nhat-quan/README.md)

[Bản JSON chuẩn](../kien-thuc/EV-002.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ev-003"></a>
## EV-003 — Phân tích từ toàn phim đến sự kiện

**Câu hỏi quyết định:** Chi tiết này đang làm nhiệm vụ gì trong chuỗi?

**Dùng khi:** Khi bóc phim dài, tập phim hoặc nhiều đoạn được tải riêng.

**Nguyên lý thực hành:** Tổ chức toàn phim, phân đoạn, chuỗi hành động, shot và sự kiện trong shot. Quan hệ trước–sau giải thích vai trò của chi tiết.

**Cách làm:**

1. Xác định mục tiêu và biến đổi của toàn phim trước.
2. Chia phân đoạn theo việc/thông tin/trạng thái thay đổi, không chỉ theo phút.
3. Gắn từng shot và sự kiện vào đơn vị cha; ghi quan hệ nối.

**Đánh đổi:** Phân tầng quá vụn làm khó tra cứu; chỉ tách khi có thay đổi đáng dùng.

**Kiểm tra:**

- Shot có đơn vị cha và một chức năng mô tả được.
- Tổng hợp cấp trên không mâu thuẫn với bằng chứng cấp dưới.

**Ví dụ tự biên soạn:** Cận hạt vào đất thuộc việc gieo, rồi thuộc chu kỳ trồng–thu; không chỉ gắn nhãn macro.

**Phản ví dụ / giới hạn:** Một cú máy dài có thể chứa nhiều nhịp diễn biến nhưng vẫn là một shot.

**Liên quan:** [ST-003](../kien-thuc/ST-003.json), [ST-005](../kien-thuc/ST-005.json), [ED-001](../kien-thuc/ED-001.json)

**Nguồn đối chiếu:** [B012](../../bai-hoc/012-cau-truc-camera/README.md), [B017](../../bai-hoc/017-mini-story-ba-nhip/README.md), [B024](../../bai-hoc/024-xau-chuoi-canh/README.md)

[Bản JSON chuẩn](../kien-thuc/EV-003.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ev-004"></a>
## EV-004 — Độ phủ xem và những điều chưa biết

**Câu hỏi quyết định:** Phần nào đã thực sự được xem/nghe?

**Dùng khi:** Khi dùng khung lấy mẫu, bản rút gọn hoặc thiếu âm thanh.

**Nguyên lý thực hành:** Tách độ phủ hình chuyển động, ảnh tĩnh và audio. Không suy ra đã xem trọn từ việc có khung đầu–giữa–cuối.

**Cách làm:**

1. Ghi các khoảng hình đã xem liên tục, các khung lấy mẫu và khoảng âm đã nghe.
2. Dùng null cùng lý do thiếu, thay vì đoán thông số.
3. Xem lại đoạn quanh điểm cắt, tiếp xúc hoặc biến hình khi kết luận phụ thuộc diễn tiến.

**Đánh đổi:** Xem lại tốn công nhưng ưu tiên vùng có thể thay đổi quyết định.

**Kiểm tra:**

- Không có kết luận âm khi audio chưa được nghe.
- Không gán máy tĩnh tuyệt đối từ ba khung gần giống.

**Ví dụ tự biên soạn:** Ba khung tay cầm dao cho phép thấy hình thể; chưa đủ xác nhận dao có xuyên tay giữa các khung hay không.

**Phản ví dụ / giới hạn:** Không quan sát thấy người ở ba khung không chứng minh toàn clip chỉ có một người.

**Liên quan:** [EV-001](../kien-thuc/EV-001.json), [CA-004](../kien-thuc/CA-004.json), [QC-001](../kien-thuc/QC-001.json)

**Nguồn đối chiếu:** [B001](../../bai-hoc/001-bon-cau-truc-camera/README.md), [B021](../../bai-hoc/021-lam-chu-cam-xuc/README.md), [B032](../../bai-hoc/032-dieu-khien-am-thanh/README.md)

[Bản JSON chuẩn](../kien-thuc/EV-004.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ev-005"></a>
## EV-005 — Mốc thời gian, khung hình và ranh giới

**Câu hỏi quyết định:** Đơn vị thời gian có chính xác và nối được không?

**Dùng khi:** Khi phân tích từng shot/giây hoặc hợp nhất nhiều phần video.

**Nguyên lý thực hành:** Dùng giây số cho tính toán, giữ timecode hiển thị và frame rate nếu biết. Khoảng thời gian quy ước gồm điểm đầu, không gồm điểm cuối.

**Cách làm:**

1. Đánh dấu điểm vào/ra trên tệp thực; ghi độ chính xác đo.
2. Giữ thời gian cục bộ và offset về bản gốc cho từng phần.
3. Kiểm tra chồng/hở; sự kiện dưới một giây có thể có bản ghi riêng.

**Đánh đổi:** Khung lấy mẫu định kỳ dễ bỏ sót cú cắt nhanh; chỉ mục từng giây không thay thế phát hiện ranh giới.

**Kiểm tra:**

- end lớn hơn start với shot; thời lượng bằng hiệu hai mốc.
- Thời điểm sự kiện nằm trong shot cha; phần thiếu được khai báo.

**Ví dụ tự biên soạn:** Đoạn bắt đầu ở phút 8 có local 2.4 giây thì mốc toàn phim là 482.4 giây nếu offset đã xác minh.

**Phản ví dụ / giới hạn:** Timecode kiểu phút:giây không phải frame timecode; không cộng số frame khi chưa biết tốc độ.

**Liên quan:** [EV-003](../kien-thuc/EV-003.json), [EV-004](../kien-thuc/EV-004.json), [MO-006](../kien-thuc/MO-006.json)

**Nguồn đối chiếu:** [B017](../../bai-hoc/017-mini-story-ba-nhip/README.md), [B024](../../bai-hoc/024-xau-chuoi-canh/README.md)

[Bản JSON chuẩn](../kien-thuc/EV-005.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ev-006"></a>
## EV-006 — Ưu tiên bằng chứng và giữ bất đồng

**Câu hỏi quyết định:** Khi nguồn mâu thuẫn, ta dùng gì để ra quyết định?

**Dùng khi:** Khi bảng nguồn, video, hướng dẫn mô hình và nguyên tắc kho khác nhau.

**Nguyên lý thực hành:** Ưu tiên chỉ dẫn hiện hành của người dùng và mục tiêu đã chốt cho lựa chọn sáng tạo; sự thật quan sát phải theo bằng chứng phù hợp. Không ép video vào nhãn sẵn có.

**Cách làm:**

1. Ghi hai phát biểu và nguồn của từng phát biểu.
2. Đối chiếu video cho nội dung quan sát; tài liệu đúng phiên bản cho tính năng.
3. Chưa giải được thì giữ bất đồng và chọn phương án có điều kiện, không xóa nguồn bất tiện.

**Đánh đổi:** Nhãn chưa xác định làm thống kê ít đẹp nhưng giữ được độ tin cậy.

**Kiểm tra:**

- Quyết định ghi rõ dựa trên phiên bản nào và điều kiện nào.
- Không nâng ý kiến tác giả thành cấu trúc nội bộ mô hình.

**Ví dụ tự biên soạn:** Bảng gọi shot rộng là cận: giữ nhãn gốc, thêm nhãn kiểm lại và trạng thái đối chiếu.

**Phản ví dụ / giới hạn:** Quy tắc nền chung không được dùng để sửa trái yêu cầu timelapse đã chốt.

**Liên quan:** [EV-001](../kien-thuc/EV-001.json), [AI-007](../kien-thuc/AI-007.json), [QC-006](../kien-thuc/QC-006.json)

**Nguồn đối chiếu:** [B010](../../bai-hoc/010-lam-chu-ngon-ngu-dien-anh/README.md), [B015](../../bai-hoc/015-logic-chuyen-dong-vat-ly/README.md), [B033](../../bai-hoc/033-sua-prompt-bi-bo-qua/README.md)

[Bản JSON chuẩn](../kien-thuc/EV-006.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).
