# Kết quả kiểm — FILM-KB 1.1.0, 18/10/2026

- 130 mục kiến thức khớp schema; 9 schema hợp lệ theo JSON Schema 2020-12. Phần mở rộng knowledge 1.1.0 vẫn đọc được 90 mục lưu trữ 1.0.0.
- Liên kết nội bộ, mã kiến thức và 27 nguồn ngoài được kiểm; 33 bài nguồn được ánh xạ.
- 12 ca dữ liệu cố ý sai được phát hiện: mốc thời gian, mã trùng, cha thiếu, vượt phạm vi, chồng shot, dẫn nguồn không có, null thiếu lý do, khai quá độ phủ, mã core sai, hiệu ứng khán giả không có nguồn, kết luận chuyển động/âm từ ảnh tĩnh.
- Ba ca sai mới được phát hiện: thiếu phần phải giữ trong ca quyết định, nguồn phát biểu không gắn với mục, chẩn đoán không có phép thử tiếp theo.
- Mẫu kịch bản, shot, yêu cầu tạo, phân tích, quyết định và ví dụ hợp lệ được kiểm.
- Hồ sơ Farm và hai shot ví dụ từ báo cáo được kiểm theo đúng core 1.0.0 đã ghim và checksum gói lưu trữ. Không nâng ghim Farm trong lượt này.
- Gói xuất có 130 dòng JSONL khớp JSON chuẩn; bản Markdown chứa phần chiều sâu và sổ nguồn. SHA-256/kích thước của năm tệp gói mới cùng hai gói cũ được kiểm.
- 60 mục giữ nguyên và 30 mục cũ được nâng version; không có nội dung đổi mà giữ cùng mã/phiên bản.
- Các bài/ảnh/phân tích nguồn cũ được giữ nguyên byte, đối chiếu theo danh mục trước sửa.

[Chi tiết 1.1.0](ket-qua-1.1.0.json) · [Báo cáo cũ 1.0.0](ket-qua-cau-truc.json) · [Cách chạy lại](../cong-cu/README.md)

Phạm vi là kiểm cấu trúc, nguồn/tham chiếu, bản xuất và tính nguyên vẹn dữ liệu. Rà nội dung có đối chiếu nguồn được mô tả riêng trong [báo cáo rà](../kiem-toan/RA_SOAT_1_1_0.md). Chưa tạo video mới, chưa chạy bộ 40 tình huống trên các AI khác và chưa kiểm phản ứng khán giả.
