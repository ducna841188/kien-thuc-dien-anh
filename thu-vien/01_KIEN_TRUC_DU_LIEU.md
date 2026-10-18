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

Mã ổn định, phiên bản thay khi nội dung đổi. Không tái dùng mã đã bỏ cho ý khác. Ngách liên kết core hiện hành trên main và ghi version đã kiểm; bản phân tích giữ revision nguồn hoặc checksum/asset ID. Nếu không có dữ liệu đo thì null với lý do; khác với số 0, không có hoặc không áp dụng.

Schema mô tả hình dạng dữ liệu. Kiểm ngữ nghĩa bổ sung kiểm thời gian, quan hệ cha, tham chiếu, độ phủ và quyền kết luận. Schema đúng chưa có nghĩa phân tích đúng video.

Tài sản nguồn và lời nguồn được thuật lại là bằng chứng có revision; phân tích do thư viện biên soạn là tài liệu hiện hành có thể sửa. Khi phát hiện lỗi phân tích, sửa đúng tệp và dẫn bằng chứng, ghi nhật ký; không giữ một kết luận sai chỉ vì muốn “giữ nguyên phân tích”.

## Tìm kiếm và giới hạn

muc-luc.json tra mã/chuyên đề; tuyen-tra-cuu.json tra theo vấn đề. cong-cu/tra_cuu.py là tìm từ khóa cục bộ, chưa phải tìm ngữ nghĩa. JSONL có một mục kiến thức mỗi dòng; phần phân tích video giữ ở corpus riêng. Không tự dùng toàn bộ dữ liệu nguồn làm ví dụ trả lời đúng.

## Hợp đồng dữ liệu hiện hành

Schema kiến thức có application_depth tùy chọn. Phiên bản schema mô tả hợp đồng dữ liệu, khác version của nội dung; các tệp schema hiện hành luôn được sửa tại cùng đường dẫn. Không sao schema theo bản phát hành.

| Thành phần application_depth | Chức năng |
| --- | --- |
| mechanism | Quan hệ/cơ chế cần xét; có thể là phương pháp tổng hợp, không tự là kết quả khoa học |
| worked_example | Brief, phần phải giữ, hai phương án, cách chọn và dấu kiểm |
| failure_diagnosis | Triệu chứng, các nguyên nhân có thể và phép thử tiếp theo |
| evidence_links | Phát biểu cụ thể được nguồn hỗ trợ và giới hạn; mảng rỗng không có nghĩa mục đã được thực nghiệm |

Các ca ở vi-du/bon-ca-ra-quyet-dinh.json là synthetic_worked_examples, chưa thực hiện và không dùng thay analysis. Bản đồ năng lực, vòng sản xuất và bảng phép kiểm là hướng dẫn điều phối, không thêm nhãn quan sát giả vào video nguồn.

Schema phân tích cho phép tài sản video, ảnh, báo cáo, âm thanh riêng và ví dụ giả lập. Mốc của bằng chứng trực tiếp phải khớp độ phủ đã khai; basis phải dẫn đúng loại bằng chứng. Bản phân tích lịch sử giữ core_version ở thời điểm lập, còn mẫu và ví dụ thực hành đang dùng phải dẫn mã/phiên bản hiện hành.

manifest.version là bản thư viện hiện hành; version của từng mục chỉ đổi khi mục đó đổi. Mỗi mục có một tệp chuẩn. Chuyên đề Markdown, CORE.md và CORE.jsonl là các dạng xuất phục vụ đọc khác nhau, đều phản ánh cùng dữ liệu hiện hành; không là các phiên bản lịch sử.

Gói xuất và kết quả kiểm dùng tên cố định. Lịch sử, diff và khôi phục dùng Git; thay đổi được ghi trong một [CHANGELOG.md](CHANGELOG.md) chung. Corpus tổ chức theo video/asset thật, mỗi phân tích được sửa tại tệp hiện hành của nó; không nhân thư mục theo version chỉ vì biên tập lại.
