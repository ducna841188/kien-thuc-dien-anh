# Quy ước cho thư viện kiến thức làm phim

Người dùng chốt ngày 18/10/2026.

- Kiến thức chung lưu repo này, trong thu-vien/. Nhánh Farm lưu ducna841188/yt-ly-tu-that/Farm/Thu_vien_kien_thuc.
- Đọc thu-vien/00_HUONG_DAN_AI.md, manifest và quy trình tác vụ trước khi sử dụng.
- JSON mục kiến thức là bản chuẩn; Markdown chuyên đề và gói đọc là bản xuất. Giữ mã và quản lý phiên bản.
- Chủ động bổ sung/sửa có căn cứ và nhật ký. Thay đổi đảo nguyên tắc đang dùng phải trình rõ trước áp dụng rộng.
- Giữ tài sản nguồn và dấu vết bằng chứng. Phân tích do thư viện biên soạn được sửa tại chỗ khi có căn cứ, kèm nguồn/mốc và nhật ký; không sửa lời nguồn được trích hoặc bịa quan sát để khớp giả thuyết.
- Tách quan sát, nguồn thuật lại, diễn giải, đề xuất và kết quả thử. Chưa biết phải ghi rõ.
- Ưu tiên ứng dụng thực hành cho khán giả YouTube; nền chung không bị mặc định theo Farm.
- Khi cập nhật dữ liệu, chạy kiểm tra cấu trúc, liên kết, mã và quan hệ thời gian thích hợp. Không báo kiểm nghiệm video/khán giả/AI khác nếu chưa thực hiện.

## Cập nhật tại chỗ — quyết định hiện hành của người dùng ngày 18/10/2026

- Sửa trực tiếp tệp/mục hiện hành, giữ mã và đường dẫn ổn định; version trong metadata là lần sửa mới nhất. Không tạo bản sao v1/v2, hậu tố ngày/version, thư mục archive hoặc báo cáo riêng cho mỗi lượt sửa.
- Git lưu toàn bộ lịch sử và diff. Khi cần bản cũ, đọc commit tương ứng; main chỉ giữ bản hiện hành.
- Một nhật ký thay đổi chung cho thư viện là thu-vien/CHANGELOG.md của repo này, gồm các thay đổi liên quan nhánh Farm. Không mở thêm nhật ký theo đợt/ngách; kết quả kiểm hiện hành ghi đè thu-vien/kiem-thu/ket-qua.json.
- Gói AI luôn ở thu-vien/goi-doc/CORE.md, CORE.jsonl và SOURCES.json; xuất lại ghi đè cùng đường dẫn. JSON chuẩn vẫn là nguồn, Markdown/gói là bản xuất tự động.
- Nhánh ngách đọc core trên main và đối chiếu manifest hiện hành; không buộc người dùng đọc gói cũ. Ghi version đã kiểm trong hồ sơ; nguồn của quan sát vẫn có asset ID/checksum/commit để truy nguyên.
- Giữ lựa chọn sáng tạo và dữ liệu nguồn. Bằng chứng mới khác dữ liệu cũ là dữ liệu mới có định danh, không phải một bản sao tài liệu theo phiên bản.
