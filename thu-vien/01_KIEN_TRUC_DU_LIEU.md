# Kiến trúc hai tầng và các loại bản ghi

## Tầng 1: film.core

Mỗi mã EV/AU/ST/DR/CA/MO/LI/CO/ED/SO/AI/QC/YT chỉ một mục thực hành. JSON trong kien-thuc/ là bản chuẩn; Markdown chuyên đề và gói đọc được xuất từ đó. Mức co_ban, trung_cap, nang_cao mô tả độ phức tạp của quyết định, không phải cấp học thuật.

Nền chung gồm kỹ thuật và cách chọn theo mục tiêu. Ví dụ một kỹ thuật dùng trong ngách này không biến thành yêu cầu cho mọi ngách.

## Tầng 2: hồ sơ ngách và bộ bằng chứng

Mỗi ngách có lời hứa, tệp mục tiêu, lựa chọn đã chốt, quy tắc có điều kiện, nguồn, corpus và ứng viên đề xuất về core. Ngách tham chiếu mã/phiên bản core. Farm ở repo yt-ly-tu-that/Farm/Thu_vien_kien_thuc.

Các hồ sơ mô hình ở mo-hinh/ phục vụ cả hai tầng, là phần triển khai theo thời điểm. Chúng không tạo một tầng kiến thức nghệ thuật thứ ba.

## Phân loại bản ghi

| Bản ghi | Nội dung | Không được dùng thay |
| --- | --- | --- |
| Knowledge | Cách ra quyết định có điều kiện | Bằng chứng đã thấy trong video cụ thể |
| Analysis | Quan sát, diễn giải, độ phủ và câu hỏi | Kịch bản tái dựng được xem như sự thật nguồn |
| Decision | Lý do chọn giữa phương án, phần phải giữ và phép kiểm | Bằng chứng lựa chọn đã thành công |
| Script | Ý đồ hình–tiếng theo nhịp diễn biến | Danh sách thông số công cụ |
| Shot plan | Nhiệm vụ hình/âm, trạng thái và điểm nối | Kết quả đã sinh |
| Generation request | Cách nhập phù hợp model/chế độ | Bảo đảm đầu ra tuân thủ |
| Model profile | Năng lực/cách nhập có ngày và nguồn | Quy luật điện ảnh ổn định |
| Niche profile | Cụ thể hóa theo khán giả và thể loại | Chân lý chung về mọi khán giả |

## Định danh, phiên bản và dữ liệu thiếu

Mã ổn định, phiên bản thay khi nội dung đổi. Không tái dùng mã đã bỏ cho ý khác. Bản ngách ghim core bằng phiên bản và commit; bản phân tích ghim nguồn hoặc lưu checksum/asset ID. Nếu không có dữ liệu đo thì null với lý do; khác với số 0, không có hoặc không áp dụng.

Schema mô tả hình dạng dữ liệu. Kiểm ngữ nghĩa bổ sung kiểm thời gian, quan hệ cha, tham chiếu, độ phủ và quyền kết luận. Schema đúng chưa có nghĩa phân tích đúng video.

## Tìm kiếm và giới hạn

muc-luc.json tra mã/chuyên đề; tuyen-tra-cuu.json tra theo vấn đề. cong-cu/tra_cuu.py là tìm từ khóa cục bộ, chưa phải tìm ngữ nghĩa. JSONL có một mục kiến thức mỗi dòng; phần phân tích video giữ ở corpus riêng. Không tự dùng toàn bộ dữ liệu nguồn làm ví dụ trả lời đúng.

## Hợp đồng mở rộng ở bản 1.1.0

knowledge.schema 1.1.0 thêm application_depth tùy chọn; bản ghi kiến thức 1.0.0 vẫn hợp lệ. Tám hợp đồng phân tích/tác vụ còn lại vẫn là 1.0.0. schema_version của manifest chỉ bản bộ hợp đồng; xem chi tiết trong tuong-thich.json.

| Thành phần application_depth | Chức năng |
| --- | --- |
| mechanism | Quan hệ/cơ chế cần xét; có thể là phương pháp tổng hợp, không tự là kết quả khoa học |
| worked_example | Brief, phần phải giữ, hai phương án, cách chọn và dấu kiểm |
| failure_diagnosis | Triệu chứng, các nguyên nhân có thể và phép thử tiếp theo |
| evidence_links | Phát biểu cụ thể được nguồn hỗ trợ và giới hạn; mảng rỗng không có nghĩa mục đã được thực nghiệm |

Các ca ở vi-du/bon-ca-ra-quyet-dinh.json là synthetic_worked_examples, chưa thực hiện và không dùng thay analysis. Bản đồ năng lực, vòng sản xuất và bảng phép kiểm là hướng dẫn điều phối, không thêm nhãn quan sát giả vào video nguồn.

manifest.version là bản phát hành; version của từng mục chỉ đổi khi mục đó đổi. JSONL bản cũ được giữ nguyên byte, cùng checksum và commit trong tuong-thich.json. Kiểm tương thích cấu trúc không tự đổi ghim tri thức của ngách.
