# EV — Bằng chứng và chuẩn phân tích

Phiên bản 1.2.1. Tách điều quan sát được, suy luận và đề xuất; giữ mốc thời gian và độ phủ.

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
| [EV-007](#ev-007) | Học từ phim nhiều lượt xem mà không nhầm tương quan với nguyên nhân | trung_cap |
| [EV-008](#ev-008) | Định nghĩa nhãn và đo nhất quán trước khi thống kê video | trung_cap |

<a id="ev-001"></a>
## EV-001 — Tách quan sát, diễn giải và đề xuất

**Phiên bản mục:** 1.0.0

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

**Phiên bản mục:** 1.0.0

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

**Phiên bản mục:** 1.0.0

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

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Phần nào đã thực sự được xem/nghe?

**Dùng khi:** Khi dùng khung lấy mẫu, bản rút gọn hoặc thiếu âm thanh.

**Nguyên lý thực hành:** Tách độ phủ hình chuyển động, ảnh tĩnh và audio. Không suy ra đã xem trọn từ việc có khung đầu–giữa–cuối. Xem đủ frame đứng không tự xác nhận nhịp vận tốc, che/lộ hoặc đồng bộ âm. Khoảng chưa kiểm có thể chứa lỗi quyết định.

**Cách làm:**

1. Ghi các khoảng hình đã xem liên tục, các khung lấy mẫu và khoảng âm đã nghe.
2. Dùng null cùng lý do thiếu, thay vì đoán thông số.
3. Xem lại đoạn quanh điểm cắt, tiếp xúc hoặc biến hình khi kết luận phụ thuộc diễn tiến.
4. Ghi khoảng chuyển động/âm đã tiếp cận; với lỗi AI ưu tiên xem toàn clip và rà thêm vùng tiếp xúc/che lộ, nhưng không lấy rà điểm thay việc xem toàn.

**Đánh đổi:** Xem lại tốn công nhưng ưu tiên vùng có thể thay đổi quyết định.

**Kiểm tra:**

- Không có kết luận âm khi audio chưa được nghe.
- Không gán máy tĩnh tuyệt đối từ ba khung gần giống.
- Kết luận toàn clip chỉ được đưa khi phạm vi xem/nghe phù hợp với kết luận đó.

**Ví dụ tự biên soạn:** Ba khung tay cầm dao cho phép thấy hình thể; chưa đủ xác nhận dao có xuyên tay giữa các khung hay không.

**Phản ví dụ / giới hạn:** Không quan sát thấy người ở ba khung không chứng minh toàn clip chỉ có một người.

**Liên quan:** [EV-001](../kien-thuc/EV-001.json), [CA-004](../kien-thuc/CA-004.json), [QC-001](../kien-thuc/QC-001.json), [AI-013](../kien-thuc/AI-013.json), [DR-008](../kien-thuc/DR-008.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Độ phủ phải gắn với kết luận cụ thể, không chỉ số ảnh đã lấy.

**Tình huống:** Ba ảnh của clip trao hộp đều đúng nhưng chưa có diễn tiến giữa ảnh.

**Phần phải giữ:** Mục tiêu và các phần đã duyệt trong tình huống.

| Phương án | Thực hiện |
| --- | --- |
| A | Báo trao hộp liên tục đã đạt. |
| B | Ghi hình mốc phù hợp, chuyển động/tiếp xúc chưa xác minh. |

**Cách chọn:** Chọn B cho đến khi đã xem khoảng hành động cần kết luận.

**Dấu hiệu kiểm trong ca:**

- Kết luận toàn clip chỉ được đưa khi phạm vi xem/nghe phù hợp với kết luận đó.

**Nếu gặp:** Báo đạt nhưng clip vẫn có tay xuyên ở giữa.

Có thể do: Kiểm chỉ ở các ảnh mốc.

Thử tiếp: Xem toàn diễn tiến và rà khoảng chuyển quyền giữ vật.
**Nguồn đối chiếu:** [B001](../../bai-hoc/001-bon-cau-truc-camera/README.md), [B021](../../bai-hoc/021-lam-chu-cam-xuc/README.md), [B032](../../bai-hoc/032-dieu-khien-am-thanh/README.md)

[Bản JSON chuẩn](../kien-thuc/EV-004.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ev-005"></a>
## EV-005 — Mốc thời gian, khung hình và ranh giới

**Phiên bản mục:** 1.2.1

**Câu hỏi quyết định:** Đơn vị thời gian có chính xác và nối được không?

**Dùng khi:** Khi phân tích từng shot/giây hoặc hợp nhất nhiều phần video.

**Nguyên lý thực hành:** Dùng giây số cho tính toán, giữ timecode hiển thị và frame rate nếu biết. Khoảng thời gian quy ước gồm điểm đầu, không gồm điểm cuối.

**Cách làm:**

1. Đánh dấu điểm vào/ra trên tệp thực; ghi độ chính xác đo.
2. Giữ thời gian cục bộ và offset về bản gốc cho từng phần.
3. Kiểm tra chồng/hở; sự kiện dưới một giây có thể có bản ghi riêng.
4. Chuẩn hóa mọi mốc về cùng trục gốc; duration_seconds là độ dài trục gốc nếu biết, không dùng độ dài đoạn cắt thay cho nó. Chưa biết độ dài gốc thì để null và ghi offset/giới hạn.

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

**Phiên bản mục:** 1.0.0

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

<a id="ev-007"></a>
## EV-007 — Học từ phim nhiều lượt xem mà không nhầm tương quan với nguyên nhân

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Có thể học điều gì từ một video thành công, và điều gì còn chưa biết?

**Dùng khi:** Chọn phim tham khảo, so kênh lớn, giải thích một video hàng triệu lượt xem.

**Nguyên lý thực hành:** Lượt xem xác nhận mức phân phối tích lũy trong một hoàn cảnh; riêng con số đó không xác định thủ pháp nào gây thành công. Tách đặc điểm quan sát được, giả thuyết về tác dụng và bằng chứng hiệu quả.

**Cách làm:**

1. Ghi ngày đo, tuổi video, quy mô/kênh, dạng phim, ngôn ngữ và nguồn lưu lượng nếu tiếp cận được; thiếu thì để chưa biết.
2. Chọn thêm phim cùng nhu cầu nhưng kết quả khác, tránh chỉ lấy những phim nổi tiếng rồi tìm một đặc điểm chung.
3. Đổi đặc điểm thành giả thuyết có thể bác bỏ: làm rõ kết quả thao tác có giúp người xem mới kể lại đúng tiến trình không? Giữ nguồn phản chứng và các phim cùng tác giả không độc lập.

**Đánh đổi:** Mẫu đối chiếu giúp giảm thiên lệch nhưng vẫn có nhiều yếu tố chưa kiểm soát; chưa phải thử nghiệm nhân quả.

**Kiểm tra:**

- Báo cáo tách view công khai khỏi dữ liệu riêng của kênh chưa có.
- Không viết “cận cảnh làm tăng X% view” từ vài phim quan sát.

**Ví dụ tự biên soạn:** Ba phim đồ thủ công nổi bật đều có cận tay. Thay vì chốt tỷ lệ cận, đề xuất kiểm việc người mới hiểu điểm tiếp xúc ở bản có/không có cận.

**Phản ví dụ / giới hạn:** Phim ít view có thể mới đăng hoặc tiếp cận sai tệp; không đủ căn cứ coi kỹ thuật của phim đó kém.

**Liên quan:** [EV-002](../kien-thuc/EV-002.json), [AU-006](../kien-thuc/AU-006.json), [QC-003](../kien-thuc/QC-003.json), [YT-010](../kien-thuc/YT-010.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Đặc điểm hình, độ nổi tiếng, nhu cầu chủ đề, lịch sử kênh và phân phối cùng thay đổi. Chỉ nhìn những phim đã thắng làm mất các trường hợp có cùng thủ pháp nhưng không thắng.

**Tình huống:** Ba phim đồ thủ công nổi bật đều có cận tay. Thay vì chốt tỷ lệ cận, đề xuất kiểm việc người mới hiểu điểm tiếp xúc ở bản có/không có cận.

**Phần phải giữ:** Tài liệu gốc và mốc đo view. Câu hỏi cụ thể về khả năng hiểu điểm tiếp xúc.

| Phương án | Thực hiện |
| --- | --- |
| A | Sao chép tỷ lệ cận của ba phim nổi tiếng và coi đó là chuẩn chung. |
| B | Chọn một điểm cần truyền đạt, thiết kế hai cách thể hiện và kiểm đúng khả năng theo dõi ở tệp mục tiêu. |

**Cách chọn:** Chọn B khi cần ra quyết định kỹ thuật; A chỉ dùng như mô tả phong cách của tập mẫu, không làm quy luật.

**Dấu hiệu kiểm trong ca:**

- Báo cáo tách view công khai khỏi dữ liệu riêng của kênh chưa có.
- Không viết “cận cảnh làm tăng X% view” từ vài phim quan sát.

**Nếu gặp:** Thay phong cách liên tục nhưng không biết vì sao kết quả khác.

Có thể do: Mẫu chỉ gồm phim thắng. Khán giả/tuổi video/nguồn đề xuất khác nhau.

Thử tiếp: Lập bảng các yếu tố khác nhau và chọn một câu hỏi nhỏ để thử ở lần sản xuất tiếp theo.
**Nguồn đối chiếu:** [SRC-YT-CTR](https://support.google.com/youtube/answer/7628154?hl=en), [SRC-YT-RECOMMENDATIONS](https://support.google.com/youtube/answer/16533387?hl=en)

[Bản JSON chuẩn](../kien-thuc/EV-007.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ev-008"></a>
## EV-008 — Định nghĩa nhãn và đo nhất quán trước khi thống kê video

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Hai người hoặc hai AI có đang gắn cùng một nghĩa cho “tĩnh”, “nhịp” và “êm” không?

**Dùng khi:** Phân tích nhiều video, tổng hợp tỷ lệ shot hoặc xây dữ liệu học cho AI khác.

**Nguyên lý thực hành:** Số liệu chỉ so sánh được khi đơn vị, điều kiện gắn nhãn và phạm vi quan sát tương thích. Định nghĩa nhãn bằng dấu hiệu nhìn/nghe được, cho phép chưa xác định và lưu bất đồng.

**Cách làm:**

1. Viết sổ nhãn: định nghĩa, đơn vị, ví dụ đạt/không đạt, nguồn bằng chứng cần. “Máy tĩnh” cần xem chuyển động; không suy từ ba ảnh.
2. Phân biệt tỷ lệ theo số shot với tỷ lệ theo thời lượng; một shot dài có trọng số rất khác. Ghi phần chưa xem trong mẫu số.
3. Cho hai lượt phân tích độc lập trên một phần mẫu đủ đa dạng, so điểm bất đồng rồi sửa định nghĩa; ghi đó là kiểm nhãn, không phải xác nhận ý đồ tác giả.

**Đánh đổi:** Sổ nhãn quá chi li làm chậm nạp; ưu tiên biến ảnh hưởng quyết định trước và giữ bản nhãn gốc khi đổi quy ước.

**Kiểm tra:**

- Mọi tỷ lệ nêu rõ tử số, mẫu số, đơn vị và phần chưa biết.
- Nhãn cảm xúc dự kiến không bị trộn với lời tự báo của người xem.

**Ví dụ tự biên soạn:** Một phim có 2 shot: tĩnh 50 giây và máy đi 10 giây. Theo số shot là 50% tĩnh; theo thời lượng đã xem là khoảng 83,3%.

**Phản ví dụ / giới hạn:** Hai bảng cùng ghi 80% static nhưng một bảng suy từ thumbnail, bảng kia xem toàn chuyển động: không gộp như cùng phép đo.

**Liên quan:** [EV-003](../kien-thuc/EV-003.json), [EV-004](../kien-thuc/EV-004.json), [EV-005](../kien-thuc/EV-005.json), [AU-004](../kien-thuc/AU-004.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Nhãn là một thao tác đo có quy ước. Sai khác trong định nghĩa hoặc mẫu số có thể tạo ra kết luận khác dù cùng video.

**Tình huống:** Một phim có 2 shot: tĩnh 50 giây và máy đi 10 giây. Theo số shot là 50% tĩnh; theo thời lượng đã xem là khoảng 83,3%.

**Phần phải giữ:** Cùng đoạn video, đơn vị và độ phủ khi so nhãn.

| Phương án | Thực hiện |
| --- | --- |
| A | Gộp mọi số phần trăm được nguồn thuật lại. |
| B | Giữ bảng nguồn riêng, chuẩn hóa đơn vị rồi chỉ tổng hợp phần nhãn đủ bằng chứng. |

**Cách chọn:** Chọn B khi so phim; nếu không chuẩn hóa được thì báo bảng song song, không tạo trung bình chung.

**Dấu hiệu kiểm trong ca:**

- Mọi tỷ lệ nêu rõ tử số, mẫu số, đơn vị và phần chưa biết.
- Nhãn cảm xúc dự kiến không bị trộn với lời tự báo của người xem.

**Nếu gặp:** Hai lượt phân tích khác xa nhau về tỷ lệ nhịp nhanh.

Có thể do: Một lượt đếm cut, lượt kia gắn nhãn mật độ sự kiện. Khoảng xem hoặc định nghĩa nhãn khác nhau.

Thử tiếp: Lấy cùng một đoạn, gắn riêng cut và sự kiện có ý nghĩa; xem bất đồng ở định nghĩa hay quan sát.
**Nguồn đối chiếu:** [SRC-YALE-EDIT](https://filmanalysis.yale.edu/editing/), [SRC-PERCEPTION-EVENTS](https://pmc.ncbi.nlm.nih.gov/articles/PMC3208769/)

[Bản JSON chuẩn](../kien-thuc/EV-008.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).
