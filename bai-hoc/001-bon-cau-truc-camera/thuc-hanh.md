# Thực hành — chọn máy theo ý đồ và kiểm tra video AI

**Phần bổ sung tự biên soạn.** Các câu lệnh dưới chưa được chạy thử trong đợt này. Thời lượng là mục tiêu cho bài tập; chọn thời lượng được công cụ của bạn hỗ trợ và điều chỉnh nhịp tương ứng. Không có khẳng định về tỷ lệ thành công hay khả năng thực thi chính xác của Veo, Seedance hoặc mô hình khác.

[Bài chính](README.md) · [Đọc ảnh nguồn](doc-anh.md)

## 1. Chuẩn bị một cảnh chung

Dùng cùng một ảnh nhân vật đã duyệt và cùng bối cảnh: cô gái ngồi trên ghế đẩu dưới hiên nhà, cầm một nan tre ngang trước người, quan sát mép nan. Ánh sáng tự nhiên mềm. Bàn tre ở bên cạnh; sân và mái hiên tạo các lớp không gian.

**Mục tiêu:** khi thử đường máy, hạn chế thay cả hành động, bối cảnh và ánh sáng cùng lúc. Nếu những yếu tố đó cùng đổi, khó biết chuyển động máy đóng góp gì vào kết quả.

Nếu chỉ có ảnh chính diện chặt, chuẩn bị thêm góc ba phần tư và ảnh toàn bối cảnh trước bài đi vòng hoặc lùi máy. Các vùng chưa thấy trong tham chiếu có thể bị AI suy diễn.

Không dùng video đã có đường máy khác làm nguồn chuyển động cho bài thử đầu tiên, vì sẽ khó phân biệt tác động của nguồn chuyển động với tác động của câu lệnh.

## 2. Cảnh máy cố định làm mốc đối chiếu

Đây là lựa chọn bổ sung, không phải một trong bốn mục của nguồn.

```text
Tạo một cảnh liên tục dài năm giây, không cắt cảnh.

Dùng ảnh tham chiếu nhân vật cho gương mặt, kiểu tóc, trang phục và tỷ lệ cơ thể. Dùng ảnh bối cảnh cho sân, mái hiên, ghế đẩu, bàn và vị trí đồ vật.

Cô gái ngồi yên trên ghế đẩu, cầm một nan tre ngang trước ngực và quan sát mép nan với vẻ tập trung nhẹ. Chuyển động tự nhiên rất nhỏ ở mắt và bàn tay.

Trung cảnh, máy ngang tầm mắt nhân vật khi ngồi. Máy cố định hoàn toàn trong suốt cảnh. Nan tre và hai bàn tay vẫn nằm trong khung. Ánh sáng tự nhiên mềm giữ nguyên.

Chỉ có một cô gái. Giữ nguyên gương mặt, trang phục, cấu trúc nan tre và vị trí đồ vật.
```

**Điều cần quan sát:** chỉ với hành động trong khung, trạng thái tập trung có đọc được không? Nếu có, điều đó giúp bạn tránh đồng nhất máy đứng yên với cảnh thiếu cảm xúc.

## 3. Bốn phiên bản đường máy và cách vận hành

### A. Tiến máy — tập trung vào khoảnh khắc quan sát

```text
Tạo một cảnh liên tục dài năm giây, không cắt cảnh.

Dùng ảnh tham chiếu nhân vật cho gương mặt, kiểu tóc, trang phục và tỷ lệ cơ thể. Dùng ảnh bối cảnh cho sân, mái hiên, ghế đẩu, bàn và vị trí đồ vật.

Cô gái ngồi trên ghế đẩu, cầm một nan tre ngang trước ngực và quan sát mép nan. Giữ biểu cảm tập trung nhẹ; chuyển động tay rất nhỏ.

Bắt đầu bằng trung cảnh ngang tầm mắt nhân vật khi ngồi. Máy từ từ tiến thẳng về phía cô gái, kết thúc ở khung gần hơn để đọc rõ ánh mắt. Nan tre và hai bàn tay vẫn nằm ở phần dưới khung. Nhân vật không tiến về máy.

Chuyển động tiến máy êm và liên tục. Giữ tiêu cự ổn định, không phóng tiêu cự. Giữ nguyên hướng sáng, gương mặt, tóc, trang phục và bố trí sân. Chỉ có một cô gái.
```

**Tiêu chí đạt:** khung chặt hơn; không biến thành một cảnh chân dung mới; tay và vật thể vẫn có cấu trúc hợp lý.

### B. Đi vòng — làm rõ các lớp không gian

```text
Tạo một cảnh liên tục dài năm giây, không cắt cảnh.

Dùng cùng ảnh tham chiếu nhân vật và toàn cảnh sân. Cô gái ngồi trên ghế đẩu, cầm một nan tre ngang trước ngực và quan sát mép nan. Cơ thể cô giữ cùng hướng trong suốt cảnh.

Bắt đầu ở góc nhìn chính diện, khung đủ thấy người đang ngồi, ghế và một phần bàn cạnh cô. Máy đi êm theo một cung ngắn quanh cô gái, từ phía trước sang phía bên phải của cô, kết thúc ở góc hơi chếch phải. Cung mong muốn là ba mươi độ; giữ khoảng cách máy tới cô gái và độ cao gần như ổn định.

Máy luôn hướng vào cô gái. Các lớp bàn, hiên và sân thay đổi tương quan theo vị trí máy. Cô gái không tự xoay theo máy.

Giữ nguyên gương mặt, trang phục, hướng sáng, cấu trúc ghế và vị trí đồ vật. Chỉ có một cô gái. Không phóng tiêu cự, không đổi địa điểm.
```

**Tiêu chí đạt:** góc nhìn thay đổi; nhân vật không tự quay; lớp gần–xa không méo hoặc trượt bất hợp lý. Ba mươi độ là ý đồ để đánh giá, không phải con số bảo đảm được thực hiện.

### C. Lùi máy để hé lộ — từ người tới nơi chốn

```text
Tạo một cảnh liên tục dài năm giây, không cắt cảnh.

Dùng ảnh nhân vật và ảnh toàn cảnh cùng sân nhà để khóa mặt, trang phục, ghế, bàn, hiên và các rổ tre đã có trong ảnh bối cảnh.

Cô gái ngồi trên ghế đẩu, cầm một nan tre ngang trước ngực và quan sát mép nan. Hành động nhỏ, tự nhiên.

Bắt đầu ở trung cảnh ngang tầm mắt cô gái khi ngồi. Máy từ từ lùi thẳng ra sau, kết thúc ở toàn cảnh thấy cô gái dưới hiên, chiếc bàn cạnh cô và các rổ tre đã đặt sẵn trong sân. Mục tiêu là cho người xem nhận ra không gian làm việc xung quanh cô.

Giữ tiêu cự ổn định, không dùng phóng tiêu cự để thay cho lùi máy. Tất cả vật thể thuộc cùng một sân nhà; không thêm công trình hoặc đồ vật ngoài ảnh bối cảnh. Giữ nguyên ánh sáng và vị trí nhân vật. Chỉ có một cô gái.
```

**Tiêu chí đạt:** cuối cảnh có thông tin mới đã được chuẩn bị trong bối cảnh; không gian không tự biến hình. Nếu không có ảnh toàn, hãy ghi nhận phần môi trường do AI suy diễn khi chấm.

### D. Máy cầm tay nhẹ — thử cảm giác gần gũi

```text
Tạo một cảnh liên tục dài năm giây, không cắt cảnh.

Dùng cùng ảnh tham chiếu nhân vật và sân nhà. Cô gái ngồi trên ghế đẩu, cầm một nan tre ngang trước ngực và quan sát mép nan với biểu cảm tập trung nhẹ.

Trung cảnh ngang tầm mắt cô gái khi ngồi. Máy giữ gần cùng vị trí nhưng có dao động cầm tay rất nhỏ, chậm, tự nhiên. Khung hình luôn dễ đọc; đường chân trời tương đối ổn định. Không đi vòng hoặc tiến gần có chủ ý.

Luôn nhìn rõ mắt, hai bàn tay và nan tre. Giữ nguyên gương mặt, tóc, trang phục, hướng sáng và vị trí đồ vật. Chỉ có một cô gái. Không giật máy, không tạo rung bằng cách làm méo người hoặc bối cảnh.
```

**Tiêu chí đạt:** cảm giác cầm tay đến từ dao động của máy; không làm mất chi tiết thao tác. So với bản cố định, tự đánh giá cách nào hợp giọng điệu phim hơn.

## 4. Cách thử đối chiếu

1. Chọn một công cụ và một phiên bản mô hình cụ thể; ghi lại tên hiển thị.
2. Giữ cùng ảnh tham chiếu, tỷ lệ khung, thời lượng và các thiết lập có thể giữ chung. Nếu công cụ cho chọn hạt giống ngẫu nhiên, ghi lại để thuận tiện đối chiếu.
3. Tạo bản cố định và các bản cần thử theo ngân sách bạn chọn. Không cần dùng đủ bốn bản cho mọi dự án.
4. Xem cả video ở tốc độ bình thường, sau đó so khung đầu–giữa–cuối để tìm lỗi bố cục và nhân vật. Ba khung không thay thế việc xem toàn chuyển động.
5. Ghi phần AI làm đúng, làm sai và cách sửa; mỗi lượt chỉ thay một nhóm yêu cầu chính.

Không đánh giá chỉ bằng khung hình đẹp nhất. Một video có một khung đẹp nhưng sai thao tác hoặc biến nhân vật vẫn có thể không dùng được.

### Phiếu ghi kết quả

| Phiên bản | Đường máy đúng? | Mặt và trang phục nhất quán? | Hành động đọc rõ? | Không gian hợp lý? | Hợp cảm xúc? | Quyết định |
| --- | --- | --- | --- | --- | --- | --- |
| Cố định | Chưa thử | Chưa thử | Chưa thử | Chưa thử | Chưa thử | Chưa có dữ liệu |
| Tiến máy | Chưa thử | Chưa thử | Chưa thử | Chưa thử | Chưa thử | Chưa có dữ liệu |
| Đi vòng | Chưa thử | Chưa thử | Chưa thử | Chưa thử | Chưa thử | Chưa có dữ liệu |
| Lùi hé lộ | Chưa thử | Chưa thử | Chưa thử | Chưa thử | Chưa thử | Chưa có dữ liệu |
| Cầm tay | Chưa thử | Chưa thử | Chưa thử | Chưa thử | Chưa thử | Chưa có dữ liệu |

Có thể ghi đạt / cần sửa / không dùng, kèm mốc giây cụ thể. Một lỗi làm mất tính liên tục của nhân vật hoặc sai hành động chính cần được xử lý trước khi chọn bản chỉ vì đường máy đẹp.

## 5. Ví dụ dựng ba mươi giây cho cảnh làm tre

**Đề xuất biên soạn, không phải diễn biến có sẵn trong ảnh nguồn.** Đây là bảng dựng năm cảnh nối bằng cắt cảnh. Có thể tạo từng cảnh riêng, rồi lấy phần phù hợp để ghép theo nhịp dựng. Mốc sáu giây là phân bổ thành phẩm tham khảo, không khẳng định mọi công cụ tạo được đúng sáu giây.

| Mã cảnh | Thời gian thành phẩm | Nội dung và chức năng | Lựa chọn máy | Nhãn máy quay |
| --- | --- | --- | --- | --- |
| B001-S01 | 00–06 giây | Từ cô gái mở ra hiên và sân, giới thiệu nơi làm việc | Lùi máy nhẹ để hé lộ | MS→WS — trung→toàn; eye-level — ngang mắt; dolly-out — lùi máy |
| B001-S02 | 06–12 giây | Nhìn rõ tay và dụng cụ xử lý nan tre | Máy cố định, ưu tiên thao tác | CU — cận; slight high angle — hơi cao; static — cố định |
| B001-S03 | 12–18 giây | Cô kiểm tra mép nan; đọc sự tập trung | Tiến máy rất nhẹ | MS→MCU — trung→trung cận; eye-level — ngang mắt; push-in — tiến máy |
| B001-S04 | 18–24 giây | Nan tre hoặc sản phẩm hoàn thành đặt lên bàn; dành thời gian đọc kết quả | Máy cố định | CU — cận; eye-level/slight high — ngang/hơi cao; static — cố định |
| B001-S05 | 24–30 giây | Cô ngồi cạnh thành phẩm trong không gian sân; kết thúc bình thản | Một cung ngắn nếu bổ sung thông tin; nếu gây phô diễn thì giữ cố định | WS — toàn; seated eye-level — ngang mắt khi ngồi; short orbit/static — cung ngắn/cố định |

Giữ vị trí bàn, ghế, hướng sáng, trang phục và trạng thái sản phẩm liên tục qua các cảnh. Bảng này chủ động không dùng cầm tay vì giọng điệu đang hướng tới yên tĩnh. Việc đã học một kỹ thuật không buộc phải đưa kỹ thuật đó vào phim.

## 6. Bài tập để tự kiểm tra kiến thức

1. **Phân biệt kỹ thuật:** một cảnh làm mặt nhân vật lớn lên có chắc là tiến máy không? Nêu thêm một khả năng và dấu hiệu cần kiểm tra.
2. **Viết ý đồ:** với một cảnh hé lộ, viết riêng “khung đầu biết gì” và “khung cuối biết thêm gì”.
3. **Sửa yêu cầu mâu thuẫn:** sửa câu “máy cố định hoàn toàn nhưng đi vòng ba mươi độ” thành hai phương án quay riêng.
4. **Giải thích lựa chọn:** chọn cảnh cố định hoặc tiến máy cho thao tác vót tre; giải thích bằng thông tin khán giả cần đọc.
5. **Kiểm tra nguồn:** chỉ ra vì sao hai ảnh tĩnh không đủ chứng minh một đường máy hoặc cường độ rung.

### Gợi ý đáp án

1. Có thể là phóng tiêu cự, cắt khung hoặc nhân vật tự tiến gần. Cần xem vị trí điểm nhìn, quan hệ các lớp cảnh và toàn diễn biến.
2. Ví dụ: đầu thấy người cầm nan; cuối biết người ngồi dưới hiên cạnh các rổ đã hoàn thành. Thông tin mới phải thật sự xuất hiện và đọc được.
3. Phương án một giữ vị trí và hướng nhìn cố định; phương án hai cho máy đi theo cung, giữ khoảng cách tương đối ổn định. Không dùng hai yêu cầu đối lập cùng lúc.
4. Nếu cần theo dõi đường dụng cụ và nan tre, cảnh cố định rõ thao tác là lựa chọn hợp lý; nếu cần đọc phản ứng sau khi kiểm tra, có thể thử tiến nhẹ. Không có một đáp án đúng cho mọi cảnh.
5. Ảnh không thể hiện toàn chuyển động theo thời gian; nhòe hoặc mũi tên chỉ là dấu hiệu/minh họa. Phải có video hoặc dữ liệu đường máy để kiểm chứng.

## 7. Mẫu mô tả một cảnh để dùng lại

```text
Mục tiêu cảnh: Khán giả cần nhận ra/cảm thấy điều gì?
Thời lượng thành phẩm: ...
Nguồn tham chiếu: Mặt và trang phục từ đâu? Bối cảnh từ đâu?
Khung đầu: Cỡ cảnh, góc nhìn, chủ thể, đồ vật nào trong khung?
Hành động chính: Một hành động cần thấy rõ.
Máy quay: Vị trí đầu, đường đi hoặc cách giữ máy, tốc độ tương đối.
Khung cuối: Chủ thể nằm đâu? Thông tin nào mới xuất hiện?
Tính liên tục: Những yếu tố nào cần giữ nguyên?
Điều cần chấm sau khi tạo: Dấu hiệu đạt và lỗi khiến cảnh không dùng được.
```

Mẫu này là công cụ lập kế hoạch, không phải danh sách bắt buộc nhét đủ vào mọi câu lệnh. Khi đã có ảnh tham chiếu rõ, ưu tiên mô tả điều cần chuyển động và điều cần giữ ổn định; tránh lặp dài những phần hình đã xác định.
