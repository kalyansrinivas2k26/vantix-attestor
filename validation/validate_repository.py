from pathlib import Path
import json,re,hashlib,sys
ROOT=Path(__file__).resolve().parents[1]; errs=[]
required=['README.md','.gitignore','LICENSE','SECURITY.md','CONTRIBUTING.md','CHANGELOG.md','UPLOAD_READY.md','FINAL_HANDOFF.md','INDEPENDENT_REVIEW_PROMPT.md','.github/workflows/validate.yml','SHA256SUMS.txt','workflows/VANTIX-Attestor-Commitment-Assurance-v0.3-public.json','workflows/VANTIX-Attestor-Commitment-Assurance-Error-Handler-v0.3-public.json','workflows/VANTIX-Attestor-Service-Recovery-v0.2-public.json','workflows/VANTIX-Attestor-Customer-Momentum-v0.1-public.json','workflows/VANTIX-Attestor-Adversarial-Regression-Harness-v0.1-public.json','evidence/reports/commitment-assurance-synthetic.html','evidence/reports/service-recovery-synthetic.html','evidence/reports/customer-momentum-synthetic.html','evidence/reports/adversarial-regression-v0.1.html','evidence/screenshots/commitment-assurance-green.png','evidence/screenshots/service-recovery-green.png','evidence/screenshots/customer-momentum-green.png','evidence/screenshots/adversarial-regression-green.png','evidence/offline-exact-node-test-results.json','scripts/checksums.py','scripts/validate_graph.py','tests/offline_exact_node_tests.js','validation/NEGATIVE_TEST_EVIDENCE.md','docs/PLAIN_LANGUAGE_SUMMARY.md','docs/AUDIENCE_GUIDE.md','docs/EVIDENCE_PROVENANCE.md','docs/OWASP_AI_SECURITY_MAPPING.md','docs/PMI_AI_GOVERNANCE_MAPPING.md','docs/RELEASE_LINEAGE.md','docs/GITHUB_PRESENTATION_CHECKLIST.md','docs/FREEZE_GAP_MATRIX.md','docs/architecture.md','docs/executive-brief.md','docs/evidence-index.md','docs/quality-scorecard.md','docs/security-threat-model.md','docs/six-sigma-measurement.md','docs/test-catalogue.md','docs/demo-script.md','standards/VANTIX-EXECUTIVE-DOCUMENTATION-STANDARD-v1.0.md']
for rel in required:
    if not (ROOT/rel).exists(): errs.append('missing required:'+rel)
for pattern in ['FINAL_HANDOFF_v*.md','INDEPENDENT_REVIEW_PROMPT_v*.md','README-PROPOSED.md']:
    for p in ROOT.glob(pattern): errs.append('stale duplicate canonical:'+p.name)
for p in ROOT.rglob('*.json'):
    try: json.loads(p.read_text(encoding='utf-8'))
    except Exception as e: errs.append(f'json parse:{p.relative_to(ROOT)}:{e}')
readme=(ROOT/'README.md').read_text(encoding='utf-8')
if not readme.startswith('# VANTIX Attestor'): errs.append('root identity not VANTIX Attestor')
if 'Portfolio Preview v0.1.2' not in readme[:1400]: errs.append('README active release not v0.1.2')
if re.search(r'Portfolio Preview v0\.1(?:\.1)?\s+[—-]',readme): errs.append('stale pre-v0.1.2 active banner in README')
counts={'VANTIX-Attestor-Commitment-Assurance-v0.3-public.json':20,'VANTIX-Attestor-Commitment-Assurance-Error-Handler-v0.3-public.json':3,'VANTIX-Attestor-Service-Recovery-v0.2-public.json':20,'VANTIX-Attestor-Customer-Momentum-v0.1-public.json':24,'VANTIX-Attestor-Adversarial-Regression-Harness-v0.1-public.json':10}
for fn,n in counts.items():
    p=ROOT/'workflows'/fn
    if p.exists():
        d=json.loads(p.read_text()); got=len(d.get('nodes',[]))
        if got!=n: errs.append(f'workflow node count:{fn}:{got}!={n}')
        if d.get('active') is True: errs.append('public workflow active:'+fn)
ids=['CA-N01','CA-N02','CA-N03','CA-N04','SR-N01','SR-N02','SR-N03','SR-N04','CM-N01','CM-N02','CM-N03','SEC-01','SEC-02','SEC-03','SEC-04','XMOD-01','XMOD-02','XMOD-03']
hp=ROOT/'workflows/VANTIX-Attestor-Adversarial-Regression-Harness-v0.1-public.json'; rp=ROOT/'evidence/reports/adversarial-regression-v0.1.html'
if hp.exists():
    ht=hp.read_text()
    for x in ids:
        if x not in ht: errs.append('harness missing id:'+x)
if rp.exists():
    rt=rp.read_text()
    if 'Passed: 18/18' not in rt or 'Status: <b>PASSED</b>' not in rt: errs.append('adversarial report not 18/18 PASSED')
    for x in ids:
        if x not in rt: errs.append('report missing id:'+x)
    if 'No live Salesforce, model-provider, or customer action occurred.' not in rt: errs.append('adversarial report live-boundary missing')
op=ROOT/'evidence/offline-exact-node-test-results.json'
if op.exists() and hp.exists():
    ev=json.loads(op.read_text()); sha=hashlib.sha256(hp.read_bytes()).hexdigest()
    if ev.get('workflowSha256')!=sha: errs.append('offline evidence workflow hash mismatch')
    if ev.get('evidenceClass')!='OFFLINE_EXACT_NODE_CODE_EXECUTION' or ev.get('n8nRuntimeExecution') is not False: errs.append('offline evidence classification invalid')
    if ev.get('testCount')!=5 or ev.get('passCount')!=5 or ev.get('failCount')!=0: errs.append('offline exact-node tests not 5/5')
secret_pats=[re.compile(r'AIza[0-9A-Za-z_-]{20,}'),re.compile(r'sk-[0-9A-Za-z]{20,}'),re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),re.compile(r'''(?:api[_-]?key|access[_-]?token|client[_-]?secret)\s*[:=]\s*["'][A-Za-z0-9_-]{16,}''',re.I)]
for p in ROOT.rglob('*'):
    if not p.is_file() or p.name=='SHA256SUMS.txt' or '__pycache__' in p.parts: continue
    if p.suffix.lower() not in {'.md','.json','.py','.js','.mjs','.yml','.yaml','.html','.txt','.sh','.env'}: continue
    txt=p.read_text(encoding='utf-8',errors='ignore')
    if any(q.search(txt) for q in secret_pats): errs.append('possible secret:'+p.relative_to(ROOT).as_posix())
link_re=re.compile(r'(?<!!)\[[^\]]+\]\(([^)]+)\)')
def slug(h):
    s=re.sub(r'<[^>]+>','',h.strip().lower()); s=re.sub(r'[^\w\s-]','',s); return re.sub(r'\s+','-',s)
anchors={}
for p in ROOT.rglob('*.md'):
    txt=p.read_text(encoding='utf-8',errors='ignore'); anchors[p.resolve()]={slug(m.group(1)) for m in re.finditer(r'^#{1,6}\s+(.+?)\s*$',txt,re.M)}
for p in ROOT.rglob('*.md'):
    txt=p.read_text(encoding='utf-8',errors='ignore')
    for target in link_re.findall(txt):
        target=target.strip().split()[0].strip('<>')
        if target.startswith(('http://','https://','mailto:')): continue
        if target.startswith('#'):
            if target[1:].lower() not in anchors[p.resolve()]: errs.append(f'broken anchor:{p.relative_to(ROOT)}->{target}')
            continue
        pathpart,_,anchor=target.partition('#'); q=(p.parent/pathpart).resolve()
        try:q.relative_to(ROOT.resolve())
        except ValueError: errs.append(f'link escapes repo:{p.relative_to(ROOT)}->{target}'); continue
        if not q.exists(): errs.append(f'broken link:{p.relative_to(ROOT)}->{target}'); continue
        if anchor and q.suffix.lower()=='.md' and anchor.lower() not in anchors.get(q,set()): errs.append(f'broken cross anchor:{p.relative_to(ROOT)}->{target}')
sp=ROOT/'docs/quality-scorecard.md'
if sp.exists():
    t=sp.read_text(); rows=re.findall(r'^\| [^|*][^|]* \| (\d+) \| (\d+) \|',t,re.M); weights=sum(int(a) for a,b in rows); score=sum(int(b) for a,b in rows)
    if weights!=100: errs.append(f'score weights={weights}')
    if score!=96: errs.append(f'canonical score={score}, expected 96')
    m=re.search(r'\| \*\*Total\*\* \| \*\*(\d+)\*\* \| \*\*(\d+)\*\*',t)
    if not m: errs.append('score total row missing')
    elif int(m.group(1))!=weights or int(m.group(2))!=score: errs.append(f'score total mismatch:{m.groups()} vs {weights}/{score}')
for p in set(list(ROOT.rglob('*.md'))+[ROOT/'README.md']):
    if not p.exists(): continue
    rel=p.relative_to(ROOT).as_posix()
    if rel.startswith('standards/'): continue
    txt=p.read_text(encoding='utf-8',errors='ignore').lower()
    for banned in ['mckinsey-standard','mckinsey-style','independent audit','no competitor does this','production-ready']:
        if banned in txt: errs.append(f'banned wording:{rel}:{banned}')
if errs:
    print('ATTESTOR REPOSITORY VALIDATION FAILED')
    for e in errs: print('-',e)
    sys.exit(1)
print('ATTESTOR REPOSITORY VALIDATION PASSED')
print('- required artifacts, identity/version, JSON and workflow counts passed')
print('- 18/18 adversarial evidence and offline hash binding passed')
print('- secrets, Markdown links/anchors, score arithmetic and wording passed')
