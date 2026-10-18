# Đánh giá khả năng AI dùng thư viện

[48 tình huống](tinh-huong.json) bao phủ năm tác vụ. Đây là bộ đề chuẩn bị, chưa có kết quả chạy độc lập trên ChatGPT/Claude/Gemini hoặc mô hình khác.

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

## Phạm vi tình huống chuyên sâu

T25–T40 kiểm lựa chọn fps/nhòe, phối cảnh/vùng nét, trọng lượng và khả thi ảnh đầu, miền màu, cut/sự kiện, điểm nhìn, điều đáng quan tâm, thời gian có chức năng, thiết kế thử YouTube, học từ view, âm, sáng theo đường đi, giới hạn bản sơ và cập nhật tại chỗ. Các tình huống này được chuẩn bị để chạy trên AI khác; kết quả cấu trúc không phải kết quả vượt qua bộ đề.

## Tình huống T41–T48

Tám đề mới kiểm phân biệt sắc thái được nhận ra/cảm xúc tự trải nghiệm; mong chờ khi biết trước kết; trục và ảnh lật; clip mượt nhưng sai hành động; nhận diện sau che lộ; chi phí giây dùng thực; giá trị riêng của loạt AI; công khai AI khác kết quả xét duyệt. Đây vẫn là đề đã chuẩn bị, chưa phải tám lượt đã chạy trên mô hình ngoài.
