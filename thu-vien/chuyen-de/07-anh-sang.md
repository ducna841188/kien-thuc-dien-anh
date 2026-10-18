# LI — Ánh sáng

Phiên bản 1.0.0. Thiết kế nguồn, hướng, chất lượng và độ tương phản có thể đối chiếu.

[Mục lục](../README.md) · [Chuẩn ra quyết định](../03_RA_QUYET_DINH.md)

Mỗi mục dưới là hướng dẫn có điều kiện. Tác dụng cảm xúc là giả thuyết thiết kế; chưa có thử tạo video hoặc kiểm nghiệm khán giả cho các ví dụ mới. Thuật ngữ xem [từ điển](../TU_DIEN.md).

| Mã | Quyết định | Mức |
| --- | --- | --- |
| [LI-001](#li-001) | Nguồn sáng và động cơ chiếu sáng | co_ban |
| [LI-002](#li-002) | Độ mềm/cứng và kích thước nguồn nhìn từ chủ thể | trung_cap |
| [LI-003](#li-003) | Tương phản, bù sáng và vùng tối | trung_cap |
| [LI-004](#li-004) | Phơi sáng và giữ thông tin hình | trung_cap |
| [LI-005](#li-005) | Liên tục ánh sáng và thời gian trong cảnh | nang_cao |
| [LI-006](#li-006) | Bề mặt, phản chiếu và tách chủ thể | nang_cao |

<a id="li-001"></a>
## LI-001 — Nguồn sáng và động cơ chiếu sáng

**Câu hỏi quyết định:** Ánh sáng trong cảnh có thể đến từ đâu?

**Dùng khi:** Khi thiết kế ảnh, quay hoặc nối nhiều góc.

**Nguyên lý thực hành:** Bắt đầu bằng nguồn, hướng và vai trò của ánh sáng. Nguồn nhìn thấy trong cảnh và đèn dùng để mô phỏng nó không phải lúc nào là cùng một vật.

**Cách làm:**

1. Ghi cửa sổ, trời, đèn hoặc lửa làm cơ sở.
2. Chọn phía sáng chính và các vật nhận sáng.
3. Giữ hướng bóng/phản chiếu phù hợp khi đổi góc.

**Đánh đổi:** Bám tự nhiên quá cứng có thể làm thông tin khó thấy; có thể tăng/định hình ánh sáng theo ý đồ.

**Kiểm tra:**

- Hướng sáng không tự đảo giữa hai góc cùng thời điểm.
- Vùng sáng mới có nguồn hoặc chủ ý cách điệu được ghi.

**Ví dụ tự biên soạn:** Ánh cửa sổ chiếu bàn; cận tay vẫn giữ phía sáng tương ứng.

**Phản ví dụ / giới hạn:** Phim cách điệu có thể dùng nguồn phi thực nhưng cần quy tắc nhất quán trong cảnh.

**Liên quan:** [LI-005](../kien-thuc/LI-005.json), [DR-002](../kien-thuc/DR-002.json), [CO-005](../kien-thuc/CO-005.json)

**Nguồn đối chiếu:** [B002](../../bai-hoc/002-prompt-cau-truc/README.md), [B008](../../bai-hoc/008-muoi-cu-phap-veo/README.md), [SRC-ASC-KAUFMAN](https://theasc.com/article/filming-12-angry-men/)

[Bản JSON chuẩn](../kien-thuc/LI-001.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="li-002"></a>
## LI-002 — Độ mềm/cứng và kích thước nguồn nhìn từ chủ thể

**Câu hỏi quyết định:** Muốn biên bóng và chuyển vùng sáng như thế nào?

**Dùng khi:** Khi cần thấy chất liệu, khuôn mặt hoặc không khí.

**Nguyên lý thực hành:** Chất lượng bóng liên quan kích thước góc của nguồn tại chủ thể. Mô tả biên bóng nhìn thấy và quan hệ sáng thay vì chỉ nói cinematic.

**Cách làm:**

1. Chọn biên bóng rõ hay chuyển êm.
2. Xét độ lớn nguồn so với khoảng cách tới chủ thể.
3. Giữ chi tiết cần đọc ở phía bóng bằng bố trí hoặc bù sáng khi cần.

**Đánh đổi:** Mềm có thể giảm nổi khối/bề mặt; cứng có thể làm tương phản khó giữ.

**Kiểm tra:**

- Biên bóng đúng ý đồ, không đổi thất thường trong cùng shot.
- Không suy mọi cảnh ngoài trời đều sáng mềm.

**Ví dụ tự biên soạn:** Nguồn bên có biên bóng rõ làm vết trên vật liệu nổi hơn; cửa lớn có thể cho chuyển sáng êm.

**Phản ví dụ / giới hạn:** Ánh cứng vẫn có thể yên bình nếu mức tương phản, bố cục và hoàn cảnh phù hợp.

**Liên quan:** [LI-003](../kien-thuc/LI-003.json), [CO-004](../kien-thuc/CO-004.json), [CA-007](../kien-thuc/CA-007.json)

**Nguồn đối chiếu:** [B008](../../bai-hoc/008-muoi-cu-phap-veo/README.md), [B011](../../bai-hoc/011-anh-sang-bo-nen-nhip-cham/README.md), [SRC-YALE-STAGING](https://filmanalysis.yale.edu/mise-en-scene/)

[Bản JSON chuẩn](../kien-thuc/LI-002.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="li-003"></a>
## LI-003 — Tương phản, bù sáng và vùng tối

**Câu hỏi quyết định:** Phần tối cần giấu hay cần đọc tới mức nào?

**Dùng khi:** Khi cân bằng độ rõ và không khí.

**Nguyên lý thực hành:** Tách mức sáng tổng thể khỏi chênh sáng–tối. Bù sáng nâng vùng tối; chặn ánh phản xạ có thể giữ vùng tối sâu hơn. Không gán tỷ lệ số khi chưa đo.

**Cách làm:**

1. Chọn chi tiết phải giữ ở vùng sáng và tối.
2. Điều chỉnh hướng/độ bù hoặc nền thay vì chỉ tăng mọi độ sáng.
3. Kiểm chuỗi hình và thiết bị hiển thị đích.

**Đánh đổi:** Tương phản thấp có thể thiếu tách lớp; tương phản cao có thể che hành động.

**Kiểm tra:**

- Nhìn được bằng chứng quan trọng mà vẫn giữ không khí.
- Không coi high-key là chỉ phơi sáng quá hoặc low-key là chỉ ảnh thiếu sáng.

**Ví dụ tự biên soạn:** Mặt được đọc rõ trong phòng tối mà cửa sổ vẫn là hướng sáng chính.

**Phản ví dụ / giới hạn:** Một hình sáng rực vẫn có thể có bóng đen sâu; sáng tổng thể và tương phản là hai trục.

**Liên quan:** [LI-004](../kien-thuc/LI-004.json), [CO-003](../kien-thuc/CO-003.json), [QC-001](../kien-thuc/QC-001.json)

**Nguồn đối chiếu:** [B008](../../bai-hoc/008-muoi-cu-phap-veo/README.md), [SRC-YALE-STAGING](https://filmanalysis.yale.edu/mise-en-scene/)

[Bản JSON chuẩn](../kien-thuc/LI-003.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="li-004"></a>
## LI-004 — Phơi sáng và giữ thông tin hình

**Câu hỏi quyết định:** Chi tiết nào được ưu tiên khi dải sáng vượt khả năng?

**Dùng khi:** Khi hình cháy sáng, tối bệt hoặc làm việc với nhiều nguồn.

**Nguyên lý thực hành:** Xét chủ thể, điểm sáng và thông tin cần giữ. Các thiết lập máy thật tương tác; chữ ghi thông số trong prompt không đảm bảo tệp thực tuân thủ.

**Cách làm:**

1. Chọn vùng cần giữ chi tiết và điểm sáng được phép mất.
2. Dùng biểu đồ/đo hình khi có công cụ thay vì chỉ nhìn một màn hình.
3. Duyệt chuyển sáng theo thời gian, không chỉ ảnh đầu.

**Đánh đổi:** Giữ mọi vùng có thể làm hình phẳng; ưu tiên thẩm mỹ phải đi cùng khả năng đọc.

**Kiểm tra:**

- Mặt, tay, chữ hoặc vật chứng thiết yếu không mất ngoài ý đồ.
- Không dùng hậu kỳ để hứa khôi phục chi tiết đã không có.

**Ví dụ tự biên soạn:** Cửa sổ có thể sáng hơn nhiều, nhưng thao tác trên bàn vẫn phải đọc đủ.

**Phản ví dụ / giới hạn:** Một vùng trắng không chi tiết có thể là cách điệu; phải được chấp nhận trong bản yêu cầu.

**Liên quan:** [CA-007](../kien-thuc/CA-007.json), [CO-006](../kien-thuc/CO-006.json), [AI-007](../kien-thuc/AI-007.json)

**Nguồn đối chiếu:** [B022](../../bai-hoc/022-veo-tu-co-ban-den-quy-trinh/README.md), [SRC-YALE-CAMERA](https://filmanalysis.yale.edu/cinematography/)

[Bản JSON chuẩn](../kien-thuc/LI-004.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="li-005"></a>
## LI-005 — Liên tục ánh sáng và thời gian trong cảnh

**Câu hỏi quyết định:** Các góc có thuộc cùng một thời điểm và không gian không?

**Dùng khi:** Khi tạo nhiều shot hoặc đổi bối cảnh theo ngày/mùa.

**Nguyên lý thực hành:** Ghi sơ đồ hướng sáng, độ mềm, bóng và nguồn thực. Cho phép ánh sáng thay đổi khi câu chuyện/thời tiết/thời gian thay đổi có tín hiệu.

**Cách làm:**

1. Lưu một ảnh chuẩn cùng sơ đồ và trạng thái thời tiết.
2. So vật mốc, phía bóng, phản chiếu và màu qua điểm nối.
3. Nếu chuyển thời gian, chọn cảnh/âm hoặc diễn tiến làm rõ bước đổi.

**Đánh đổi:** Ép mọi shot cùng sáng tuyệt đối có thể làm mất chuyển mùa/giờ có chủ đích.

**Kiểm tra:**

- Thay đổi có lý do và không nhấp nháy vô cớ.
- Góc cận không tạo một mặt trời thứ hai ngược cảnh rộng.

**Ví dụ tự biên soạn:** Cảnh chiều chuyển đêm có tín hiệu ngoài trời rồi nguồn đèn trong nhà nhận vai chính.

**Phản ví dụ / giới hạn:** Cùng vật dưới nắng và trong bóng có màu/độ sáng khác mà vẫn giữ thiết kế.

**Liên quan:** [EV-002](../kien-thuc/EV-002.json), [CO-005](../kien-thuc/CO-005.json), [AI-002](../kien-thuc/AI-002.json)

**Nguồn đối chiếu:** [B002](../../bai-hoc/002-prompt-cau-truc/README.md), [B024](../../bai-hoc/024-xau-chuoi-canh/README.md)

[Bản JSON chuẩn](../kien-thuc/LI-005.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="li-006"></a>
## LI-006 — Bề mặt, phản chiếu và tách chủ thể

**Câu hỏi quyết định:** Muốn vật liệu và hình khối được đọc như thế nào?

**Dùng khi:** Khi vật bóng, trong, ướt hoặc có nền khó tách.

**Nguyên lý thực hành:** Đặt nguồn và góc nhìn theo cách bề mặt phản xạ. Viền sáng là một phương án tách, cùng với chênh sáng, màu, nét và vị trí.

**Cách làm:**

1. Chọn phần bề mặt cần mô tả.
2. Điều chỉnh nguồn/góc/nền để phản chiếu có hình hợp lý.
3. Kiểm viền, chất liệu và vùng trong suốt qua chuyển động.

**Đánh đổi:** Tăng viền có thể tạo quầng giả; giảm phản chiếu quá mức làm mất vật liệu.

**Kiểm tra:**

- Kim loại không tự thành nhựa; nước không thành khối đặc.
- Phản chiếu đổi hợp lý với người, vật và máy.

**Ví dụ tự biên soạn:** Một dải sáng trên bình gốm bóng cho thấy độ cong; nền tối giúp hơi nước đọc được.

**Phản ví dụ / giới hạn:** Không cần viền sáng trên mọi người; nền và hướng sáng tự nhiên có thể đã đủ.

**Liên quan:** [CO-004](../kien-thuc/CO-004.json), [CA-005](../kien-thuc/CA-005.json), [QC-002](../kien-thuc/QC-002.json)

**Nguồn đối chiếu:** [B008](../../bai-hoc/008-muoi-cu-phap-veo/README.md), [B023](../../bai-hoc/023-negative-prompt/README.md)

[Bản JSON chuẩn](../kien-thuc/LI-006.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).
