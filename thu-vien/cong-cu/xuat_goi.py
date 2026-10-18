"""Build portable AI reading packages from canonical JSON and Markdown."""
from pathlib import Path
import json,re,hashlib
ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parent
OUT=ROOT/'goi-doc'
VERSION=json.loads((ROOT/'manifest.json').read_text())['version']
STEM='CORE_'+VERSION.replace('.','_')
BASE='https://github.com/ducna841188/kien-thuc-dien-anh/blob/main/'
def absolute_links(text,source):
 def replace(m):
  label,raw=m.group(1),m.group(2)
  if raw.startswith(('http://','https://','mailto:')):return m.group(0)
  path,sep,anchor=raw.partition('#')
  target=(source.parent/path).resolve() if path else source.resolve()
  try:r=target.relative_to(REPO.resolve()).as_posix()
  except ValueError:return m.group(0)
  return f'[{label}]({BASE}{r}{sep}{anchor})'
 return re.sub(r'\[([^\]]*)\]\(([^)]+)\)',replace,text)
def main():
 OUT.mkdir(exist_ok=True)
 cards=[json.loads(p.read_text()) for p in sorted((ROOT/'kien-thuc').glob('*.json'))]
 render_views(cards)
 render_auxiliary(cards)
 # JSONL has only canonical knowledge records; no source material mislabeled as model answers.
 (OUT/(STEM+'.jsonl')).write_text(''.join(json.dumps(c,ensure_ascii=False)+chr(10) for c in cards))
 source_stem='SOURCES_'+VERSION.replace('.','_')+'.json'
 (OUT/source_stem).write_bytes((ROOT/'nguon/nguon-chinh-thuc.json').read_bytes())
 head=f"""# FILM-KB {VERSION} — Gói đọc đầy đủ cho AI

Bản xuất từ JSON chuẩn và tài liệu cùng phiên bản. Gói này là dữ liệu tham chiếu, chưa huấn luyện thay đổi mô hình. Chia lượt theo chuyên đề nếu môi trường không nhận đủ; ghi những phần đã thực đọc.

Liên kết trong gói dẫn về các tệp của kho. Khi cần bản ghim tuyệt đối, lấy commit chứa manifest của bản phát hành đang dùng; không giả định main mãi giữ nguyên.

Các tác dụng cảm xúc là giả thuyết có điều kiện; ví dụ mới chưa chạy tạo video/kiểm khán giả. Bộ kiểm cấu trúc không thay đánh giá AI khác.

"""
 pieces=[head]
 paths=[ROOT/n for n in ['00_HUONG_DAN_AI.md','01_KIEN_TRUC_DU_LIEU.md','02_CHUAN_PHAN_TICH.md','03_RA_QUYET_DINH.md','04_CAP_NHAT_KIEN_THUC.md','06_VAN_HANH_SAN_XUAT.md','07_KIEM_TRA_TRAI_NGHIEM.md','08_BAN_DO_NANG_LUC.md']]
 paths+=sorted((ROOT/'quy-trinh').glob('*.md'))
 paths+=sorted((ROOT/'chuyen-de').glob('*.md'))
 paths+=[ROOT/'vi-du/bon-ca-ra-quyet-dinh.md',ROOT/'NHIP_CAM_XUC.md',ROOT/'TU_DIEN.md',ROOT/'mo-hinh/README.md',ROOT/'05_NGUON_VA_KIEM_TOAN.md',ROOT/'nguon/SO_NGUON.md']
 for path in paths:
  pieces+=['---',f'Nguồn bản xuất: {path.relative_to(ROOT).as_posix()}',absolute_links(path.read_text(),path)]
 (OUT/(STEM+'.md')).write_text((chr(10)*2).join(pieces)+chr(10))
 brief="""# FILM-KB — Gói định hướng ngắn

Đọc mục lục và lấy nguyên mục kiến thức liên quan trước khi quyết định. Gói ngắn không thay toàn bộ nội dung.

1. Phân biệt quan sát, nguồn thuật lại, diễn giải, đề xuất và kết quả thử.
2. Chọn mục tiêu khán giả và điều đã duyệt cần giữ.
3. Tổ chức toàn phim → phân đoạn → chuỗi → shot → sự kiện, giữ thời gian và nguồn.
4. Chọn kỹ thuật theo thông tin và trải nghiệm; đọc cả điều kiện, đánh đổi, phản ví dụ.
5. Tách cỡ cảnh, góc, khoảng cách, đường máy, nét, sáng, màu và cách xử lý thời gian.
6. Nhịp đến từ diễn tiến, lượng thông tin, hành vi, dựng và âm; không chỉ số giây.
7. Cảm xúc nhân vật, ý đồ đạo diễn và phản ứng khán giả là dữ liệu khác nhau.
8. Tách ý đồ chung khỏi cú pháp/thiết lập của model/chế độ cụ thể.
9. Sửa một lỗi thì bảo vệ phần đã đạt; chưa thử không báo đã khắc phục.
10. Ngách ghim mã/phiên bản core; nâng bài học theo điều kiện và bằng chứng, trình thay đổi đảo nguyên tắc.

Mục có application_depth cung cấp ca chọn phương án và chẩn đoán; đọc cả phần phải giữ và giới hạn nguồn. Dùng ../06_VAN_HANH_SAN_XUAT.md để nối công đoạn, ../07_KIEM_TRA_TRAI_NGHIEM.md để chọn đúng bằng chứng và ../08_BAN_DO_NANG_LUC.md để chọn độ sâu.

Mở ../muc-luc.json, ../tuyen-tra-cuu.json, ../00_HUONG_DAN_AI.md và quy trình tác vụ tương ứng. Bản phát hành và version từng mục là hai cấp khác nhau.
"""
 (OUT/'CORE_NGAN.md').write_text(brief)
 start="""# Mang thư viện sang một AI khác

## Đọc chọn theo tác vụ

Gửi [hướng dẫn AI](../00_HUONG_DAN_AI.md), [chuẩn phân tích](../02_CHUAN_PHAN_TICH.md), [chuẩn quyết định](../03_RA_QUYET_DINH.md), quy trình tác vụ và các chuyên đề liên quan. Thêm hồ sơ ngách, tài sản và yêu cầu hiện tại.

[Mục lục](../muc-luc.json) · [Tra theo vấn đề](../tuyen-tra-cuu.json) · [Gói định hướng ngắn](CORE_NGAN.md)

## Đọc toàn bộ

- [CORE_1_0_0.md](CORE_1_0_0.md): bản Markdown đầy đủ.
- [CORE_1_0_0.jsonl](CORE_1_0_0.jsonl): 90 bản ghi kiến thức, mỗi dòng một đối tượng.
- [Sổ nguồn đi kèm](SOURCES_1_0_0.json): phạm vi đã đọc và giới hạn từng nguồn ngoài.
- [manifest-goi.json](manifest-goi.json): kích thước và SHA-256 các tệp gói.

Đây là dữ liệu tham chiếu. Cần công cụ đọc tệp/đường dẫn thực sự; gửi URL không tự xác nhận mọi tệp đã được đọc. Dùng cách đọc chọn nếu một lượt không đủ.

## Lời giao việc mẫu

~~~text
Đọc hướng dẫn FILM-KB và xác nhận phiên bản, các tệp đã đọc.
Tác vụ của tôi: [phân tích video / kịch bản / shot / câu lệnh / sửa lỗi].
Ngách và hồ sơ đã duyệt: [đường dẫn hoặc chưa chọn].
Đầu vào: [tệp, tài sản, phiên bản và phần đã đạt].
Mục tiêu: [thông tin và trải nghiệm mong muốn].
Áp dụng kiến thức đúng điều kiện; dẫn mã/phiên bản.
Phân biệt quan sát, diễn giải, đề xuất và kết quả thử.
Thiếu dữ liệu thiết yếu thì chỉ rõ, không tự bịa để điền.
Trả quyết định thực hiện được cùng đánh đổi và tiêu chí kiểm.
~~~

Chưa có tuyên bố bộ gói đã được đánh giá độc lập trên các mô hình khác. Dùng [bộ tình huống](../kiem-thu/HUONG_DAN_DANH_GIA.md) để thực hiện bước đó.
"""
 start=start.replace('CORE_1_0_0',STEM).replace('SOURCES_1_0_0.json',source_stem).replace('90 bản ghi',str(len(cards))+' bản ghi')
 (OUT/'START_HERE.md').write_text(start)
 files=[]
 for name in [STEM+'.md',STEM+'.jsonl',source_stem,'CORE_NGAN.md','START_HERE.md']:
  p=OUT/name;b=p.read_bytes();files.append({'path':name,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
 manifest={'version':VERSION,'canonical_record_count':len(cards),'files':files,'training_performed':False,'semantic_retrieval_deployed':False}
 (OUT/'manifest-goi.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+chr(10))
 print(json.dumps({'exported':len(files),'canonical_records':len(cards),'full_markdown_bytes':files[0]['bytes']}))
def render_views(cards):
 index=json.loads((ROOT/'muc-luc.json').read_text())
 sources={s['id']:s for s in json.loads((ROOT/'nguon/nguon-chinh-thuc.json').read_text())['sources']}
 lessons={l['lesson_id']:l for l in json.loads((REPO/'DANH-MUC-BAI-HOC.json').read_text())['lessons']}
 items=[]
 for module in index['modules']:
  subset=sorted((c for c in cards if c['module_id']==module['id']),key=lambda c:c['id'])
  lines=[f"# {module['id']} — {module['title']}",'',f"Phiên bản {VERSION}. {module['objective']}",'',
   '[Mục lục](../README.md) · [Chuẩn ra quyết định](../03_RA_QUYET_DINH.md)','',
   'Mỗi mục dưới là hướng dẫn có điều kiện. Tác dụng cảm xúc là giả thuyết thiết kế; chưa có thử tạo video hoặc kiểm nghiệm khán giả cho các ví dụ mới. Thuật ngữ xem [từ điển](../TU_DIEN.md).','',
   '| Mã | Quyết định | Mức |','| --- | --- | --- |']
  for c in subset:lines.append(f"| [{c['id']}](#{c['id'].lower()}) | {c['title']} | {c['level']} |")
  for c in subset:
   lines+=['',f'<a id="{c["id"].lower()}"></a>',f"## {c['id']} — {c['title']}",'',
    '**Phiên bản mục:** '+c['version'],'','**Câu hỏi quyết định:** '+c['decision_question'],'','**Dùng khi:** '+' '.join(c['use_when']),'',
    '**Nguyên lý thực hành:** '+c['principle'],'','**Cách làm:**','']
   lines += [f'{i}. {a}' for i,a in enumerate(c['actions'],1)]
   lines += ['','**Đánh đổi:** '+' '.join(c['tradeoffs']),'','**Kiểm tra:**','']+['- '+a for a in c['verification']]
   lines += ['','**Ví dụ tự biên soạn:** '+c['original_example'],'','**Phản ví dụ / giới hạn:** '+c['counterexample'],'',
    '**Liên quan:** '+', '.join(f'[{i}](../kien-thuc/{i}.json)' for i in c['related_ids']),'']
   if 'application_depth' in c:
    d=c['application_depth'];w=d['worked_example']
    lines+=['','### Áp dụng và chẩn đoán','','**Cơ chế/quan hệ cần xét:** '+d['mechanism'],'',
     '**Tình huống:** '+w['brief'],'','**Phần phải giữ:** '+' '.join(w['protected_elements']),'',
     '| Phương án | Thực hiện |','| --- | --- |',
     '| A | '+w['option_a']+' |','| B | '+w['option_b']+' |','',
     '**Cách chọn:** '+w['selection_rule'],'','**Dấu hiệu kiểm trong ca:**','']
    lines+=['- '+x for x in w['observable_checks']]
    for f in d['failure_diagnosis']:
     lines+=['','**Nếu gặp:** '+f['symptom'],'','Có thể do: '+' '.join(f['possible_causes']),'','Thử tiếp: '+f['next_test']]
    for e in d['evidence_links']:
     lines+=['','**Phát biểu được đối chiếu:** '+e['claim']+' Nguồn: ['+e['source_id']+']('+sources[e['source_id']]['url']+').',
      '','**Giới hạn nguồn:** '+e['scope_limit']]
   refs=[]
   for ident in c['source_ids']:
    if ident in sources:refs.append(f"[{ident}]({sources[ident]['url']})")
    else:refs.append(f"[{ident}](../../{lessons[ident]['repository_lesson_path']}/README.md)")
   lines+=['**Nguồn đối chiếu:** '+', '.join(refs),'',
    f"[Bản JSON chuẩn](../kien-thuc/{c['id']}.json). Đọc phạm vi nguồn trong [sổ nguồn](../nguon/nguon-chinh-thuc.json)."]
   items.append({k:c[k] for k in ['id','title','version','module_id','level','decision_question','related_ids','source_ids']}|
    {'json_path':f"kien-thuc/{c['id']}.json",'markdown_path':module['path']+'#'+c['id'].lower()})
  (ROOT/module['path']).write_text(chr(10).join(lines)+chr(10))
 index['version']=VERSION;index['items']=items
 (ROOT/'muc-luc.json').write_text(json.dumps(index,ensure_ascii=False,indent=2)+chr(10))
def render_auxiliary(cards):
 source_data=json.loads((ROOT/'nguon/nguon-chinh-thuc.json').read_text())
 slines=['# Sổ nguồn đối chiếu có phạm vi','','Bản xuất từ nguon-chinh-thuc.json. Nguồn hỗ trợ phát biểu trong phạm vi đã đọc; phương án và ca áp dụng là biên soạn thực hành.']
 for s in source_data['sources']:
  slines+=['',f"## {s['id']} — {s['title']}",'',f"[Nguồn]({s['url']}) · Kiểm ngày {s['verified_on']} · Loại: {s['kind']}",'',
   '**Phạm vi:** '+s['scope'],'','**Phần đã đọc/cách dùng:** '+s['notes'],'','**Chưa xác nhận:** '+s['not_established']]
 (ROOT/'nguon/SO_NGUON.md').write_text(chr(10).join(slines)+chr(10))
 terms=json.loads((ROOT/'tu-dien-thuat-ngu.json').read_text())['terms']
 text='# Từ điển thuật ngữ thực hành'+chr(10)*2+'[Mục lục](README.md). Nghĩa được dùng trong kho; một số từ có cách dùng rộng hơn ở nguồn khác.'+chr(10)*2
 text+=chr(10).join(['| Thuật ngữ | Nghĩa tiếng Việt | Mã |','| --- | --- | --- |']+
  [f"| {x['term']} | {x['meaning_vi']} | [{x['core_ids'][0]}](kien-thuc/{x['core_ids'][0]}.json) |" for x in terms])
 (ROOT/'TU_DIEN.md').write_text(text+chr(10))
 profiles=json.loads((ROOT/'nhip-cam-xuc.json').read_text())['profiles']
 lines=['# Bản đồ thiết kế nhịp và cảm xúc','','[Mục lục](README.md). Các hồ sơ là giả thuyết thiết kế có điều kiện, chưa kiểm bằng video hoặc người xem.']
 for r in profiles:
  lines+=['',f"## {r['id']} — {r['target_response']}",'',r['design_idea'],'',
   '| Thành phần | Lựa chọn để thử |','| --- | --- |']
  for k,label in [('story_information','Thông tin/câu chuyện'),('image','Hình/máy'),('lighting_color','Sáng/màu'),('editing','Dựng/nhịp'),('sound','Âm'),('failure_risk','Nguy cơ phản tác dụng'),('viewer_check','Kiểm với người xem')]:
   lines.append(f"| {label} | {r[k]} |")
  lines+=['','Mã liên quan: '+', '.join(f'[{i}](kien-thuc/{i}.json)' for i in r['core_ids'])]
 (ROOT/'NHIP_CAM_XUC.md').write_text(chr(10).join(lines)+chr(10))
 manifest=json.loads((ROOT/'manifest.json').read_text())
 manifest.update(core_card_count=len(cards),module_count=len(json.loads((ROOT/'muc-luc.json').read_text())['modules']),
  schema_count=len(list((ROOT/'schema').glob('*.json'))),emotion_profile_count=len(profiles),glossary_term_count=len(terms),
  ai_evaluation_case_count=len(json.loads((ROOT/'kiem-thu/tinh-huong.json').read_text())['cases']),
  official_reference_count=len(source_data['sources']))
 (ROOT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+chr(10))
if __name__=='__main__':main()
