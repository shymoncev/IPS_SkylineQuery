Inverted Pinnacle Skyline Project
개요
이 프로젝트는 Inverted Pinnacle Skyline 알고리즘을 사용하여 다차원 데이터에서 지배되지 않는 중요한 포인트를 추출하는 데 중점을 둡니다. 특히 당뇨병 전 단계 데이터를 분석하는 것을 목표로 하며, 스카이라인 포인트를 시각화하여 데이터의 분포와 특징을 직관적으로 이해할 수 있도록 합니다.

주요 기능
데이터 생성:  전당뇨 범위에 해당하는 데이터셋을 생성합니다.
Inverted Pinnacle Skyline 계산: 데이터셋에서 지배되지 않는 높은 위험도 포인트를 추출합니다.
계층별 스카이라인 형성: 데이터에서 계층별로 스카이라인을 반복적으로 형성하여 다양한 위험도 계층을 분석합니다.
시각화: 3D 시각화를 통해 Inverted Pinnacle Skyline 포인트와 전체 데이터 분포를 시각화합니다.

Directory Structure:
ADS_Skyline/
├── IPS_prediabetes.py       # Inverted Pinnacle Skyline 알고리즘을 적용하여 전당뇨 데이터 분석
├── Linear Speach.py         # 선형 탐색을 통한 지배되지 않는 데이터 포인트 분석
├── data_generation.py       # 당뇨병 전증의 범위를 기반하여 데이터를 생성하는 코드
├── skyline/                 # 스카이라인 알고리즘과 관련된 주요 모듈을 포함하는 폴더
│   ├── IPS.py               # Inverted Pinnacle Skyline 알고리즘 구현
│   ├── layered.py           # 계층형 스카이라인 형성 함수
│   └── plotting.py          # 스카이라인 포인트 및 전체 데이터의 3D 시각화 함수
└── requirements.txt         # 필요한 Python 패키지 목록


주요 알고리즘 설명
Inverted Pinnacle Skyline
Inverted Pinnacle Skyline 알고리즘은 다차원 데이터에서 지배되지 않는 데이터를 추출하는 알고리즘입니다. 기존 스카이라인 알고리즘과 반대 방향으로 지배 관계를 판단하여, 특정 속성에서 높은 값이나 위험도를 가진 데이터를 찾는 데 중점을 둡니다.

계층형 스카이라인
계층형 스카이라인(layered skyline)은 스카이라인 포인트를 찾고 이를 제거한 뒤, 남은 데이터에서 다시 스카이라인을 형성하는 과정을 반복하여 계층별 스카이라인을 형성합니다. 이를 통해 데이터의 다층적 분포와 위험도 계층을 이해할 수 있습니다.


## 설치 및 실행 방법

### 1. 가상 환경 생성 및 패키지 설치
```bash
python -m venv venv
source venv/bin/activate  # MacOS/Linux
venv\Scripts\activate     # Windows
pip install -r requirements.txt
# 2.실행예시
# 데이터 생성 및 분석: IPS_prediabetes.py
python IPS_prediabetes.py
# 시각화: visualize_Inverted_Pinnacle_skyline
python skyline/plotting.py

### 2. **사용 예제**
```markdown
## 사용 예제

### Inverted Pinnacle Skyline 계산 예제
```python
from data_generation import generate_prediabetes_data
from skyline.IPS import Inverted_Pinnacle_dnc_skyline_optimized

# 데이터 생성
data = generate_prediabetes_data(num_samples=30)

# Inverted Pinnacle Skyline 계산
skyline = Inverted_Pinnacle_dnc_skyline_optimized(data)

# 결과 출력
print("Inverted Pinnacle Skyline Points:", skyline)
