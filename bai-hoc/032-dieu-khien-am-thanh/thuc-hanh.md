# Thực hành bài 032 — Chỉ đạo âm thanh: lời, tiếng thao tác, môi trường và khoảng lặng

Phần tự biên soạn, chưa chạy thử trên mô hình. Các mốc thời lượng là ý đồ dựng; chọn thiết lập được công cụ thực tế hỗ trợ.

[Về bài chính](README.md)

## 1. Đặt giỏ lên bàn có tiếng đúng pha

Kiểm tra cùng sự kiện ở hình và tiếng.

```text
Dùng ảnh bối cảnh đã duyệt. Cô gái từ từ hạ chiếc giỏ đang cầm xuống bàn gỗ rồi buông tay. Cận vừa tay và đáy giỏ, máy tĩnh. Tiếng giỏ cọ rất nhỏ khi tay điều chỉnh; một tiếng cộc nhẹ đúng lúc đáy giỏ chạm bàn, tắt dần sau tiếp xúc. Nền sân yên với gió nhỏ. Cảnh không thoại, không nhạc.
```

**Tiêu chí đạt:** Không có tiếng chạm trước vật; giỏ không nhảy; không thêm câu nói/nhạc; nền không lấn tiếng chạm.

## 2. Hai mức yên tĩnh

So hai ý đồ khác nhau, không kỳ vọng câu chữ khóa âm tuyệt đối.

```text
Bản A: Cảnh cận tay vuốt nan tre, chỉ tiếng cọ nan và gió nền rất nhỏ; cảnh không thoại, không nhạc.
Bản B: Giữ cùng hành động và máy. Yêu cầu đầu ra im hoàn toàn trong toàn cảnh. Nếu công cụ vẫn sinh tiếng, bỏ âm trong hậu kỳ và ghi rõ cách đạt kết quả.
```

**Tiêu chí đạt:** A vẫn nghe được vật liệu. B không còn âm sau kiểm tra/xử lý. Không báo mô hình tạo im tuyệt đối nếu đã tắt tiếng hậu kỳ.

## Nhật ký thử để tránh kết luận vội

| Phiên bản mô hình/công cụ | Ảnh tham chiếu | Câu lệnh thay đổi | Điểm làm đúng | Lỗi và mốc giây | Dùng/sửa |
| --- | --- | --- | --- | --- | --- |
| Chưa thử | Chưa thử | Chưa thử | Chưa có dữ liệu | Chưa có dữ liệu | Chưa kết luận |

Giữ các biến không liên quan ổn định khi so sánh hai phiên bản. Xem toàn chuyển động, đối chiếu khung đầu–giữa–cuối; không đánh giá chỉ bằng khung đẹp nhất.
