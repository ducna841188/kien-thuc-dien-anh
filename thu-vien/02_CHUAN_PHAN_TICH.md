# Chuẩn phân tích video theo thời gian và bằng chứng

## Các lượt phân tích

1. Tiếp nhận: tệp/URL, nguồn, checksum nếu có, độ dài, audio, tỉ lệ, fps nếu xác định được, các phần cắt và offset.
2. Đọc toàn cảnh: lời hứa, thay đổi chính, cách vào/kết, các phân đoạn. Nêu giả thuyết khán giả riêng.
3. Lập ranh giới: shot theo cut/chuyển cảnh thực; không đặt lại ranh giới chỉ vì mỗi giây đổi hình.
4. Quan sát từng shot và sự kiện: hành động, tiếp xúc, máy, hình, tiếng và những phần chưa biết.
5. Xem các điểm nối: trạng thái vật, hướng, thời gian, thông tin, âm và lý do giữ/cắt.
6. Tổng hợp chuỗi: tiến trình, mong chờ/kết quả, nhịp và ý đồ cảm xúc.
7. Rút ứng dụng: giữ điều kiện và phản ví dụ, tách kế hoạch tái dựng khỏi nguồn.

Nếu không có khả năng xem/nghe đầy đủ trong lượt đó, ghi độ phủ thật và ưu tiên xem lại các đoạn ảnh hưởng kết luận. Không đánh dấu đã kiểm toàn bộ chỉ vì có metadata hoặc ảnh mẫu.

## 25 nhóm thuộc tính cho mỗi shot

Tóm tắt; số chủ thể; nhận diện; hành động; trạng thái đầu; tiếp xúc/biến đổi; trạng thái cuối; bối cảnh; bố cục; cỡ cảnh; vị trí/góc máy; chuyển động máy; hiệu ứng ống/phối cảnh; nét; ánh sáng; màu; chất liệu; chữ trong hình; cách xử lý thời gian; điểm vào; điểm ra; âm nền; tiếng hành động; thoại; nhạc.

Mỗi thuộc tính lưu value, status, basis, evidence_refs và uncertainty_reason. Được phép chưa biết; không dùng một câu mẫu chung để giả hoàn tất tất cả shot.

| Trạng thái | Ý nghĩa |
| --- | --- |
| observed | Điều thực sự quan sát; ghi loại bằng chứng trực tiếp |
| source_report | Nội dung được một bảng/báo cáo thuật lại |
| interpretation | Cách đọc hoặc phân loại chưa thể coi là đo trực tiếp |
| unknown | Chưa đủ dữ liệu; value = null và có lý do |
| synthetic | Ví dụ thiết kế/giả lập, không phải video có thật |

## Từng giây và dưới một giây

Shot, sự kiện và khoảng âm dùng giây số. Một giây có thể chứa nhiều shot; một shot có thể dài nhiều giây. Sự kiện ngắn dùng mốc nhỏ hơn một giây khi bằng chứng cho phép. Chỉ mục từng giây được suy từ các khoảng đã có để tra cứu, không biến ảnh mẫu thành độ phủ chuyển động.

Mốc của đoạn cắt phải quy về bản gốc bằng offset. Quy ước khoảng [start, end): chứa điểm đầu, không chứa điểm cuối. Không đổi phút:giây sang frame timecode khi chưa biết fps; video tốc độ khung biến thiên cần theo timestamp thực khi công cụ cho đo.

## Những kết luận cần kiểm đặc biệt

- Chuyển động máy, vận tốc, vật xuyên/biến hình: cần diễn tiến, không chỉ một ảnh.
- Cut/dissolve/J-cut/L-cut: cần xem/nghe quanh ranh giới tương ứng.
- Âm phát lúc tiếp xúc: cần nghe và đối chiếu với hình.
- Tiêu cự, loại máy, LUT, khẩu độ: thiếu metadata không tự đoán thành thông số thật.
- Cảm xúc khán giả: ý đồ và diễn giải khác phản hồi có phương pháp thu.

## Tổng hợp nhịp và cảm xúc

Ghi theo khoảng: việc khán giả đang theo, thông tin mới, điều đang chờ, nguồn nhịp trong hình/tiếng/dựng, trải nghiệm dự kiến, bằng chứng và giới hạn. Điểm số nếu tự tạo phải có định nghĩa; không báo như phép đo tâm lý chuẩn.

Mẫu ở mau/phan-tich-video.json. Ví dụ trong vi-du/phan-tich-gia-lap.json chỉ dùng kiểm cấu trúc.

## Phân tích sâu

Phân biệt ba tuyến: điểm cắt; sự kiện/thay đổi có ý nghĩa; âm. Một sự kiện có thể qua nhiều shot, một shot có thể có nhiều sự kiện. Giữ ranh giới shot theo bằng chứng cắt/chuyển cảnh; dùng sự kiện và findings/diễn giải để mô tả đổi mục tiêu hoặc quan hệ, không sửa cut cho khớp cảm giác nhịp.

Rà chức năng theo thứ tự: lời hứa→điều đáng quan tâm→thông tin mới→cách làm rõ bằng hình/âm→điểm cắt/chuyển thời gian→bằng chứng kết quả. Ở tiếp xúc, ghi điểm đỡ/người giữ, pha chạm–chuyển lực–nhả và trạng thái ra. Với bố cục/màu/ánh sáng, kiểm biến đổi trong cả diễn tiến và qua các góc, không chỉ ảnh đầu.

Trước thống kê nhiều phim, định nghĩa nhãn và mẫu số: theo số shot hay theo thời lượng; phần đã xem và phần chưa rõ; nhãn quan sát hay nhãn nguồn thuật lại. Lưu bất đồng giữa lượt gắn nhãn, chỉ gộp phần tương thích. Một nhận định từ phim nhiều view vẫn là giả thuyết về tác dụng cho đến khi có bằng chứng phù hợp.

Mã mở rộng: EV-007, EV-008, AU-007, DR-008, CA-011, ED-009, ED-010, YT-010. Xem [bảng kiểm trải nghiệm](07_KIEM_TRA_TRAI_NGHIEM.md) để không suy cảm xúc từ chỉ số hành vi.
