# Thực hành bài 006 — Giảm lỗi hình thể, màu và phụ kiện bằng yêu cầu có mục tiêu

Phần tự biên soạn, chưa chạy thử trên mô hình. Các mốc thời lượng là ý đồ dựng; chọn thiết lập được công cụ thực tế hỗ trợ.

[Về bài chính](README.md)

## 1. Kiểm một hành động nhấc rổ

So hai phiên bản chỉ khác nội dung loại trừ nếu công cụ có trường đó.

```text
MÔ TẢ CHÍNH: trung cảnh ngang mắt, Lan áo bà ba nâu vải thô nhấc một rổ tre bằng hai tay, chậm và rõ, từ bàn lên ngang eo; máy cố định, ánh sáng mềm.
BẢN A: dùng mô tả chính và ảnh chuẩn.
BẢN B: giữ nguyên đầu vào; nếu có trường negative theo hướng dẫn Veo, thêm: extra fingers, duplicated limbs, warped basket, clothing changes, texture bleeding.
Nghĩa tiếng Việt: thừa ngón, chi nhân đôi, rổ méo, thay trang phục, chất liệu tràn. Không chép phần giải thích này vào trường loại trừ. Với công cụ không hỗ trợ, dùng mô tả tích cực phù hợp thay thế.
```

**Tiêu chí đạt:** Ghi lỗi ở giai đoạn chạm, nhấc và giữ; kiểm cả phần bị che. Nhiều bản thử mới giúp đánh giá xu hướng, một cặp chưa đủ kết luận tỷ lệ.

## Nhật ký thử để tránh kết luận vội

| Phiên bản mô hình/công cụ | Ảnh tham chiếu | Câu lệnh thay đổi | Điểm làm đúng | Lỗi và mốc giây | Dùng/sửa |
| --- | --- | --- | --- | --- | --- |
| Chưa thử | Chưa thử | Chưa thử | Chưa có dữ liệu | Chưa có dữ liệu | Chưa kết luận |

Giữ các biến không liên quan ổn định khi so sánh hai phiên bản. Xem toàn chuyển động, đối chiếu khung đầu–giữa–cuối; không đánh giá chỉ bằng khung đẹp nhất.
