#!/usr/bin/env python3
# shortlines.py - FASTA 파일에서 지정한 길이보다 짧은 서열 줄의 개수를 센다
# 사용법: python3 src/shortlines.py <FASTA파일> <최소길이>

import sys
import os

# 1. 인자가 둘 다 입력되었는지 검사
if len(sys.argv) < 3:
    print(f"사용법: python3 {sys.argv[0]} <FASTA파일> <최소길이>")
    sys.exit(1)

fasta_file = sys.argv[1]
min_len_str = sys.argv[2]

# 2. 파일이 실제로 존재하는지 검사
if not os.path.isfile(fasta_file):
    print(f"오류: 파일을 찾을 수 없습니다: {fasta_file}")
    sys.exit(1)

# 3. 두 번째 인자가 숫자인지 검사 (.isdigit())
if not min_len_str.isdigit():
    print(f"오류: 최소 길이는 숫자여야 합니다: {min_len_str}")
    sys.exit(1)

min_len = int(min_len_str)
count = 0

# 4. 파일 읽기 및 헤더를 제외한 줄 길이 비교
with open(fasta_file) as f:
    for line in f:
        line = line.rstrip()
        # 헤더('>')가 아닌 서열 줄인 경우에만 길이 비교
        if not line.startswith(">"):
            if len(line) < min_len:
                count = count + 1

print(count)
