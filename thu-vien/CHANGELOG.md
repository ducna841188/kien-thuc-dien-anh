# Nhật ký thay đổi chung — FILM-KB và Farm

Đây là nhật ký duy nhất cho các cập nhật thư viện core–Farm. Nội dung làm việc luôn là bản hiện hành; Git giữ diff và toàn bộ bản trước. Các mục bên dưới là lịch sử, không phải hướng dẫn để chọn đọc bản cũ.

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
