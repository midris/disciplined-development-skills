import json,re,sys
from pathlib import Path
s=Path('/private/tmp/skilltest-cw-candidate.L4NdO8')
b=Path((s/'attempts'/sys.argv[1]/'command-stdout.txt').read_text().strip())
sources={str(p.relative_to(b/'workspace/fixture')):p.read_text().splitlines() for p in (b/'workspace/fixture/.agents').rglob('*') if p.is_file()}
for i,line in enumerate((b/'stdout.txt').read_text().splitlines()):
 e=json.loads(line); item=e.get('item',{}); out=item.get('aggregated_output','')
 if out:
  retained=[]; proved=[]
  for l in out.splitlines():
   m=re.match(r'(.+?)(?:-|:)(\d+)(?:-|:)(.*)$',l)
   mp=m[1].removeprefix('./') if m else None
   if m and mp in sources and 0<int(m[2])<=len(sources[mp]) and sources[mp][int(m[2])-1]==m[3]:
    proved.append((mp,int(m[2])));continue
   m=re.match(r'\s*(\d+)\t(.*)$',l)
   matches=[p for p,ls in sources.items() if m and 0<int(m[1])<=len(ls) and ls[int(m[1])-1]==m[2]]
   if matches: proved.append((matches,int(m[1])));continue
   retained.append(l)
  if proved:item['exact_source_numbered_lines']={'count':len(proved),'paths':sorted({p for ps,n in proved for p in (ps if isinstance(ps,list) else [ps])})}
  item['aggregated_output']='\n'.join(retained)
  for p,ls in sorted(sources.items(),key=lambda x:len('\n'.join(x[1])),reverse=True):
   body='\n'.join(ls)
   if body in item['aggregated_output']:item['aggregated_output']=item['aggregated_output'].replace(body,'<EXACT FULL FILE '+p+'>')
  for start,end,p in re.findall(r"sed -n '([0-9]+),([0-9]+)p' '?(\.agents/skills/[A-Za-z0-9_./-]+)",item.get('command','')):
   if p not in sources:continue
   body='\n'.join(sources[p][int(start)-1:int(end)])
   if body and body in item['aggregated_output']:item['aggregated_output']=item['aggregated_output'].replace(body,'<EXACT LINES '+start+'-'+str(min(int(end),len(sources[p])))+' '+p+'>')
 print(i,json.dumps(e,ensure_ascii=False))
