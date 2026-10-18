# Cập nhật kiến thức tại chỗ

## Quyền và quy ước hiện hành

Chủ động bổ sung/sửa có căn cứ. Người dùng chốt: sửa trực tiếp tài liệu/mã hiện hành, chỉ giữ bản mới nhất ở mỗi đường dẫn. Git lưu lịch sử; [CHANGELOG.md](CHANGELOG.md) là một nhật ký chung cho thư viện và các thay đổi liên quan Farm. Không tạo bản sao theo ngày/version, thư mục archive hay báo cáo riêng cho mỗi lượt.

Thay đổi đảo nguyên tắc sáng tạo đang dùng phải trình rõ trước áp dụng rộng. Quy ước lưu trữ tại chỗ đã được người dùng chỉ định, áp dụng ngay. Giữ nguồn và dấu vết quan sát, không sửa bằng chứng để khớp giả thuyết.

## Một lượt cập nhật

1. Đọc tệp hiện hành, manifest, các mã/tài liệu phụ thuộc và yêu cầu mới.
2. Xác định lỗi hoặc điều cần thêm; ghi căn cứ, điều kiện, phản ví dụ và tác động.
3. Sửa đúng JSON/tài liệu cũ. Chỉ thêm mã mới khi có một nội dung/chức năng mới, không thêm mã chỉ để chứa bản sửa.
4. Cập nhật version của mục đổi và version thư viện khi xuất bản. Ngách đọc core hiện hành, kiểm các mã đang dùng và cập nhật metadata; giữ lựa chọn sáng tạo đã chốt.
5. Xuất lại chuyên đề và gói vào cùng đường dẫn: goi-doc/CORE.md, CORE.jsonl, SOURCES.json và manifest-goi.json.
6. Chạy các kiểm phù hợp; ghi đè kết quả hiện hành ở kiem-thu/ket-qua.json. Không báo video/khán giả/AI ngoài đã kiểm khi chưa thực hiện.
7. Ghi một mục vào CHANGELOG.md: version/ngày, nội dung và lý do đổi, mã/tệp ảnh hưởng, căn cứ cần thiết và trạng thái kiểm. Commit Git cung cấp phần diff chi tiết.

## Vòng học từ ngách

Nhập nguồn theo asset/video thật, ghi mốc và độ phủ. Phân tích theo cùng chuẩn; tách quan sát, nguồn thuật lại, diễn giải và đề xuất. Sửa phân tích tại tệp hiện hành, giữ dấu vết bằng chứng. Khi có thêm một nguồn thật, tạo định danh nguồn mới; không xem nó như bản sao v2 của tài liệu.

Tổng hợp bài học có điều kiện, kiểm nguồn thuận/trái và tính độc lập. Tách chức năng có thể chuyển giao khỏi gu hoặc tỷ lệ của một tác giả. Phân loại bổ sung, sửa điều kiện, sửa dữ kiện hoặc đảo nguyên tắc; mục đảo nguyên tắc giữ proposed_reversal cho đến khi được chốt.

## Truy nguyên và quay lại

Để xem trước–sau hoặc phục hồi, dùng lịch sử/diff/commit của Git tại đúng đường dẫn. Nhật ký giúp tìm mốc thay đổi, không chứa toàn bộ bản sao nội dung cũ. Không cần đọc các bản trước để sử dụng thư viện hiện hành.

Revision, checksum và asset ID trong một phân tích cho biết bằng chứng đã dùng. Chúng không buộc tài liệu hướng dẫn đang dùng trỏ về phiên bản cũ. Dữ liệu chưa biết tiếp tục ghi rõ; chưa thử không đổi thành đạt.
