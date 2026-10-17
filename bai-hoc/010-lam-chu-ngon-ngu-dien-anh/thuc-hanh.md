# Thực hành bài 010 — Kết hợp cỡ cảnh, góc máy và chuyển động để kể chuyện

Phần tự biên soạn, chưa chạy thử trên mô hình. Các mốc thời lượng là ý đồ dựng; chọn thiết lập được công cụ thực tế hỗ trợ.

[Về bài chính](README.md)

## 1. Ba điểm nhìn cho cùng hành động

Thử ảnh hưởng của góc máy mà kiểm soát các biến khác.

```text
Đầu vào cùng nhân vật Lan áo bà ba nâu, đứng cạnh bàn ở hiên; cô đặt rổ rồi nhìn sang mẹ. Giữ cùng cỡ trung cảnh, thời lượng, ánh sáng mềm và camera đứng tại vị trí mỗi shot.
A. Máy ngang tầm mắt Lan, đường chân trời ngang.
B. Máy cao hơn nhìn xuống vừa phải, giữ rổ trong khung.
C. Máy thấp hơn nhìn lên vừa phải, giữ cả mặt và rổ, chân trời ngang.
Tạo từng bản riêng, dùng ảnh tham chiếu khi hỗ trợ. Ghi mọi thay đổi cắt khung cần thiết. Không coi cảm xúc của ba bản đã được quyết định chỉ bằng tên góc.
```

**Tiêu chí đạt:** So thông tin nhìn thấy, tỷ lệ người/môi trường, mức đọc mặt/tay và cảm giác trong ngữ cảnh. Chọn bản phục vụ câu chuyện.

## 2. Phân biệt pan với truck

Nhận diện chuyển động từ kết quả, không chỉ từ prompt.

```text
Bối cảnh hiên nhà có cột gỗ gần máy, Lan ở giữa và cổng phía xa.
BẢN PAN: máy đứng tại một vị trí, xoay từ trái sang phải để thấy từ cổng tới Lan.
BẢN TRUCK: máy dời ngang từ trái sang phải, giữ hướng nhìn và độ cao tương đối ổn định; cột gần đổi vị trí so với cổng xa.
Giữ thiết kế cảnh. Tạo riêng hai shot, ghi model và thiết lập.
```

**Tiêu chí đạt:** Pan đổi hướng nhìn tại chỗ; truck có dịch chuyển vị trí và thay tương quan gần–xa. Nếu nền méo/chảy thì không coi là thị sai đúng.

## Nhật ký thử để tránh kết luận vội

| Phiên bản mô hình/công cụ | Ảnh tham chiếu | Câu lệnh thay đổi | Điểm làm đúng | Lỗi và mốc giây | Dùng/sửa |
| --- | --- | --- | --- | --- | --- |
| Chưa thử | Chưa thử | Chưa thử | Chưa có dữ liệu | Chưa có dữ liệu | Chưa kết luận |

Giữ các biến không liên quan ổn định khi so sánh hai phiên bản. Xem toàn chuyển động, đối chiếu khung đầu–giữa–cuối; không đánh giá chỉ bằng khung đẹp nhất.
