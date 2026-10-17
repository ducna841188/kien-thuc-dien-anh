# Thực hành bài 024 — Xâu chuỗi cảnh: kéo dài hành động và dựng phim có kiểm soát

Phần tự biên soạn, chưa chạy thử trên mô hình. Các mốc thời lượng là ý đồ dựng; chọn thiết lập được công cụ thực tế hỗ trợ.

[Về bài chính](README.md)

## 1. Hai đoạn luồn cùng một nan tre

Chỉ thực hiện nếu công cụ hỗ trợ tiếp diễn video; không nhập cả hai như một yêu cầu nhiều cảnh.

```text
Đoạn A: Từ ảnh đã duyệt, cô gái giữ khung rổ bằng tay trái. Tay phải luồn một nan tre qua đúng khe trước mặt, dừng khi nan còn nhô ra. Cận tay, máy tĩnh, thời gian thực, tiếng tre cọ nhỏ.
Sau khi duyệt A, dùng video A làm đầu vào mở rộng: Tiếp tục từ trạng thái cuối. Tay trái vẫn giữ khung. Tay phải kéo chính nan đang nhô ra qua thêm một đoạn, miết nan sát vành rồi dừng. Giữ cùng góc, ánh sáng và nền tiếng.
```

**Tiêu chí đạt:** Không lặp lại từ đầu; nan không đổi; lực và hướng tiếp tục hợp lý; điểm nối không nhảy tay.

## 2. Phương án dựng bằng cắt

Tạo hai cảnh độc lập nếu không có mở rộng.

```text
Cảnh A: Trung cảnh cô gái ngồi đan, hai tay bắt đầu luồn một nan. Máy tĩnh.
Cảnh B: Tạo từ ảnh cận đã duyệt của cùng bộ rổ, cùng trang phục và hướng sáng. Cận hai tay kéo nan qua khe rồi miết xuống. Máy tĩnh; giữ rõ điểm chạm.
Dựng hai cảnh tại cùng pha bắt đầu kéo; chỉ dùng phần chuyển động đạt.
```

**Tiêu chí đạt:** Hai góc cùng diễn tả một thao tác; không báo đây là cảnh dài liền mạch nếu thực tế có cắt.

## Nhật ký thử để tránh kết luận vội

| Phiên bản mô hình/công cụ | Ảnh tham chiếu | Câu lệnh thay đổi | Điểm làm đúng | Lỗi và mốc giây | Dùng/sửa |
| --- | --- | --- | --- | --- | --- |
| Chưa thử | Chưa thử | Chưa thử | Chưa có dữ liệu | Chưa có dữ liệu | Chưa kết luận |

Giữ các biến không liên quan ổn định khi so sánh hai phiên bản. Xem toàn chuyển động, đối chiếu khung đầu–giữa–cuối; không đánh giá chỉ bằng khung đẹp nhất.
