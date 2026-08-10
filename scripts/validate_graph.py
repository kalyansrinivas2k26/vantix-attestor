from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[1]; WF=ROOT/'workflows'; errs=[]
expected={
'VANTIX-Attestor-Commitment-Assurance-v0.3-public.json':20,
'VANTIX-Attestor-Commitment-Assurance-Error-Handler-v0.3-public.json':3,
'VANTIX-Attestor-Service-Recovery-v0.2-public.json':20,
'VANTIX-Attestor-Customer-Momentum-v0.1-public.json':24,
'VANTIX-Attestor-Adversarial-Regression-Harness-v0.1-public.json':10,
}
for fn,count in expected.items():
    p=WF/fn
    if not p.exists(): errs.append('missing:'+fn); continue
    d=json.loads(p.read_text(encoding='utf-8')); names={n.get('name') for n in d.get('nodes',[])}
    if len(d.get('nodes',[]))!=count: errs.append(f'node_count:{fn}:{len(d.get("nodes",[]))}!={count}')
    for src,cfg in d.get('connections',{}).items():
        if src not in names: errs.append(f'unknown_source:{fn}:{src}')
        for group in cfg.get('main',[]):
            for edge in group:
                dst=edge.get('node')
                if dst not in names: errs.append(f'dangling:{fn}:{src}->{dst}')
                slow=src.lower(); dlow=str(dst).lower()
                ai=('ai ' in slow or slow.startswith('ai') or 'narrative' in slow or 'critique' in slow)
                consequential=any(x in dlow for x in ['execute permitted','close promise','execute action'])
                if ai and consequential: errs.append(f'ai_direct_consequential_edge:{fn}:{src}->{dst}')
p=WF/'VANTIX-Attestor-Commitment-Assurance-v0.3-public.json'
if p.exists():
    d=json.loads(p.read_text()); c=d.get('connections',{})
    def targets(name):
        out=[]
        for g in c.get(name,{}).get('main',[]): out += [e.get('node') for e in g]
        return out
    if '13 Execute Permitted Synthetic Actions' in targets('08 AI Diagnosis - Synthetic Structured Replay'): errs.append('CA_ai_diagnosis_bypass')
    if '13 Execute Permitted Synthetic Actions' in targets('09 AI Critique - Synthetic Structured Replay'): errs.append('CA_ai_critique_bypass')
    if '13 Execute Permitted Synthetic Actions' not in targets('12 Validate Human Approval Boundaries'): errs.append('CA_human_approval_to_execution_path_missing')
if errs:
    print('ATTESTOR GRAPH VALIDATION FAILED')
    for e in errs: print('-',e)
    sys.exit(1)
print('ATTESTOR GRAPH VALIDATION PASSED')
print('- node counts, dangling targets and AI/consequential invariants passed')
