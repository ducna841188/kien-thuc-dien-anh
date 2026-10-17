# Bài 007 — Đọc bản đồ công cụ và chọn theo công việc

Bộ 12 ảnh giới thiệu mười tên công cụ, chia nhóm người dùng và minh họa hai quy trình ảnh thành video. Tài liệu giữ danh sách để tham khảo, tách khỏi bảng xếp hạng hiện tại và các số liệu marketing chưa có nguồn.

**Nguồn:** [10 công cụ tạo Video AI tốt nhất - bạn cần biết để không bị bỏ lại phía sau](https://drive.google.com/drive/folders/1kQEIkAS6cgAaOJyujBFBgl13v8fIA1xH). Đã đọc **12/12 ảnh**. Ngày biên soạn: 17/10/2026.

[Đọc từng ảnh](doc-anh.md) · [Bài thực hành](thuc-hanh.md) · [Nguồn và mã kiểm tra](nguon.json) · [Danh mục toàn bộ](../../DANH-MUC-BAI-HOC.md)

**Quy ước:** phần “Nguồn” diễn đạt ý trong bộ ảnh. Phần “Phân tích và áp dụng” do người biên soạn bổ sung. Hiệu quả của câu lệnh chưa được kiểm nghiệm bằng lần tạo video trong đợt này.

## Những điều cần học

| Nội dung | Mã ảnh nguồn |
| --- | --- |
| Phân biệt sinh chuyển động với biên tập | B007-01, B007-05, B007-06, B007-07 |
| Danh sách mười tên và mức thông tin thực có | B007-04, B007-05, B007-06, B007-07, B007-08 |
| Quy trình ảnh thành video có thể chuyển giao | B007-09, B007-10 |
| Đo lợi ích bằng dữ liệu của dự án | B007-00, B007-02, B007-03, B007-11 |

## 1. Phân biệt sinh chuyển động với biên tập

**Nguồn:** Nguồn gom công cụ thiết kế, biên tập và sinh video vào cùng một danh sách.

**Phân tích và áp dụng:** Tách công việc cần làm: tạo khung hình, sinh chuyển động từ ảnh, dựng nhiều shot, thêm chữ/giọng/nhạc và xuất bản. Một nền tảng có thể làm nhiều việc, nhưng cần thử đúng chế độ. Sơ đồ ảnh → AI → video chỉ mô tả khái quát, không phải kiến trúc kỹ thuật.

**Ví dụ cho cảnh nông thôn:** Cảnh Lan mang rổ cần sinh chuyển động; chuỗi ba cảnh cần biên tập để khớp nhịp, thêm âm thanh và xuất bản.

**Kiểm tra kết quả:** Xác định đầu vào và đầu ra từng công đoạn; không chọn công cụ template khi mục tiêu chính là một hành động mới trong ảnh.

![Minh họa nguồn B007-01](anh-goc/01.jpg)

## 2. Danh sách mười tên và mức thông tin thực có

**Nguồn:** Tác giả gọi đây là mười lựa chọn phổ biến, rồi mô tả một số công cụ theo nhóm.

**Phân tích và áp dụng:** Bảng dưới chỉ ghi nội dung có trong ảnh, không xác nhận toàn bộ khả năng hiện hành hoặc xếp hạng chất lượng.

| Tên trong nguồn | Vai trò nguồn mô tả | Mức chi tiết trong bộ ảnh |
| --- | --- | --- |
| Hailuo AI | Ảnh thành video | Có lưu đồ bốn bước |
| Vidful AI | Tạo video từ ảnh/chữ cho truyền thông | Mô tả khái quát |
| Canva | Thiết kế với template và kéo thả | Mô tả khái quát |
| VEED.IO | Biên tập video online | Mô tả khái quát |
| CapCut | Dựng/hiệu ứng cho mạng xã hội | Mô tả khái quát |
| Fotor | Sửa ảnh kết hợp video | Mô tả khái quát |
| Runway | Công cụ video AI | Mô tả khái quát |
| Luma | Tạo chuyển động từ ảnh | Mô tả khái quát, tên tính năng cần chỉnh |
| Kling AI | Không có phần giải thích riêng | Chỉ xuất hiện ở lưới logo |
| Leonardo AI | Tạo chuyển động từ ảnh | Có lưu đồ năm bước |

**Ví dụ cho cảnh nông thôn:** Chọn một tác vụ thử thống nhất thay vì học cùng lúc cả mười công cụ: ảnh Lan ở hiên, động tác nhấc rổ và máy đứng yên.

**Kiểm tra kết quả:** Công cụ có đầu vào phù hợp, kết quả giữ thiết kế và thao tác, chi phí tính theo số clip dùng được.

![Minh họa nguồn B007-04](anh-goc/04.jpg)

## 3. Quy trình ảnh thành video có thể chuyển giao

**Nguồn:** Các lưu đồ đều có chọn ảnh, điều chỉnh yêu cầu/chuyển động, tạo, kiểm và tải.

**Phân tích và áp dụng:** Giữ nguyên nguyên tắc dù giao diện thay đổi. Ảnh đầu vào xác lập người và bố cục; prompt diễn tả chuyển động và máy. Luma dùng tên Dream Machine trong tài liệu chính thức; Leonardo có quy trình tạo video từ ảnh và các dòng Motion. Không sao chép thanh Motion Strength=5 sang mọi phiên bản.

**Ví dụ cho cảnh nông thôn:** Tải ảnh chuẩn Lan ở hiên, mô tả cô nhìn sang trái và nâng rổ nhẹ, camera cố định; duyệt clip rồi mới dựng.

**Kiểm tra kết quả:** Ảnh không bị cắt sai; đúng người, hướng chuyển động và đường máy; kiểm cả khung giữa và cuối.

![Minh họa nguồn B007-09](anh-goc/09.jpg)

## 4. Đo lợi ích bằng dữ liệu của dự án

**Nguồn:** Nguồn nêu lợi ích marketing và hai câu chuyện ứng dụng mang tên TripAdvisor, LangMaster.

**Phân tích và áp dụng:** Tách chất lượng sản xuất khỏi hiệu quả truyền thông. Chấm clip dùng được, thời gian sửa và chi phí trước; khi có chiến dịch thật mới đo tương tác/chuyển đổi với thiết kế so sánh rõ. Không dùng các tỷ lệ trong ảnh làm dự báo kết quả của bạn.

**Ví dụ cho cảnh nông thôn:** So hai phiên bản mở đầu phim ở cùng kênh và thời gian; giữ nội dung chính, ghi tiêu chí trước khi xem kết quả.

**Kiểm tra kết quả:** Có định nghĩa chỉ số, mẫu, thời gian và điều kiện so; không nhầm tăng tương tác với tăng doanh thu.

![Minh họa nguồn B007-00](anh-goc/00.jpg)

## Điểm cần hiểu có điều kiện

- Chưa có căn cứ trong bộ ảnh cho +80% tương tác và +60% chuyển đổi; không thể khái quát sang mọi dự án.
- Hai case study không cung cấp chiến dịch hay báo cáo xác minh. Tài liệu chỉ thuật lại việc nguồn nêu, không xác nhận kết quả hoặc quan hệ nhân quả.
- Không có benchmark chứng minh mười công cụ tốt nhất/phổ biến nhất; Kling chỉ có logo, không tự bổ sung thông số từ hình.
- Tên Image2Motion bị gắn thiếu nhất quán giữa Luma và Leonardo trong chính bộ ảnh. Tài liệu tham chiếu chính thức được thêm để người học kiểm lại.
- Tiêu đề 60 giây, mặc định chuyển động 5, giao diện và tuyên bố miễn phí không được dùng làm điều kiện hiện tại.
- Không phải mọi công cụ ảnh thành video tự thêm âm thanh, nhạc hoặc tạo phim hoàn chỉnh.

## Cách đưa vào quy trình sản xuất

Chốt một tác vụ → chọn công cụ có đầu vào phù hợp → kiểm hướng dẫn đúng mô hình → tạo mẫu ngắn → ghi bản dùng được, thời gian và chi phí → dựng thành chuỗi → chỉ mở rộng sau khi đạt tiêu chí. Danh sách nguồn là điểm khảo sát, không phải yêu cầu đăng ký cả mười dịch vụ.

## Tự kiểm tra kiến thức

- Công cụ dựng video và mô hình sinh chuyển động giải quyết hai việc gì?
- Ảnh logo có cho biết độ dài clip hay giá sử dụng không?
- Muốn chứng minh tăng chuyển đổi cần bổ sung dữ liệu gì?

## Nguồn đối chiếu bổ sung

- [Luma — Dream Machine quick start](https://lumalabs.ai/learning-hub/web-quick-start): Đối chiếu tên và quy trình tạo video từ ảnh.
- [Leonardo — Generating Video](https://intercom.help/leonardo-ai/en/articles/11027827-generating-video-on-leonardo-ai): Đối chiếu quy trình và chọn mô hình hiện hành.

**Giới hạn:** đây là tài liệu học từ ảnh. Không dùng một hình minh họa để xác nhận chuyển động, thời lượng, độ chính xác thao tác hay khả năng hiện tại của một sản phẩm. Những phần chưa kiểm chứng được ghi rõ trong bản đọc ảnh.
