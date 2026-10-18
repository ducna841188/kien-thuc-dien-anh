"""Validate FILM-KB structure and evidence contracts. Does not assess video content."""
from pathlib import Path
import json,sys,re,hashlib,math,argparse,copy,unicodedata
from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parents[1]
def load(p):return json.loads(Path(p).read_text())
def json_errors(data,schema):
 return [f"{'/'.join(map(str,e.absolute_path))}: {e.message}" for e in Draft202012Validator(schema).iter_errors(data)]
def knowledge_errors(card,schema,known_ids,source_ids):
 errors=json_errors(card,schema)
 if errors:return errors
 if any(i not in known_ids for i in card['related_ids']+card['prerequisite_ids']):errors.append('card references missing core')
 if any(i not in source_ids for i in card['source_ids']):errors.append('card references missing source')
 for e in card.get('application_depth',{}).get('evidence_links',[]):
  if e['source_id'] not in source_ids or e['source_id'] not in card['source_ids']:errors.append('scoped claim source is not attached to card')
 return errors

def decision_errors(data,schema,cards,current_version):
 errors=json_errors(data,schema)
 if errors:return errors
 if data['core_version']!=current_version:errors.append('working example/template core version is stale')
 option_ids=[x['id'] for x in data['options']]
 if len(option_ids)!=len(set(option_ids)):errors.append('duplicate decision option ID')
 if data['selected_option_id'] is not None and data['selected_option_id'] not in option_ids:errors.append('selected decision option is missing')
 for ref in data['knowledge_refs']:
  if ref['id'] not in cards:errors.append('decision references missing core '+ref['id'])
  elif ref['version']!=cards[ref['id']]['version']:errors.append('decision knowledge version is stale '+ref['id'])
 return errors

def current_dependency_errors(dependency,current_version):
 errors=[]
 if dependency.get('repository')!='ducna841188/kien-thuc-dien-anh':errors.append('working core repository mismatch')
 if dependency['version']!=current_version:errors.append('niche dependency needs current core version review')
 if dependency['commit'] is not None:errors.append('working core dependency must follow main')
 if dependency['manifest_url']!='https://github.com/ducna841188/kien-thuc-dien-anh/blob/main/thu-vien/manifest.json':errors.append('working manifest URL must follow main')
 return errors

def current_layout_errors(paths,expected_logs=('CHANGELOG.md',)):
 errors=[]
 for path in paths:
  if re.search(r'(?:^|/)(?:(?:CORE|SOURCES)_\d|manifest-goi-\d|ket-qua-\d|ra-soat-\d|RA_SOAT_\d)',path):errors.append('versioned active copy '+path)
  if any(part.lower() in ('archive','archives','luu-tru') for part in Path(path).parts):errors.append('active archive folder '+path)
 logs={p for p in paths if Path(p).name=='CHANGELOG.md'}
 if logs!=set(expected_logs):errors.append('change log must be centralized')
 return errors
def spans_cover(spans,duration):
 if duration is None:return False
 point=0.0
 for s in sorted(spans,key=lambda x:x['start_seconds']):
  if s['start_seconds']>point+1e-6:return False
  point=max(point,s['end_seconds'])
 return point>=duration-1e-6

def point_inside(time,span):
 return span['start_seconds']<=time<span['end_seconds']

def interval_covered(start,end,spans):
 if start==end:return any(point_inside(start,s) or s['start_seconds']==s['end_seconds']==start for s in spans)
 point=start
 for s in sorted(spans,key=lambda x:x['start_seconds']):
  if s['end_seconds']<=point:continue
  if s['start_seconds']>point+1e-6:return False
  point=max(point,s['end_seconds'])
  if point>=end-1e-6:return True
 return False

def intervals_overlap(e,span):
 if e['start_seconds'] is None or e['end_seconds'] is None:return True
 if e['start_seconds']==e['end_seconds']:return point_inside(e['start_seconds'],span)
 return e['start_seconds']<span['end_seconds'] and e['end_seconds']>span['start_seconds']
def analysis_errors(data,schema=None,known_core=None):
 schema=schema or load(ROOT/'schema/analysis.schema.json')
 errs=json_errors(data,schema)
 if errs:return errs
 def bad(s):errs.append(s)
 duration=data['duration_seconds']
 for name,value in [('duration',duration),('fps',data['fps']),('offset',data['time_origin']['local_offset_seconds'])]:
  if value is not None and not math.isfinite(value):bad(name+' non-finite value')
 assetids=[x['id'] for x in data['assets']]
 evids=[x['id'] for x in data['evidence_records']]
 segids=[x['id'] for x in data['segments']]
 seqids=[x['id'] for x in data['sequences']]
 shotids=[x['id'] for x in data['shots']]
 eventids=[x['id'] for s in data['shots'] for x in s['events']]
 viewerids=[x['id'] for x in data['viewer_evidence']]
 for label,ids in [('asset',assetids),('evidence',evids),('viewer',viewerids),('segment',segids),('sequence',seqids),('shot',shotids),('event',eventids)]:
  if len(ids)!=len(set(ids)):bad('duplicate '+label+' ID')
 if set(evids)&set(viewerids):bad('viewer and media evidence ID collision')
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
  if not math.isfinite(t):bad('non-finite sample frame time')
  if duration is not None and t>=duration:bad('sample frame outside half-open duration')
 if data['coverage']['whole_visual_reviewed'] and not spans_cover(data['coverage']['visual_motion_intervals'],duration):bad('whole visual flag exceeds coverage')
 if data['coverage']['whole_audio_reviewed'] and data['coverage']['audio_presence']!='absent' and not spans_cover(data['coverage']['audio_intervals'],duration):bad('whole audio flag exceeds coverage')
 if data['coverage']['audio_presence']=='absent' and data['coverage']['audio_intervals']:bad('audio coverage contradicts absent audio')
 segs={s['id']:s for s in data['segments']};seqs={s['id']:s for s in data['sequences']}
 def within(x,parent,label):
  if x['start_seconds']<parent['start_seconds']-1e-6 or x['end_seconds']>parent['end_seconds']+1e-6:bad(label+' outside parent')
  if x['start_seconds']==x['end_seconds'] and not point_inside(x['start_seconds'],parent):bad(label+' point outside half-open parent')
 for s in data['sequences']:
  if s['segment_id'] not in segs:bad('missing segment parent')
  else:within(s,segs[s['segment_id']],'sequence')
 assets={a['id']:a for a in data['assets']}
 for e in data['evidence_records']:
  if e['asset_id'] not in assetids:bad('evidence missing asset')
  if (e['start_seconds'] is None)!=(e['end_seconds'] is None):bad('evidence has incomplete time span')
  if e['start_seconds'] is not None and e['end_seconds'] is not None:check_span(e,'evidence',True)
  if data['record_type']=='synthetic_example' and e['kind']!='synthetic':bad('synthetic record has non-synthetic evidence')
  if e['kind'] in ('motion_interval','audio_interval'):
   allowed=('video',) if e['kind']=='motion_interval' else ('video','audio')
   if assets.get(e['asset_id'],{}).get('kind') not in allowed:bad(e['kind']+' has incompatible asset kind')
   if e['start_seconds'] is None or e['end_seconds'] is None:bad('direct interval needs timestamps')
   else:
    check_span(e,'direct interval')
    spans=data['coverage']['visual_motion_intervals' if e['kind']=='motion_interval' else 'audio_intervals']
    if not interval_covered(e['start_seconds'],e['end_seconds'],spans):bad('direct evidence exceeds reviewed coverage')
  if e['kind']=='still_frame':
   if assets.get(e['asset_id'],{}).get('kind') not in ('video','image'):bad('still frame has incompatible asset kind')
   if e['start_seconds'] is not None and e['end_seconds'] is not None:
    if e['start_seconds']!=e['end_seconds']:bad('still frame evidence must be a point')
    elif not (any(abs(e['start_seconds']-t)<1e-6 for t in data['coverage']['sampled_frame_times']) or interval_covered(e['start_seconds'],e['end_seconds'],data['coverage']['visual_motion_intervals'])):bad('still frame exceeds reviewed coverage')
 for viewer in data['viewer_evidence']:
  if viewer['time_range'] is not None:check_span(viewer['time_range'],'viewer evidence')
 viewerids=set(viewerids);evidence={e['id']:e for e in data['evidence_records']}
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
 def basis_ok(basis,refs,label,span=None,complete=False):
  required={'direct_motion':'motion_interval','direct_still':'still_frame','direct_audio':'audio_interval','source_report':'source_report','synthetic':'synthetic'}.get(basis)
  candidates=[evidence[r] for r in refs if r in evidence and evidence[r]['kind']==required]
  if required and not candidates:bad(label+' lacks evidence matching basis')
  if basis.startswith('direct_') and span is not None:
   if candidates and not any(intervals_overlap(e,span) for e in candidates):bad(label+' evidence belongs to another time interval')
   if complete:
    spans=[e for e in candidates if e['start_seconds'] is not None and e['end_seconds'] is not None]
    if not interval_covered(span['start_seconds'],span['end_seconds'],spans):bad(label+' event exceeds its cited evidence')
 for s in data['shots']:
  if s['sequence_id'] not in seqs:bad('missing sequence parent')
  else:within(s,seqs[s['sequence_id']],'shot')
  for field,v in s['observed'].items():
   refs_ok(v['evidence_refs'],field)
   if v['status']!='unknown':basis_ok(v['basis'],v['evidence_refs'],field,s)
   if v['status']=='observed':
    if field.startswith('audio_') and v['basis']!='direct_audio':bad(field+' observed without audio')
    if not field.startswith('audio_') and v['basis']=='direct_audio':bad(field+' visual observation uses audio only')
    if field in ['camera_motion','time_treatment'] and v['basis']!='direct_motion':bad(field+' observed without motion')
   if field=='subject_count' and v['value'] is not None and (isinstance(v['value'],bool) or not isinstance(v['value'],int) or v['value']<0):bad('subject count must be nonnegative integer or null')
   if data['record_type']=='synthetic_example' and v['status'] not in ['synthetic','unknown']:bad('synthetic example claims non-synthetic observation')
   if v['status']=='observed' and v['basis']=='direct_motion' and not any(e['kind']=='motion_interval' and e['id'] in v['evidence_refs'] for e in data['evidence_records']):bad(field+' lacks motion evidence record')
   if v['status']=='observed' and v['basis']=='direct_audio' and not any(e['kind']=='audio_interval' and e['id'] in v['evidence_refs'] for e in data['evidence_records']):bad(field+' lacks audio evidence record')
  for event in s['events']:
   check_span(event,'event',True);within(event,s,'event');refs_ok(event['evidence_refs'],'event')
   basis_ok(event['basis'],event['evidence_refs'],'event',event,complete=True)
   if event['basis'].startswith('direct_'):
    if event['channel']=='audio' and event['basis']!='direct_audio':bad('audio event lacks direct audio basis')
    if event['channel']=='visual' and event['basis']=='direct_audio':bad('visual event uses audio only')
    if event['channel']=='both':
     for kinds in [('motion_interval','still_frame'),('audio_interval',)]:
      spans=[evidence[r] for r in event['evidence_refs'] if r in evidence and evidence[r]['kind'] in kinds and evidence[r]['start_seconds'] is not None and evidence[r]['end_seconds'] is not None]
      if not interval_covered(event['start_seconds'],event['end_seconds'],spans):bad('audiovisual event needs both evidence channels')
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

def scoped_evidence_tests(schema,known):
 """Mock metadata only: no video, audio or viewer research is performed."""
 seed=copy.deepcopy(load(ROOT/'vi-du/phan-tich-gia-lap.json'))
 seed['record_type']='analysis';seed['assets'][0].update(kind='video',title='Mock fixture; no real footage reviewed')
 seed['evidence_records'][0].update(kind='motion_interval',start_seconds=0,end_seconds=1)
 seed['coverage']['visual_motion_intervals']=[{'start_seconds':0,'end_seconds':1}]
 for shot in seed['shots']:
  for value in shot['observed'].values():value.update(value=None,status='unknown',basis='unknown',evidence_refs=[],uncertainty_reason='Mock fixture has no input for this field')
  shot['interpretations']=[];shot['events']=[]
 seed['shots'][0]['observed']['summary'].update(value='Mock visible feature within reviewed interval',status='observed',basis='direct_motion',evidence_refs=['SYN-E1'],uncertainty_reason=None)
 positive=[('partial motion interval',seed)]
 still=copy.deepcopy(seed);still['assets'][0]['kind']='image'
 still['evidence_records'][0].update(kind='still_frame',start_seconds=0.5,end_seconds=0.5)
 still['coverage'].update(visual_motion_intervals=[],sampled_frame_times=[0.5])
 still['shots'][0]['observed']['summary']['basis']='direct_still';positive.append(('sampled image feature',still))
 audio=copy.deepcopy(seed);audio['assets'][0]['kind']='audio'
 audio['evidence_records'][0].update(kind='audio_interval')
 audio['coverage'].update(visual_motion_intervals=[],audio_intervals=[{'start_seconds':0,'end_seconds':1}],audio_presence='present')
 audio['shots'][0]['observed']['summary'].update(value=None,status='unknown',basis='unknown',evidence_refs=[],uncertainty_reason='Audio-only fixture')
 audio['shots'][0]['observed']['audio_action'].update(value='Mock audible click',status='observed',basis='direct_audio',evidence_refs=['SYN-E1'],uncertainty_reason=None)
 positive.append(('separate audio asset',audio))
 broad=copy.deepcopy(seed);broad['evidence_records'][0]['end_seconds']=12;broad['coverage']['visual_motion_intervals'][0]['end_seconds']=12
 positive.append(('broad evidence may cover multiple shots',broad))
 results=[]
 for name,data in positive:
  errors=analysis_errors(data,schema,known)
  if errors:raise AssertionError('valid scoped fixture rejected '+name+': '+str(errors))
  results.append({'case':name,'valid_fixture_accepted':True})
 negative=[]
 def add(name,edit,base=None):
  data=copy.deepcopy(base if base is not None else seed);edit(data);negative.append((name,data))
 add('evidence exceeds declared coverage',lambda d:d['evidence_records'][0].update(end_seconds=3))
 add('observation cites another shot',lambda d:(d['evidence_records'][0].update(start_seconds=6,end_seconds=7),d['coverage'].update(visual_motion_intervals=[{'start_seconds':6,'end_seconds':7}])))
 add('incomplete direct evidence timestamps',lambda d:d['evidence_records'][0].update(start_seconds=None))
 add('motion interval backed by image',lambda d:d['assets'][0].update(kind='image'))
 add('still basis cites no still frame',lambda d:d['shots'][0]['observed']['summary'].update(basis='direct_still'))
 event={'id':'MOCK-EVENT','start_seconds':2,'end_seconds':2.5,'channel':'visual','description':'Mock event only','basis':'direct_motion','evidence_refs':['SYN-E1'],'state_before':None,'state_after':None}
 add('event exceeds cited interval',lambda d:d['shots'][0]['events'].append(copy.deepcopy(event)))
 add('event point at excluded shot end',lambda d:d['shots'][0]['events'].append(event|{'start_seconds':3,'end_seconds':3}))
 add('audio coverage with absent audio',lambda d:d['coverage'].update(audio_presence='absent'),audio)
 viewer={'id':'MOCK-VIEWER','method':'Mock unit-test record','sample_description':'No real viewers','time_range':None,'finding':'Mock finding','limits':'Unit-test fixture only','supports_causal_claim':False}
 add('duplicate viewer evidence IDs',lambda d:d['viewer_evidence'].extend([copy.deepcopy(viewer),copy.deepcopy(viewer)]))
 add('viewer range reversed',lambda d:d['viewer_evidence'].append(viewer|{'time_range':{'start_seconds':3,'end_seconds':2}}))
 add('frame at excluded duration end',lambda d:d['coverage']['sampled_frame_times'].append(12))
 add('non-finite frame timestamp',lambda d:d['coverage']['sampled_frame_times'].append(float('nan')))
 for name,data in negative:
  errors=analysis_errors(data,schema,known)
  if not errors:raise AssertionError('invalid scoped fixture accepted '+name)
  results.append({'case':name,'invalid_fixture_rejected':True,'reason':errors[0]})
 return results

def run(farm_root=None):
 schemas={p.name.split('.')[0]:load(p) for p in (ROOT/'schema').glob('*.json')}
 for s in schemas.values():Draft202012Validator.check_schema(s)
 card_paths=list((ROOT/'kien-thuc').glob('*.json'))
 cards=[load(p) for p in card_paths];ids={x['id'] for x in cards};cardmap={c['id']:c for c in cards}
 assert len(ids)==len(cards)
 sources=load(ROOT/'nguon/nguon-chinh-thuc.json')['sources'];sourceids={x['id'] for x in sources}
 assert len(sourceids)==len(sources),'duplicate source ID'
 audit=load(ROOT/'nguon/kiem-toan-33-bai.json');sourceids|={x['lesson_id'] for x in audit['lessons']}
 assert len(audit['lessons'])==33
 errors=[]
 expected=load(ROOT/'manifest.json');index=load(ROOT/'muc-luc.json')
 terms=load(ROOT/'tu-dien-thuat-ngu.json')['terms']
 termkeys=[unicodedata.normalize('NFC',t['term']).strip().casefold() for t in terms]
 if len(termkeys)!=len(set(termkeys)):errors.append('duplicate glossary term')
 if len(terms)!=expected['glossary_term_count']:errors.append('manifest glossary count')
 if sum('application_depth' in c for c in cards)!=expected['application_depth_card_count']:errors.append('manifest application depth count')
 cases=load(ROOT/'kiem-thu/tinh-huong.json')['cases']
 if len(cases)!=expected['ai_evaluation_case_count'] or len({c['id'] for c in cases})!=len(cases):errors.append('AI evaluation case inventory mismatch')
 design=load(ROOT/'vi-du/bon-ca-ra-quyet-dinh.json')['cases'][0]['scene_design']
 design_view=(ROOT/'vi-du/bon-ca-ra-quyet-dinh.md').read_text()
 if not all(v in design_view for v in design.values()):errors.append('stale integrated scene design view')
 if index['version']!=expected['version']:errors.append('catalog release version is stale')
 if len(index['items'])!=len(cards) or {x['id'] for x in index['items']}!=ids:errors.append('catalog does not map canonical cards exactly once')
 modules={m['id']:m for m in index['modules']}
 for path,c in zip(card_paths,cards):
  if path.stem!=c['id']:errors.append('canonical filename differs from ID')
 for item in index['items']:
  if item['id'] not in cardmap:continue
  c=cardmap[item['id']]
  if any(item[k]!=c[k] for k in ['title','version','module_id','level','decision_question','related_ids','source_ids']):errors.append('stale catalog metadata '+c['id'])
  if item['json_path']!=f"kien-thuc/{c['id']}.json" or item['markdown_path']!=modules[c['module_id']]['path']+'#'+c['id'].lower():errors.append('stale catalog path '+c['id'])
 for c in cards:
  errors+=knowledge_errors(c,schemas['knowledge'],ids,sourceids)
  module=next(m for m in index['modules'] if m['id']==c['module_id'])
  view=(ROOT/module['path']).read_text()
  if c['principle'] not in view or c['original_example'] not in view:errors.append('stale markdown view '+c['id'])
  if 'application_depth' in c and c['application_depth']['worked_example']['selection_rule'] not in view:errors.append('stale application depth '+c['id'])
 for s in sources:errors+=json_errors(s,schemas['source'])
 for m in load(ROOT/'mo-hinh/ho-so.json')['profiles']:errors+=json_errors(m,schemas['model'])
 for key in ['muc-luc.json','tuyen-tra-cuu.json','nhip-cam-xuc.json','kiem-thu/tinh-huong.json','vi-du/bon-ca-ra-quyet-dinh.json','tu-dien-thuat-ngu.json','quy-trinh/tasks.json']:
  d=load(ROOT/key)
  items=d.get('items',d.get('routes',d.get('profiles',d.get('cases',d.get('terms',d.get('tasks',[]))))))
  for x in items:
   for i in x.get('core_ids',[]):
    if i not in ids:errors.append(key+' missing core '+i)
 for name in ['phan-tich-video']:
  errors+=analysis_errors(load(ROOT/'mau'/f'{name}.json'),schemas['analysis'],ids)
 for name in ['phan-tich-gia-lap']:
  errors+=analysis_errors(load(ROOT/'vi-du'/f'{name}.json'),schemas['analysis'],ids)
 for path,kind in [('mau/quyet-dinh.json','decision'),('vi-du/sua-loi-it-thay-doi.json','decision'),
  ('mau/kich-ban.json','script'),('mau/danh-sach-shot.json','shot-plan'),('mau/yeu-cau-tao.json','generation-request')]:
  data=load(ROOT/path)
  errors+=decision_errors(data,schemas[kind],cardmap,expected['version']) if kind=='decision' else json_errors(data,schemas[kind])
  if data['core_version']!=expected['version']:errors.append('stale working example/template '+path)
 one_schema={'$schema':schemas['analysis']['$schema'],'$ref':'#/$defs/shot','$defs':schemas['analysis']['$defs']}
 errors+=json_errors(load(ROOT/'mau/mot-shot.json'),one_schema)
 for s in audit['lessons']:
  for i in s['core_ids']:
   if i not in ids:errors.append('audit missing core '+i)
 if len(cards)!=expected['core_card_count']:errors.append('manifest card count')
 if len(sources)!=expected['official_reference_count']:errors.append('manifest reference count')
 latest=ROOT/'goi-doc/CORE.jsonl'
 if [json.loads(x) for x in latest.read_text().splitlines() if x.strip()]!=sorted(cards,key=lambda c:c['id']):errors.append('exported JSONL differs from canonical cards')
 pack=load(ROOT/'goi-doc/manifest-goi.json')
 if pack['version']!=expected['version'] or pack['storage_mode']!='in_place_latest':errors.append('package current version/policy mismatch')
 if {x['path'] for x in pack['files']}!={'CORE.md','CORE.jsonl','SOURCES.json','CORE_NGAN.md','START_HERE.md'}:errors.append('package paths must be stable')
 if load(ROOT/'goi-doc/SOURCES.json')!=load(ROOT/'nguon/nguon-chinh-thuc.json'):errors.append('exported sources differ from canonical registry')
 for entry in pack['files']:
  b=(ROOT/'goi-doc'/entry['path']).read_bytes()
  if len(b)!=entry['bytes'] or hashlib.sha256(b).hexdigest()!=entry['sha256']:errors.append('package manifest mismatch '+entry['path'])
 errors+=link_errors(ROOT.parent)
 active_paths=[p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts]
 errors+=current_layout_errors(active_paths)
 farm_files=0
 farm_version=None
 if farm_root:
  farm_root=Path(farm_root)
  p=load(farm_root/'ho-so-ngach.json');errors+=json_errors(p,schemas['niche'])
  errors+=current_dependency_errors(p['core_dependency'],expected['version'])
  farm_ids,farm_version=ids,p['core_dependency']['version']
  for rule in p['rules']:
   if any(i not in farm_ids for i in rule['core_ids']):errors.append('farm rule missing current core')
  errors+=analysis_errors(load(farm_root/'vi-du-vid01-tu-bao-cao.json'),schemas['analysis'],farm_ids)
  errors+=link_errors(farm_root);farm_files=sum(x.is_file() for x in farm_root.rglob('*'))
  errors+=current_layout_errors([x.relative_to(farm_root).as_posix() for x in farm_root.rglob('*') if x.is_file()],expected_logs=())
 negative=negative_tests(schemas['analysis'],ids)
 scoped=scoped_evidence_tests(schemas['analysis'],ids)
 sample=next(c for c in cards if c.get('application_depth',{}).get('evidence_links'))
 bad_depth=copy.deepcopy(sample);bad_depth['application_depth']['worked_example'].pop('protected_elements')
 bad_source=copy.deepcopy(sample);bad_source['application_depth']['evidence_links'][0]['source_id']='MISSING-SOURCE'
 bad_test=copy.deepcopy(sample);bad_test['application_depth']['failure_diagnosis'][0]['next_test']=''
 contract_tests=[
  {'case':'missing protected elements rejected','passed':bool(knowledge_errors(bad_depth,schemas['knowledge'],ids,sourceids))},
  {'case':'unattached scoped claim source rejected','passed':bool(knowledge_errors(bad_source,schemas['knowledge'],ids,sourceids))},
  {'case':'empty diagnostic next test rejected','passed':bool(knowledge_errors(bad_test,schemas['knowledge'],ids,sourceids))},
  {'case':'versioned active copy rejected','passed':bool(current_layout_errors(['CHANGELOG.md','goi-doc/CORE_1_2_0.jsonl']))},
  {'case':'separate niche change log rejected','passed':bool(current_layout_errors(['CHANGELOG.md','farm/CHANGELOG.md']))},
  {'case':'old working dependency rejected','passed':bool(current_dependency_errors({'version':'old','commit':'old','manifest_url':'old'},expected['version']))}]
 decision=load(ROOT/'vi-du/sua-loi-it-thay-doi.json')
 bad_option=copy.deepcopy(decision);bad_option['selected_option_id']='MISSING-OPTION'
 bad_ref=copy.deepcopy(decision);bad_ref['knowledge_refs'][0]['version']='old-version'
 contract_tests.extend([
  {'case':'missing selected decision option rejected','passed':bool(decision_errors(bad_option,schemas['decision'],cardmap,expected['version']))},
  {'case':'stale decision knowledge version rejected','passed':bool(decision_errors(bad_ref,schemas['decision'],cardmap,expected['version']))}])
 if not all(t['passed'] for t in contract_tests):errors.append('knowledge contract test failed')
 if errors:raise AssertionError(json.dumps(errors,ensure_ascii=False,indent=2))
 return {'core_cards':len(cards),'schemas_valid':len(schemas),'external_sources':len(sources),
  'legacy_lessons_mapped':33,'negative_fixture_tests':negative,'relative_links_valid':True,
  'version':expected['version'],'storage_mode':'in_place_latest','farm_files_checked':farm_files,'farm_current_core_version_checked':farm_version,
  'single_current_copy_policy_valid':True,'knowledge_contract_tests':contract_tests,'scoped_evidence_fixture_tests':scoped,
  'catalog_matches_canonical':True,'current_decision_references_valid':True,
  'integrated_scene_design_matches':True,'inventory_counts_valid':True,
  'package_checksums_valid':True,'canonical_jsonl_matches':True,
  'generated_video_tests':0,'external_model_evaluations':0,
  'scope':'Schema, references, local links, timing/evidence contracts. Does not certify observation or artistic quality.'}
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--farm-root');parser.add_argument('--report')
 args=parser.parse_args();report=run(args.farm_root)
 if args.report:Path(args.report).write_text(json.dumps(report,ensure_ascii=False,indent=2)+chr(10))
 print(json.dumps(report,ensure_ascii=False,indent=2))
