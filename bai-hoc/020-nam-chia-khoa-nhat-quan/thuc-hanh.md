# Thực hành bài 020 — Năm lớp giữ nhất quán nhân vật — bài ôn và áp dụng

Phần tự biên soạn, chưa chạy thử trên mô hình. Các mốc thời lượng là ý đồ dựng; chọn thiết lập được công cụ thực tế hỗ trợ.

[Về bài chính](README.md)

## 1. Ba cảnh cùng một người

Bài ôn cho tạo từ văn bản hoặc bố trí cảnh với tham chiếu: giữ khối nhận diện, thay việc làm. Chỉ dùng ảnh tham chiếu theo đúng chế độ được hỗ trợ.

```text
HỒ SƠ CỐ ĐỊNH: Lan, nữ Việt Nam 30 tuổi, mặt trái xoan, tóc đen búi thấp, áo bà ba nâu đất vải thô #6B4938, quần đen; phong cách hiện thực tự nhiên.
CẢNH A: trung cảnh Lan đứng ở hiên, nhìn rổ rau, camera cố định.
CẢNH B: sao chép nguyên hồ sơ; Lan trong bếp nhấc rổ bằng hai tay, ánh sáng cửa sổ mềm, trung cảnh.
CẢNH C: sao chép nguyên hồ sơ; cận mặt Lan ở hiên, cô mỉm cười rất nhẹ.
Tạo từng cảnh riêng với ảnh tham chiếu đã duyệt nếu được hỗ trợ. Giữ cấu trúc mặt, tóc, trang phục và chất liệu.
```

**Tiêu chí đạt:** Đánh dấu sáu nhóm: mặt, tóc, hình thể, trang phục, màu mục tiêu, phong cách cho từng cảnh. Không gộp thành tỷ lệ khi chưa định nghĩa cách chấm.

## 2. Ảnh đã duyệt → một thao tác đan giỏ

Thử prompt tập trung chuyển động sau khi ảnh cảnh đã giữ đúng mặt, vóc dáng và trang phục. Không cần tạo ảnh hay video ngay trong đợt đọc bài này.

```text
Đầu vào ngoài prompt: một ảnh cảnh đã duyệt, thấy đúng nhân vật ngồi trước giỏ và nan tre, hai tay ở vị trí chuẩn bị thao tác.
Chuyển động: người phụ nữ giữ vành giỏ bằng tay trái. Tay phải luồn một đầu nan qua khe cạnh vành, kéo nhẹ để nan nằm sát rồi dừng. Máy cố định theo khung ảnh, thời gian thật; thấy rõ tay, nan và điểm tiếp xúc. Âm nan cọ nhẹ, nền vườn rất nhỏ.
```

**Tiêu chí đạt:** Giữ nhận diện/hình thể/trang phục của ảnh; nan đi qua đúng khe, tay không xuyên giỏ; không sinh thêm người. Lưu ảnh đầu vào, câu lệnh, chế độ và lỗi theo giây.

## Nhật ký thử để tránh kết luận vội

| Phiên bản mô hình/công cụ | Ảnh tham chiếu | Câu lệnh thay đổi | Điểm làm đúng | Lỗi và mốc giây | Dùng/sửa |
| --- | --- | --- | --- | --- | --- |
| Chưa thử | Chưa thử | Chưa thử | Chưa có dữ liệu | Chưa có dữ liệu | Chưa kết luận |

Giữ các biến không liên quan ổn định khi so sánh hai phiên bản. Xem toàn chuyển động, đối chiếu khung đầu–giữa–cuối; không đánh giá chỉ bằng khung đẹp nhất.
