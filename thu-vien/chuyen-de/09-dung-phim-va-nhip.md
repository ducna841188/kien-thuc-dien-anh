# ED — Dựng phim và điều khiển nhịp

Phiên bản 1.0.0. Chọn điểm cắt, thông tin, thời gian và nhịp căng–thả ở nhiều quy mô.

[Mục lục](../README.md) · [Chuẩn ra quyết định](../03_RA_QUYET_DINH.md)

Mỗi mục dưới là hướng dẫn có điều kiện. Tác dụng cảm xúc là giả thuyết thiết kế; chưa có thử tạo video hoặc kiểm nghiệm khán giả cho các ví dụ mới. Thuật ngữ xem [từ điển](../TU_DIEN.md).

| Mã | Quyết định | Mức |
| --- | --- | --- |
| [ED-001](#ed-001) | Nhịp trong shot, giữa shot và toàn phim | co_ban |
| [ED-002](#ed-002) | Điểm cắt theo hành động, thông tin và phản ứng | trung_cap |
| [ED-003](#ed-003) | Nối hành động, ánh mắt và trạng thái | trung_cap |
| [ED-004](#ed-004) | Nén thời gian, lược việc và giữ nhân quả | trung_cap |
| [ED-005](#ed-005) | Tăng, giữ và thả mong chờ | nang_cao |
| [ED-006](#ed-006) | Montage, dựng song song và liên hệ ý tưởng | nang_cao |
| [ED-007](#ed-007) | Cảnh xen và chuyển cảnh có chức năng | trung_cap |
| [ED-008](#ed-008) | Dựng bản thô, rà trải nghiệm và hoàn thiện | nang_cao |

<a id="ed-001"></a>
## ED-001 — Nhịp trong shot, giữa shot và toàn phim

**Câu hỏi quyết định:** Nhịp đang đến từ yếu tố nào?

**Dùng khi:** Khi video quá chậm, quá dồn hoặc đều đều.

**Nguyên lý thực hành:** Xét chuyển động, diễn xuất, lượng thông tin, âm thanh, thời lượng và quan hệ chuỗi. Không lấy thời lượng trung bình làm định nghĩa duy nhất của nhịp.

**Cách làm:**

1. Đọc một shot với âm và không âm để tách đóng góp.
2. Rà chỗ đổi việc, thông tin và năng lượng trong chuỗi.
3. Chọn thay đổi nhỏ nhất phục vụ trải nghiệm cần đạt.

**Đánh đổi:** Tăng tốc cắt có thể tạo năng lượng nhưng cũng tăng công sức theo dõi.

**Kiểm tra:**

- Nêu được yếu tố đang tạo nhịp ở một mốc cụ thể.
- Bản sửa không chỉ cắt đều theo một số giây.

**Ví dụ tự biên soạn:** Chuỗi thao tác ngắn, rõ có thể nhẹ nhàng; cảnh dài nhiều biến cố vẫn có thể căng.

**Phản ví dụ / giới hạn:** Giữ hình lâu không tự tạo thư giãn hoặc chiều sâu.

**Liên quan:** [AU-005](../kien-thuc/AU-005.json), [MO-005](../kien-thuc/MO-005.json), [SO-006](../kien-thuc/SO-006.json)

**Nguồn đối chiếu:** [B017](../../bai-hoc/017-mini-story-ba-nhip/README.md), [B024](../../bai-hoc/024-xau-chuoi-canh/README.md), [SRC-YALE-EDIT](https://filmanalysis.yale.edu/editing/)

[Bản JSON chuẩn](../kien-thuc/ED-001.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ed-002"></a>
## ED-002 — Điểm cắt theo hành động, thông tin và phản ứng

**Câu hỏi quyết định:** Cắt lúc nào giúp người xem nhận đúng điều cần?

**Dùng khi:** Khi có nhiều phiên bản điểm vào/ra.

**Nguyên lý thực hành:** Chọn điểm cắt theo điều vừa đủ hiểu, mong chờ và hướng chú ý. Không bắt buộc cắt ngay khi hành động kết thúc.

**Cách làm:**

1. Xác định thông tin phải được nhận trước cut.
2. Thử vào sớm/muộn và ra sớm/muộn quanh sự kiện.
3. Giữ hoặc bỏ nhịp phản ứng theo vai trò của nó.

**Đánh đổi:** Cắt rất gọn có thể mất trọng lượng thao tác; giữ dư có thể lặp thông tin.

**Kiểm tra:**

- Không bỏ mất kết quả cần xác nhận.
- Không cắt làm động tác có vẻ bị lặp hoặc nhảy vô cớ.

**Ví dụ tự biên soạn:** Đợi bát thật sự đứng trên khay rồi mới chuyển nếu việc đặt là bằng chứng cần thấy.

**Phản ví dụ / giới hạn:** Cắt trước tiếp xúc có thể tạo mong chờ nếu shot sau trả đúng sự kiện.

**Liên quan:** [DR-003](../kien-thuc/DR-003.json), [ED-003](../kien-thuc/ED-003.json), [SO-004](../kien-thuc/SO-004.json)

**Nguồn đối chiếu:** [B024](../../bai-hoc/024-xau-chuoi-canh/README.md), [B032](../../bai-hoc/032-dieu-khien-am-thanh/README.md)

[Bản JSON chuẩn](../kien-thuc/ED-002.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ed-003"></a>
## ED-003 — Nối hành động, ánh mắt và trạng thái

**Câu hỏi quyết định:** Qua cut, điều gì cần giữ để hiểu liên tục?

**Dùng khi:** Khi dựng nhiều góc của một việc hoặc tương tác.

**Nguyên lý thực hành:** Kiểm thời gian, hướng, vị trí, tay đang làm, trạng thái vật và âm. Nối đúng ý nghĩa có thể quan trọng hơn khớp mọi pixel, tùy phong cách.

**Cách làm:**

1. So cuối shot trước và đầu shot sau ở tốc độ xem thật.
2. Kiểm bàn tay, mức đầy, vị trí người/vật và đích nhìn.
3. Nếu có nhảy thời gian, cho dấu tiến triển để người xem không hiểu là lỗi.

**Đánh đổi:** Khớp quá máy móc có thể làm nhịp kém; bỏ qua sai trạng thái có thể phá niềm tin.

**Kiểm tra:**

- Không nhân đôi việc cắt/đổ hoặc vật đã nhận.
- Hướng nhìn và không gian nối được hoặc đổi có chủ đích.

**Ví dụ tự biên soạn:** Cận cho thấy chốt rời móc; góc rộng kế tiếp cửa bắt đầu mở từ trạng thái phù hợp.

**Phản ví dụ / giới hạn:** Một jump cut chủ ý có thể nén việc mà vẫn cần trạng thái tiến triển hiểu được.

**Liên quan:** [CA-004](../kien-thuc/CA-004.json), [DR-006](../kien-thuc/DR-006.json), [MO-006](../kien-thuc/MO-006.json)

**Nguồn đối chiếu:** [B013](../../bai-hoc/013-tach-shot-hoi-thoai/README.md), [B024](../../bai-hoc/024-xau-chuoi-canh/README.md)

[Bản JSON chuẩn](../kien-thuc/ED-003.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ed-004"></a>
## ED-004 — Nén thời gian, lược việc và giữ nhân quả

**Câu hỏi quyết định:** Bước nào có thể bỏ mà người xem vẫn hiểu?

**Dùng khi:** Khi công đoạn dài, lặp hoặc vượt thời lượng phim.

**Nguyên lý thực hành:** Giữ mốc bắt đầu, biến đổi quan trọng và kết quả; nén phần lặp. Chỉ cho thời gian cụ thể khi nguồn đủ xác nhận.

**Cách làm:**

1. Lập chuỗi trạng thái thực trước khi rút gọn.
2. Giữ bước gây ra kết quả khó suy ra.
3. Dùng cảnh chuyển hoặc thay đổi vật/thời điểm để báo khoảng lược.

**Đánh đổi:** Nén nhiều làm tiến độ dễ xem nhưng có thể che kỹ thuật hoặc quy luật tự nhiên.

**Kiểm tra:**

- Không tạo hiểu nhầm cây lớn tức thì hay món chín chỉ sau một động tác.
- Không tự gán cùng một mẻ/nguyên liệu qua các cảnh chưa xác minh.

**Ví dụ tự biên soạn:** Gieo, tín hiệu thời gian rồi cây lớn; không nhất thiết phải quay mọi ngày.

**Phản ví dụ / giới hạn:** Video dạy thao tác có thể cần giữ bước lặp để người mới hiểu cách làm.

**Liên quan:** [MO-006](../kien-thuc/MO-006.json), [ST-005](../kien-thuc/ST-005.json), [EV-006](../kien-thuc/EV-006.json)

**Nguồn đối chiếu:** [B017](../../bai-hoc/017-mini-story-ba-nhip/README.md), [B024](../../bai-hoc/024-xau-chuoi-canh/README.md)

[Bản JSON chuẩn](../kien-thuc/ED-004.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ed-005"></a>
## ED-005 — Tăng, giữ và thả mong chờ

**Câu hỏi quyết định:** Đường nhịp có thay đổi tương xứng với điều đang chờ không?

**Dùng khi:** Khi phim phẳng hoặc kết quả không có sức nặng.

**Nguyên lý thực hành:** Thiết kế các nhịp đặt kỳ vọng, tiến triển, chậm/giữ và nhận kết quả. Đây là công cụ bố trí, không đường cong áp đặt mọi thể loại.

**Cách làm:**

1. Đánh dấu điều đang chờ ở từng chuỗi.
2. Dồn hoặc giãn thông tin theo độ cần hiểu.
3. Cho kết quả và dư âm có không gian trước nhiệm vụ mới.

**Đánh đổi:** Trì hoãn quá lâu dễ bực; trả mọi thứ quá sớm có thể mất lực theo dõi.

**Kiểm tra:**

- Có tương phản nhịp nhưng không đổi đột ngột trái lời hứa.
- Không nhất thiết tăng nhạc hoặc cắt nhanh để tạo cao trào.

**Ví dụ tự biên soạn:** Sau chuỗi làm ngắn, giữ sản phẩm và phản ứng sử dụng nó.

**Phản ví dụ / giới hạn:** Phim ru ngủ có thể hạn chế các đỉnh kích thích; vẫn có thể có tiến triển nhẹ.

**Liên quan:** [AU-003](../kien-thuc/AU-003.json), [ST-004](../kien-thuc/ST-004.json), [SO-006](../kien-thuc/SO-006.json)

**Nguồn đối chiếu:** [B017](../../bai-hoc/017-mini-story-ba-nhip/README.md), [B024](../../bai-hoc/024-xau-chuoi-canh/README.md)

[Bản JSON chuẩn](../kien-thuc/ED-005.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ed-006"></a>
## ED-006 — Montage, dựng song song và liên hệ ý tưởng

**Câu hỏi quyết định:** Hai hình đặt cạnh nhau khiến người xem liên hệ điều gì?

**Dùng khi:** Khi dựng nhiều nơi, nhiều tuyến hoặc biến đổi dài.

**Nguyên lý thực hành:** Ghi loại quan hệ: đồng thời, trước–sau, so sánh, đối lập hoặc liên tưởng. Tránh để cắt xen tự tạo phát biểu sự thật sai.

**Cách làm:**

1. Đặt tên quan hệ mong muốn cho từng cặp/nhóm shot.
2. Giữ dấu định hướng đủ để phân biệt nơi/người/thời điểm.
3. Kiểm người xem có suy ra một sự kiện không được bằng chứng hỗ trợ.

**Đánh đổi:** Liên tưởng mạnh có thể làm người xem suy quan hệ nhân quả ngoài ý đồ.

**Kiểm tra:**

- Không coi hai tuyến cắt xen là chắc chắn đồng thời.
- Điểm trở lại mỗi tuyến bổ sung thông tin mới.

**Ví dụ tự biên soạn:** Hai bàn tay ở hai thế hệ có thể được nối bằng nhịp thao tác để gợi truyền nghề.

**Phản ví dụ / giới hạn:** Trong phim tài liệu, đặt cảnh thú săn cạnh con mồi không tự chứng minh chúng cùng sự kiện.

**Liên quan:** [ST-005](../kien-thuc/ST-005.json), [ST-006](../kien-thuc/ST-006.json), [EV-001](../kien-thuc/EV-001.json)

**Nguồn đối chiếu:** [SRC-YALE-EDIT](https://filmanalysis.yale.edu/editing/)

[Bản JSON chuẩn](../kien-thuc/ED-006.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ed-007"></a>
## ED-007 — Cảnh xen và chuyển cảnh có chức năng

**Câu hỏi quyết định:** Hình/âm ở giữa hai đoạn đang nối điều gì?

**Dùng khi:** Khi đổi nơi, thời điểm, công việc hoặc trọng tâm.

**Nguyên lý thực hành:** Cảnh xen có thể định hướng, lược thời gian, cho khoảng thở hoặc gợi liên hệ. Hiệu ứng dissolve/fade không tự làm điểm nối hợp lý.

**Cách làm:**

1. Nêu điều đổi và điều giữ qua ranh giới.
2. Chọn hình hoặc âm có quan hệ với cả hai bên.
3. Thử cut đơn giản trước khi thêm hiệu ứng chuyển.

**Đánh đổi:** Cảnh xen đẹp nhưng không liên quan có thể làm mạch đứt.

**Kiểm tra:**

- Người xem hiểu đã đổi nơi/thời gian khi cần.
- Loại chuyển cảnh chỉ được ghi chắc khi đã xem quanh ranh giới.

**Ví dụ tự biên soạn:** Ngoại cảnh đêm giữa phủ thùng và mở thùng có thể báo thời gian qua nếu mạch đủ rõ.

**Phản ví dụ / giới hạn:** Chuyển thẳng vào việc mới có thể tốt hơn thêm phong cảnh khi địa lý đã rõ.

**Liên quan:** [SO-004](../kien-thuc/SO-004.json), [ED-004](../kien-thuc/ED-004.json), [ST-005](../kien-thuc/ST-005.json)

**Nguồn đối chiếu:** [B024](../../bai-hoc/024-xau-chuoi-canh/README.md)

[Bản JSON chuẩn](../kien-thuc/ED-007.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).

<a id="ed-008"></a>
## ED-008 — Dựng bản thô, rà trải nghiệm và hoàn thiện

**Câu hỏi quyết định:** Bản dựng đã hoạt động trước khi trang trí chưa?

**Dùng khi:** Khi ráp nhiều clip hoặc sửa phim dài.

**Nguyên lý thực hành:** Dựng theo câu chuyện/thông tin trước, rồi tinh nhịp, âm, màu và chất lượng xuất. Mỗi vòng duyệt có câu hỏi riêng.

**Cách làm:**

1. Làm bản thô đủ đầu–giữa–cuối với vật liệu có thật.
2. Rà mạch và trải nghiệm liền phim, đánh dấu lỗi theo mốc.
3. Sửa cấu trúc trước các chỉnh nhỏ dễ bị bỏ khi đổi dựng.

**Đánh đổi:** Hoàn thiện sớm một shot có thể tốn công nếu nó bị loại khỏi câu chuyện.

**Kiểm tra:**

- Có thể giải thích lý do giữ mỗi đoạn.
- Tệp xuất được xem/nghe lại, không chỉ timeline.

**Ví dụ tự biên soạn:** Một chuỗi làm việc thiếu kết quả cần bổ sung cấu trúc trước khi tăng hạt phim hay nhạc.

**Phản ví dụ / giới hạn:** Một lỗi kỹ thuật chặn xem có thể cần sửa ngay để còn đánh giá bản thô.

**Liên quan:** [QC-001](../kien-thuc/QC-001.json), [ST-008](../kien-thuc/ST-008.json), [AI-008](../kien-thuc/AI-008.json)

**Nguồn đối chiếu:** [B024](../../bai-hoc/024-xau-chuoi-canh/README.md), [SRC-BMD-TRAINING](https://www.blackmagicdesign.com/products/davinciresolve/training)

[Bản JSON chuẩn](../kien-thuc/ED-008.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json).
