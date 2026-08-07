from pathlib import Path
import hashlib, sys
root=Path(__file__).resolve().parents[1]
ledger=root/'SHA256SUMS.txt'
entries={}
for line in ledger.read_text().splitlines():
    if not line.strip(): continue
    h, path=line.split('  ./',1)
    entries[path]=h
actual={}
for p in root.rglob('*'):
    if not p.is_file(): continue
    rel=p.relative_to(root).as_posix()
    if rel in {'SHA256SUMS.txt'} or rel.startswith('.git/'): continue
    actual[rel]=hashlib.sha256(p.read_bytes()).hexdigest()
fail=[]
for rel,h in actual.items():
    if rel not in entries: fail.append(f'File omitted from ledger: {rel}')
    elif entries[rel]!=h: fail.append(f'Hash mismatch: {rel}')
for rel in entries:
    if rel not in actual: fail.append(f'Missing file: {rel}')
print({'status':'PASS' if not fail else 'FAILED','expectedFiles':len(actual),'ledgerEntries':len(entries),'failures':fail})
sys.exit(1 if fail else 0)
