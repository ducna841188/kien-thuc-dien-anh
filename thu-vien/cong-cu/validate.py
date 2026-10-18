"""Validate FILM-KB structure and evidence contracts. Does not assess video content."""
from pathlib import Path
import json,sys,re,hashlib,math,argparse,copy,unicodedata
from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parents[1]
def load(p):return json.loads(Path(p).read_text())
def json_errors(data,schema):
 return [f"{'/'.join(map(str,e.absolute_path))}: {e.message}" for e in Draft202012Validator(schema).iter_errors(data)]
def spans_cover(spans,duration):
 if duration is None:return False
 point=0.0
 for s in sorted(spans,key=lambda x:x['start_seconds']):
  if s['start_seconds']>point+1e-6:return False
  point=max(point,s['end_seconds'])
 return point>=duration-1e-6
def analysis_errors(data,schema=None,known_core=None):
 schema=schema or load(ROOT/'schema/analysis.schema.json')
 errs=json_errors(data,schema)
 if errs:return errs
 def bad(s):errs.append(s)
 duration=data['duration_seconds']
 assetids=[x['id'] for x in data['assets']]
 evids=[x['id'] for x in data['evidence_records']]
 segids=[x['id'] for x in data['segments']]
 seqids=[x['id'] for x in data['sequences']]
 shotids=[x['id'] for x in data['shots']]
 eventids=[x['id'] for s in data['shots'] for x in s['events']]
 for label,ids in [('asset',assetids),('evidence',evids),('segment',segids),('sequence',seqids),('shot',shotids),('event',eventids)]:
  if len(ids)!=len(set(ids)):bad('duplicate '+label+' ID')
 if data['time_origin']['original_asset_id'] not in assetids:bad('missing time origin asset')
 def check_span(x,label,allow_point=False):
  st=x['start_seconds'];en=x['end_seconds']
  if not math.isfinite(st) or not math.isfinite(en):bad(label+' non-finite time')
  if en<st or (en==st and not allow_point):bad(label+' end must be after start')
  if duration is not None and en>duration+1e-6:bad(label+' exceeds duration')
 for label,items in [('segment',data['segments']),('sequence',data['sequences']),('shot',data['shots'])]:
  last=-1
  for x in items:
   check_span(x,label)
   if x['start_seconds']<last-1e-6:bad(label+' overlap or unsorted')
   last=x['end_seconds']
 for x in data['coverage']['visual_motion_intervals']+data['coverage']['audio_intervals']:
  check_span(x,'coverage')
 for t in data['coverage']['sampled_frame_times']:
  if duration is not None and t>duration:bad('sample frame exceeds duration')
 if data['coverage']['whole_visual_reviewed'] and not spans_cover(data['coverage']['visual_motion_intervals'],duration):bad('whole visual flag exceeds coverage')
 if data['coverage']['whole_audio_reviewed'] and data['coverage']['audio_presence']!='absent' and not spans_cover(data['coverage']['audio_intervals'],duration):bad('whole audio flag exceeds coverage')
 segs={s['id']:s for s in data['segments']};seqs={s['id']:s for s in data['sequences']}
 def within(x,parent,label):
  if x['start_seconds']<parent['start_seconds']-1e-6 or x['end_seconds']>parent['end_seconds']+1e-6:bad(label+' outside parent')
 for s in data['sequences']:
  if s['segment_id'] not in segs:bad('missing segment parent')
  else:within(s,segs[s['segment_id']],'sequence')
 for e in data['evidence_records']:
  if e['asset_id'] not in assetids:bad('evidence missing asset')
  if e['start_seconds'] is not None and e['end_seconds'] is not None:check_span(e,'evidence',True)
  if data['record_type']=='synthetic_example' and e['kind']!='synthetic':bad('synthetic record has non-synthetic evidence')
 viewerids={x['id'] for x in data['viewer_evidence']}
 def refs_ok(refs,label):
  for r in refs:
   if r not in set(evids)|viewerids:bad(label+' missing evidence '+r)
 def core_ok(ids):
  if known_core:
   for i in ids:
    if i not in known_core:bad('missing core '+i)
 def interp_ok(x):
  refs_ok(x['evidence_refs'],'interpretation');core_ok(x['core_ids'])
  if x['status']=='supported_viewer_report' and not (set(x['evidence_refs'])&viewerids):bad('viewer effect lacks linked viewer data')
 for s in data['shots']:
  if s['sequence_id'] not in seqs:bad('missing sequence parent')
  else:within(s,seqs[s['sequence_id']],'shot')
  for field,v in s['observed'].items():
   refs_ok(v['evidence_refs'],field)
   if v['status']=='observed':
    if field.startswith('audio_') and v['basis']!='direct_audio':bad(field+' observed without audio')
    if field in ['camera_motion','time_treatment'] and v['basis']!='direct_motion':bad(field+' observed without motion')
   if field=='subject_count' and v['value'] is not None and (isinstance(v['value'],bool) or not isinstance(v['value'],int) or v['value']<0):bad('subject count must be nonnegative integer or null')
   if data['record_type']=='synthetic_example' and v['status'] not in ['synthetic','unknown']:bad('synthetic example claims non-synthetic observation')
   if v['status']=='observed' and v['basis']=='direct_motion' and not any(e['kind']=='motion_interval' and e['id'] in v['evidence_refs'] for e in data['evidence_records']):bad(field+' lacks motion evidence record')
   if v['status']=='observed' and v['basis']=='direct_audio' and not any(e['kind']=='audio_interval' and e['id'] in v['evidence_refs'] for e in data['evidence_records']):bad(field+' lacks audio evidence record')
  for event in s['events']:
   check_span(event,'event',True);within(event,s,'event');refs_ok(event['evidence_refs'],'event')
  for x in s['interpretations']:interp_ok(x)
 for x in data['findings']:interp_ok(x)
 for x in data['emotional_intent']:
  check_span(x,'emotional intent');refs_ok(x['evidence_refs'],'emotional intent');core_ok(x['core_ids'])
 if data['record_type']=='synthetic_example' and any(a['kind']!='synthetic' for a in data['assets']):bad('synthetic example has real asset')
 return errs

def link_errors(base):
 errors=[]
 for p in base.rglob('*.md'):
  content=p.read_text()
  for raw in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',content):
   if raw.startswith(('https://','http://','mailto:')):continue
   path,_,anchor=raw.partition('#')
   q=(p.parent/path).resolve() if path else p
   if not q.exists():errors.append(f'{p.relative_to(base)} missing {raw}');continue
   if anchor and q.is_file() and q.suffix=='.md':
    text=q.read_text();anchors=set(re.findall(r'<a id="([^"]+)"',text))
    for heading in re.findall(r'^#{1,6}\s+(.+)$',text,re.M):
     clean=heading.strip().lower()
     clean=re.sub(r'[^\w\s-]','',clean,flags=re.U);clean=clean.replace(' ','-')
     anchors.add(clean)
    if anchor not in anchors:errors.append(f'{p.relative_to(base)} unknown anchor {raw}')
 return errors

def negative_tests(schema,known):
 demo=load(ROOT/'vi-du/phan-tich-gia-lap.json')
 assert not analysis_errors(demo,schema,known)
 mutations=[]
 def add(name,fn):
  d=copy.deepcopy(demo);fn(d);mutations.append((name,d))
 add('invalid time order',lambda d:d['shots'][0].update(end_seconds=-1))
 add('duplicate shot ID',lambda d:d['shots'][1].update(id=d['shots'][0]['id']))
 add('missing parent',lambda d:d['shots'][0].update(sequence_id='NOPE'))
 add('outside parent',lambda d:d['sequences'][0].update(end_seconds=11))
 add('overlapping shots',lambda d:d['shots'][1].update(start_seconds=2.5))
 add('invented evidence',lambda d:d['shots'][0]['observed']['summary'].update(evidence_refs=['NOPE']))
 add('null without reason',lambda d:d['shots'][0]['observed']['focus'].update(uncertainty_reason=None))
 add('whole coverage overclaim',lambda d:d['coverage'].update(whole_visual_reviewed=True))
 add('missing core reference',lambda d:d['shots'][0]['interpretations'][0].update(core_ids=['ZZ-999']))
 add('invented viewer effect',lambda d:d['shots'][0]['interpretations'][0].update(status='supported_viewer_report'))
 def still_motion(d):
  d['record_type']='analysis';d['shots'][0]['observed']['camera_motion'].update(status='observed',basis='direct_still')
 add('motion asserted from still',still_motion)
 def still_audio(d):
  d['record_type']='analysis';d['shots'][0]['observed']['audio_action'].update(status='observed',basis='direct_still')
 add('audio asserted from still',still_audio)
 results=[]
 for name,data in mutations:
  errs=analysis_errors(data,schema,known)
  if not errs:raise AssertionError('failed to reject '+name)
  results.append({'case':name,'rejected_as_expected':True,'reason':errs[0]})
 return results

def run(farm_root=None):
 schemas={p.name.split('.')[0]:load(p) for p in (ROOT/'schema').glob('*.json')}
 for s in schemas.values():Draft202012Validator.check_schema(s)
 cards=[load(p) for p in (ROOT/'kien-thuc').glob('*.json')];ids={x['id'] for x in cards}
 assert len(ids)==len(cards)
 sources=load(ROOT/'nguon/nguon-chinh-thuc.json')['sources'];sourceids={x['id'] for x in sources}
 audit=load(ROOT/'nguon/kiem-toan-33-bai.json');sourceids|={x['lesson_id'] for x in audit['lessons']}
 assert len(audit['lessons'])==33
 errors=[]
 for c in cards:
  errors+=json_errors(c,schemas['knowledge'])
  if any(x not in ids for x in c['related_ids']+c['prerequisite_ids']):errors.append('card references missing core')
  if any(x not in sourceids for x in c['source_ids']):errors.append('card references missing source')
  index=load(ROOT/'muc-luc.json')
  module=next(m for m in index['modules'] if m['id']==c['module_id'])
  view=(ROOT/module['path']).read_text()
  if c['principle'] not in view or c['original_example'] not in view:errors.append('stale markdown view '+c['id'])
 for s in sources:errors+=json_errors(s,schemas['source'])
 for m in load(ROOT/'mo-hinh/ho-so.json')['profiles']:errors+=json_errors(m,schemas['model'])
 for key in ['muc-luc.json','tuyen-tra-cuu.json','nhip-cam-xuc.json','kiem-thu/tinh-huong.json']:
  d=load(ROOT/key)
  items=d.get('items',d.get('routes',d.get('profiles',d.get('cases',[]))))
  for x in items:
   for i in x.get('core_ids',[]):
    if i not in ids:errors.append(key+' missing core '+i)
 for name in ['phan-tich-video']:
  errors+=analysis_errors(load(ROOT/'mau'/f'{name}.json'),schemas['analysis'],ids)
 for name in ['phan-tich-gia-lap']:
  errors+=analysis_errors(load(ROOT/'vi-du'/f'{name}.json'),schemas['analysis'],ids)
 for path,kind in [('mau/quyet-dinh.json','decision'),('vi-du/sua-loi-it-thay-doi.json','decision'),
  ('mau/kich-ban.json','script'),('mau/danh-sach-shot.json','shot-plan'),('mau/yeu-cau-tao.json','generation-request')]:
  errors+=json_errors(load(ROOT/path),schemas[kind])
 one_schema={'$schema':schemas['analysis']['$schema'],'$ref':'#/$defs/shot','$defs':schemas['analysis']['$defs']}
 errors+=json_errors(load(ROOT/'mau/mot-shot.json'),one_schema)
 for s in audit['lessons']:
  for i in s['core_ids']:
   if i not in ids:errors.append('audit missing core '+i)
 expected=load(ROOT/'manifest.json')
 if len(cards)!=expected['core_card_count']:errors.append('manifest card count')
 errors+=link_errors(ROOT.parent)
 farm_files=0
 if farm_root:
  farm_root=Path(farm_root)
  p=load(farm_root/'ho-so-ngach.json');errors+=json_errors(p,schemas['niche'])
  if p['core_dependency']['version']!=expected['version']:errors.append('farm version mismatch')
  for rule in p['rules']:
   if any(i not in ids for i in rule['core_ids']):errors.append('farm rule missing core')
  errors+=analysis_errors(load(farm_root/'vi-du-vid01-tu-bao-cao.json'),schemas['analysis'],ids)
  errors+=link_errors(farm_root);farm_files=sum(x.is_file() for x in farm_root.rglob('*'))
 negative=negative_tests(schemas['analysis'],ids)
 if errors:raise AssertionError(json.dumps(errors,ensure_ascii=False,indent=2))
 return {'core_cards':len(cards),'schemas_valid':len(schemas),'external_sources':len(sources),
  'legacy_lessons_mapped':33,'negative_fixture_tests':negative,'relative_links_valid':True,
  'farm_files_checked':farm_files,'generated_video_tests':0,'external_model_evaluations':0,
  'scope':'Schema, references, local links, timing/evidence contracts. Does not certify observation or artistic quality.'}
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--farm-root');parser.add_argument('--report')
 args=parser.parse_args();report=run(args.farm_root)
 if args.report:Path(args.report).write_text(json.dumps(report,ensure_ascii=False,indent=2)+chr(10))
 print(json.dumps(report,ensure_ascii=False,indent=2))
