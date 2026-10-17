# Bài 001 — Bốn cấu trúc camera thiết yếu dành cho AI Director

**Ý chính cần học:** chọn cách quay theo điều khán giả cần nhận ra hoặc cảm thấy trong cảnh. Sau đó mới mô tả đường đi của máy, khung hình đầu và khung hình cuối.

| Thông tin | Giá trị |
| --- | --- |
| Tên thư mục nguồn | 4 Cấu Trúc Camera Thiết Yếu Dành Cho AI Director |
| Nguồn | [Bài trên Google Drive](https://drive.google.com/drive/folders/1T8Eq1hxU22Cmk63jmHwSObFfVhCL8B3n) |
| Phạm vi đọc | 12/12 ảnh: một bìa, hai trang dẫn nhập, tám trang kỹ thuật, một trang tổng kết |
| Độ phân giải | Tất cả ảnh: 1834 × 1024 điểm ảnh |
| Trạng thái | Đã đọc ảnh và biên soạn; chưa thử sinh video |
| Bản đối chiếu | [Đọc từng ảnh](doc-anh.md) · [Bài thực hành](thuc-hanh.md) · [Danh mục nguồn](nguon.json) |

Trong bài này, **“nguồn”** là điều đọc được từ bộ ảnh. **“Phân tích bổ sung”** là phần giải thích và đề xuất thực hành do người biên soạn xây dựng. Các hiệu quả cảm xúc được xem là khả năng phụ thuộc bối cảnh, không phải kết quả chắc chắn.

## 1. Bản đồ kiến thức

![Sơ đồ tự biên soạn: vị trí máy đầu, cuối và cách nhìn bốn kỹ thuật](minh-hoa/bon-cach-xu-ly-may-quay.png)

*Hình bổ sung, mô tả nguyên lý. A là vị trí đầu, B là vị trí cuối; sơ đồ không mô tả tỷ lệ không gian hoặc tốc độ thực tế.*

| Bạn muốn khán giả nhận gì? | Lựa chọn nên thử | Thay đổi cần nhìn thấy | Nguồn |
| --- | --- | --- | --- |
| Chú ý hơn đến trạng thái nhân vật | **Push-in — tiến máy** | Khoảng cách máy–chủ thể giảm; khung hình thường chặt hơn | B001-03, 04 |
| Hiểu hình khối, quan hệ chủ thể–không gian | **Orbit — đi máy vòng quanh chủ thể** | Góc nhìn thay đổi; các lớp cảnh dịch chuyển tương đối | B001-05, 06 |
| Phát hiện bối cảnh hoặc thông tin mới | **Reveal — cú máy hé lộ**, ví dụ **dolly-out — lùi máy** | Cuối cảnh cho thấy điều đầu cảnh chưa cho thấy | B001-07, 08 |
| Cảm giác đang ở gần một sự kiện diễn ra | **Handheld — máy cầm tay** | Dao động có kiểm soát, giữ hành động quan trọng dễ đọc | B001-09, 10 |
| Theo dõi thao tác rõ, yên hoặc chờ đợi | **Static shot — cảnh máy cố định** | Máy đứng yên; chuyển động và ý nghĩa đến từ bên trong khung | Phân tích bổ sung; đối chiếu [Adobe](https://blog.adobe.com/en/publish/2018/02/26/6-tips-still-photographers-learning-shoot-video) |

Hàng cuối được bổ sung để tránh suy ra rằng cảnh điện ảnh bắt buộc phải chuyển động máy. Tài liệu Adobe khuyên làm chủ chuyển động trong khung trước khi thêm chuyển động máy.

### Bốn mục trong ảnh không cùng một loại khái niệm

**Phân tích bổ sung:** tiến máy và đi vòng mô tả **đường đi**; hé lộ mô tả **dụng ý kể chuyện**; cầm tay mô tả **cách vận hành**. Vì vậy chúng có thể kết hợp. Ví dụ một máy cầm tay vẫn có thể tiến gần, hoặc một cú đi vòng có thể hé lộ một vật phía sau chủ thể.

Khi mới học, nên thử riêng từng yếu tố để nhận ra tác dụng. Khi kết hợp, hãy xác định yếu tố chính và lý do của phần kết hợp.

Đừng nhầm đường máy với **cỡ cảnh** — toàn, trung, cận — hoặc **góc máy** — ngang mắt, thấp, cao. Một cú đi vòng vẫn có thể giữ cùng cỡ cảnh và độ cao.

## 2. Tiến máy — đưa sự chú ý đến gần nhân vật

![Ảnh nguồn B001-03: tiến máy và tập trung cảm xúc](anh-goc/03.jpg)

### Nội dung nguồn

Ảnh 03 gắn kỹ thuật với nội tâm, tâm trạng và khoảnh khắc quyết định. Ảnh 04 nêu tình huống suy tư, độc thoại, nhìn vào vật quan trọng hoặc bộc lộ cảm xúc.

Câu lệnh gốc: `slow push-in toward the character` — **máy từ từ tiến về phía nhân vật**.

### Phân tích bổ sung

Hãy xác định **điểm chú ý ở cuối cảnh**. Đó có thể là đôi mắt, nét mặt khi nhìn một vật, hoặc một chi tiết trên bàn. Tiến máy có mục đích khi việc đến gần giúp khán giả đọc điều trước đó còn nhỏ hoặc ít nổi bật.

Ví dụ với phim sinh hoạt nông thôn: cô gái kiểm tra nan tre sau khi vót. Máy tiến nhẹ từ trung cảnh đến khung gần hơn để người xem đọc được sự tập trung và thay đổi biểu cảm nhỏ. Không cần thêm một trạng thái bi kịch chỉ để “có cảm xúc”.

**Phân biệt với zoom — thay đổi tiêu cự:** dolly đưa máy đến vị trí khác; zoom thay đổi tiêu cự khi máy có thể ở nguyên vị trí. Hai cách đều có thể làm chủ thể lớn hơn trong khung nhưng không tạo cùng quan hệ phối cảnh. Đây là phân biệt kỹ thuật được [hướng dẫn Google](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/video-gen-prompt-guide#camera_movements) nêu rõ.

### Cách viết cho AI

- Điểm đầu: nhân vật được thấy ở cỡ nào, máy ở độ cao nào.
- Đường máy: tiến nhẹ về một đích rõ ràng; nói rõ nhân vật có đứng yên hay không.
- Điểm cuối: phần nào của nhân vật hoặc vật thể cần đọc rõ.
- Điều giữ ổn định: gương mặt, trang phục, hướng sáng và bố trí đồ vật.

### Cách tự kiểm tra

Chủ thể phải lớn lên do máy tiến, thay vì tự đi sát máy ngoài dự định. Hậu cảnh giữ được quan hệ không gian hợp lý. Cảnh không tự cắt sang một góc khác. Nếu AI chỉ phóng to khung hoặc đổi mặt nhân vật, chưa đạt ý đồ của bài tập.

### Điều không nên học thành luật

Ảnh 04 có nhận định máy đứng yên dẫn đến không có cảm xúc. Nhận định này quá tuyệt đối. Một gương mặt, khoảng lặng hoặc bàn tay chậm lại trong cảnh cố định vẫn có thể truyền tải cảm xúc. Tiến máy là một lựa chọn nhấn mạnh, không phải điều kiện bắt buộc.

## 3. Đi vòng quanh chủ thể — cho thấy chiều sâu và quan hệ không gian

![Ảnh nguồn B001-05: máy đi vòng quanh một nhân vật](anh-goc/05.jpg)

### Nội dung nguồn

Ảnh 05 gắn kỹ thuật với chiều sâu và vẻ uy lực. Ảnh 06 nêu bối cảnh rộng, giới thiệu địa điểm, khoảnh khắc anh hùng hoặc cao trào.

Câu lệnh gốc: `smooth 30-degree orbit around the character` — **máy đi êm theo cung ba mươi độ quanh nhân vật**.

### Phân tích bổ sung

Máy đổi vị trí trên một cung quanh chủ thể, đồng thời giữ hướng nhìn về chủ thể. Thứ thay đổi là góc nhìn và tương quan các lớp không gian. Hình có nhiều lớp gần–xa sẽ giúp người học nhận ra chuyển động rõ hơn.

Đừng để AI diễn giải “quay quanh” thành **nhân vật tự xoay tại chỗ**. Trong bài tập đầu tiên, có thể giữ nhân vật tương đối ổn định và chỉ thay đường máy.

**Khác với pan — lia ngang:** lia ngang xoay hướng nhìn từ một vị trí; đi vòng đổi vị trí máy quanh chủ thể. [Adobe mô tả pan](https://www.adobe.com/uk/creativecloud/video/production/cinematography/camera-shots-and-angles/pan-shot.html) là chuyển động xoay ngang từ điểm đặt máy cố định.

### Cách viết cho AI

Chỉ định góc nhìn đầu, phía máy đi sang, cung ngắn mong muốn và góc kết thúc. Nếu muốn cỡ nhân vật không thay đổi nhiều, thêm yêu cầu giữ khoảng cách và độ cao gần như ổn định. Tránh yêu cầu một vòng lớn khi không có ảnh tham chiếu các mặt còn lại của nhân vật hoặc bối cảnh.

Ba mươi độ là con số trong ví dụ nguồn. Bộ ảnh không đưa ra bằng chứng rằng đây là góc tối ưu cho mọi cảnh, hoặc AI luôn thực hiện chính xác con số đó.

### Ví dụ áp dụng

Một cung nhẹ quanh cô gái ngồi ở sân có thể làm rõ vị trí người, bàn tre và hiên nhà. Nếu mục tiêu là xem tay vót nan, máy cố định ở góc đọc rõ thao tác thường đáng thử trước; không cần đi vòng chỉ để tạo cảm giác chuyển động.

### Cách tự kiểm tra

Góc nhìn phải thực sự đổi. Các vật ở gần và xa không trượt như những tấm ảnh rời. Nhân vật không tự xoay, đổi khuôn mặt, đổi quần áo hoặc mọc thêm chi. Đồ vật không xuất hiện, biến mất vô lý khi đi sang góc khác.

## 4. Hé lộ — quyết định thông tin nào xuất hiện ở cuối cảnh

![Ảnh nguồn B001-07: hình ghép minh họa ý tưởng mở từ nhân vật sang không gian](anh-goc/07.jpg)

*Ảnh nguồn là hình ghép minh họa. Không có video để xác nhận đây là hai khung của cùng một cú máy liên tục, hoặc xác nhận tốc độ chuyển động.*

### Nội dung nguồn

Ảnh 07 sử dụng lùi máy để mở bối cảnh. Ảnh 08 đề xuất dùng ở đầu video, đầu chương, chỗ chuyển phân đoạn hoặc khi cần giới thiệu không gian ấn tượng.

Câu lệnh gốc: `slow dolly-out to reveal the environment` — **máy từ từ lùi ra để hé lộ môi trường xung quanh**.

### Phân tích bổ sung

Câu hỏi quan trọng nhất là: **khán giả biết thêm điều gì ở khung cuối?** Nếu đầu và cuối chỉ khác mức rộng, nhưng không thêm thông tin có ích, cú máy có thể chỉ tạo chuyển động trang trí.

Ví dụ: mở đầu thấy cô gái đang ngồi đan; khi máy lùi, người xem mới nhận ra cô ngồi dưới hiên một ngôi nhà, cạnh nhiều rổ tre đã hoàn thành. Không gian mới làm rõ nơi chốn và kết quả công việc.

Hé lộ không chỉ thực hiện bằng lùi máy. Một cú lia sang bên cũng có thể đưa thông tin ban đầu nằm ngoài khung vào tầm nhìn; [Adobe có mô tả riêng kiểu lia hé lộ](https://www.adobe.com/uk/creativecloud/video/production/cinematography/camera-shots-and-angles/pan-shot.html). Bài này giữ lùi máy làm ví dụ chính để bám nguồn.

### Cách viết cho AI

1. Nêu khung đầu thấy gì.
2. Nêu đường máy giúp mở thêm phần nào của không gian.
3. Nêu khung cuối phải thấy rõ điều gì mới.
4. Giữ các vật thể thuộc cùng một không gian liên tục.

Nếu ảnh đầu quá chặt và phần bối cảnh cần mở ra chưa có tham chiếu, AI phải suy diễn vùng chưa thấy. Khi tính nhất quán quan trọng, nên chuẩn bị thêm ảnh toàn cảnh của cùng bối cảnh.

### Cách tự kiểm tra

Thông tin mới xuất hiện có chủ đích và dễ đọc. Vị trí nhân vật không bị đổi vô cớ. Không gian không tự biến thành một địa điểm khác. Không có vật thể lớn mọc vào giữa cảnh để tạo hiệu ứng “hoành tráng”.

## 5. Máy cầm tay — lựa chọn cảm giác hiện diện

![Ảnh nguồn B001-09: máy cầm tay trong một bối cảnh chạy giữa phố mưa](anh-goc/09.jpg)

### Nội dung nguồn

Ảnh 09 gắn máy cầm tay với cảm giác quay thật. Ảnh 10 đề xuất hành động, rượt đuổi, đối thoại căng thẳng, phim tài liệu hoặc sinh tồn.

Câu lệnh gốc: `subtle handheld shake 3–5%` — **dao động máy cầm tay nhẹ, với mức “ba đến năm phần trăm” theo cách viết trong ảnh**.

### Phân tích bổ sung

Hãy coi cầm tay là lựa chọn về cảm giác quan sát. Độ rung cần phù hợp với hoàn cảnh người cầm máy và việc khán giả phải theo dõi. Rung không tự sửa được lỗi tay, vật lý, ánh sáng hoặc tính nhất quán.

Trong phim yên tĩnh, một cảnh cầm tay rất nhẹ có thể gợi sự gần gũi; một cảnh cố định cũng có thể phù hợp hơn. Trong cảnh chạy, mức dao động có thể lớn hơn nhưng vẫn phải đọc được hướng đi và hành động chính. Đây là đề xuất nghệ thuật, không phải số đo bắt buộc.

### Vì sao không áp dụng máy móc “3–5%”?

Bộ ảnh không định nghĩa phần trăm này đo theo chiều cao khung, góc xoay, biên độ dịch chuyển hay cường độ một hiệu ứng. Không thể đổi nó thành tham số chung cho mọi mô hình video. Nếu công cụ có thanh chỉnh rung thật, phải xem đúng thang đo của công cụ đó.

Với câu lệnh văn bản, có thể thử mô tả bằng hành vi nhìn thấy: **dao động nhỏ, chậm; khung hình vẫn dễ đọc; đường chân trời tương đối ổn định**. Chưa có lần sinh video trong đợt này để chứng minh cách diễn đạt nào hiệu quả hơn.

### Cách tự kiểm tra

Rung đến từ chuyển động của toàn khung, không phải đồ vật tự uốn cong. Mặt, bàn tay và chi tiết cần quan sát vẫn đọc được. Không xuất hiện cú giật hoặc đổi góc vô cớ. Nếu rung làm mất thông tin cần học từ thao tác thủ công, hãy giảm rung hoặc chuyển sang máy cố định.

## 6. Những nhận định cần chú giải

| Mã | Nội dung trong nguồn | Cách hiểu dùng trong kho học tập |
| --- | --- | --- |
| N01 | Ảnh 01 quy phần lớn chất lượng chưa đạt cho camera, kèm con số 90% | Nguồn không đưa dữ liệu hoặc phương pháp đo. Không dùng con số này làm thống kê đã được chứng minh. |
| N02 | Ảnh 04 gắn máy đứng yên với không có cảm xúc | Không dùng như quy luật. Biểu cảm, hành động trong khung, âm thanh và thời gian cũng tạo cảm xúc. |
| N03 | Ảnh 05–06 gắn đi vòng với uy lực, chiều sâu và cảnh hành động hay hơn | Đây là khả năng về cách thể hiện; phù hợp hay không phụ thuộc câu chuyện, dàn cảnh và vị trí máy. |
| N04 | Ảnh 07 dùng lùi máy để hé lộ | Giữ đúng là một cách thực hiện. Không đồng nhất “hé lộ” với duy nhất một đường máy. |
| N05 | Ảnh 09 đưa mức rung 3–5% | Đơn vị chưa được định nghĩa. Không coi là tham số chuẩn hoặc bảo đảm được AI thực hiện. |
| N06 | Ảnh 10 liên hệ hình sạch, ổn định với cảm giác giả như đồ họa máy tính | Ổn định không đồng nghĩa giả. Đánh giá thêm ánh sáng, vật liệu, chuyển động chủ thể và tính nhất quán. |
| N07 | Tên bài gọi chung bốn mục là cấu trúc camera | Dùng tên nguồn để tra cứu; trong phân tích, phân biệt đường đi, dụng ý kể chuyện và cách vận hành. |

Các nhận xét ở cột cuối là phân tích bổ sung. Chúng không thay đổi nội dung ảnh gốc và không gán lại cho người làm bộ ảnh.

## 7. Chuyển kiến thức thành yêu cầu cho một cảnh

**Khung thực hành tự biên soạn:** mục tiêu → khung đầu → hành động chủ thể → bối cảnh → một lựa chọn máy chính → khung cuối → điều cần giữ nhất quán.

Ví dụ: “Khán giả nhận ra cô gái đang tập trung kiểm tra nan tre. Bắt đầu trung cảnh ngang mắt khi ngồi. Cô giữ nan tre và nhìn theo mép nan. Máy tiến rất nhẹ. Kết thúc ở khung gần hơn để đọc ánh mắt; vẫn giữ nan tre ở mép dưới khung. Giữ nguyên mặt, tóc, trang phục, vị trí ghế và hướng sáng.”

Đây là đề xuất tổ chức câu lệnh của tài liệu này, không phải cú pháp bắt buộc của một mô hình. [Google DeepMind](https://deepmind.google/models/veo/prompt-guide/) cũng khuyến khích xác định khung hình, chuyển động, ánh sáng, nhân vật, địa điểm và hành động khi viết yêu cầu.

Với nguồn ảnh chuyển thành video, hãy kiểm tra ảnh tham chiếu có đủ không gian cho khung cuối hay không. Một chuyển động máy đẹp vẫn có thể không dùng được nếu làm sai thao tác hoặc nhân vật.

Mở [bài thực hành](thuc-hanh.md) để lấy bốn câu lệnh đầy đủ, một cảnh cố định làm mốc đối chiếu, bảng dựng nông thôn ba mươi giây và phiếu chấm kết quả.

## 8. Từ vựng để tra nhanh

| Thuật ngữ | Nghĩa dùng trong bài |
| --- | --- |
| AI Director | Người đạo diễn quá trình tạo video bằng AI |
| Push-in / dolly-in | Tiến máy về phía chủ thể |
| Dolly-out / pull-back | Lùi máy ra xa chủ thể |
| Orbit / arc shot | Đi máy theo cung quanh chủ thể |
| Pan | Lia ngang từ vị trí đặt máy cố định |
| Tilt | Ngẩng hoặc cúi hướng nhìn từ vị trí đặt máy cố định |
| Zoom | Thay đổi tiêu cự để đổi góc nhìn bao quát và độ lớn chủ thể trong khung |
| Reveal | Hé lộ thông tin, nhân vật hoặc không gian trước đó chưa thấy |
| Handheld | Cách quay cầm tay, có thể có dao động |
| Static / locked-off | Máy được giữ cố định |
| Hero shot | Cảnh tôn chủ thể, thường nhấn vai trò hoặc vẻ nổi bật |
| Parallax | Sự dịch chuyển tương đối của các lớp gần–xa khi điểm nhìn di chuyển |
| CGI | Hình ảnh được tạo bằng đồ họa máy tính |
| Prompt | Câu lệnh mô tả đầu vào cho AI |

## 9. Nguồn đối chiếu bổ sung

Các nguồn dưới chỉ dùng đối chiếu thuật ngữ và hướng dẫn viết yêu cầu; không chứng minh các tỷ lệ, hiệu quả tuyệt đối hoặc tỷ lệ thành công của bộ ảnh.

- [Google — Video generation prompt guide](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/video-gen-prompt-guide): phân biệt dolly, zoom, cung máy, máy cố định và cầm tay.
- [Google DeepMind — How to create effective prompts with Veo 3](https://deepmind.google/models/veo/prompt-guide/): các thành phần cần cân nhắc khi mô tả cảnh.
- [Adobe — Pan shot](https://www.adobe.com/uk/creativecloud/video/production/cinematography/camera-shots-and-angles/pan-shot.html): định nghĩa lia ngang và ví dụ hé lộ bằng lia.
- [Adobe — 6 Tips for Still Photographers Learning to Shoot Video](https://blog.adobe.com/en/publish/2018/02/26/6-tips-still-photographers-learning-shoot-video): chuyển động máy cần có lý do; học quan sát chuyển động trong khung.

Ngày truy cập đối chiếu: 17/10/2026. Không có video được tạo hoặc đánh giá bằng mô hình trong đợt biên soạn này.
