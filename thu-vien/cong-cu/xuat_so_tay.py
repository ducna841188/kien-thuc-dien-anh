"""Export the current human handbook pilot. Requires reportlab for PDF generation."""
from pathlib import Path
import json,os,hashlib
from xml.sax.saxutils import escape
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / 'ban-cho-nguoi'
DATA = json.loads((BOOK / 'chuong-01.json').read_text())
META = json.loads((BOOK / 'manifest.json').read_text())
CARDS = {p.stem: json.loads(p.read_text()) for p in (ROOT / 'kien-thuc').glob('*.json')}
BASE = 'https://github.com/ducna841188/kien-thuc-dien-anh/blob/main/thu-vien/'
FONT_ROOT = Path(os.environ.get('FILM_KB_FONT_DIR','/usr/share/fonts/truetype/dejavu'))
for name, file in [('Book', 'DejaVuSans.ttf'), ('BookBold', 'DejaVuSans-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(FONT_ROOT / file)))
pdfmetrics.registerFontFamily('Book', normal='Book', bold='BookBold')

INK = '#193334'; TEAL = '#17675F'; GOLD = '#BD7C36'; BLUE = '#56788C'; MUTED = '#647573'
PAPER = '#F6F4ED'; PALE = '#E8F0EC'; WHITE = '#FFFFFF'; LINE = '#CBD7D1'

def clean(text):
    return text.replace('–', '-').replace('—', '-').replace('\u2011', '-')

class Figure:
    def __init__(self, width=1200, height=470):
        self.width, self.height, self.items = width, height, []
    def rect(self, x, y, w, h, fill=WHITE, stroke=LINE, sw=2):
        self.items.append(('rect', (x,y,w,h), fill, stroke, sw)); return self
    def line(self, x1,y1,x2,y2, stroke=INK, sw=4):
        self.items.append(('line', (x1,y1,x2,y2), None, stroke, sw)); return self
    def circle(self,x,y,r,fill=BLUE,stroke=None,sw=2):
        self.items.append(('circle',(x,y,r),fill,stroke,sw)); return self
    def text(self,x,y,text,size=24,color=INK,bold=False):
        self.items.append(('text',(x,y,clean(text),size,bold),color,None,0)); return self
    def arrow(self,x1,y1,x2,y2,color=TEAL):
        import math
        self.line(x1,y1,x2,y2,color,4)
        a=math.atan2(y2-y1,x2-x1)
        for delta in [-0.48,0.48]: self.line(x2,y2,x2-14*math.cos(a+delta),y2-14*math.sin(a+delta),color,4)
    def svg(self,path):
        out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.width}" height="{self.height}" viewBox="0 0 {self.width} {self.height}" role="img">',
             '<title>Sơ đồ giảng giải tự biên soạn</title>']
        for kind,p,fill,stroke,sw in self.items:
            style=f'fill="{fill or "none"}" stroke="{stroke or "none"}" stroke-width="{sw}"'
            if kind=='rect': x,y,w,h=p; out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" {style}/>')
            elif kind=='circle': x,y,r=p; out.append(f'<circle cx="{x}" cy="{y}" r="{r}" {style}/>')
            elif kind=='line': x1,y1,x2,y2=p; out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" {style} stroke-linecap="round"/>')
            else:
                x,y,t,s,b=p; out.append(f'<text x="{x}" y="{y}" font-family="DejaVu Sans,sans-serif" font-size="{s}" font-weight="{700 if b else 400}" fill="{fill}">{escape(t)}</text>')
        out.append('</svg>'); Path(path).write_text('\n'.join(out)+'\n')
    def pdf(self,c,x,y,width):
        scale=width/self.width
        c.saveState(); c.translate(x,y+self.height*scale); c.scale(scale,-scale)
        for kind,p,fill,stroke,sw in self.items:
            c.setLineWidth(sw)
            if fill:c.setFillColor(colors.HexColor(fill))
            if stroke:c.setStrokeColor(colors.HexColor(stroke))
            if kind=='rect':
                xx,yy,w,h=p;c.roundRect(xx,yy,w,h,12,stroke=int(bool(stroke)),fill=int(bool(fill)))
            elif kind=='circle': xx,yy,r=p;c.circle(xx,yy,r,stroke=int(bool(stroke)),fill=int(bool(fill)))
            elif kind=='line':c.line(*p)
            else:
                xx,yy,t,s,b=p;c.saveState();c.translate(xx,yy);c.scale(1,-1);c.setFont('BookBold' if b else 'Book',s);c.drawString(0,0,t);c.restoreState()
        c.restoreState()

def state_figure():
    f=Figure()
    for i in range(3):
        x=12+i*398
        f.rect(x,10,382,450,WHITE,LINE)
        f.text(x+24,52,DATA['states'][i]['label'],28,TEAL,True)
        f.circle(x+100,125,25,BLUE)
        f.rect(x+74,157,52,96,BLUE,None)
        table=316;by=216 if i==0 else 236
        f.line(x+45,table,x+350,table,MUTED,6)
        f.line(x+65,table,x+65,390,LINE,5);f.line(x+326,table,x+326,390,LINE,5)
        f.rect(x+188,by,122,80,'#D2AC7B',GOLD,3)
        f.line(x+188,by+18,x+310,by+18,GOLD,2)
        if i<2:
            left=(x+188,by+55);right=(x+310,by+55)
        else:left=(x+154,250);right=(x+346,245)
        f.line(x+88,185,*left,BLUE,9);f.line(x+118,184,*right,BLUE,9)
        f.circle(*left,8,GOLD);f.circle(*right,8,GOLD)
        if i==0:
            f.arrow(x+335,235,x+335,285)
            f.text(x+45,426,'Tay đang đỡ; còn khoảng hở',20,MUTED)
        elif i==1:
            f.circle(x+249,316,6,TEAL)
            f.text(x+45,426,'Bàn + tay cùng tham gia đỡ',20,MUTED)
        else:
            f.text(x+45,426,'Hộp ở lại; tay đã rời',20,MUTED)
    return f

def framing_figure():
    f=Figure(1200,490)
    for x in [12,612]:f.rect(x,10,576,470,WHITE,LINE)
    f.text(38,52,'A. HIỂU QUAN HỆ',28,TEAL,True)
    f.text(638,52,'B. ĐỌC TIẾP XÚC',28,TEAL,True)
    f.rect(38,75,524,320,'#F3F2EB',None)
    f.line(80,310,530,310,MUTED,6)
    f.line(115,310,115,380,LINE,5);f.line(500,310,500,380,LINE,5)
    f.circle(190,145,25,BLUE);f.rect(164,177,52,99,BLUE,None)
    f.rect(318,245,118,65,'#D2AC7B',GOLD,3)
    f.line(177,205,318,282,BLUE,9);f.line(204,204,436,282,BLUE,9)
    f.circle(318,282,7,GOLD);f.circle(436,282,7,GOLD)
    f.text(38,438,'Người - bàn - hộp - đường thao tác',21,MUTED)
    f.rect(638,75,524,320,'#F3F2EB',None)
    f.line(662,332,1137,332,MUTED,6)
    f.rect(785,190,220,142,'#D2AC7B',GOLD,3)
    f.line(785,225,1005,225,GOLD,3)
    f.line(666,155,785,268,BLUE,17);f.line(1134,155,1005,268,BLUE,17)
    f.circle(785,268,13,GOLD);f.circle(1005,268,13,GOLD)
    f.circle(895,332,7,TEAL)
    f.text(638,438,'Tay - đáy hộp - mặt bàn',21,MUTED)
    return f

def sound_figure():
    f=Figure(1200,420)
    f.rect(12,10,1176,400,WHITE,LINE)
    marks=[('T1. Hạ',210),('T2. Chạm',500),('T3. Nhả',790),('T4. Giữ',1080)]
    for label,x in marks:
        f.text(x-85,68,label,26,TEAL,True)
        f.line(x,92,x,325,LINE,2)
    f.text(40,153,'Hình',24,INK,True);f.text(40,282,'Âm',24,INK,True)
    f.line(178,145,1120,145,BLUE,5)
    f.line(178,268,1120,268,MUTED,3)
    for x,amp in [(500,52),(510,35),(520,28),(530,20),(540,12),(550,8),(560,4)]:
        f.line(x,268-amp,x,268+amp,TEAL,4)
    f.circle(500,145,10,GOLD)
    f.text(186,373,'Một mốc tiếp xúc; không có tiếng đặt mới ở phần chỉ giữ kết quả.',22,MUTED)
    return f

FIGURES={'ba-trang-thai':state_figure(),'hai-khung-hinh':framing_figure(),'am-va-tiep-xuc':sound_figure()}

def export_markdown():
    modules={m['id']:m for m in json.loads((ROOT/'muc-luc.json').read_text())['modules']}
    lines=['# Sổ tay điện ảnh thực hành','',f"Bản cho người học {META['version']} · Kiến thức nền {META['core_version']} · Ưu tiên máy tính, hình lớn.",'',
           '**Hiện có:** mục lục 13 chương và một chương mẫu. Các chương 2–13 đang ở mức đề cương; cuốn đầy đủ chưa hoàn thành.','',
           '[Đọc chương mẫu](chuong-01.md) · [Tải bản PDF khổ ngang](SO_TAY_DIEN_ANH.pdf) · [Thư viện kiến thức chuẩn](../README.md)','',
           '## Ba đường đọc','',
           '- Đọc nhanh: mục tiêu → hình → điều cần kiểm ở chương mẫu.',
           '- Học tuần tự: xem ví dụ, tự làm bài tập rồi đọc gợi ý đối chiếu.',
           '- Tra khi làm: mở mã kiến thức cuối bài theo vấn đề đang gặp.','',
           '## Mục lục dự kiến','',
           '| Chương | Cần làm được | Trạng thái |','| --- | --- | --- |']
    for c in META['chapters']:
        title=f"{int(c['id'][-2:]):02}. {c['title']}"
        link='chuong-01.md' if c['markdown_path'] else '../'+modules[c['module_id']]['path']
        status='Có chương mẫu' if c['markdown_path'] else 'Đề cương; liên kết mở kiến thức nền'
        lines.append(f"| [{title}]({link}) | {c['learning_goal']} | {status} |")
    lines+=['','## Cách cập nhật','',
            'Kiến thức chuẩn nằm ở JSON core. Bản giải thích cho người học nằm ở chuong-01.json; chương Markdown và PDF được xuất từ đó. Mỗi đường dẫn có một bản hiện hành; version nằm trong metadata, lịch sử dùng Git và [nhật ký chung](../CHANGELOG.md).','',
            'Ảnh là tình huống hư cấu tự biên soạn; sơ đồ là minh họa, không là dữ liệu đo. [Nguồn và prompt hình minh họa](minh-hoa/manifest.json). Phần Lý Tử Thất sẽ dùng khung/mốc nguồn khi đã tiếp nhận video; hiện chưa phân tích tám video mới.']
    (BOOK/'README.md').write_text('\n'.join(lines)+'\n')
    d=DATA
    lines=['# Chương mẫu 01 — '+d['title'],'',d['subtitle'],'',f"Bản người học {d['version']} · Core {d['core_version']} · Mẫu để đọc thử.",'',
           '[Mục lục](README.md) · [Bản PDF](SO_TAY_DIEN_ANH.pdf)','',d['intro'],'','## Sau bài này','']
    lines+=['- '+x for x in d['objectives']]
    lines+=['','## 1. Bắt đầu từ một việc','',d['scenario'],'','![Ảnh hư cấu: người và hộp ở mặt bàn](minh-hoa/tinh-huong-hop.png)','',d['image_note'],'']
    for row in d['evidence_layers']:lines += ['**'+row['label']+':** '+row['text'],'']
    lines+=['## 2. Cho người xem bằng chứng','', '![Ba trạng thái: đỡ, chạm, nhả](minh-hoa/ba-trang-thai.svg)','']
    for row in d['states']:lines+=['**'+row['label']+':** '+row['text'],'']
    lines += [d['state_takeaway'],'','## 3. Chọn khung theo thông tin','', '![Hai cách chọn khung: quan hệ và tiếp xúc](minh-hoa/hai-khung-hinh.svg)','']
    for row in d['framing']:lines+=['**'+row['label']+':** '+row['text'],'']
    lines += [d['framing_takeaway'],'','## 4. Một việc, ba hướng kể','']
    for row in d['variants']:
        lines+=['### '+row['name'],'','**Câu hỏi:** '+row['question'],'','**Thông tin:** '+row['information'],'',
                '**Hình:** '+row['image'],'','**Nhịp và âm:** '+row['rhythm_sound'],'','**Điểm cần cân nhắc:** '+row['risk'],'']
    lines += [d['variant_takeaway'],'','## 5. '+d['sound']['title'],'','![Mốc hình và tiếng tiếp xúc](minh-hoa/am-va-tiep-xuc.svg)','',d['sound']['body'],'']
    lines += ['- '+x for x in d['sound']['checks']]
    lines += ['','## 6. Một phiếu quyết định đã điền','', '| Cần chốt | Lựa chọn trong ví dụ |','| --- | --- |']
    lines += ['| '+r['label']+' | '+r['text']+' |' for r in d['decision_card']]
    lines += ['','**Mô tả ý đồ cho công cụ AI:**','', '> '+d['ai_intent'],'',d['ai_note'],'','## 7. Tự làm một lần','',d['exercise']['brief'],'']
    lines += [f'{i}. {x}' for i,x in enumerate(d['exercise']['questions'],1)]
    lines += ['','<details>','<summary>Gợi ý đối chiếu sau khi tự làm</summary>','',d['exercise']['answer'],'','</details>','', '## Điều cần nhớ','']
    lines += ['- '+x for x in d['summary']]
    lines += ['','## Tra sâu theo mã','']
    lines += [f"- [{r['id']}@{r['version']} — {CARDS[r['id']]['title']}](../kien-thuc/{r['id']}.json)" for r in d['core_refs']]
    lines += ['','Các cách kể là phương án thiết kế chưa tạo clip/kiểm người xem. [Bản dữ liệu chương](chuong-01.json) · [Prompt và phương pháp hình](minh-hoa/manifest.json).']
    (BOOK/'chuong-01.md').write_text('\n'.join(lines)+'\n')

W,H=1120,700
class BookPDF:
    def __init__(self,path):
        self.c=canvas.Canvas(str(path),pagesize=(W,H),invariant=1)
        self.c.setTitle('Sổ tay điện ảnh thực hành - Chương mẫu 01')
        self.c.setAuthor('FILM-KB');self.page=0;self.minimum_y=H
    def p(self,text,x,y,w,size=17,color=INK,bold=False,allow_footer=False):
        style=ParagraphStyle('body',fontName='BookBold' if bold else 'Book',fontSize=size,leading=size*1.42,textColor=colors.HexColor(color))
        p=Paragraph(escape(clean(text)).replace('\n','<br/>'),style)
        _,h=p.wrap(w,H)
        if y-h<(8 if allow_footer else 48):raise ValueError(f'Page {self.page}: text below safe area: {text[:50]}')
        p.drawOn(self.c,x,y-h);self.minimum_y=min(self.minimum_y,y-h);return y-h
    def box(self,x,y,w,h,fill=PALE,stroke=None):
        self.c.setFillColor(colors.HexColor(fill))
        if stroke:self.c.setStrokeColor(colors.HexColor(stroke))
        self.c.roundRect(x,y,w,h,12,fill=1,stroke=int(bool(stroke)))
    def new(self,section,title=None,subtitle=None):
        if self.page:self.c.showPage()
        self.page+=1;self.minimum_y=H
        self.c.setFillColor(colors.HexColor(PAPER));self.c.rect(0,0,W,H,fill=1,stroke=0)
        self.p('FILM-KB  /  SỔ TAY ĐIỆN ẢNH',52,671,750,11,TEAL,True)
        self.p(section,850,671,220,11,MUTED)
        self.c.setStrokeColor(colors.HexColor(LINE));self.c.line(52,646,1068,646)
        self.p(f"Bản người học {META['version']} · Core {META['core_version']}",52,31,750,10,MUTED,allow_footer=True)
        self.p(f'{self.page:02}',1030,31,50,10,TEAL,True,allow_footer=True)
        self.c.linkRect('', 'toc', (52,13,380,34),relative=0,thickness=0)
        if title:self.p(title,52,617,1016,34,INK,True)
        if subtitle:self.p(subtitle,52,556,1016,16,MUTED)
    def fig(self,key,x,y,w):FIGURES[key].pdf(self.c,x,y,w)
    def bullets(self,items,x,y,w,size=17):
        for item in items:
            self.c.setFillColor(colors.HexColor(TEAL));self.c.circle(x+4,y-size*.60,3,fill=1,stroke=0)
            y=self.p(item,x+22,y,w-22,size)-14
        return y
    def save(self):self.c.save()

def export_pdf():
    d=DATA;b=BookPDF(BOOK/'SO_TAY_DIEN_ANH.pdf');c=b.c
    b.new('BẢN ĐỌC THỬ  /  MÁY TÍNH')
    b.p('Một việc,\nba cách kể',52,584,365,49,INK,True)
    b.p(d['subtitle'],52,397,345,20,TEAL)
    b.p('CHƯƠNG MẪU 01',52,286,350,13,GOLD,True)
    b.p('Có mục lục 13 chương và một bài mẫu hoàn chỉnh để bạn đọc, xem hình và tự thực hành.',52,251,345,17,MUTED)
    c.drawImage(ImageReader(str(BOOK/'minh-hoa/tinh-huong-hop.png')),448,170,width=620,height=413.33,mask='auto')
    b.p('Ảnh tình huống hư cấu tạo bằng AI; không phải tư liệu Lý Tử Thất.',448,152,620,11,MUTED)
    b.box(52,56,1016,61)
    b.p('Học theo quan hệ: người xem cần nhận gì → điều gì đổi → bằng chứng nào → hình–âm nào → kiểm thế nào.',72,101,975,17,TEAL,True)

    b.new('BẢN ĐỒ ĐỌC','Một cuốn sách, ba đường đọc')
    c.bookmarkPage('toc');c.addOutlineEntry('Mục lục','toc',level=0)
    b.p('Đọc nhanh qua hình • Học tuần tự qua ví dụ • Tra theo vấn đề khi đang làm',52,559,1016,17,TEAL)
    columns=[META['chapters'][:7],META['chapters'][7:]]
    for col,chapters in enumerate(columns):
        x=52+col*526;y=512
        for ch in chapters:
            n=int(ch['id'][-2:]);state='CÓ CHƯƠNG MẪU' if n==1 else 'ĐỀ CƯƠNG'
            b.p(f"{n:02}  {ch['title']}",x,y,490,15,INK,True)
            b.p(state,x,y-29,490,10,TEAL if n==1 else MUTED)
            if n==1:c.linkRect('', 'chapter01',(x,y-42,x+490,y+1),relative=0,thickness=0)
            y-=60
    b.box(578,80,490,61)
    b.p('Chương 2–13 hiện mới có đề cương. Bản đầy đủ sẽ phát triển tại cùng đường dẫn.',596,127,453,13,MUTED)

    b.new('CHƯƠNG 01','Hình đẹp cần giúp người xem hiểu một việc', 'Bắt đầu từ người, vật, tác động và kết quả cần đọc.')
    c.bookmarkPage('chapter01');c.addOutlineEntry('Chương 01 - Một việc, ba cách kể','chapter01',level=0)
    b.fig('ba-trang-thai',52,137,1016)
    b.p(d['state_takeaway'],52,112,1016,16,TEAL)

    b.new('CHƯƠNG 01','Chọn khung theo thông tin còn thiếu', 'A giúp đọc quan hệ; B giúp đọc tiếp xúc. Cả hai đều có thể hữu ích.')
    b.fig('hai-khung-hinh',52,110,1016)
    b.p('Chưa biết vị trí máy hoặc tiêu cự từ sơ đồ này. Cỡ cảnh, vị trí máy và tiêu cự là các lựa chọn cần phân biệt.',52,89,1016,14,MUTED)

    b.new('CHƯƠNG 01','Đổi cách cung cấp thông tin, đổi cách kể', 'Các phương án dưới là ý đồ cần kiểm; tác dụng cảm xúc chưa được đo.')
    y=515
    for i,row in enumerate(d['variants']):
        h=143;b.box(52,y-h,1016,h-8,WHITE)
        label_bottom=b.p(row['name'],72,y-17,245,17,TEAL,True)
        b.p(row['question'],72,label_bottom-9,245,14,MUTED)
        b.p(row['information'],344,y-17,696,15)
        b.p(row['rhythm_sound'],344,y-79,696,13,MUTED)
        y-=150

    b.new('CHƯƠNG 01','Một ảnh cho biết gì, còn thiếu gì?', 'Đọc trung thực bằng chứng trước khi gọi tên diễn tiến hoặc cảm xúc.')
    c.drawImage(ImageReader(str(BOOK/'minh-hoa/tinh-huong-hop.png')),52,156,width=555,height=370,mask='auto')
    y=515
    for row in d['evidence_layers']:
        y=b.p(row['label'],645,y,423,18,TEAL,True)-9
        y=b.p(row['text'],645,y,423,16)-24
    b.p(d['image_note'],52,128,1016,15,MUTED)

    b.new('CHƯƠNG 01',d['sound']['title'],'Mốc dưới là sơ đồ quan hệ, không phải số giây đã đo từ một clip.')
    b.fig('am-va-tiep-xuc',52,180,1016)
    b.p(d['sound']['body'],52,166,1016,16)
    b.p('Nếu đoạn chỉ giữ kết quả, không tự thêm một tiếng đặt mới. Chưa nghe âm thanh thì chưa xác nhận đồng bộ.',52,87,1016,14,TEAL)

    b.new('CHƯƠNG 01','Từ ý đồ tới một yêu cầu có thể kiểm', 'Một phiếu ngắn trước khi chọn công cụ hoặc viết yêu cầu tạo.')
    y=520
    for row in d['decision_card']:
        b.p(row['label'],52,y,215,16,TEAL,True)
        bottom=b.p(row['text'],287,y,781,16)
        y=bottom-21
    b.p('Trang tiếp theo chuyển phiếu này thành một mô tả ý đồ; cách nhập sẽ theo công cụ thực tế.',52,110,1016,14,MUTED)

    b.new('CHƯƠNG 01','Viết điều cần xảy ra, rồi kiểm trên kết quả', 'Mẫu mô tả ý đồ cho AI; chưa phải cú pháp chung của mọi công cụ.')
    b.box(52,287,1016,240,WHITE)
    b.p(d['ai_intent'],76,504,968,21,INK)
    b.p(d['ai_note'],52,254,1016,17,TEAL)
    b.p('Khi sửa một lỗi, ghi phần phải giữ trước: người, vật, hành động, nhịp thời gian và cách đặt máy đã đạt. Sau sửa, xem lại toàn đoạn quay/tạo và các điểm nối liên quan.',52,140,1016,17,MUTED)

    b.new('THỰC HÀNH','Tự thiết kế một chuỗi, rồi tự kiểm', 'Giữ một người, cùng hộp/phòng, không thoại và trải nghiệm nhẹ.')
    y=b.bullets(d['exercise']['questions'],52,520,475,18)
    b.box(578,185,490,344,WHITE)
    b.p('Một phương án để đối chiếu',598,509,450,20,TEAL,True)
    b.p(d['exercise']['answer'],598,465,450,16)
    b.p('Bạn có thể chọn một góc liên tục hoặc nhiều cú máy. Lý do chọn và bằng chứng đọc được mới là phần cần giải thích.',52,150,475,16,TEAL)

    b.new('BƯỚC TIẾP THEO','Học từ chín video, rồi vận dụng sang Farm', 'Tám video bổ sung đã được chọn; danh sách và tệp video chưa được cung cấp trong lượt này.')
    stages=[('01','Nguồn và video mẫu','Nhận diện đúng chín video; thử đọc hình–âm rồi phân tích đầy đủ một video.'),
            ('02','Hai nhóm, mỗi nhóm ba video','Cùng chuẩn toàn phim → phân đoạn → chuỗi → cú máy → sự kiện; đối chiếu và ghi ngoại lệ.'),
            ('03','Hai video để đối chiếu sau','Ghi trước dự đoán từ bảy video, rồi phân tích chi tiết cả hai; cuối cùng đủ chín hồ sơ.'),
            ('04','Đoạn thử và ứng dụng','Tách DNA phong cách, bằng chứng hiệu quả và khả thi AI; giữ nhân vật/bối cảnh Farm riêng.')]
    y=516
    for n,title,text in stages:
        b.box(52,y-70,64,64,PALE);b.p(n,66,y-19,44,22,TEAL,True)
        b.p(title,139,y,929,19,INK,True);b.p(text,139,y-34,929,15,MUTED);y-=107
    b.p('VID_01 hiện có bảng/12 ảnh; chuyển động và âm thanh vẫn cần video để xác minh.',52,75,1016,14,TEAL)

    b.new('TRA CỨU','Bốn điều cần mang sang cảnh tiếp theo', 'Các mã dưới liên kết tới bản kiến thức chuẩn đang dùng.')
    b.bullets(d['summary'],52,520,1016,17)
    for col,refs in enumerate([d['core_refs'][:6],d['core_refs'][6:12],d['core_refs'][12:]]):
        x=52+col*350;y=338
        for ref in refs:
            text=f"{ref['id']}@{ref['version']}  {CARDS[ref['id']]['title']}"
            bottom=b.p(text,x,y,315,12,MUTED)
            c.linkURL(BASE+'kien-thuc/'+ref['id']+'.json',(x,bottom,x+315,y),relative=0,thickness=0)
            y=bottom-8
    b.save()
    return b.page

def main():
    for name,figure in FIGURES.items():figure.svg(BOOK/'minh-hoa'/f'{name}.svg')
    export_markdown()
    pages=export_pdf()
    current=json.loads((BOOK/'manifest.json').read_text());current['pdf_page_count']=pages
    paths=['README.md','chuong-01.md','chuong-01.json','SO_TAY_DIEN_ANH.pdf','minh-hoa/manifest.json']+DATA['illustrations']
    current['files']=[{'path':name,'bytes':(BOOK/name).stat().st_size,'sha256':hashlib.sha256((BOOK/name).read_bytes()).hexdigest()} for name in paths]
    (BOOK/'manifest.json').write_text(json.dumps(current,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'pages':pages,'pdf':str(BOOK/'SO_TAY_DIEN_ANH.pdf'),'authored_chapters':1,'planned_chapters':13},ensure_ascii=False))

if __name__=='__main__':main()
