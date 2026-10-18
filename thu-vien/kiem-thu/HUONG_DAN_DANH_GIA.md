# Đánh giá khả năng AI dùng thư viện

[24 tình huống](tinh-huong.json) bao phủ năm tác vụ. Đây là bộ đề chuẩn bị, chưa có kết quả chạy độc lập trên ChatGPT/Claude/Gemini hoặc mô hình khác.

## Cách thực hiện

1. Ghi model, phiên bản, ngày, cách nạp, tệp đã đọc và giới hạn đầu vào.
2. Đưa hướng dẫn đọc, chuẩn liên quan và dữ liệu tình huống.
3. Giữ nguyên đề khi so; lưu nguyên đầu ra, không chỉ ví dụ đẹp.
4. Chấm theo must_do và kiểm người chấm: bịa quan sát, đổi phần đã chốt hoặc bỏ nguồn là lỗi trọng yếu.
5. Ghi riêng: đúng phạm vi bằng chứng, quyết định có lý do, hành động dùng được, giữ ràng buộc, dẫn mã và nêu phép kiểm.
6. Tổng hợp lỗi theo tác vụ; sửa hướng dẫn/kiến thức rồi chạy lại ca bị ảnh hưởng. Không coi một điểm tổng là xác nhận mọi ngách.

Thang 0–2 là quy ước đánh giá nội bộ, không chuẩn đo tâm lý hoặc điểm benchmark công nghiệp. Chưa có ngưỡng thắng một mô hình khác.

## Kiểm tự động khác kiểm suy luận

cong-cu/validate.py kiểm schema, mã, liên kết và quan hệ dữ liệu. Nó không xem video, không nghe audio và không chấm chất lượng nghệ thuật. Ca dữ liệu hợp lệ/sai được chạy riêng để bảo đảm bộ kiểm phát hiện các lỗi cấu trúc có ý nghĩa.
