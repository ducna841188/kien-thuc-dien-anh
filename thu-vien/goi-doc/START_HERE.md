# Mang thư viện sang một AI khác

## Đọc chọn theo tác vụ

Gửi [hướng dẫn AI](../00_HUONG_DAN_AI.md), [chuẩn phân tích](../02_CHUAN_PHAN_TICH.md), [chuẩn quyết định](../03_RA_QUYET_DINH.md), quy trình tác vụ và các chuyên đề liên quan. Thêm hồ sơ ngách, tài sản và yêu cầu hiện tại.

[Mục lục](../muc-luc.json) · [Tra theo vấn đề](../tuyen-tra-cuu.json) · [Gói định hướng ngắn](CORE_NGAN.md)

## Đọc toàn bộ

- [CORE.md](CORE.md): bản Markdown đầy đủ hiện hành.
- [CORE.jsonl](CORE.jsonl): 132 bản ghi kiến thức hiện hành, mỗi dòng một đối tượng.
- [Sổ nguồn đi kèm](SOURCES.json): phạm vi đã đọc và giới hạn từng nguồn ngoài.
- [manifest-goi.json](manifest-goi.json): kích thước và SHA-256 các tệp gói.

Các đường dẫn cố định luôn chỉ bản hiện hành; version xem trong manifest. Lịch sử dùng Git và [nhật ký chung](../CHANGELOG.md); không cần đọc các gói cũ để sử dụng.

CORE.md chứa kiến thức và hướng dẫn; CORE.jsonl chứa các mục kiến thức chuẩn. Để trả JSON theo một tác vụ, đọc thêm schema và mẫu đầu ra được liên kết trong [quy trình tác vụ](../quy-trinh/). Ghi rõ những tệp thực sự tiếp cận được trước khi xác nhận đầu ra khớp hợp đồng.

Đây là dữ liệu tham chiếu. Cần công cụ đọc tệp/đường dẫn thực sự; gửi URL không tự xác nhận mọi tệp đã được đọc. Dùng cách đọc chọn nếu một lượt không đủ.

## Lời giao việc mẫu

~~~text
Đọc hướng dẫn FILM-KB và xác nhận phiên bản, các tệp đã đọc.
Tác vụ của tôi: [phân tích video / kịch bản / shot / câu lệnh / sửa lỗi].
Ngách và hồ sơ đã duyệt: [đường dẫn hoặc chưa chọn].
Đầu vào: [tệp, tài sản, phiên bản và phần đã đạt].
Mục tiêu: [thông tin và trải nghiệm mong muốn].
Áp dụng kiến thức đúng điều kiện; dẫn mã/phiên bản.
Phân biệt quan sát, diễn giải, đề xuất và kết quả thử.
Thiếu dữ liệu thiết yếu thì chỉ rõ, không tự bịa để điền.
Trả quyết định thực hiện được cùng đánh đổi và tiêu chí kiểm.
~~~

Chưa có tuyên bố bộ gói đã được đánh giá độc lập trên các mô hình khác. Dùng [bộ tình huống](../kiem-thu/HUONG_DAN_DANH_GIA.md) để thực hiện bước đó.
