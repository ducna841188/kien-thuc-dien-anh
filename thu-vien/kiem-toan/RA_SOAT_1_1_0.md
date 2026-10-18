# Rà soát tầng 1 — FILM-KB 1.1.0

Ngày 18/10/2026. [Thư viện](../README.md) · [Dấu vết từng mục](ra-soat-1.1.0.json) · [Nhật ký](../CHANGELOG.md).

## Kết luận chuyên môn

Bản 1.0.0 có nền tốt về quyết định theo mục tiêu, phân biệt bằng chứng, giữ phần đã duyệt và tách nền chung khỏi ngách. Điểm yếu là nhiều mục dừng ở nguyên lý ngắn; AI khác có thể nhắc đúng thuật ngữ nhưng còn thiếu cách chọn khi các yêu cầu kéo khác hướng hoặc đầu ra gặp lỗi. Bản này thêm chiều vận hành, không đảo nguyên tắc đang dùng.

**90 mục cũ đã rà: 60 giữ nguyên, 30 làm rõ; thêm 40 mục, tổng 130.** Mỗi mục mới/làm rõ có ca so hai phương án, phần phải giữ, dấu kiểm và chẩn đoán. Sổ nguồn có 27 tài liệu ngoài: 14 đã có và 13 bổ sung trong lượt này.

## Những khoảng trống được xử lý

| Khoảng trống trước | Cải tiến | Mã tiêu biểu |
| --- | --- | --- |
| Có chú ý/nhịp nhưng thiếu phân biệt cut và sự kiện | Bổ sung cách định hướng khi đổi việc, eye trace và thời gian nhận diện | AU-007, ED-009, ED-010 |
| Kể chuyện ngắn gọn nhưng khó xử lý phim ít xung đột | Thêm mạch quan hệ, lặp biến đổi, giá trị nhỏ và mô-típ | ST-009–012, AU-008–009 |
| Diễn xuất dễ thành nhãn cảm xúc; tiếp xúc còn tổng quát | Mục tiêu/chiến thuật/ý ngầm, chuyển lực và dấu đời sống có chức năng | DR-007–009 |
| Quang học/sáng có nguyên lý nhưng ít điều kiện so | Thêm vùng nét nhiều biến, fps/phơi/nhòe, phơi sáng và suy giảm nguồn | CA-012, MO-007, LI-007–008 |
| Màu cần quy trình cụ thể cho nhiều nguồn AI/quay thật | Cân trắng, cân/khớp trước look, nhận diện miền dữ liệu | CO-007–009 |
| Âm có lớp nhưng thiếu chẩn đoán đỉnh, che nhau và phân câu | Automation/EQ/động theo sự kiện, không gian và nhạc có chức năng | SO-009–011 |
| Prompt/job chưa thành một chuỗi sản xuất đủ rõ | Bản sơ, sổ trạng thái, khả thi ảnh đầu, chọn hậu kỳ và hiệu chỉnh công cụ | AI-009–013, QC-007–009 |
| YouTube dễ bị đọc thành tối ưu CTR/retention | Ba câu hỏi hiệu suất, ý tưởng/góc, thiết kế A/B, học phim nổi bật và tiếp cận | YT-007–011, EV-007–008 |

## Phạm vi theo chuyên đề

| Chuyên đề | Cũ | Giữ nguyên | Làm rõ | Thêm | Hiện tại |
| --- | ---: | ---: | ---: | ---: | ---: |
| [EV — Bằng chứng và chuẩn phân tích](../chuyen-de/01-bang-chung-va-phan-tich.md) | 6 | 5 | 1 | 2 | 8 |
| [AU — Khán giả, chú ý và cảm xúc](../chuyen-de/02-khan-gia-chu-y-cam-xuc.md) | 6 | 3 | 3 | 3 | 9 |
| [ST — Kịch bản và cấu trúc](../chuyen-de/03-kich-ban-va-cau-truc.md) | 8 | 4 | 4 | 4 | 12 |
| [DR — Đạo diễn, diễn xuất và dàn cảnh](../chuyen-de/04-dao-dien-dan-canh.md) | 6 | 5 | 1 | 3 | 9 |
| [CA — Bố cục, máy quay và quang học](../chuyen-de/05-bo-cuc-may-quay-quang-hoc.md) | 10 | 8 | 2 | 2 | 12 |
| [MO — Chuyển động và thời gian](../chuyen-de/06-chuyen-dong-thoi-gian.md) | 6 | 5 | 1 | 2 | 8 |
| [LI — Ánh sáng](../chuyen-de/07-anh-sang.md) | 6 | 4 | 2 | 2 | 8 |
| [CO — Màu sắc và thiết kế hình ảnh](../chuyen-de/08-mau-sac-thiet-ke-hinh.md) | 6 | 4 | 2 | 3 | 9 |
| [ED — Dựng phim và điều khiển nhịp](../chuyen-de/09-dung-phim-va-nhip.md) | 8 | 6 | 2 | 3 | 11 |
| [SO — Âm thanh, nhạc và lời kể](../chuyen-de/10-am-thanh-nhac-loi.md) | 8 | 6 | 2 | 3 | 11 |
| [AI — Sản xuất bằng AI](../chuyen-de/11-san-xuat-bang-ai.md) | 8 | 5 | 3 | 5 | 13 |
| [QC — Kiểm tra và học từ kết quả](../chuyen-de/12-kiem-tra-va-hoc-tu-ket-qua.md) | 6 | 3 | 3 | 3 | 9 |
| [YT — YouTube: lời hứa và phản hồi](../chuyen-de/13-youtube-loi-hua-phan-hoi.md) | 6 | 2 | 4 | 5 | 11 |

## 30 mục làm rõ và lý do

| Mã | Điểm được làm rõ |
| --- | --- |
| [AI-003](../kien-thuc/AI-003.json) | Hợp đồng hành động cần trạng thái vào/ra và điểm chuyển lực, không chỉ chuỗi động từ. |
| [AI-007](../kien-thuc/AI-007.json) | Prompt, giao diện dịch vụ và kết quả thực cần ba lớp ghi nhận khác nhau. |
| [AI-008](../kien-thuc/AI-008.json) | Sửa tối thiểu còn cần điều kiện dừng để tránh lặp vô hạn bằng câu chữ. |
| [AU-001](../kien-thuc/AU-001.json) | Hồ sơ khán giả là giả thuyết vận hành cần được đối chiếu, không mô tả chắc mọi cá nhân. |
| [AU-002](../kien-thuc/AU-002.json) | Độ nổi thị giác cần phục vụ thông tin ở đúng thời điểm, không chỉ làm ảnh có điểm sáng. |
| [AU-004](../kien-thuc/AU-004.json) | Cần tránh một đường cảm xúc đẹp trên giấy bị hiểu thành dữ liệu đã đo. |
| [CA-001](../kien-thuc/CA-001.json) | Cỡ cảnh là quyết định lượng thông tin; tỷ lệ cận/toàn không tự định nghĩa một phong cách tốt. |
| [CA-008](../kien-thuc/CA-008.json) | So quang học cần giữ rõ biến vị trí máy; thay tiêu cự từ cùng vị trí khác với lùi máy để bù khung. |
| [CO-001](../kien-thuc/CO-001.json) | Màu dùng được ngay phải giữ quan hệ độ sáng, vật liệu và bối cảnh, không gán bảng cảm xúc tuyệt đối. |
| [CO-006](../kien-thuc/CO-006.json) | Nguồn AI khác quay thật ở dữ liệu có thể còn lại, nên không mặc định quy trình camera Log. |
| [DR-001](../kien-thuc/DR-001.json) | Tính quan sát được phải nối với mục tiêu và phản ứng, tránh ra lệnh diễn bằng danh sách nét mặt. |
| [ED-001](../kien-thuc/ED-001.json) | Đếm cut không mô tả hết công sức theo dõi hoặc giá trị thời gian. |
| [ED-002](../kien-thuc/ED-002.json) | Điểm cắt cần xét pha hành động và thời gian nhận diện của shot mới. |
| [EV-004](../kien-thuc/EV-004.json) | Độ phủ phải gắn với kết luận cụ thể, không chỉ số ảnh đã lấy. |
| [LI-002](../kien-thuc/LI-002.json) | Độ mềm gắn kích thước biểu kiến nguồn, không đơn giản là đèn yếu hoặc trời ấm. |
| [LI-003](../kien-thuc/LI-003.json) | Tương phản không bắt buộc giải bằng sơ đồ ba đèn; môi trường hắt và che sáng có vai trò lớn. |
| [MO-006](../kien-thuc/MO-006.json) | Thời gian kể chuyện và cách lấy mẫu/đổi tốc cần được ghi riêng. |
| [QC-003](../kien-thuc/QC-003.json) | Giữ một biến là cách làm rõ thử nghiệm, chưa tự bảo đảm nhân quả trong mọi điều kiện. |
| [QC-004](../kien-thuc/QC-004.json) | Phiên bản bản phát hành và phiên bản từng mục phải được ghi tách để các ngách giữ ghim ổn định. |
| [QC-006](../kien-thuc/QC-006.json) | Nâng kiến thức cần xét chức năng và phản chứng chứ không cộng số video như số phiếu bầu. |
| [SO-005](../kien-thuc/SO-005.json) | Đủ lớn, rõ lời và thoải mái là ba câu hỏi có thể cần cách sửa khác nhau. |
| [SO-006](../kien-thuc/SO-006.json) | Nhạc nên có chức năng và phân câu; lời nhắc “thư giãn” không đủ để đặt mọi đoạn cùng một tông. |
| [ST-002](../kien-thuc/ST-002.json) | Một mục tiêu nhỏ có thể tạo lực theo dõi nếu giá trị và lựa chọn đọc được. |
| [ST-003](../kien-thuc/ST-003.json) | Nhịp cần đo bằng thay đổi có chức năng thay vì mỗi dòng một động tác. |
| [ST-007](../kien-thuc/ST-007.json) | Kể không lời cần bằng chứng và quan hệ, không phải chỉ bỏ voiceover. |
| [ST-008](../kien-thuc/ST-008.json) | Mở và kết phải cùng trả một lời hứa nhưng không cần cùng một công thức. |
| [YT-001](../kien-thuc/YT-001.json) | Mở hấp dẫn cần giao giá trị đúng lời hứa sớm nhưng không có một cấu trúc hook bắt buộc cho mọi dạng phim. |
| [YT-002](../kien-thuc/YT-002.json) | CTR cần được đọc cùng ngữ cảnh phân phối và phần trải nghiệm sau nhấp. |
| [YT-003](../kien-thuc/YT-003.json) | Điểm giữ chân cần nối với mốc thông tin và nhiều giả thuyết cạnh tranh. |
| [YT-006](../kien-thuc/YT-006.json) | Vòng học cần quay về quyết định sáng tạo cụ thể và đúng loại bằng chứng. |

## Cách đối chiếu căn cứ

Nguồn sơ cấp mới gồm nghiên cứu gốc về phân đoạn sự kiện; tài liệu nhà sản xuất về quang học/phơi sáng/cân trắng; ACES, Adobe và hướng dẫn YouTube. Sổ nguồn ghi phần đã đọc, nguồn chỉ có trích đoạn và giới hạn của mỗi tài liệu. Các phương án sáng tạo/chẩn đoán trong kho là tổng hợp có điều kiện; không gắn nhãn đã được nghiên cứu chứng minh cho mọi ví dụ.

Các làm rõ chính: 24 fps/180° không là điều kiện bắt buộc; số mm cần điều kiện vị trí/định dạng; vùng nét khác nhòe chuyển động; clip AI không tự là Log/RAW; thời lượng shot/cut không thay đo cảm xúc; nhiều view không tự chứng minh nguyên nhân. Đây là bổ sung điều kiện và chiều thao tác cho nguyên tắc v1, không đổi hướng sáng tạo hiện hành.

## Khả năng dùng ngay

- [Vòng sản xuất](../06_VAN_HANH_SAN_XUAT.md): đầu vào, đầu ra, điểm duyệt và cách quay lại sửa.
- [Bảng phép kiểm](../07_KIEM_TRA_TRAI_NGHIEM.md): từ mục tiêu tới bằng chứng và giới hạn kết luận.
- [Bản đồ năng lực](../08_BAN_DO_NANG_LUC.md): đường đọc từ căn bản tới tích hợp theo tác vụ.
- [Bốn ca áp dụng](../vi-du/bon-ca-ra-quyet-dinh.md): cùng một tài liệu, sửa trọng lượng, sửa nhịp và chẩn đoán kỳ vọng YouTube.
- [40 tình huống đánh giá AI](../kiem-thu/tinh-huong.json): chuẩn bị để kiểm AI khác, chưa phải kết quả đánh giá.
- [Gói đọc 1.1.0](../goi-doc/START_HERE.md): Markdown đầy đủ và JSONL chuẩn.

## Phiên bản, nguồn cũ và giới hạn

Không áp thay đổi đảo nguyên tắc. Giữ nguyên 33 bài/444 ảnh nguồn, các phân tích đã nạp và hai gói CORE_1_0_0. 60 mục cũ không đổi byte; 30 mục sửa được nâng version. Kho Farm vẫn ghim core 1.0.0 tại commit cũ; bản rà tầng 1 này không tự nâng ngách.

Kiểm nghiệm cần dữ liệu thật còn mở: kết quả sinh theo model/chế độ, khả năng AI khác áp dụng, phản hồi người xem và hiệu suất kênh. Chưa phân tích video nguồn mới, chưa sinh video, chưa chạy bộ đề trên AI ngoài, chưa đo khán giả. Không có bằng chứng để bảo đảm số view.

[Kết quả kiểm cấu trúc](../kiem-thu/KET_QUA.md) tách rõ những kiểm đã chạy khỏi các bước chưa thực hiện.
