import numpy as np

# 정상 단계 데이터 생성 함수
def generate_normal_data(num_samples):
    fasting_glucose = np.random.uniform(70, 99, num_samples)
    postprandial_glucose = np.random.uniform(70, 139, num_samples)
    hba1c = np.random.uniform(0, 5.699, num_samples)
    return np.vstack((fasting_glucose, postprandial_glucose, hba1c)).T

np.random.seed(2)
# 당뇨병 전 단계 생성 함수
def generate_prediabetes_data(num_samples):
    data = []
    while len(data) < num_samples:
        fasting_glucose = np.random.uniform(70, 125)
        postprandial_glucose = np.random.uniform(70, 199)
        hba1c = np.random.uniform(0, 6.4)

        # 적어도 하나 이상의 속성이 당뇨 전 단계 범위에 속해야 함
        if (100 <= fasting_glucose <= 125) or (140 <= postprandial_glucose <= 199) or (5.7 <= hba1c <= 6.4):
            data.append([fasting_glucose, postprandial_glucose, hba1c])

    return np.array(data)

def generate_diabetes_data(num_samples):
    data = []

    while len(data) < num_samples:
        # 공복 혈당 (Fasting Glucose) 데이터 생성
        fasting_glucose = np.random.uniform(70, 200)  # 70~200 mg/dL 범위
        
        # 경구 포도당 부하 검사 (Oral Glucose Tolerance Test, OGTT) 데이터 생성
        postprandial_glucose = np.random.uniform(0, 300)  # 0~300 mg/dL 범위
        
        # 당화혈색소 (HbA1c) 데이터 생성
        hba1c = np.random.uniform(0, 10)  # 0%~10% 범위
        
        # 적어도 하나의 수치가 당뇨병 범위에 속하는지 확인
        if fasting_glucose >= 126 or postprandial_glucose >= 200 or hba1c >= 6.5:
            data.append([fasting_glucose, postprandial_glucose, hba1c])

    return np.array(data)