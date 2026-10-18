# Kết quả kiểm hiện hành — FILM-KB 1.2.0, 18/10/2026

- 130 mục kiến thức khớp schema; 9 schema hợp lệ theo JSON Schema 2020-12.
- Liên kết nội bộ, mã kiến thức và 27 nguồn ngoài được kiểm; 33 bài nguồn được ánh xạ.
- 12 ca dữ liệu cố ý sai được phát hiện: mốc thời gian, mã trùng, cha thiếu, vượt phạm vi, chồng shot, dẫn nguồn không có, null thiếu lý do, khai quá độ phủ, mã core sai, hiệu ứng khán giả không có nguồn, kết luận chuyển động/âm từ ảnh tĩnh.
- Các ca sai bổ sung được phát hiện: thiếu phần phải giữ, nguồn phát biểu không gắn với mục, chẩn đoán thiếu phép thử, bản sao theo version, nhật ký riêng và phụ thuộc core cũ trong luồng làm việc.
- Mẫu kịch bản, shot, yêu cầu tạo, phân tích, quyết định và ví dụ hợp lệ được kiểm.
- Hồ sơ Farm tham chiếu core 1.2.0 hiện hành trên main; 10 quy tắc và 3 ứng viên giữ nội dung. Ví dụ hai shot từ báo cáo giữ dấu vết nguồn và trạng thái chưa kiểm video/audio.
- CORE.jsonl có 130 dòng khớp JSON chuẩn; CORE.md chứa nội dung hiện hành. SHA-256/kích thước của năm tệp gói được kiểm. Không còn gói/báo cáo theo version cạnh bản đang dùng.
- QC-004 được sửa tại chỗ theo chỉ dẫn mới; 129 mục chuyên môn còn lại không đổi. Số mục kiến thức vẫn là 130.
- 33 bài/444 ảnh nguồn, dữ liệu quan sát đã nạp và các lựa chọn sáng tạo được giữ.

[Kết quả hiện hành](ket-qua.json) · [Nhật ký chung](../CHANGELOG.md) · [Cách chạy lại](../cong-cu/README.md)

Đây là kết quả hiện hành, được cập nhật tại cùng đường dẫn. Lịch sử trước–sau dùng Git. Phạm vi là cấu trúc, nguồn/tham chiếu, bản xuất, chính sách lưu trữ và tính nguyên vẹn dữ liệu; chưa tạo video mới, chưa chạy bộ 40 tình huống trên AI ngoài hoặc đo phản ứng khán giả.
