# Bài 015 — Logic chuyển động và ràng buộc cảnh

12 ảnh về mô tả chuyển động, duy trì nhân vật/bối cảnh/camera và chuyển ý trừu tượng thành biểu hiện nhìn thấy. Tài liệu phân biệt mẹo viết prompt với suy đoán về cơ chế AI, đồng thời sửa nhầm lẫn về zoom, máy tĩnh và chuyển động nền.

**Nguồn:** [Bí Mật Veo 3.1- Tại Sao AI Không "Vẽ" Video Mà Chỉ "Dự Đoán Chuyển Động"? (Làm Chủ Logic Vật Lý)](https://drive.google.com/drive/folders/15eT4W3GaEGptuMmpU0ArNPc0Bt89hIdv). Đã đọc **12/12 ảnh**. Ngày biên soạn: 17/10/2026.

[Đọc từng ảnh](doc-anh.md) · [Bài thực hành](thuc-hanh.md) · [Nguồn và mã kiểm tra](nguon.json) · [Danh mục toàn bộ](../../DANH-MUC-BAI-HOC.md)

**Quy ước:** phần “Nguồn” diễn đạt ý trong bộ ảnh. Phần “Phân tích và áp dụng” do người biên soạn bổ sung. Hiệu quả của câu lệnh chưa được kiểm nghiệm bằng lần tạo video trong đợt này.

## Những điều cần học

| Nội dung | Mã ảnh nguồn |
| --- | --- |
| Mô tả quan hệ nhân–quả quan sát được | B015-03, B015-10, B015-11 |
| Tách chuyển động chủ thể, camera và môi trường | B015-03, B015-09, B015-10 |
| Giữ ba nhóm ràng buộc thiết yếu | B015-04, B015-05 |
| Chuyển ý cảm xúc thành biểu hiện | B015-01, B015-06, B015-08 |
| Dùng đúng từ, kiểm tra đúng kết quả | B015-07, B015-08, B015-09, B015-10 |

## 1. Mô tả quan hệ nhân–quả quan sát được

**Nguồn:** Nguồn khuyên nêu hướng, vị trí máy và phản ứng môi trường để AI có yêu cầu rõ về chuyển động.

**Phân tích và áp dụng:** Dùng chuỗi trạng thái đầu → chuyển động → tiếp xúc → kết quả. Nêu tay/dụng cụ nào tác động vật nào. Các điều này là yêu cầu đầu ra có thể kiểm tra, không chứng minh AI chạy bộ mô phỏng vật lý hay dựng mô hình 3D tường minh.

**Ví dụ cho cảnh nông thôn:** Tay trái giữ mép giỏ, tay phải đưa bó rau xuống; đáy bó chạm đáy giỏ rồi tay buông. Giỏ đặt yên trên bàn suốt shot.

**Kiểm tra kết quả:** Có tiếp xúc trước hệ quả; vật không xuyên nhau, biến dạng vô cớ, bay hoặc biến mất.

![Minh họa nguồn B015-03](anh-goc/03.jpg)

## 2. Tách chuyển động chủ thể, camera và môi trường

**Nguồn:** Nguồn gắn hành động chính với chuyển động camera và nền.

**Phân tích và áp dụng:** Ba lớp có thể cùng chuyển động hoặc một số đứng yên. Với máy tĩnh, người chạy ngang khung và hậu cảnh cố định là hợp lý. Với máy theo người, người có thể giữ vị trí gần ổn định trong khung trong khi hậu cảnh trôi. Chỉ cho lá/cành dịch khi có gió hoặc tiếp xúc, không yêu cầu nền tự chuyển để trông sống.

**Ví dụ cho cảnh nông thôn:** Máy tĩnh nhìn bờ ruộng, người gánh rau đi từ trái qua phải. Bản khác máy theo ngang giữ người giữa khung, ruộng phía sau trôi tương ứng.

**Kiểm tra kết quả:** Không nhầm người đứng tại chỗ thành đang đi; nền thay đổi phù hợp với đường máy.

![Minh họa nguồn B015-09](anh-goc/09.jpg)

## 3. Giữ ba nhóm ràng buộc thiết yếu

**Nguồn:** Nguồn dùng ràng buộc nhân vật, môi trường và camera để giảm lỗi tính liên tục.

**Phân tích và áp dụng:** Tạo bảng nhận diện, sơ đồ không gian và thông số máy mong muốn. Giữ mô tả thiết yếu và tham chiếu nếu có; tránh yêu cầu trái nhau. Continuity là tính liên tục, gồm cả trạng thái vật, hướng nhìn, thời tiết và diễn tiến hành động.

**Ví dụ cho cảnh nông thôn:** Áo nâu, khăn be, giỏ tre cố định; sân gạch và cửa gỗ cùng vị trí; sáng từ sân; máy trung cảnh tĩnh trong thao tác đặt rau.

**Kiểm tra kết quả:** Đối chiếu khung đầu–giữa–cuối và đầu shot sau; ghi chính xác thứ bị đổi.

![Minh họa nguồn B015-05](anh-goc/05.jpg)

## 4. Chuyển ý cảm xúc thành biểu hiện

**Nguồn:** Nguồn minh họa thay từ 'ngầu' hoặc 'buồn' bằng tư thế, ánh sáng, bố cục và nhịp.

**Phân tích và áp dụng:** Có thể giữ từ cảm xúc làm định hướng rồi thêm một đến hai dấu hiệu nhìn thấy/nghe được. Tránh công thức rập khuôn như cứ buồn là xanh lạnh hoặc cứ điện ảnh là xóa phông. Chỉ đạo diễn xuất bằng hành vi nhỏ hợp nhân vật.

**Ví dụ cho cảnh nông thôn:** Người nhìn luống cây héo, hạ vai và dừng bàn tay trên vành chậu; ánh sáng tự nhiên vẫn ấm, tiếng gió thưa. Sắc thái lo lắng đến từ hành vi.

**Kiểm tra kết quả:** Biểu hiện vừa đủ, không tự thêm khóc hoặc cử chỉ cường điệu.

![Minh họa nguồn B015-06](anh-goc/06.jpg)

## 5. Dùng đúng từ, kiểm tra đúng kết quả

**Nguồn:** Nguồn có mẫu năm phần và bảng thuật ngữ camera, khuyên chọn dolly-in khi muốn tiến gần vật lý.

**Phân tích và áp dụng:** Zoom thay đổi tiêu cự; dolly thay vị trí máy. Nếu muốn nhìn rõ hình khối do tiến gần, mô tả máy dịch; nếu muốn đổi khung bằng tiêu cự, zoom là từ đúng. Các nhãn 8K, cinematic hay 'chống thất bại' không thay tiêu chí kiểm tra. Thứ tự năm phần khác bài trước nhưng vẫn dùng được như bảng kế hoạch.

**Ví dụ cho cảnh nông thôn:** Để thấy bàn tay và giỏ gần dần có quan hệ không gian rõ, yêu cầu máy tiến chậm; để giữ góc nhìn cố định mà thu khung, yêu cầu zoom riêng.

**Kiểm tra kết quả:** Chuyển động đúng loại, hành động đúng nhân quả, nhận diện ổn định; không suy độ phân giải từ prompt.

![Minh họa nguồn B015-10](anh-goc/10.jpg)

## Điểm cần hiểu có điều kiện

- Giải thích 'AI dựng thế giới 3D trong tưởng tượng' là ẩn dụ của nguồn, chưa chứng minh kiến trúc Veo 3.1.
- 'AI chỉ hiểu vật lý' quá tuyệt đối; tài liệu này không khẳng định cơ chế nhận thức của mô hình.
- Nhân vật chạy trước camera đứng yên là dàn cảnh hợp lệ; hậu cảnh không cần tự chuyển động.
- Zoom là đổi tiêu cự, không phải AI hiểu sai. Dolly-in phù hợp khi ý đồ là máy dịch tới gần.
- 90%, dẫn đầu thị trường, render nhanh và chống thất bại không có kiểm chứng tương ứng trong ảnh.
- Không có định mức bắt buộc 5–7 từ mô tả ánh sáng; cỡ cảnh và cảm xúc do góc máy không phải luật cứng.

## Cách đưa vào quy trình sản xuất

Lập trạng thái đầu/cuối → tách ba lớp chuyển động → giữ ràng buộc quan trọng → chọn camera/ánh sáng phục vụ thao tác → tạo một shot → xem thời gian thật và chậm để tìm lỗi → sửa một quan hệ bị sai. Khi dùng bài cho thao tác nông thôn, ưu tiên điểm tiếp xúc và trạng thái vật liệu.

## Tự kiểm tra kiến thức

- Một người chạy với hậu cảnh đứng yên có thể đúng khi nào?
- Dolly và zoom khác nhau ở thay vị trí máy hay tiêu cự?
- Tại sao mô tả rõ nhân quả chưa bảo đảm mô hình làm đúng vật lý?

## Nguồn đối chiếu bổ sung

- [Google DeepMind: thẻ mô hình Veo 3](https://storage.googleapis.com/deepmind-media/Model-Cards/Veo-3-Model-Card.pdf): Nguồn chính thức về giới hạn nhất quán trong cảnh phức tạp của Veo 3; không dùng làm mô tả chi tiết kiến trúc hoặc bảo đảm cho phiên bản 3.1.
- [Google: hướng dẫn prompt video](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/video-gen-prompt-guide): Đối chiếu thuật ngữ máy, chuyển động và chỉ dẫn hình ảnh.

**Giới hạn:** đây là tài liệu học từ ảnh. Không dùng một hình minh họa để xác nhận chuyển động, thời lượng, độ chính xác thao tác hay khả năng hiện tại của một sản phẩm. Những phần chưa kiểm chứng được ghi rõ trong bản đọc ảnh.
