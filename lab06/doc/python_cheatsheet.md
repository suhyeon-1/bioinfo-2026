# 나의 파이썬 치트시트 (Bash & Python 비교)

## 1. 스크립트 제작 흐름 (Workflow 비교)
1. **1단계 (탐색 및 확인)**: 
   * Bash: `grep -c ">" data/seqs.fasta`
   * Python: 대화형 REPL(`python3`)에서 직접 실행하며 파일 파싱 확인
2. **2단계 (스크립트화)**: 
   * Bash: 셰뱅(`#!/usr/bin/env bash`)과 함께 `.sh` 파일 작성
   * Python: 셰뱅(`#!/usr/bin/env python3`)과 함께 `.py` 파일 작성
3. **3단계 (변수 도입)**: 
   * Bash: `FILE="data/seqs.fasta"`
   * Python: `filename = "data/seqs.fasta"`
4. **4단계 (명령행 인자 도입)**: 
   * Bash: `FILE="$1"`
   * Python: `import sys; filename = sys.argv[1]`
5. **5단계 (예외 처리 및 안전장치)**: 
   * Bash: `if [ ! -f "$1" ]`, `exit 1`
   * Python: `import os`, `if not os.path.isfile(filename): sys.exit(1)`

---

## 2. 주요 기능별 코드 비교

* **서열 개수 세기 (정수 카운트)**
  * Bash: `grep -c ">" data/seqs.fasta`
  * Python:
    ```python
    n = sum(1 for line in open("data/seqs.fasta") if line.startswith(">"))
    ```

* **헤더 제외하고 총 염기 수(글자 수) 구하기**
  * Bash: `grep -v ">" data/seqs.fasta | tr -d '\n' | wc -c`
  * Python:
    ```python
    total = sum(len(line.rstrip()) for line in open("data/seqs.fasta") if not line.startswith(">"))
    ```

* **폴더 안의 모든 FASTA 파일 반복문 처리**
  * Bash: 
    ```bash
    for FILE in data/*.fasta; do ... done
    ```
  * Python:
    ```python
    import glob
    for path in sorted(glob.glob("data/*.fasta")):
        ...
    ```

* **소수점 계산**
  * Bash: `echo "$GC $LEN" | awk '{printf "%.4f\n", $1 / $2}'`
  * Python: `print(f"{gc / length:.4f}")` (파이썬은 기본적으로 실수를 지원하므로 `awk` 같은 별도 유틸리티 불필요)

---

## 3. 언어별 특징 및 주의사항 (이동 불가 항목 포함)
1. **파이프라인(`|`)과 외부 유틸리티**:
   * Bash에서는 파이프라인으로 여러 유틸리티(`grep`, `wc`, `awk`)를 조합하는 것이 강력하지만, 파이썬에서는 자체 내장 함수와 반복문(`for`, `if`)으로 구현하므로 방식이 다름.
2. **변수 대입 시 공백 제약**:
   * Bash는 대입 시 공백이 있으면 치명적인 오류가 나지만(`FILE = "a"` 불가), 파이썬은 공백을 자유롭게 허용함(`filename = "a"` 가능).
3. **타입 관리**:
   * Bash는 모든 것을 문자열로 취급하지만, 파이썬은 정수(`int`), 문자열(`str`), 리스트(`list`), 딕셔너리(`dict`) 등 자료형 구분이 엄격하므로 `int()`나 `str()` 형변환에 주의해야 함.
