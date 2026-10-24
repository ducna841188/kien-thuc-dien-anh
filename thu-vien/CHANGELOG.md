# Nhật ký thay đổi chung — FILM-KB và Farm

Đây là nhật ký duy nhất cho các cập nhật thư viện core–Farm. Nội dung làm việc luôn là bản hiện hành; Git giữ diff và toàn bộ bản trước. Các mục bên dưới là lịch sử, không phải hướng dẫn để chọn đọc bản cũ.

## Farm — 24/10/2026 — Cụm mở đầu Vườn nhỏ, bữa cơm nhà

- Tạo bản cảnh hiện hành tại Farm/Vuon_nho_bua_com_nha/Danh_sach_canh.md trong repo Farm; phiên bản 0.1, trạng thái chờ người dùng duyệt.
- Chỉ biên soạn C01: S001–S015, tổng 51 giây, mỗi cảnh 3–4 giây. Mở thiên nhiên buổi sáng, cô gái mang dụng cụ ra vườn và làm tơi một đoạn luống.
- Mỗi cảnh có góc, bố cục, trạng thái đầu–hành động–cuối, liên tục, âm thanh và nhu cầu tham chiếu. Xuất Excel ba trang cùng bản đọc Markdown.
- Dùng các quyết định phỏng vấn mới của người dùng; không sửa bản định hướng chung hoặc phân tích video nguồn. Chưa khóa lịch mùa vụ, chưa tạo prompt, video hoặc các cụm tiếp theo.
- Kiểm 15 mã liên tiếp, tổng thời lượng, công thức dòng thời gian và bố cục ba trang Excel. Dừng ở S015 chờ duyệt.

## Farm 1.4.0 — 18/10/2026 — Rà điểm cắt và học chức năng hình VID_02

- VID_02 0.3.0 sửa tại chỗ: trích 350 frame liền kề n−1/n tại 175 ranh giới hiện hành, rà đủ 12 bảng và xác nhận đổi hình tại mỗi cặp. Giữ 176 cú là phân hoạch làm việc vì chưa loại hết cut có thể còn thiếu bên trong khoảng; chưa khai phát trọn chuyển động.
- Bằng chứng tăng từ 1.328 lên 1.665 mốc ảnh riêng (13 frame trùng bộ cũ). Thêm 12 bảng điểm cắt, bốn bảng ca sâu và một bảng màu, tổng 60 bảng; ảnh nguồn cũ giữ nguyên byte.
- Thêm 12 ca học sâu: khung trống có nhiệm vụ; sợi siro; bản đồ nguyên liệu/khối/mặt cắt; vai hai tay cán; lan–nhiệt–cuộn; chuyển điểm đỡ giỏ; gói một viên/tích lượng; khói và đổi góc; công dụng đạo cụ; gieo người nhận; chuyển quyền giữ; đời sống cùng kho thành quả.
- Thêm 17 cầu nối chú ý dự kiến (không đo mắt), 12 vùng pixel có tọa độ/checksum (không suy LUT, tỷ lệ đèn hoặc luminance tuyến tính), ba mốc thời gian có giới hạn (không gọi mốc chọn là khởi điểm thật hay toàn thời gian giữ kết quả).
- Liên kết ca sâu vào từng cú liên quan, DNA mã cũ và bản đọc; mở rộng công cụ trích ảnh cho bố cục bằng chứng mới. JSON là bản chuẩn, không tạo bản sao theo version.
- Giữ nguyên 13 giả thuyết có điều kiện, 132 mục core, nguồn/lựa chọn Farm/VID_01 và tuyến âm cũ. Âm tiếp tục ngoài phạm vi; chưa tạo clip, chạy AI ngoài hoặc kiểm khán giả.

## Farm 1.3.0 — 18/10/2026 — Đào sâu hình VID_02, loại âm khỏi phạm vi

- VID_02 0.2.0 sửa trực tiếp hồ sơ cũ: màu theo vật thể cho 176 cú, vị trí máy có vật mốc, phiếu quyết định hình và kế hoạch trạng thái đầu–tác động–cuối.
- Thêm vào dữ liệu hiện hành 26 phiếu chuỗi/77 nhịp nội dung, 175 liên kết hình giữ hai trạng thái qua cut, năm vòng chờ–trả và hai mối nối nhân quả chưa được chứng minh.
- Phân biệt thêm khối quả S171 với rưới/nhấc S172; cuộn còn ở chảo với khay nhiều ống; tải rời đất với người mang tải. Không nối bưởi/quýt thành khối vàng hoặc khẳng định nón cùng mẻ ống bánh.
- Đào sâu DNA bộ góc/trao–nhận tại mã cũ, thêm DNA-13 về màu có vật mang và biến đổi trạng thái. 13 giả thuyết của một phim, chưa nâng thành nguyên lý chung/nguyên nhân lượt xem.
- Theo người dùng: âm ngoài phạm vi, giữ dữ liệu âm cũ và bốn trường null để tương thích schema, bỏ điều kiện phải nghe âm mới hoàn tất lượt hình. Bản đọc hiện 21 nhóm hình, JSON vẫn 25 nhóm.
- Xuất lại mục lục và tám phần chi tiết từ JSON; giữ nguồn/ảnh, thời gian/ID, VID_01, lựa chọn Farm và 132 mục core. Chưa phát toàn motion, sinh clip hoặc kiểm khán giả. Lịch sử tiếp tục nằm trong Git.

## Farm 1.2.0 — 18/10/2026 — Nạp VID_02 theo ảnh có mốc

- Tiếp nhận video người dùng gán VID_02, URL FWMIPukvdsQ; giữ nguồn tải lên với checksum, 611,92 giây, 1280×720, audio stereo. Nạp từng video; chưa nhận bảy video bổ sung còn lại.
- Bản phân tích 0.1.0 có 176 cú máy dự kiến/26 chuỗi/8 phân đoạn, đủ 25 nhóm với trạng thái bằng chứng, 1.328 mốc ảnh riêng; 10 lượt rà dày tiếp xúc và 43 bảng ảnh. Gộp báo động khói 359,48 giây vào cùng cú trước, không biến sự kiện thành cut.
- Thêm phiếu tái tạo từng cú, 13 sổ trạng thái, chỉ mục từng giây và 12 giả thuyết DNA có điều kiện/ngoại lệ/phép kiểm. Chưa nâng giả thuyết một phim thành nguyên lý core hoặc công thức gây lượt xem.
- Phạm vi partial: ảnh theo toàn trục không thay phát đầy đủ chuyển động; audio đã đo tín hiệu nhưng môi trường không hỗ trợ nghe. Máy, tốc độ và ngữ nghĩa/đồng bộ âm giữ chưa biết. Chưa tạo clip/kiểm người xem.
- Sửa hàm kiểm giao khoảng để chấp nhận sự kiện điểm đúng mốc ảnh/đúng đầu khoảng, vẫn loại mốc khác hoặc cuối khoảng bị loại. Bốn ca hồi quy mới, tổng 40 ca metadata. Bộ kiểm tự đọc phân tích VID_*/phan-tich.json trong Farm.
- Sửa trạng thái hiện hành của Farm tại chỗ, giữ lựa chọn sản xuất, nguồn và phân tích VID_01. Core vẫn 1.3.1, 132 mục kiến thức và 444 ảnh bài học không đổi; bản đọc người học không đổi. Một nhật ký chung, Git giữ lịch sử.

## 1.3.1 — 18/10/2026 — Sổ tay cho máy tính và chuẩn bị bộ chín video

- Ghi nhận người dùng ưu tiên đọc trên máy tính, hình lớn và đã chọn đủ tám video bổ sung. Tạo kế hoạch tiếp nhận/nghiên cứu trong Farm; chưa nhận danh sách/media và chưa phân tích video mới.
- Thêm bản cho người học 0.1.0: mục lục 13 chương ánh xạ đủ 132 mã, một chương mẫu về ý đồ–bằng chứng–khung–âm–kiểm và PDF khổ ngang. Đây là mẫu để đọc thử, chưa là sổ tay hoàn chỉnh.
- Một ảnh tình huống hư cấu tạo bằng imagegen tích hợp; ba sơ đồ vector biên soạn chính xác cho mục đích giải thích. Prompt và phương pháp nằm trong manifest minh họa. Không dùng ảnh để chứng nhận chuyển động hoặc cảm xúc.
- JSON chương là nguồn cho bản đọc Markdown/PDF; liên kết mã@version core. Các tệp có đường dẫn cố định; Git giữ lịch sử và nhật ký vẫn tập trung tại đây.
- Giữ 132 mục kiến thức và phiên bản từng mục, 33 bài/444 ảnh nguồn, lựa chọn Farm và phân tích cũ. Chỉ metadata core–Farm cập nhật theo bản phát hành; kết quả kiểm hiện hành được cập nhật tại cùng đường dẫn.

## 1.3.0 — 18/10/2026 — Đào sâu quyết định điện ảnh và duyệt phim AI

- Rà khung/nguyên lý 130 mục hiện hành, đọc sâu các trục cần cải tiến; cập nhật 19 mục và thêm QC-010/YT-012, tổng 132 mục. Giữ toàn bộ mã cũ, sửa trực tiếp các tệp hiện hành.
- Đào sâu trục chủ đề/giá trị, lịch lộ thông tin, mong chờ khi biết trước kết; phân biệt cảm xúc nhân vật, ý đồ, sắc thái người xem nhận ra và cảm xúc họ thực trải nghiệm.
- Bổ sung ca lựa chọn dàn cảnh, mặt bằng/trục, bộ góc tối thiểu và phần dư dựng; làm rõ phép đo tương phản, chất liệu qua thời gian, điểm nghe và kiểm sau nội suy/sửa vùng.
- Thêm QC-010 để tách vẻ ảnh, ổn định theo thời gian và đúng hành động; tăng độ sâu cho duyệt take–chuỗi–toàn phim và chi phí theo giây riêng biệt dùng thực.
- Thêm YT-012 về giá trị biên tập riêng và cách giới thiệu cảnh AI; đối chiếu tài liệu YouTube hiện hành, không buộc thêm thoại hoặc hứa lượt xem/kiếm tiền.
- Bổ sung năm nguồn có phạm vi (32 nguồn), 10 thuật ngữ (147), sáu tuyến tra; cập nhật bốn hồ sơ cảm xúc và chuẩn/quy trình. Mẫu shot từ một shot thành đủ bốn shot, khớp kịch bản và ví dụ giả lập.
- Bổ sung phiếu cảnh tích hợp trong ca chiếc ghế ở JSON và bản xuất Markdown; tám đề đánh giá AI mới, tổng 48 đề chuẩn bị. Chưa chạy các đề trên AI ngoài, chưa tạo video hoặc kiểm khán giả.
- Farm chỉ cập nhật metadata phụ thuộc sang core 1.3.0; giữ quy tắc, ứng viên, nguồn quan sát và lựa chọn sản xuất. 33 bài/444 ảnh nguồn giữ nguyên; một nhật ký chung và các đường dẫn gói cố định tiếp tục được dùng.

## 1.2.1 — 18/10/2026 — Rà tính thống nhất, ví dụ và hợp đồng bằng chứng

- Làm rõ ranh giới giữa giữ tài sản/lời nguồn và sửa phân tích do thư viện tạo tại chỗ; thống nhất AGENTS core/Farm với hướng dẫn cập nhật.
- Rà 130 mục: không trùng mã/tiêu đề hoặc thuật ngữ. Làm rõ phạm vi và gộp câu lặp trong 18 mục, giữ toàn bộ mã; phân biệt thiết kế mong chờ với bố trí chi tiết, cấu trúc toàn phim với nối cảnh, thiết kế thế giới với chẩn đoán tự nhiên, khung nhịp với quyết định giữ/bỏ thời gian.
- Sửa ví dụ xếp ba bát: trạng thái vào/ra đúng, chỉ có tiếng va khi có chạm; lượt lược thời gian nằm ở cut thay vì tự thêm cut trong cùng một shot. Mẫu sửa lỗi dẫn đúng version của các mã đang dùng.
- Bổ sung quy ước trục gốc/offset/duration và kiểm đúng biên [start, end); thêm loại nguồn âm thanh riêng trong schema phân tích, giữ khả năng đọc bản ghi cũ.
- Khắc phục sáu trường hợp bộ kiểm cũ bỏ lọt: bằng chứng ngoài độ phủ, dẫn khoảng shot khác, thiếu mốc, sai loại tài sản, basis không khớp nguồn và sự kiện ngoài khoảng được dẫn. Kiểm thêm ID/phạm vi dữ liệu người xem, nguồn âm vắng mặt, mốc không hữu hạn và phiên bản/tham chiếu quyết định.
- Mục lục, chuyên đề và gói đọc được đối chiếu lại với JSON chuẩn. Năm quy trình liên kết trực tiếp schema/mẫu; hướng dẫn phân rõ gói kiến thức và hợp đồng đầu ra cần đọc. Kết quả kiểm hiện hành vẫn ở kiem-thu/ket-qua.json; không tạo bản sao hoặc nhật ký mới.
- Giữ nguồn, 444 ảnh, 10 quy tắc và 3 ứng viên Farm. Các ca kiểm là metadata giả lập; chưa tạo video, chạy AI ngoài hoặc khảo sát khán giả.

## 1.2.0 — 18/10/2026 — Sửa trực tiếp, chỉ giữ bản hiện hành

- Thực hiện quyết định mới của người dùng: sửa tại chỗ theo mã/đường dẫn cố định, version trong metadata; lịch sử dùng Git và một nhật ký chung.
- Gói AI hiện hành là goi-doc/CORE.md, CORE.jsonl, SOURCES.json và manifest-goi.json. Xóa các bản gói/manifest theo version khỏi main; không giảm 130 mục kiến thức.
- Gộp ghi chú rà và lịch sử Farm vào file này; báo cáo kiểm hiện hành dùng kiem-thu/ket-qua.json, không giữ báo cáo theo từng lượt ở main.
- Cập nhật QC-004, AGENTS, hướng dẫn đọc/cập nhật, liên kết và công cụ xuất/kiểm để các lượt sau tiếp tục sửa đúng tệp.
- Farm dùng core hiện hành trên main; chỉ metadata/phụ thuộc và quy tắc lưu trữ đổi. Giữ 10 quy tắc ngách, 3 ứng viên, lựa chọn sản xuất và dữ liệu quan sát.
- 33 bài, 444 ảnh và nguồn/phân tích đã nạp được giữ. Revision nguồn vẫn truy nguyên bằng chứng; các bản hướng dẫn cũ được xem bằng Git khi cần.
- Kiểm JSON/schema, mã/liên kết, gói xuất, chính sách một bản hiện hành và phụ thuộc Farm; xem kết quả hiện hành ở kiem-thu/ket-qua.json. Chưa tạo video hoặc đánh giá khán giả/AI ngoài.

## 1.1.0 — 18/10/2026

- Rà 90 mục: giữ nguyên 60, làm rõ 30; thêm 40 mục, tổng 130/13 chuyên đề.
- Thêm chiều áp dụng/chẩn đoán cho 70 mục: cơ chế cần xét, hai phương án, phần giữ và phép kiểm.
- Bổ sung kiến thức về sự kiện/chú ý, tiến triển và giá trị nhỏ, diễn xuất/chuyển lực, quang học/phơi/nhòe, màu nhiều nguồn, âm và sản xuất AI toàn chuỗi.
- Mở YouTube sang ý tưởng, ba câu hỏi hiệu suất, A/B, học phim nổi bật và điều kiện xem.
- Thêm 13 nguồn ngoài có phạm vi (tổng 27), 43 thuật ngữ (tổng 137), 20 tuyến tra cứu (tổng 37), 16 tình huống AI (tổng 40) và bốn ca áp dụng.
- Thêm vòng sản xuất, bảng phép kiểm trải nghiệm, bản đồ năng lực; mở schema kiến thức tương thích bản cũ và kiểm gói theo phiên bản.
- Giữ hai gói 1.0.0, nguồn cũ và ghim Farm; không áp thay đổi đảo nguyên tắc.

[Commit nội dung 1.1.0](https://github.com/ducna841188/kien-thuc-dien-anh/commit/6120ba1e9d1a5ce7e42277ef5b8e9efd125db3b5). Chi tiết rà theo từng mục có trong diff và tệp tại commit này.

## 1.0.0 — 18/10/2026

- Tiếp nhận các quyết định về hai tầng, bản cho AI trước, năm tác vụ và quyền cập nhật.
- Tổ chức 90 mục thực hành/13 nhóm, bổ sung kể chuyện, dàn cảnh, dựng, âm, khán giả và vòng học.
- Tách dữ liệu quan sát, diễn giải, tái dựng và bằng chứng người xem; chuẩn hóa mốc/độ phủ.
- Thêm schema, mẫu, hồ sơ mô hình có giới hạn và bộ kiểm tra.
- Kiểm toán liên kết 33 bài; giữ nguyên 444 ảnh/374 chuỗi byte khác nhau.
- Tạo nhánh Farm: 10 quy tắc liên kết core, 3 ứng viên nghiên cứu, hai shot ví dụ chuyển từ báo cáo VID_01 có dấu vết nguồn; chưa xem toàn video/audio. Cách ghim lúc tạo nhánh đã được thay bằng chính sách hiện hành ở 1.2.0.

Không có thay đổi đảo nguyên tắc đã chốt; các hiệu ứng tuyệt đối và số liệu quảng bá đã được chú giải ở lượt nạp cũ, tiếp tục giữ điều kiện ấy.
