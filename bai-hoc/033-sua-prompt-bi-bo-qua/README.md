# Bài 033 — Chẩn đoán và sửa prompt bị bỏ qua

Tách ba nhóm lỗi camera, hành động và phong cách/ràng buộc; xây bản thử đơn giản rồi thay từng yếu tố. Mục tiêu là xác định điều gì thực sự sai trong clip, giữ phần đã đúng và tránh nhồi thêm yêu cầu khi chưa rõ nguyên nhân.

**Nguồn:** [VEO đang làm ngơ prompt của bạn](https://drive.google.com/drive/folders/1_I1lxxVN8q4UgmE6NTPtgANVvrTZ_9kt). Đã đọc **14/14 ảnh**. Ngày biên soạn: 18/10/2026.

[Đọc từng ảnh](doc-anh.md) · [Bài thực hành](thuc-hanh.md) · [Nguồn và mã kiểm tra](nguon.json) · [Danh mục toàn bộ](../../DANH-MUC-BAI-HOC.md)

**Quy ước:** phần “Nguồn” diễn đạt ý trong bộ ảnh. Phần “Phân tích và áp dụng” do người biên soạn bổ sung. Hiệu quả của câu lệnh chưa được kiểm nghiệm bằng lần tạo video trong đợt này.

## Những điều cần học

| Nội dung | Mã ảnh nguồn |
| --- | --- |
| Bắt đầu từ lỗi quan sát được | B033-00, B033-01, B033-02, B033-13 |
| Ghi cỡ cảnh, đường máy và điểm đến | B033-03, B033-04 |
| Viết thao tác có trạng thái đầu và kết quả | B033-05, B033-06 |
| Tổ chức phong cách, ràng buộc và âm thanh | B033-07, B033-08, B033-09 |
| Tạo mốc thử rồi thay đúng một biến | B033-10, B033-11, B033-12, B033-13 |

## 1. Bắt đầu từ lỗi quan sát được

**Nguồn:** Bộ ảnh chia vấn đề thành camera, trình tự hành động và phong cách/ràng buộc; nêu mơ hồ, quá tải, mâu thuẫn như nguyên nhân thường gặp.

**Phân tích và áp dụng:** Viết một dòng: mong muốn gì, thực tế gì, lỗi ở mốc giây nào. Đây là giả thuyết chẩn đoán, không phải bằng chứng mọi lỗi do prompt. Giữ danh sách phần đã đạt để tránh sửa lan sang nhân vật, nhịp hay ánh sáng đang tốt.

**Ví dụ cho cảnh nông thôn:** Clip sân nhà đã đúng nhịp và ánh sáng nhưng sinh thêm người: đặt mục tiêu sửa số người trước, không đồng thời đổi góc máy và hành động.

**Kiểm tra kết quả:** Nhật ký có một sai lệch đo được và những yếu tố cần giữ.

![Minh họa nguồn B033-02](anh-goc/02.jpg)

## 2. Ghi cỡ cảnh, đường máy và điểm đến

**Nguồn:** Nguồn khuyên một chuyển động chính, mô tả cụ thể camera và đặt thông tin quan trọng ở vị trí dễ nhận thấy.

**Phân tích và áp dụng:** Phân biệt cỡ cảnh với chuyển động; xác định máy di chuyển hay xoay, theo chủ thể nào, bắt đầu/kết thúc ở đâu. Thử một đường máy đơn giản trước; hiệu ứng rung phụ chỉ thêm khi thật sự cần. Việc đưa lên đầu là cách trình bày, không phải khóa ưu tiên bảo đảm.

**Ví dụ cho cảnh nông thôn:** Trung cảnh một người ngồi bên bàn tre; máy tiến thẳng chậm từ khung thấy thân trên đến khung thấy mặt và vai, người giữ vị trí. Không gọi zoom nếu ý đồ là máy tiến trong không gian.

**Kiểm tra kết quả:** Theo dõi cả chủ thể lẫn nền để phân biệt máy thực hiện đường đi hay chỉ thay đổi kích thước hình.

![Minh họa nguồn B033-04](anh-goc/04.jpg)

## 3. Viết thao tác có trạng thái đầu và kết quả

**Nguồn:** Nguồn dùng động từ + đối tượng + phản ứng, một hành động chính và các nhịp chuẩn bị–chuyển biến–kết quả.

**Phân tích và áp dụng:** Xác định ai làm, tác động vào vật nào, tiếp xúc bằng bộ phận nào, kết quả giữ ở đâu. Chia ba nhịp trong một thao tác thay vì yêu cầu ba việc lớn không liên quan. Chỉ thêm phản ứng môi trường có nguyên nhân hợp lý.

**Ví dụ cho cảnh nông thôn:** Một người đặt tay lên chốt cửa gỗ, nâng chốt khỏi móc rồi đẩy cánh cửa mở; ánh sáng từ sân lọt qua khe mở rộng. Chạm chốt đơn thuần chưa đủ tạo kết quả mở cửa.

**Kiểm tra kết quả:** Xem đầu–giữa–cuối: chốt có thực sự rời móc trước khi cửa mở, tay có bám đúng vật không?

![Minh họa nguồn B033-06](anh-goc/06.jpg)

## 4. Tổ chức phong cách, ràng buộc và âm thanh

**Nguồn:** Nguồn chọn một phong cách chủ đạo, nhóm điều cần có/không có, chia âm nền, hiệu ứng và thoại; dùng hành vi để thể hiện cảm xúc.

**Phân tích và áp dụng:** Ghi một đặc điểm hình ảnh chính và thuộc tính hỗ trợ nhất quán. Chọn ràng buộc theo lỗi thực tế, giữ điều thiết yếu ngay từ bản đầu. Với âm thanh, nói rõ âm nào nổi bật và âm nào chỉ làm nền; phân biệt thứ tự liệt kê với thứ tự nghe. SynthID không phải chữ trên hình.

**Ví dụ cho cảnh nông thôn:** Cảnh bàn tre theo hình ảnh hiện thực với ánh sáng sớm dịu. Tiếng bát chạm khay rõ đúng thời điểm, chim xa nhỏ ở nền; nếu cảnh không cần thoại thì nói rõ điều đó. Một người duy nhất là điều phải giữ.

**Kiểm tra kết quả:** Không xuất hiện phong cách hoặc nhân vật ngoài ý đồ; tiếng chạm nghe được, không bị nhạc/âm nền che.

![Minh họa nguồn B033-08](anh-goc/08.jpg)

## 5. Tạo mốc thử rồi thay đúng một biến

**Nguồn:** Quy trình trong ảnh: khung năm thành phần, đơn giản hóa, thử một biến, giữ một lựa chọn chính và thêm lớp khi ổn.

**Phân tích và áp dụng:** Lưu bản hiện tại trước. Nếu quá rối, tạo mốc đơn giản và ghi nhận đã thay nhiều điều. Khi mốc đạt, đổi một biến có thể kiểm tra; ghi đúng cài đặt và xem toàn clip. Thêm âm/negative có thể làm thay đổi kết quả lần sinh tiếp theo. Nếu vẫn lỗi, kiểm tra đầu vào/chế độ hoặc đổi shot, không vô hạn thêm câu.

**Ví dụ cho cảnh nông thôn:** Giữ cùng ảnh một người xếp bát, cùng hành động và ánh sáng. Bản A máy cố định; bản B chỉ thay đường máy tiến chậm. Nếu đang sửa người thừa, giữ camera đã tốt và chỉ chỉnh phạm vi người trong cảnh.

**Kiểm tra kết quả:** So sánh theo tiêu chí đã đặt, ghi cả lỗi mới phát sinh và phần giữ được; lặp khi cần trước khi kết luận hiệu quả.

![Minh họa nguồn B033-11](anh-goc/11.jpg)

## Điểm cần hiểu có điều kiện

- 90% và lời hứa sửa trong 10 phút là tuyên bố trong nguồn, không có số liệu hay thử nghiệm kèm theo để bảo đảm.
- Đặt camera lên đầu, chọn một chuyển động hay chia ba nhịp là phương pháp tổ chức ý; không phải tham số cưỡng chế hoặc luật đúng với mọi tình huống.
- Ở B033-04 có vùng chữ hỏng phía trên bên phải; không tự đoán thành câu. Hướng dẫn rõ phía dưới được ghi lại và ảnh gốc được giữ để đối chiếu.
- Ví dụ tracking cộng handheld trong nguồn cho thấy chính nguồn cũng phối hợp đường máy và tính chất rung. 3% không có định nghĩa đo; tránh coi là tham số được công cụ hỗ trợ.
- Không đồng nhất phối hợp nhiều nguồn sáng/phong cách với mâu thuẫn: cần xét ý đồ và quan hệ cụ thể. Slow dolly với chủ thể chuyển động nhanh vẫn có thể là một lựa chọn quay có chủ ý.
- SynthID là dấu kỹ thuật vô hình theo tài liệu Google DeepMind; khác chữ phủ, logo và dấu tên nhìn thấy. Không dùng một dòng prompt để coi như đã tắt cơ chế kỹ thuật.
- Việc tạo lại sau khi sửa chữ không bảo đảm giữ mọi chi tiết video đã đạt. Bản thử một biến cần giữ các đầu vào/cài đặt có thể giữ và ghi rõ yếu tố không kiểm soát được.
- Lỗi có thể liên quan mô hình: trang Veo chính thức cũng ghi nhận tiếng nói tự nhiên, ổn định ở đoạn ngắn còn là lĩnh vực đang phát triển. Đừng quy mọi kết quả sai cho người dùng.

## Cách đưa vào quy trình sản xuất

Lưu bản đang dùng → chọn một lỗi có mốc giây → ghi phần đã đạt cần giữ → đặt giả thuyết → nếu cần tạo bản mốc đơn giản → thay một biến từ bản mốc → tạo/xem đủ clip → ghi kết quả → giữ, thử lại hoặc đổi cách quay. Chỉ thêm lớp phong cách/âm thanh khi có mục tiêu; không bỏ ràng buộc cốt yếu. Khi yêu cầu vượt khả năng chế độ hiện có, chọn đầu vào hoặc phương án shot/dựng phù hợp hơn.

## Tự kiểm tra kiến thức

- Vì sao bỏ hết phong cách để lập bản đơn giản chưa phải phép thử chỉ thay một biến?
- Làm sao phân biệt một người sai hành động với camera không thực hiện tracking?
- Trong cảnh mở cửa, các trạng thái vật lý nào phải nối với nhau để ánh sáng lọt qua có nguyên nhân?
- Vì sao không thể dùng câu no watermark để kết luận SynthID đã bị vô hiệu?

## Nguồn đối chiếu bổ sung

- [Google DeepMind — SynthID](https://deepmind.google/models/synthid/): Đối chiếu rằng dấu kỹ thuật này không nhìn thấy bằng mắt, khác chữ phủ trên hình. Truy cập 18/10/2026 theo giờ Việt Nam.
- [Google DeepMind — Veo](https://deepmind.google/models/veo/): Đối chiếu giới hạn được nhà phát triển nêu về tiếng nói tự nhiên và ổn định; không quy mọi lỗi cho cấu trúc câu lệnh. Truy cập 18/10/2026 theo giờ Việt Nam.

**Giới hạn:** đây là tài liệu học từ ảnh. Không dùng một hình minh họa để xác nhận chuyển động, thời lượng, độ chính xác thao tác hay khả năng hiện tại của một sản phẩm. Những phần chưa kiểm chứng được ghi rõ trong bản đọc ảnh.
