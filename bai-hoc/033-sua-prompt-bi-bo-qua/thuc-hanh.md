# Thực hành bài 033 — Chẩn đoán và sửa prompt bị bỏ qua

Phần tự biên soạn, chưa chạy thử trên mô hình. Các mốc thời lượng là ý đồ dựng; chọn thiết lập được công cụ thực tế hỗ trợ.

[Về bài chính](README.md)

## 1. Sửa đúng lỗi người thừa

Bắt đầu từ một bản đã đúng hành động, camera và ánh sáng. Đây là mẫu yêu cầu sửa câu lệnh, không phải công tắc trong mô hình.

```text
Hãy sửa câu lệnh gốc bên dưới, chỉ xử lý lỗi xuất hiện người thừa.
[Câu lệnh gốc và thông tin chế độ thực tế]
Phần đã đạt cần giữ: hành động, vị trí đồ vật, ánh sáng, phong cách và đường máy.
Mong muốn: toàn cảnh chỉ có đúng một người là nhân vật chính; không có người ở nền, gương, bóng phản chiếu hoặc hình người mới.
Giữ loại nhịp thời gian đang dùng; nếu bản gốc là timelapse, giữ timelapse. Không tự đổi sang thời gian thực.
Trả về câu lệnh đã sửa và liệt kê chính xác những đoạn đổi. Nếu thiếu câu lệnh gốc, yêu cầu bổ sung thay vì tự bịa phiên bản được cho là giữ nguyên.
```

**Tiêu chí đạt:** Có bản gốc thực tế để so chữ; chỉ đổi phạm vi người/ràng buộc liên quan. Sau khi sinh cần xem trọn clip, vì sửa đúng chữ chưa xác nhận video đạt.

## 2. Camera A/B từ cùng một cảnh

Tạo hai bản theo các thiết lập có thể giữ ổn định; chỉ đổi mô tả camera.

```text
Nội dung chung: Một người ngồi ở bàn tre sân nhà, nhấc một chiếc bát bằng tay phải rồi đặt vào khay và buông tay. Ánh sáng sớm dịu; tiếng bát chạm khay rõ, chim xa nhỏ. Giữ nguyên đầu vào, phong cách và thiết lập giữa hai bản.
Bản A — Camera: trung cảnh, máy cố định nhìn ngang bàn.
Bản B — Camera: bắt đầu cùng trung cảnh, máy tiến thẳng chậm về phía bàn tay, kết ở khung gần thấy tay và khay; một chuyển động liên tục.
Chỉ dùng một dòng Camera tương ứng khi chạy mỗi bản; không dán cả A lẫn B vào một prompt.
```

**Tiêu chí đạt:** Bản A thực sự cố định; bản B có máy tiến như mô tả, đồng thời vẫn hoàn thành thao tác đặt bát. Ghi những khác biệt không chủ ý và chưa kết luận từ một lần may mắn.

## 3. Kiểm tra nguyên nhân và kết quả

Tập mô tả thao tác mở cửa có đủ các trạng thái cần thiết.

```text
Máy cố định ở trung cảnh, thấy bàn tay và cánh cửa gỗ. Một người đứng bên cửa đang đóng, chốt ngang nằm trong móc. Người đó dùng tay nâng chốt khỏi móc, rồi đẩy cửa mở một đoạn và giữ cánh cửa. Ánh sáng sớm từ phía sân lọt qua khe mở. Tiếng chốt gỗ bật nhẹ trước tiếng bản lề kêu. Một người duy nhất, một thao tác mở cửa liên tục.
```

**Tiêu chí đạt:** Chốt thoát móc trước khi cửa mở; tay tiếp xúc đúng; cửa không xuyên người; ánh sáng và tiếng có thời điểm gắn hành động. Nếu quá nhiều lỗi, tách thử thao tác chốt và chuyển động cửa.

## Nhật ký thử để tránh kết luận vội

| Phiên bản mô hình/công cụ | Ảnh tham chiếu | Câu lệnh thay đổi | Điểm làm đúng | Lỗi và mốc giây | Dùng/sửa |
| --- | --- | --- | --- | --- | --- |
| Chưa thử | Chưa thử | Chưa thử | Chưa có dữ liệu | Chưa có dữ liệu | Chưa kết luận |

Giữ các biến không liên quan ổn định khi so sánh hai phiên bản. Xem toàn chuyển động, đối chiếu khung đầu–giữa–cuối; không đánh giá chỉ bằng khung đẹp nhất.
