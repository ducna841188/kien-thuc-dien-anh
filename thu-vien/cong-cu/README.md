# Công cụ cục bộ

Các công cụ chỉ đọc/kiểm hoặc xuất tệp; không gọi AI, không gửi video và không sử dụng dịch vụ trả phí.

- tra_cuu.py: tìm từ khóa cục bộ hoặc mở đúng mã; chưa phải tìm ngữ nghĩa.
- xuat_goi.py: xuất Markdown/JSONL từ nội dung chuẩn.
- validate.py: kiểm bằng JSON Schema và các ràng buộc thời gian/nguồn; không chấm chất lượng hình hoặc ý đồ nghệ thuật.

Chạy từ gốc repository:

~~~sh
python -m pip install -r thu-vien/cong-cu/requirements.txt
python thu-vien/cong-cu/tra_cuu.py "timelapse người thừa"
python thu-vien/cong-cu/tra_cuu.py --id AI-008
python thu-vien/cong-cu/xuat_goi.py
python thu-vien/cong-cu/validate.py
~~~

Nếu đã tải nhánh Farm, thêm tùy chọn:

~~~sh
python thu-vien/cong-cu/validate.py --farm-root /duong-dan/yt-ly-tu-that/Farm/Thu_vien_kien_thuc
~~~

JSON Schema mô tả cấu trúc, bộ kiểm bổ sung ràng buộc không biểu diễn đủ bằng schema như end > start và độ phủ. [Tài liệu thư viện jsonschema](https://python-jsonschema.readthedocs.io/en/stable/validate/).

## Kiểm bản phát hành 1.1.0

Xuất gói trước, sau đó chạy validate.py. Bộ kiểm so JSONL với JSON chuẩn, checksum gói mới và hai gói cũ, phần mở rộng application_depth, nguồn phát biểu cụ thể và nguyên tắc không đổi nội dung cùng mã/phiên bản.

Khi thêm --farm-root, bộ kiểm đọc đúng bản core Farm ghim qua tuong-thich.json và checksum JSONL lưu trữ. Việc này không nâng Farm lên 1.1.0. Nếu bản ghim không sẵn có hoặc commit không khớp, báo chưa kiểm được thay vì thay bằng main.

Xem báo cáo mới ở ../kiem-thu/ket-qua-1.1.0.json; báo cáo ket-qua-cau-truc.json giữ nguyên là lịch sử 1.0.0.
