# Thực hành bài 023 — Câu lệnh loại trừ: sửa đúng nhóm lỗi, giữ đúng thiết kế

Phần tự biên soạn, chưa chạy thử trên mô hình. Các mốc thời lượng là ý đồ dựng; chọn thiết lập được công cụ thực tế hỗ trợ.

[Về bài chính](README.md)

## 1. Sửa số người, giữ thao tác đã đạt

Dùng lại bản câu lệnh timelapse có thao tác đúng; chỉ tập trung lỗi nhân đôi.

```text
Dùng ảnh cảnh đã duyệt. Một người phụ nữ duy nhất thực hiện toàn bộ lao động. Tạo một cảnh tua nhanh thời gian liên tục: cô liên tiếp kéo, căng và đặt tấm phủ dài theo chiều luống; vị trí làm việc thay đổi nhanh vì lao động dài được nén trong clip. Giữ nguyên máy, cảnh và hướng thao tác của phiên bản đã đạt.
Nếu có ô loại trừ riêng: người nhân đôi, bản sao nhân vật, tay thừa, người làm thứ hai.
```

**Tiêu chí đạt:** Đúng một người trong mọi thời điểm; vẫn tua nhanh, vẫn trải tấm phủ chứ không chuyển tấm giữa hai luống.

## 2. Chỉ thêm một nhóm hình học

So sánh bản cơ sở và bản thêm danh sách ngắn.

```text
Cận hai tay theo ảnh đã duyệt. Một tay giữ nan tre, tay kia luồn một nan qua khe trước mặt rồi dừng. Máy tĩnh; giữ rõ tiếp xúc tay–nan, âm thanh tre cọ nhẹ.
Bản so sánh, nếu có ô loại trừ: tay thừa, ngón dính, nan xuyên tay.
```

**Tiêu chí đạt:** Ghi lỗi theo giây cho cả hai bản; không kết luận chỉ từ một khung hoặc một lần may mắn.

## Nhật ký thử để tránh kết luận vội

| Phiên bản mô hình/công cụ | Ảnh tham chiếu | Câu lệnh thay đổi | Điểm làm đúng | Lỗi và mốc giây | Dùng/sửa |
| --- | --- | --- | --- | --- | --- |
| Chưa thử | Chưa thử | Chưa thử | Chưa có dữ liệu | Chưa có dữ liệu | Chưa kết luận |

Giữ các biến không liên quan ổn định khi so sánh hai phiên bản. Xem toàn chuyển động, đối chiếu khung đầu–giữa–cuối; không đánh giá chỉ bằng khung đẹp nhất.
