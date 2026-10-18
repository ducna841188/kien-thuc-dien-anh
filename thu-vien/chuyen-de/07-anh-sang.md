# LI — Ánh sáng

Phiên bản 1.3.1. Thiết kế nguồn, hướng, chất lượng và độ tương phản có thể đối chiếu.

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
| [LI-007](#li-007) | Phơi sáng: chọn biến theo điều cần bảo vệ | co_ban |
| [LI-008](#li-008) | Khoảng cách nguồn: độ suy giảm và vùng sáng ổn định | trung_cap |

<a id="li-001"></a>
## LI-001 — Nguồn sáng và động cơ chiếu sáng

**Phiên bản mục:** 1.0.0

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

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Muốn biên bóng và chuyển vùng sáng như thế nào?

**Dùng khi:** Khi cần thấy chất liệu, khuôn mặt hoặc không khí.

**Nguyên lý thực hành:** Chất lượng bóng liên quan kích thước góc của nguồn tại chủ thể. Mô tả biên bóng nhìn thấy và quan hệ sáng thay vì chỉ nói cinematic. Cùng kích thước thực, đổi khoảng cách có thể đổi độ mềm và độ suy giảm; nếu tăng kích thước để bù thì đó là một tổ hợp khác.

**Cách làm:**

1. Chọn biên bóng rõ hay chuyển êm.
2. Xét độ lớn nguồn so với khoảng cách tới chủ thể.
3. Giữ chi tiết cần đọc ở phía bóng bằng bố trí hoặc bù sáng khi cần.
4. Kiểm bóng ở vật/ mặt quan trọng, ghi hướng và độ chuyển mép bóng; so tại vị trí hành động thật, không chỉ khung đầu.

**Đánh đổi:** Mềm có thể giảm nổi khối/bề mặt; cứng có thể làm tương phản khó giữ.

**Kiểm tra:**

- Biên bóng đúng ý đồ, không đổi thất thường trong cùng shot.
- Không suy mọi cảnh ngoài trời đều sáng mềm.
- Không dùng mềm/cứng thay cho sáng/tối hoặc tương phản cao/thấp.

**Ví dụ tự biên soạn:** Nguồn bên có biên bóng rõ làm vết trên vật liệu nổi hơn; cửa lớn có thể cho chuyển sáng êm.

**Phản ví dụ / giới hạn:** Ánh cứng vẫn có thể yên bình nếu mức tương phản, bố cục và hoàn cảnh phù hợp.

**Liên quan:** [LI-003](../kien-thuc/LI-003.json), [CO-004](../kien-thuc/CO-004.json), [CA-007](../kien-thuc/CA-007.json), [LI-008](../kien-thuc/LI-008.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Độ mềm gắn kích thước biểu kiến nguồn, không đơn giản là đèn yếu hoặc trời ấm.

**Tình huống:** Nguồn xa hơn giúp đều qua đường đi nhưng bóng cứng hơn.

**Phần phải giữ:** Mục tiêu và các phần đã duyệt trong tình huống.

| Phương án | Thực hiện |
| --- | --- |
| A | Hạ công suất để gọi ánh sáng mềm. |
| B | So kích thước biểu kiến hoặc bố trí nguồn/bounce, đồng thời kiểm công suất và độ đều. |

**Cách chọn:** Chọn B nếu cần đổi mép bóng; công suất riêng không xác định độ mềm.

**Dấu hiệu kiểm trong ca:**

- Không dùng mềm/cứng thay cho sáng/tối hoặc tương phản cao/thấp.

**Nếu gặp:** Hình tối đi nhưng bóng vẫn gắt.

Có thể do: Đổi độ sáng thay vì kích thước biểu kiến.

Thử tiếp: Giữ mức sáng tương đương, thử thay kích thước/vị trí nguồn và so bóng.
**Nguồn đối chiếu:** [B008](../../bai-hoc/008-muoi-cu-phap-veo/README.md), [B011](../../bai-hoc/011-anh-sang-bo-nen-nhip-cham/README.md), [SRC-YALE-STAGING](https://filmanalysis.yale.edu/mise-en-scene/), [SRC-ILT-LIGHT](https://homepages.inf.ed.ac.uk/rbf/CVonline/LOCAL_COPIES/RYER/ch06.html)

[Bản JSON chuẩn](../kien-thuc/LI-002.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="li-003"></a>
## LI-003 — Tương phản, bù sáng và vùng tối

**Phiên bản mục:** 1.3.0

**Câu hỏi quyết định:** Phần tối cần giấu hay cần đọc tới mức nào?

**Dùng khi:** Khi cân bằng độ rõ và không khí.

**Nguyên lý thực hành:** Tách mức sáng tổng thể khỏi chênh sáng–tối. Bù sáng nâng vùng tối; chặn ánh phản xạ có thể giữ vùng tối sâu hơn. Không gán tỷ lệ số khi chưa đo. Tách độ mềm của bóng khỏi chênh sáng hai phía. Fill/bounce có thể nâng phía tối, negative fill giảm hắt; cần giữ lý do nguồn và thông tin chính.

**Cách làm:**

1. Chọn chi tiết phải giữ ở vùng sáng và tối.
2. Điều chỉnh hướng/độ bù hoặc nền thay vì chỉ tăng mọi độ sáng.
3. Kiểm chuỗi hình và thiết bị hiển thị đích.
4. So một thay đổi tại vị trí chủ thể: thêm bề mặt hắt, bớt hắt hoặc đổi hướng nguồn; kiểm ảnh hưởng nền, phản chiếu và chuyển động.
5. Nếu dùng tỷ lệ tương phản, ghi đang so nguồn key với fill, hai phía chủ thể hay mức tín hiệu ảnh; ghi cách đo. Không coi các tỷ lệ ấy là cùng phép đo hoặc suy số lux từ hình đã grade.
6. Kiểm độ tương phản ở các vị trí hành động then chốt và sau đổi góc; một tay đi vào bóng có thể làm mất đúng bằng chứng dù ảnh đầu vẫn đẹp.

**Đánh đổi:** Tương phản thấp có thể thiếu tách lớp; tương phản cao có thể che hành động.

**Kiểm tra:**

- Nhìn được bằng chứng quan trọng mà vẫn giữ không khí.
- Không coi high-key là chỉ phơi sáng quá hoặc low-key là chỉ ảnh thiếu sáng.
- Thao tác sửa độ nổi không phá quan hệ sáng có chủ đích trong cảnh.
- Tỷ lệ ghi số có định nghĩa và cách đo; thiếu thì mô tả quan hệ thay vì bịa số.

**Ví dụ tự biên soạn:** Mặt được đọc rõ trong phòng tối mà cửa sổ vẫn là hướng sáng chính.

**Phản ví dụ / giới hạn:** Một hình sáng rực vẫn có thể có bóng đen sâu; sáng tổng thể và tương phản là hai trục.

**Liên quan:** [LI-004](../kien-thuc/LI-004.json), [CO-003](../kien-thuc/CO-003.json), [QC-001](../kien-thuc/QC-001.json), [LI-006](../kien-thuc/LI-006.json), [LI-008](../kien-thuc/LI-008.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Tương phản không bắt buộc giải bằng sơ đồ ba đèn; môi trường hắt và che sáng có vai trò lớn.

**Tình huống:** Một vật sáng hòa vào nền sáng dù ánh rất mềm.

**Phần phải giữ:** Mục tiêu và các phần đã duyệt trong tình huống.

| Phương án | Thực hiện |
| --- | --- |
| A | Thêm rim light mạnh vào mọi cảnh. |
| B | So đổi nền/độ hắt/hướng sáng theo nguồn hợp lý trước. |

**Cách chọn:** Chọn theo khả năng đọc vật và phong cách; không bắt một sơ đồ đèn chung.

**Dấu hiệu kiểm trong ca:**

- Thao tác sửa độ nổi không phá quan hệ sáng có chủ đích trong cảnh.

**Nếu gặp:** Có chiều sâu nhưng vật như ghép vào nền.

Có thể do: Độ tách hoặc viền sáng trái nguồn đã thiết lập.

Thử tiếp: So phương án giảm cạnh tranh nền với phương án tăng sáng chủ thể; giữ vật liệu nhất quán.
**Nguồn đối chiếu:** [B008](../../bai-hoc/008-muoi-cu-phap-veo/README.md), [SRC-YALE-STAGING](https://filmanalysis.yale.edu/mise-en-scene/)

[Bản JSON chuẩn](../kien-thuc/LI-003.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="li-004"></a>
## LI-004 — Phơi sáng và giữ thông tin hình

**Phiên bản mục:** 1.0.0

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

**Phiên bản mục:** 1.0.0

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

**Phiên bản mục:** 1.0.0

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

<a id="li-007"></a>
## LI-007 — Phơi sáng: chọn biến theo điều cần bảo vệ

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Cần thay độ sáng bằng cách nào mà vẫn giữ vùng nét và chuyển động mong muốn?

**Dùng khi:** Quay thật, làm tiền kỳ hoặc sửa clip AI tối/sáng nhưng chưa biết nguyên nhân.

**Nguyên lý thực hành:** Khẩu độ và thời gian phơi ảnh hưởng lượng sáng ghi nhận đồng thời ảnh hưởng vùng nét/nhòe. ISO là điều khiển theo hệ thống máy, không tự tăng photon; cách máy xử lý nhiễu và vùng sáng cần kiểm theo cấu hình. Không đánh đổi mù thông tin quan trọng chỉ để hình sáng hơn.

**Cách làm:**

1. Chọn phần phải giữ: nhòe chuyển động, vùng rõ, chi tiết vùng sáng/tối. Với quay thật, ưu tiên điều chỉnh nguồn/ND/khẩu hoặc thời gian theo đúng ràng buộc.
2. Kiểm cảnh ở điều kiện thực và công cụ đo phù hợp; ghi rõ phần bị cắt dữ liệu khác với phần chỉ hiển thị tối. Với AI xuất sẵn, không giả định có RAW/Log để cứu.
3. Nếu sửa bằng hậu kỳ, so nhiễu, dải chuyển và màu sau chỉnh; mất chi tiết do clipping không tự được phục hồi chính xác bằng tăng sáng hay AI.

**Đánh đổi:** Thêm sáng thay đổi cảm giác nguồn; mở khẩu giảm dung sai nét; đổi thời gian phơi đổi nhòe; nâng tín hiệu có thể lộ nhiễu.

**Kiểm tra:**

- Bằng chứng chính vẫn đọc được và vùng cần giữ không mất ngoài ý đồ.
- Thay độ sáng không vô tình đổi trải nghiệm chuyển động hoặc độ rõ quan trọng.

**Ví dụ tự biên soạn:** Cần tay và vật cùng rõ khi quay: thay vì mở hết khẩu, thử bổ sung/bố trí lại sáng và kiểm vùng phản chiếu.

**Phản ví dụ / giới hạn:** Vùng tối có thể là chủ ý; không ép mọi cảnh về cùng độ sáng hoặc cùng một mức da bất kể bối cảnh.

**Liên quan:** [LI-004](../kien-thuc/LI-004.json), [CA-012](../kien-thuc/CA-012.json), [MO-007](../kien-thuc/MO-007.json), [CO-006](../kien-thuc/CO-006.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Các điều khiển dùng chung ngân sách hình ảnh: thay một biến có thể giải độ sáng nhưng làm hỏng nét hoặc chuyển động. Lựa chọn cần bắt đầu từ thông tin phải giữ.

**Tình huống:** Cần tay và vật cùng rõ khi quay: thay vì mở hết khẩu, thử bổ sung/bố trí lại sáng và kiểm vùng phản chiếu.

**Phần phải giữ:** Tay và vật đủ rõ. Thông tin phản chiếu quan trọng không mất.

| Phương án | Thực hiện |
| --- | --- |
| A | Mở khẩu tối đa dù thao tác đi qua nhiều khoảng cách. |
| B | Giữ vùng rõ cần thiết rồi điều chỉnh ánh sáng/ND theo môi trường và máy thực tế. |

**Cách chọn:** Chọn B khi vùng nét là ràng buộc; không có biến phơi sáng tối ưu cho mọi cảnh.

**Dấu hiệu kiểm trong ca:**

- Bằng chứng chính vẫn đọc được và vùng cần giữ không mất ngoài ý đồ.
- Thay độ sáng không vô tình đổi trải nghiệm chuyển động hoặc độ rõ quan trọng.

**Nếu gặp:** Hình đủ sáng nhưng mất chi tiết thao tác hoặc nhòe khác ý đồ.

Có thể do: Biến phơi sáng được chọn sai ưu tiên. Clip đầu vào đã mất dữ liệu.

Thử tiếp: So trước/sau tại vùng thông tin chính; nếu dữ liệu đã mất, đánh giá sửa cục bộ hay tạo/quay lại thay vì hứa khôi phục thật.

**Phát biểu được đối chiếu:** ISO là một điều khiển gain trong hệ thống máy số; khẩu và thời gian phơi liên quan lượng sáng tới cảm biến. Nguồn: [SRC-NIKON-ISO](https://www.nikonusa.com/learn-and-explore/c/products-and-innovation/iso-control).

**Giới hạn nguồn:** Tăng ISO không tự thêm photon vào cảm biến hoặc xác nhận có thể cứu phần dữ liệu đã cắt.
**Nguồn đối chiếu:** [SRC-RED-SHUTTER](https://www.reddigitalcinema.com/red-101/shutter-angle-tutorial), [SRC-NIKON-APERTURE](https://www.nikonusa.com/learn-and-explore/c/tips-and-techniques/understanding-maximum-aperture), [SRC-NIKON-ISO](https://www.nikonusa.com/learn-and-explore/c/products-and-innovation/iso-control)

[Bản JSON chuẩn](../kien-thuc/LI-007.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="li-008"></a>
## LI-008 — Khoảng cách nguồn: độ suy giảm và vùng sáng ổn định

**Phiên bản mục:** 1.1.0

**Câu hỏi quyết định:** Nguồn nên ở đâu để người/vật đi qua cảnh vẫn giữ quan hệ sáng phù hợp?

**Dùng khi:** Dàn cảnh có chuyển động, ánh sáng quá tụt theo bước chân hoặc nền cần tối hơn.

**Nguyên lý thực hành:** Với nguồn gần đúng nguồn điểm và điều kiện phù hợp, độ rọi giảm theo bình phương khoảng cách. Nguồn lớn ở gần, phản xạ phòng và chùm sáng có thể lệch mô hình đơn giản; dùng quy luật để dự đoán rồi đo/xem thử. Khoảng cách nguồn cũng thay đổi kích thước biểu kiến và chất bóng.

**Cách làm:**

1. Vẽ vị trí nguồn, chủ thể và vùng hành động; kiểm tại các mốc gần/xa quan trọng thay vì chỉ một vị trí đẹp.
2. Muốn tương đối đều qua đường đi, so nguồn xa hơn hoặc nguồn phủ phù hợp; muốn tách sáng chủ thể/nền, so bố trí có độ chênh khoảng cách lớn. Bù công suất và kích thước nguồn khi cần.
3. Với ảnh/video AI, mô tả dấu kết quả sáng nhất quán theo vị trí và kiểm lại; đừng hứa model tuân đúng công thức lux.

**Đánh đổi:** Đẩy nguồn ra xa có thể cần thêm công suất và làm bóng cứng hơn nếu không tăng kích thước; đưa gần có thể tăng chênh sáng ngoài ý đồ.

**Kiểm tra:**

- Sáng không nhảy vô cớ khi chủ thể đi qua vùng liên tục.
- Mô tả mềm/cứng xét kích thước biểu kiến, không chỉ khoảng cách đơn lẻ.

**Ví dụ tự biên soạn:** Người đi cạnh một đèn bàn: có thể chủ ý sáng tăng khi gần đèn; với cảnh cần mặt ổn định, thử bố trí nguồn phủ khác thay vì kéo sáng từng frame.

**Phản ví dụ / giới hạn:** Không dùng 1/r² như phép đo chính xác cho mọi softbox sát chủ thể hoặc trời sáng rộng; các điều kiện xấp xỉ phải phù hợp.

**Liên quan:** [LI-001](../kien-thuc/LI-001.json), [LI-002](../kien-thuc/LI-002.json), [LI-005](../kien-thuc/LI-005.json), [MO-008](../kien-thuc/MO-008.json)


### Áp dụng và chẩn đoán

**Cơ chế/quan hệ cần xét:** Khoảng cách là biến thiết kế cả độ sáng lẫn chất lượng hình. Quy tắc nguồn điểm là mô hình giới hạn; phản xạ và kích thước thực làm kết quả tại trường quay cần kiểm riêng.

**Tình huống:** Người đi cạnh một đèn bàn: có thể chủ ý sáng tăng khi gần đèn; với cảnh cần mặt ổn định, thử bố trí nguồn phủ khác thay vì kéo sáng từng frame.

**Phần phải giữ:** Đường đi đã duyệt. Nguồn sáng có lý do và chênh sáng có chủ đích.

| Phương án | Thực hiện |
| --- | --- |
| A | Đặt nguồn rất gần cho đẹp ở mốc đầu rồi khóa phơi sáng và bỏ kiểm cuối đường. |
| B | Kiểm các mốc đường đi, chọn nguồn và mức chênh sáng phù hợp toàn hành động. |

**Cách chọn:** Chọn B nếu hành động cần liên tục; A chỉ chấp nhận khi chênh sáng đó có lý do và phục vụ cảnh.

**Dấu hiệu kiểm trong ca:**

- Sáng không nhảy vô cớ khi chủ thể đi qua vùng liên tục.
- Mô tả mềm/cứng xét kích thước biểu kiến, không chỉ khoảng cách đơn lẻ.

**Nếu gặp:** Mặt sáng tối rất mạnh dù người chỉ dịch nhẹ.

Có thể do: Nguồn gần so với độ dài đường đi. Bị che nguồn hoặc đổi hướng mặt.

Thử tiếp: Giữ đường người, thử vị trí nguồn khác và kiểm cả bóng, nền, công suất; không chỉ so độ sáng trung bình.

**Phát biểu được đối chiếu:** Quy luật bình phương khoảng cách cần điều kiện gần đúng nguồn điểm. Nguồn: [SRC-ILT-LIGHT](https://homepages.inf.ed.ac.uk/rbf/CVonline/LOCAL_COPIES/RYER/ch06.html).

**Giới hạn nguồn:** Không áp chính xác cho mọi nguồn lớn ở gần, phòng nhiều phản xạ hoặc mọi hình do AI sinh.
**Nguồn đối chiếu:** [SRC-ILT-LIGHT](https://homepages.inf.ed.ac.uk/rbf/CVonline/LOCAL_COPIES/RYER/ch06.html)

[Bản JSON chuẩn](../kien-thuc/LI-008.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).
