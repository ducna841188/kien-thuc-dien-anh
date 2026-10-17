# Thực hành bài 030 — Chẩn đoán nhầm thoại và lập phiếu phân vai

Phần tự biên soạn, chưa chạy thử trên mô hình. Các mốc thời lượng là ý đồ dựng; chọn thiết lập được công cụ thực tế hỗ trợ.

[Về bài chính](README.md)

## 1. Điền phiếu rồi tạo một lượt

Dùng hai nhân vật đã duyệt; chưa chạy thử.

```text
PHIẾU LƯỢT A
Nhân vật nói: bà theo ảnh góc A, ngồi bên trái bàn.
Người nghe: cô gái, bên phải bàn, chỉ lộ vai tiền cảnh.
Lời nguyên văn: 'Con đã đan xong chiếc giỏ chưa?'
Giọng: tiếng Việt, giọng nữ lớn tuổi ấm, tốc độ vừa.
Máy: trung cận bà, tĩnh, giữ rõ miệng.
Hành động: bà hỏi một câu rồi nhìn cô gái; tay nghỉ trên bàn.
Bối cảnh: giữ ảnh đã duyệt, cùng giỏ và nguồn sáng.
Âm thanh: chỉ bà có lời, nền sân nhỏ.
```

**Tiêu chí đạt:** Chấm năm mục riêng: vai/lời/giọng/môi/máy. Nếu một mục sai, ghi mốc giây và đề xuất sửa đúng mục.

## 2. Tạo lượt đáp riêng, kiểm tra sao chép ngược

Không mang cả câu của A vào lần tạo B.

```text
Dùng ảnh góc B đã duyệt: cô gái bên phải bàn là người nói duy nhất, nhìn về phía bà bên trái ngoài vùng thấy miệng. Cô nói tiếng Việt bằng giọng nữ trẻ tự nhiên: 'Vâng, con vừa làm xong.' Sau câu cô gật rất nhẹ rồi môi nghỉ. Trung cận, máy tĩnh, cùng bối cảnh và nền sân của cảnh A.
```

**Tiêu chí đạt:** Tên, mặt, vị trí, giọng và câu đều thuộc B; không tự nhắc lại câu của bà; hai góc giữ cùng không gian.

## Nhật ký thử để tránh kết luận vội

| Phiên bản mô hình/công cụ | Ảnh tham chiếu | Câu lệnh thay đổi | Điểm làm đúng | Lỗi và mốc giây | Dùng/sửa |
| --- | --- | --- | --- | --- | --- |
| Chưa thử | Chưa thử | Chưa thử | Chưa có dữ liệu | Chưa có dữ liệu | Chưa kết luận |

Giữ các biến không liên quan ổn định khi so sánh hai phiên bản. Xem toàn chuyển động, đối chiếu khung đầu–giữa–cuối; không đánh giá chỉ bằng khung đẹp nhất.
