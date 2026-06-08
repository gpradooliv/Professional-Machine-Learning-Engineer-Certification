#!/usr/bin/env python3
from __future__ import annotations
import argparse, re
from pathlib import Path

BLOCKED = [re.compile(r'(^|/)\.env($|\.)', re.I), re.compile(r'credentials.*\.json$', re.I), re.compile(r'service[-_]?account.*\.json$', re.I), re.compile(r'.*\.(pem|key|p12|pfx)$', re.I)]
SECRETS = {'api_key': re.compile(r"(?i)(api[_-]?key|secret|token)\s*[:=]\s*['\"][^'\"]{12,}['\"]"), 'google_key': re.compile(r'AIza[0-9A-Za-z\-_]{30,}'), 'aws_key': re.compile(r'AKIA[0-9A-Z]{16}'), 'private_key': re.compile(r'-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----')}
SKIP = {'.git','.venv','venv','node_modules','__pycache__'}
TEXT = {'.py','.md','.txt','.json','.yaml','.yml','.toml','.ini','.cfg','.sh','.ps1','.sql','.js','.ts','.tsx','.jsx'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--repo-root',default='.'); args=ap.parse_args()
    root=Path(args.repo_root).resolve(); issues=[]
    for p in root.rglob('*'):
        if p.is_dir() or any(part in SKIP for part in p.parts): continue
        rel=p.relative_to(root).as_posix()
        if any(rx.search(rel) for rx in BLOCKED): issues.append(f'[arquivo bloqueado] {rel}')
        if p.suffix.lower() not in TEXT: continue
        text=p.read_text(encoding='utf-8',errors='ignore')
        for name,rx in SECRETS.items():
            if rx.search(text): issues.append(f'[possível segredo: {name}] {rel}')
    if issues:
        print('ATENÇÃO: revise antes de publicar:')
        for item in sorted(set(issues)): print(' -',item)
        raise SystemExit(1)
    print('Varredura básica concluída sem padrões evidentes de segredo.')
    print('Revise também histórico Git, datasets, notebooks, imagens e PI.')
if __name__=='__main__': main()
