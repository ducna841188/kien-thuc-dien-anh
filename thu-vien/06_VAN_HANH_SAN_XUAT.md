# Từ yêu cầu đến bản phim có thể duyệt

FILM-KB 1.1.0. [Mục lục](README.md) · [Chuẩn quyết định](03_RA_QUYET_DINH.md) · [Tiêu chí trải nghiệm](07_KIEM_TRA_TRAI_NGHIEM.md).

Quy trình này nối năm tác vụ của kho vào một vòng sản xuất. Mục tiêu là tìm lỗi bằng đầu ra phù hợp và sửa trước khi chi phí lan sang những phần khác. Dự án nhỏ có thể gộp bước; các loại bằng chứng vẫn cần được phân biệt.

## Chọn giá trị trước khi chọn thủ pháp

Viết một brief đủ để quyết định: người xem cần nhận gì; họ biết gì trước khi vào; điều sẽ được thấy/nghe trong phim; trạng thái đầu–cuối; phần phải giữ; tài sản đã có; điều chưa biết. Khi chưa có ngách, để tệp khán giả và điều kiện ngách thành biến mở, không tự điền bằng Farm.

Chọn trải nghiệm chính để giải đánh đổi. Một phim vừa muốn hướng dẫn chính xác vừa muốn cho người xem nghỉ ngơi có thể cần cách phân lớp hoặc hai phiên bản; không giải bằng việc thêm đồng thời mọi loại cảnh. Dẫn [AU-001](kien-thuc/AU-001.json), [YT-008](kien-thuc/YT-008.json).

## Các điểm duyệt và đầu ra

| Bước | Quyết định và đầu ra cụ thể | Đủ để chuyển tiếp khi | Nếu chưa đạt |
| --- | --- | --- | --- |
| 1. Brief | Lời hứa, trải nghiệm chính, điều bắt buộc, dữ liệu thiếu | Có thể dùng brief để chọn giữa hai phương án | Làm rõ đúng biến chặn; tiếp tục phần độc lập |
| 2. Kịch bản | Các nhịp đầu→tác động→trạng thái mới, chức năng hình–âm | Mỗi phần có đóng góp; kết trả giá trị phù hợp | Sửa quan hệ hoặc bỏ/gộp nhịp; chưa cần sinh hình đẹp |
| 3. Bản dựng sơ | Ảnh phác có thời gian, âm/lời tạm khi cần | Mạch, lượng thông tin và thời lượng dự kiến có thể theo dõi | Sửa cấu trúc, coverage hoặc cách giao thông tin |
| 4. Khả thi | Tài sản có mã, sổ trạng thái, bài thử shot khó | Phần rủi ro then chốt có cách làm hoặc dự phòng | Sửa ảnh đầu, dàn cảnh, chia job hoặc chọn công đoạn khác |
| 5. Tạo/quay | Yêu cầu theo model/chế độ, các take và lý do dùng/loại | Take đáp ứng chức năng hình–âm và phần phải giữ | Sửa có giả thuyết; không mặc định cứ tăng prompt |
| 6. Dựng nội dung | Chuỗi take theo mạch với âm tạm | Việc đọc được, trạng thái nối hợp lý, thời gian có chức năng | Sửa thứ tự/điểm cắt/thông tin; tạo thêm đúng phần thiếu |
| 7. Hoàn thiện | Âm, màu, chữ/đồ họa, xử lý cục bộ | Các lớp hỗ trợ cùng mục tiêu, không sinh lỗi liên tục | Sửa theo từng tầng; kiểm lại phụ thuộc |
| 8. Bản giao | Tệp xuất, thông số, phiên bản và biên bản kiểm | Tệp mở lại đúng hình/âm, thông tin chính đọc được trong điều kiện dự kiến | Sửa xuất hoặc nguyên nhân nguồn, không chỉ đổi đuôi tệp |
| 9. Học từ kết quả | Phản hồi và số liệu có phạm vi; quyết định giữ/sửa/thử tiếp | Kết luận dẫn đúng loại bằng chứng | Giữ chưa biết, chọn phép kiểm tiếp theo có ích |

Mã điều phối: [QC-007](kien-thuc/QC-007.json), [AI-009](kien-thuc/AI-009.json), [QC-009](kien-thuc/QC-009.json). Việc duyệt cấu trúc chưa xác nhận cảm xúc khán giả; một take đạt ở cận không xác nhận mọi góc khác.

## Sổ tài sản và trạng thái

Nhận diện trả lời “vật/người nào”; trạng thái trả lời “đang ở đâu, ai giữ, đã thay đổi ra sao”. Theo [AI-010](kien-thuc/AI-010.json), tối thiểu ghi:

| Trường | Ví dụ tự biên soạn | Dùng để quyết định |
| --- | --- | --- |
| Mã và bản tài sản | HOP-01@r2; tham chiếu hình đã duyệt | Take nào dùng đúng vật |
| Thuộc tính giữ | Nắp gỗ cùng thiết kế, một khóa đồng | Đổi nhận diện hay chỉ đổi ánh sáng |
| Trạng thái vào | Mở, rỗng, trên bàn, người A giữ nắp | Ảnh đầu có khả thi không |
| Tác động | A đặt vật M01 vào rồi đóng | Điều gì phải được thấy, có thể lược gì |
| Trạng thái ra | Đóng, có M01 bên trong, trên bàn | Shot sau nối từ đâu |
| Phụ thuộc | Shot nhận hộp phải khởi đầu đúng trạng thái | Thay một take ảnh hưởng những đâu |
| Dữ liệu thiếu | Chưa biết mặt sau hộp; chưa kiểm tiếng khóa | Không để AI tự bịa thành phần đã duyệt |

Không khóa độ ướt, mức đầy hay màu hiển thị bất biến nếu hành động/ánh sáng phải làm chúng đổi. Chỉ ghi chi tiết có ích cho nhận diện, quan hệ hoặc bằng chứng; tránh biến sổ thành danh sách ràng buộc không thể thực hiện.

## Từ ý đồ sang yêu cầu tạo AI

Tách bốn lớp. Lớp 1 là chức năng của shot trong phim. Lớp 2 là nội dung và các trạng thái cần đúng. Lớp 3 là tài sản tham chiếu và thẩm quyền của từng ảnh/video. Lớp 4 là cách nhập trong công cụ thật: model/version/chế độ, thông số hỗ trợ, độ dài và cấu hình. Sau cùng là kết quả thực, không nhập ngược điều mong muốn vào cột đã đạt.

Ví dụ ý đồ chung: “cho thấy đáy thùng chạm sàn rồi tay mới nhả; giữ một người, thiết kế thùng, góc máy và nhịp thời gian đã duyệt”. Đây là yêu cầu sản xuất, chưa là cú pháp có thể dán nguyên vào mọi model. Một công cụ cần mô tả chuyển động ngắn; công cụ khác có trường tham chiếu hoặc điều khiển riêng. Kiểm [AI-007](kien-thuc/AI-007.json), [AI-011](kien-thuc/AI-011.json), [AI-013](kien-thuc/AI-013.json).

Nếu công cụ không giữ được ràng buộc, so các đường giải: thay tư thế đầu, đổi dàn cảnh, chia shot theo chức năng, sửa vùng, ghép, thay âm hoặc tạo lại. Chọn theo phần phải giữ và chi phí thực dùng, không theo mong muốn ép một model giải hết. Xem [AI-012](kien-thuc/AI-012.json).

## Khi sửa và khi dừng thử

Mỗi lượt sửa có một câu hỏi: lỗi gì, giả thuyết nguyên nhân nào, đổi gì, giữ gì, xem/đo bằng cách nào? Nếu chưa có đầu ra mới, trạng thái là đề xuất. Nếu thử không cải thiện đúng tiêu chí, kiểm lại giả thuyết, đầu vào hoặc công cụ; không tự tăng độ dài prompt vô hạn.

Ngân sách thử theo ảnh hưởng và độ chưa chắc. Thử sớm cảnh tiếp xúc/nhận diện quyết định kết, giữ cảnh đơn giản đủ tốt và dự phòng công đoạn hậu kỳ. Không có số lần sinh cố định bảo đảm đạt; tính cả take bỏ, phần giây dùng được và công sửa.

## Cầu nối tới thư viện ngách

Phim nguồn giữ riêng, phân tích theo cùng [chuẩn](02_CHUAN_PHAN_TICH.md), rồi rút ứng viên có điều kiện. Ngách thêm tệp khán giả, môi trường, công đoạn/chuyên môn và lựa chọn phong cách. Tầng 1 giữ cách ra quyết định có thể chuyển giao. Khi nâng nguyên lý, giữ cả nguồn thuận/trái và lý do điều kiện mở rộng; không lấy số video hoặc view thay căn cứ.
