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

## Xuất và kiểm bản hiện hành

xuat_goi.py luôn ghi đè CORE.md, CORE.jsonl, SOURCES.json, CORE_NGAN.md, START_HERE.md và manifest-goi.json ở goi-doc/. Không tạo gói mang hậu tố version; version hiện hành nằm trong manifest. JSON chuẩn là nguồn cho chuyên đề và gói đọc.

Xuất trước, kiểm sau. Bộ kiểm đối chiếu JSONL/sổ nguồn với JSON chuẩn, checksum các tệp gói, application_depth, nguồn phát biểu, mã, liên kết, thời gian và độ phủ. Bộ kiểm cũng phát hiện tệp gói/báo cáo theo version và nhật ký riêng ngoài vị trí chung.

Bộ kiểm đối chiếu thêm mục lục với JSON chuẩn; phiên bản và phương án được chọn trong ví dụ quyết định; loại tài sản, basis, khoảng bằng chứng và độ phủ; mốc sự kiện, dữ liệu người xem và biên [start, end). Các ca kiểm là dữ liệu giả lập để thử bộ kiểm, không là lượt xem/nghe video hoặc khảo sát khán giả. Ví dụ lịch sử Farm vẫn giữ core_version lúc được lập và dấu vết nguồn.

Với --farm-root, đối chiếu core_dependency với manifest hiện hành: version đã kiểm phải khớp, manifest_url trỏ main và commit = null. Kiểm cấu trúc không tự đổi lựa chọn sáng tạo của ngách. Nếu thiếu hoặc lệch dữ liệu, báo lỗi cần cập nhật; không âm thầm dùng bản cũ.

Ghi đè kết quả tại một đường dẫn:

~~~sh
python thu-vien/cong-cu/validate.py --farm-root /duong-dan/yt-ly-tu-that/Farm/Thu_vien_kien_thuc --report thu-vien/kiem-thu/ket-qua.json
~~~

[Kết quả hiện hành](../kiem-thu/ket-qua.json) · [Nhật ký chung](../CHANGELOG.md). Lịch sử nội dung và kết quả cũ được xem bằng Git.
