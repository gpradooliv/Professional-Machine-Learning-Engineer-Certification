#!/usr/bin/env python3
from __future__ import annotations
import argparse, shutil
from pathlib import Path

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('project_name'); ap.add_argument('--target-dir',default='generated-projects'); args=ap.parse_args()
    src=Path(__file__).resolve().parents[1]/'templates'/'project-template'
    dst=Path(args.target_dir).resolve()/args.project_name
    if dst.exists(): raise SystemExit(f'Diretório já existe: {dst}')
    shutil.copytree(src,dst)
    package=args.project_name.replace('-','_')
    for p in dst.rglob('*'):
        if p.is_file():
            try: txt=p.read_text(encoding='utf-8')
            except UnicodeDecodeError: continue
            p.write_text(txt.replace('{{PROJECT_NAME}}',args.project_name).replace('{{PACKAGE_NAME}}',package),encoding='utf-8')
    old=dst/'src'/'PACKAGE_NAME'
    if old.exists(): old.rename(dst/'src'/package)
    print('Projeto criado em:',dst)
    print('Execute: git init && git add . && git commit -m "chore: initialize project scaffold"')
if __name__=='__main__': main()
