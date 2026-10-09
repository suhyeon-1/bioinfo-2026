#!/usr/bin/env python3
# mkproject.py - 입력받은 이름의 프로젝트 폴더 구조를 생성한다
# 사용법: python3 src/mkproject.py <프로젝트이름>

import sys
import os

# 1. 인자가 입력되지 않은 경우 검사
if len(sys.argv) < 2:
    print(f"사용법: python3 {sys.argv[0]} <프로젝트이름>")
    sys.exit(1)

project_name = sys.argv[1]

# 2. 같은 이름의 폴더가 이미 존재하는지 검사
if os.path.isdir(project_name):
    print(f"오류: 폴더가 이미 존재합니다: {project_name}")
    sys.exit(1)

# 3. 프로젝트 폴더 및 하위 폴더(data, doc, src) 생성
os.makedirs(os.path.join(project_name, "data"))
os.makedirs(os.path.join(project_name, "doc"))
os.makedirs(os.path.join(project_name, "src"))

print(f"프로젝트가 성공적으로 생성되었습니다: {project_name}")
