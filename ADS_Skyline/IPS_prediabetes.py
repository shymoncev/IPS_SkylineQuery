import numpy as np
import timeit
from skyline.IPS import Inverted_Pinnacle_dnc_skyline_optimized  # Inverted_Pinnacle Skyline 기능
from data_generation import generate_prediabetes_data  # 당뇨병 전 단계 데이터 생성 함수
from skyline.plotting import visualize_Inverted_Pinnacle_skyline  # 시각화 함수 임포트

# 계층별 스카이라인 형성 함수
def layered_skyline(data):
    """
    데이터를 입력받아 계층별 스카이라인을 반복적으로 형성하는 함수.
    스카이라인을 반복적으로 형성하며, 각 스카이라인을 제거한 후 남은 데이터에서 다시 스카이라인을 형성.
    :param data: 입력 데이터 (공복 혈당, 식후 혈당, HbA1c)
    :return: 각 계층에서 형성된 스카이라인 리스트
    """
    layers = []  # 계층별 스카이라인 리스트
    
    # 데이터가 남아있을 때까지 반복
    while len(data) > 0:
        # 현재 데이터에서 스카이라인을 형성
        skyline = Inverted_Pinnacle_dnc_skyline_optimized(data)
        
        # 스카이라인이 비어 있으면 종료
        if len(skyline) == 0:
            break
        
        # 형성된 스카이라인을 저장
        layers.append(skyline)
        
        # 스카이라인에 속하는 데이터를 데이터에서 제거
        data = np.array([point for point in data if point not in skyline])
    
    return layers

# 메인 함수
def main():
    # 데이터 생성
    num_samples = 30  # 데이터 샘플 수
    data = generate_prediabetes_data(num_samples=num_samples)

    # Inverted_Pinnacle Skyline을 적용하여 가장 높은 위험도 데이터를 계산하는 함수 실행 시간 측정
    execution_time = timeit.timeit(lambda: Inverted_Pinnacle_dnc_skyline_optimized(data), number=1)

    # Inverted_Pinnacle Skyline 연산 시간 출력
    print(f"Inverted Pinnacle Skyline 연산 시간: {execution_time:.6f}초")

    # 계층별 스카이라인 형성 및 시각화
    remaining_data = data.copy()  # 원래 데이터를 복사하여 남은 데이터로 사용
    layers = layered_skyline(remaining_data)

    for i, layer in enumerate(layers):
        print(f"Layer {i + 1} - Selected Inverted Pinnacle Skyline Points:")
        for point in layer:
            print(f"Fasting Glucose: {point[0]:.2f}, Postprandial Glucose: {point[1]:.2f}, HbA1c: {point[2]:.2f}")
        print(f"Total Points in Layer {i + 1}: {len(layer)}\n")

        # 남은 데이터만 시각화 (배제된 포인트는 다음 시각화에서 제외)
        visualize_Inverted_Pinnacle_skyline(remaining_data, layer)

        # 스카이라인에 속한 포인트를 남은 데이터에서 제외
        remaining_data = np.array([point for point in remaining_data if point not in layer])

if __name__ == "__main__":
    main()
