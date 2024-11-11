import numpy as np
import timeit  # 정확한 시간 측정을 위해 timeit 모듈 사용
from data_generation import generate_prediabetes_data

# 지배 관계를 확인하는 함수
def dominates(point1, point2):
    """
    point1이 point2를 지배하는지 여부를 판단하는 함수
    point1이 모든 속성에서 point2보다 크거나 같고, 적어도 하나의 속성에서 작아야 함.
    :param point1: 데이터 포인트 1 (FPG, OGTT, HbA1c)
    :param point2: 데이터 포인트 2 (FPG, OGTT, HbA1c)
    :return: point1이 point2를 지배하면 True, 그렇지 않으면 False
    """
    return all(x >= y for x, y in zip(point1, point2)) and any(x > y for x, y in zip(point1, point2))

# 선형 탐색을 사용하여 지배되지 않는 위험도가 가장 높은 데이터를 찾는 함수
def find_high_risk_data_linear_search(data):
    """
    모든 데이터를 비교하여 지배되지 않는 가장 높은 위험도 데이터를 찾는 함수.
    최종 출력은 서로 비교할 수 없는 가장 높은 위험도 데이터만 포함됨.
    :param data: 입력 데이터 (공복 혈당, 식후 혈당, HbA1c)
    :return: 지배되지 않는 높은 위험도 데이터 리스트
    """
    high_risk_data = []  # 최종 출력될 리스트

    # 모든 데이터 포인트를 하나씩 탐색
    for i, point in enumerate(data):
        is_dominated = False  # 해당 데이터가 지배되는지 여부
        for j, other_point in enumerate(data):
            if i != j:  # 자기 자신과는 비교하지 않음
                if dominates(other_point, point):  # 다른 데이터가 현재 데이터를 지배하는지 확인
                    is_dominated = True
                    break  # 지배되는 경우, 해당 데이터를 건너뜀

        # 지배되지 않는 데이터만 출력 리스트에 추가
        if not is_dominated:
            high_risk_data.append(point)

    return high_risk_data

def main():
    # 데이터 생성
    num_samples = 30  # 데이터 샘플 수
    data = generate_prediabetes_data(num_samples=num_samples)  # 당뇨병 전 단계 데이터를 생성

    # 선형 탐색을 사용하여 가장 높은 위험군 데이터를 계산하는 함수 실행 시간 측정
    execution_time = timeit.timeit(lambda: find_high_risk_data_linear_search(data), number=1)

    # 선형 탐색 연산 시간 출력
    print(f"선형 탐색 연산 시간: {execution_time:.6f}초")

    # 선형 탐색 후 데이터를 실제로 출력하기
    high_risk_data = find_high_risk_data_linear_search(data)

    if not high_risk_data:
        print("No high risk data found.")
    else:
        # 높은 위험군 데이터 출력 (터미널에 표시)
        print("Selected High Risk Data (Linear Search):")
        for point in high_risk_data:
            print(f"Fasting Glucose: {point[0]:.2f}, Postprandial Glucose: {point[1]:.2f}, HbA1c: {point[2]:.2f}")
        print(f"Total Selected High Risk Data: {len(high_risk_data)}")

if __name__ == "__main__":
    main()
