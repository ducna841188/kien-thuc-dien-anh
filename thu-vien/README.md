# FILM-KB — Thư viện kiến thức làm phim cho AI

Phiên bản **1.1.0**, ngày 18/10/2026. **130 mục thực hành · 13 chuyên đề · 10 hồ sơ nhịp–cảm xúc · 5 quy trình tác vụ · 137 thuật ngữ.**

Lượt rà tầng 1: giữ nguyên 60 mục, làm rõ 30 mục, thêm 40 mục; đối chiếu 27 nguồn ngoài. [Báo cáo thay đổi](kiem-toan/RA_SOAT_1_1_0.md) · [Dữ liệu rà từng mục](kiem-toan/ra-soat-1.1.0.json).

Thư viện chung phục vụ làm phim cho khán giả YouTube, từ căn bản đến nâng cao. Bản này ưu tiên dữ liệu và hướng dẫn cho AI; bản minh họa dành cho người học sẽ làm sau. Kiến thức theo ngách ở repo riêng và liên kết mã/phiên bản.

## Bắt đầu

1. [Hướng dẫn AI](00_HUONG_DAN_AI.md).
2. [Chuẩn phân tích](02_CHUAN_PHAN_TICH.md) và [chuẩn quyết định](03_RA_QUYET_DINH.md).
3. [Mục lục JSON](muc-luc.json), [tra theo vấn đề](tuyen-tra-cuu.json), [bản đồ nhịp–cảm xúc](NHIP_CAM_XUC.md).
4. [Bản đồ năng lực](08_BAN_DO_NANG_LUC.md), [vận hành sản xuất](06_VAN_HANH_SAN_XUAT.md) và [kiểm trải nghiệm](07_KIEM_TRA_TRAI_NGHIEM.md).
5. [Bốn ca áp dụng](vi-du/bon-ca-ra-quyet-dinh.md) và [gói đọc cho AI](goi-doc/START_HERE.md).

## Các chuyên đề

| Nhóm | Phạm vi | Nội dung |
| --- | --- | --- |
| EV | Tách điều quan sát được, suy luận và đề xuất; giữ mốc thời gian và độ phủ. | [Bằng chứng và chuẩn phân tích](chuyen-de/01-bang-chung-va-phan-tich.md) |
| AU | Chọn nhu cầu, lượng thông tin, mức mong chờ và trải nghiệm cần kiểm. | [Khán giả, chú ý và cảm xúc](chuyen-de/02-khan-gia-chu-y-cam-xuc.md) |
| ST | Xây thay đổi từ đơn vị hành động đến toàn phim; chọn điều cần kể bằng hình/tiếng. | [Kịch bản và cấu trúc](chuyen-de/03-kich-ban-va-cau-truc.md) |
| DR | Tổ chức người, vật, không gian và hành vi có mục tiêu. | [Đạo diễn, diễn xuất và dàn cảnh](chuyen-de/04-dao-dien-dan-canh.md) |
| CA | Chọn thông tin trong khung, góc nhìn, khoảng cách và vùng nét. | [Bố cục, máy quay và quang học](chuyen-de/05-bo-cuc-may-quay-quang-hoc.md) |
| MO | Phân biệt máy/người/môi trường, chỉ đạo quỹ đạo và loại nhịp thời gian. | [Chuyển động và thời gian](chuyen-de/06-chuyen-dong-thoi-gian.md) |
| LI | Thiết kế nguồn, hướng, chất lượng và độ tương phản có thể đối chiếu. | [Ánh sáng](chuyen-de/07-anh-sang.md) |
| CO | Tổ chức màu từ vật liệu đến hậu kỳ; giữ quan hệ màu qua chuỗi. | [Màu sắc và thiết kế hình ảnh](chuyen-de/08-mau-sac-thiet-ke-hinh.md) |
| ED | Chọn điểm cắt, thông tin, thời gian và nhịp căng–thả ở nhiều quy mô. | [Dựng phim và điều khiển nhịp](chuyen-de/09-dung-phim-va-nhip.md) |
| SO | Gắn tiếng với không gian, sự kiện và ưu tiên cảm nhận. | [Âm thanh, nhạc và lời kể](chuyen-de/10-am-thanh-nhac-loi.md) |
| AI | Chuyển ý đồ thành đầu vào, kiểm kết quả và chọn cách sửa. | [Sản xuất bằng AI](chuyen-de/11-san-xuat-bang-ai.md) |
| QC | Duyệt, thử có kiểm soát, quản lý phiên bản và nâng kiến thức đúng phạm vi. | [Kiểm tra và học từ kết quả](chuyen-de/12-kiem-tra-va-hoc-tu-ket-qua.md) |
| YT | Kết nối cách giới thiệu phim, trải nghiệm xem và dữ liệu khán giả. | [YouTube: lời hứa và phản hồi](chuyen-de/13-youtube-loi-hua-phan-hoi.md) |

## Quy trình và chuẩn dữ liệu

- [Phân tích video](quy-trinh/01-phan-tich-video.md).
- [Kịch bản](quy-trinh/02-kich-ban.md).
- [Danh sách shot](quy-trinh/03-danh-sach-shot.md).
- [Câu lệnh AI](quy-trinh/04-cau-lenh-ai.md).
- [Chẩn đoán và sửa lỗi](quy-trinh/05-chan-doan-sua-loi.md).
- [Kiến trúc dữ liệu](01_KIEN_TRUC_DU_LIEU.md), [schema](schema/), [mẫu](mau/), [ví dụ](vi-du/).
- [Hồ sơ mô hình](mo-hinh/README.md), [từ điển](TU_DIEN.md), [bộ đánh giá AI](kiem-thu/HUONG_DAN_DANH_GIA.md).

## Nguồn, phiên bản và nhánh ngách

[Kiểm toán nguồn](05_NGUON_VA_KIEM_TOAN.md) · [Sổ nguồn dễ đọc](nguon/SO_NGUON.md) · [Quy tắc cập nhật](04_CAP_NHAT_KIEN_THUC.md) · [Manifest](manifest.json) · [Nhật ký](CHANGELOG.md).

[Nhánh Farm](https://github.com/ducna841188/yt-ly-tu-that/tree/main/Farm/Thu_vien_kien_thuc) có hồ sơ khán giả và cách áp dụng riêng. [33 bài ảnh gốc](../DANH-MUC-BAI-HOC.md) vẫn được giữ nguyên.

**Phạm vi nghiệm thu:** nội dung biên soạn, cấu trúc dữ liệu, liên kết, nguồn và ca kiểm tra. Chưa tạo video mới, chưa đánh giá độc lập trên các AI khác và chưa xác nhận tác dụng cảm xúc bằng người xem.
