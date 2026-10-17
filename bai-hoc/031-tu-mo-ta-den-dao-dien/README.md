# Bài 031 — Tra cứu máy quay: cỡ cảnh, góc nhìn và chuyển động

Ba quyết định độc lập giúp mô tả cảnh chính xác: nhìn gần đến đâu, nhìn từ hướng/độ cao nào và máy có chuyển động gì. Bài cung cấp thang cỡ cảnh, góc cao–thấp–ngang–nghiêng và nhóm xoay tại chỗ/di chuyển trong không gian để chọn theo mục tiêu kể chuyện.

**Nguồn:** [Từ Mô Tả đến Đạo Diễn- Nâng Cấp Prompt Veo3.1 Của Bạn Ngay Lập Tức](https://drive.google.com/drive/folders/17sYCtB5SAM-8djJiv-yRbp6-yBPuw9fM). Đã đọc **12/12 ảnh**. Ngày biên soạn: 18/10/2026.

[Đọc từng ảnh](doc-anh.md) · [Bài thực hành](thuc-hanh.md) · [Nguồn và mã kiểm tra](nguon.json) · [Danh mục toàn bộ](../../DANH-MUC-BAI-HOC.md)

**Quy ước:** phần “Nguồn” diễn đạt ý trong bộ ảnh. Phần “Phân tích và áp dụng” do người biên soạn bổ sung. Hiệu quả của câu lệnh chưa được kiểm nghiệm bằng lần tạo video trong đợt này.

## Những điều cần học

| Nội dung | Mã ảnh nguồn |
| --- | --- |
| Cỡ cảnh trả lời cần nhìn bằng chứng gì | B031-00, B031-01, B031-02, B031-03, B031-04 |
| Tách độ cao, hướng nhìn và độ nghiêng | B031-05, B031-06, B031-07 |
| Lia, ngẩng/cúi, xoay là đổi hướng tại chỗ | B031-08, B031-09 |
| Dịch chuyển phải có quỹ đạo và vật mốc | B031-08, B031-10 |
| Dùng bảng tra để chọn một phương án | B031-11 |

## 1. Cỡ cảnh trả lời cần nhìn bằng chứng gì

**Nguồn:** Nguồn đưa thang rất rộng → rộng → trung → trung cận → cận → đặc tả.

**Phân tích và áp dụng:** EWS (rất rộng) cho quan hệ người–không gian; WS/LS (toàn/rộng) cho toàn thân; MS (trung) thường từ thắt lưng; MCU (trung cận) thường từ ngực; CU (cận) tập trung mặt/vật; ECU (đặc tả) chỉ chi tiết. Đây là hướng nhận diện, cần nêu phần phải giữ trong khung.

**Ví dụ cho cảnh nông thôn:** Phủ luống dùng toàn thân và chiều dài tấm; đan dùng cận hai tay và khe; phản ứng dùng trung cận mặt.

**Kiểm tra kết quả:** Không chọn cận mặt cho cảnh cần chứng minh vật chạm đất; nhãn khớp hình thực.

![Minh họa nguồn B031-02](anh-goc/02.jpg)

## 2. Tách độ cao, hướng nhìn và độ nghiêng

**Nguồn:** Nguồn giới thiệu góc ngang mắt, cao, thấp và nghiêng cùng các độ cao hông/gối/đất.

**Phân tích và áp dụng:** Viết máy cao bằng gì và nhìn theo hướng nào. High/low angle (góc cao/thấp) mô tả nhìn xuống/lên; hip/knee/ground level (ngang hông/gối/sát đất) mô tả nơi đặt máy. Dutch angle (khung nghiêng) là xoay chân trời, có thể đi cùng góc thấp nhưng không bắt buộc.

**Ví dụ cho cảnh nông thôn:** Máy ngang gối, nhìn gần ngang để thấy bước chân cô dọc luống. Muốn nhìn xuống thao tác bàn, dùng máy cao hơn tay và hướng xuống rõ.

**Kiểm tra kết quả:** Máy có đúng vị trí và hướng, chân trời chỉ nghiêng khi chủ ý; không làm dáng người méo để giả góc.

![Minh họa nguồn B031-07](anh-goc/07.jpg)

## 3. Lia, ngẩng/cúi, xoay là đổi hướng tại chỗ

**Nguồn:** Nguồn phân biệt pan, tilt và roll.

**Phân tích và áp dụng:** Pan (lia ngang) quét trái/phải; tilt (ngẩng/cúi) quét lên/xuống; roll (xoay trục nhìn) làm chân trời quay. Với mỗi yêu cầu nêu điểm đầu/cuối nhìn và tốc độ. Khung nghiêng cố định không đòi tiếp tục roll suốt cảnh.

**Ví dụ cho cảnh nông thôn:** Máy cố định vị trí, cúi chậm từ mặt cô xuống đôi tay đang giữ giỏ. Không đồng thời hạ thân máy xuống sân.

**Kiểm tra kết quả:** Điểm đặt không dịch chuyển vô cớ; hướng nhìn tới đích; không nhầm tilt với nâng/hạ máy.

![Minh họa nguồn B031-09](anh-goc/09.jpg)

## 4. Dịch chuyển phải có quỹ đạo và vật mốc

**Nguồn:** Nguồn liệt kê dolly, tracking/truck, crane/boom và arc/orbit.

**Phân tích và áp dụng:** Dolly in/out (tiến/lùi) đổi khoảng cách; truck (chạy ngang) đổi vị trí sang bên; tracking (bám theo) cần nói từ sau, trước hay bên; crane/boom (nâng/hạ theo cần) đổi độ cao trong không gian; orbit (đi vòng) đổi phía nhìn quanh chủ thể. Zoom đổi góc nhìn qua tiêu cự, không cần thân máy tiến.

**Ví dụ cho cảnh nông thôn:** Bám ngang cùng cô mang giỏ để giữ cỡ toàn thân; hàng cây và bờ luống dịch tương đối. Nếu chỉ cần tập trung mắt, thử tiến rất nhẹ trong cảnh riêng.

**Kiểm tra kết quả:** Nền và chủ thể có quan hệ không gian đúng; nhân vật không xoay thay máy; đường đi không xuyên bàn.

![Minh họa nguồn B031-10](anh-goc/10.jpg)

## 5. Dùng bảng tra để chọn một phương án

**Nguồn:** Nguồn nối mục tiêu kể chuyện với cỡ/góc/chuyển động.

**Phân tích và áp dụng:** Chọn thông tin trước rồi một tổ hợp đơn giản. Thân mật có thể trung cận ngang mắt tĩnh; giới thiệu sân có thể rộng lia chậm. Nếu cần chính xác thao tác, ưu tiên đọc rõ điểm tiếp xúc hơn cảm giác uy lực. Kiểm tra cả đầu–giữa–cuối.

**Ví dụ cho cảnh nông thôn:** Đoạn đời sống: toàn sân ngang mắt tĩnh → cận tay hơi cao tĩnh → trung cận phản ứng tiến nhẹ. Mỗi cảnh một nhiệm vụ.

**Kiểm tra kết quả:** Không đổi góc liên tục chỉ để có nhiều thuật ngữ; từng chuyển động có lý do.

![Minh họa nguồn B031-11](anh-goc/11.jpg)

## Điểm cần hiểu có điều kiện

- Thư mục có 12 tệp: bìa, 01–09, 011, 012; không có tệp tên số 10 trong kiểm kê. Đã đọc đủ hiện có, không bịa trang thiếu.
- Cỡ cảnh, góc và chuyển động là ba trục; CU không tự đồng nghĩa tele (ống kính góc hẹp), góc thấp không tự đồng nghĩa máy đang tiến.
- Khung nghiêng Dutch angle khác tilt ngẩng/cúi; roll là chuyển động xoay, Dutch angle có thể được giữ cố định.
- Tracking không chỉ chạy song song; nguồn có ví dụ bám từ phía sau nên phải ghi rõ đường đi.
- Tác dụng tâm lý của góc là có điều kiện; không tự bảo đảm uy lực/yếu thế/căng thẳng.
- Một số ảnh hoặc chữ mẫu không hoàn toàn khớp nhãn, có chữ lạc; giữ nguyên nguồn và dùng bản thực hành đã làm rõ.
- Không cần máy chuyển động để cảnh có chất điện ảnh; ảnh tĩnh không chứng minh máy đã thực hiện quỹ đạo.

## Cách đưa vào quy trình sản xuất

Xác định điều cần nhìn → chọn cỡ → đặt độ cao/hướng/độ nghiêng → chọn máy tĩnh hoặc một quỹ đạo → nêu chủ thể cần giữ và điểm kết → tạo từ nguồn đã duyệt → xem chuyển động và thao tác → sửa thuật ngữ mâu thuẫn. Bảng tra là gợi ý, không công thức cảm xúc bắt buộc.

## Tự kiểm tra kiến thức

- Máy ngang gối có nhất thiết nhìn lên không?
- Giữ chân trời nghiêng khác xoay roll suốt cảnh ra sao?
- Tracking từ phía sau cần bổ sung gì so với chỉ viết 'tracking'?

**Giới hạn:** đây là tài liệu học từ ảnh. Không dùng một hình minh họa để xác nhận chuyển động, thời lượng, độ chính xác thao tác hay khả năng hiện tại của một sản phẩm. Những phần chưa kiểm chứng được ghi rõ trong bản đọc ảnh.
