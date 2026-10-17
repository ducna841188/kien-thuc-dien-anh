# Thực hành bài 003 — Giữ nhất quán thiết kế nhân vật qua năm lớp kiểm soát

Phần tự biên soạn, chưa chạy thử trên mô hình. Các mốc thời lượng là ý đồ dựng; chọn thiết lập được công cụ thực tế hỗ trợ.

[Về bài chính](README.md)

## 1. Ba cảnh cùng một người

Tập tách đặc điểm cố định khỏi hành động và bối cảnh.

```text
HỒ SƠ CỐ ĐỊNH: Lan, nữ Việt Nam 30 tuổi, mặt trái xoan, tóc đen búi thấp, áo bà ba nâu đất vải thô #6B4938, quần đen; phong cách hiện thực tự nhiên.
CẢNH A: trung cảnh Lan đứng ở hiên, nhìn rổ rau, camera cố định.
CẢNH B: sao chép nguyên hồ sơ; Lan trong bếp nhấc rổ bằng hai tay, ánh sáng cửa sổ mềm, trung cảnh.
CẢNH C: sao chép nguyên hồ sơ; cận mặt Lan ở hiên, cô mỉm cười rất nhẹ.
Tạo từng cảnh riêng với ảnh tham chiếu đã duyệt nếu được hỗ trợ. Giữ cấu trúc mặt, tóc, trang phục và chất liệu.
```

**Tiêu chí đạt:** Đánh dấu sáu nhóm: mặt, tóc, hình thể, trang phục, màu mục tiêu, phong cách cho từng cảnh. Không gộp thành tỷ lệ khi chưa định nghĩa cách chấm.

## Nhật ký thử để tránh kết luận vội

| Phiên bản mô hình/công cụ | Ảnh tham chiếu | Câu lệnh thay đổi | Điểm làm đúng | Lỗi và mốc giây | Dùng/sửa |
| --- | --- | --- | --- | --- | --- |
| Chưa thử | Chưa thử | Chưa thử | Chưa có dữ liệu | Chưa có dữ liệu | Chưa kết luận |

Giữ các biến không liên quan ổn định khi so sánh hai phiên bản. Xem toàn chuyển động, đối chiếu khung đầu–giữa–cuối; không đánh giá chỉ bằng khung đẹp nhất.
