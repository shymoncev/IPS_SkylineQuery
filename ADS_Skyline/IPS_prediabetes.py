import sys
import os
import numpy as np
import timeit
from data_generation import (
    generate_normal_data,
    generate_prediabetes_data,
    generate_diabetes_data,
)
from skyline.IPS import Inverted_Pinnacle_dnc_skyline_optimized
from skyline.plotting import visualize_Inverted_Pinnacle_skyline

# 계층별 스카이라인 형성 함수
def layered_skyline(data):
    """
    계층별 스카이라인을 형성합니다.
    """
    layers = []
    while len(data) > 0:
        skyline = Inverted_Pinnacle_dnc_skyline_optimized(data)
        if len(skyline) == 0:
            break
        layers.append(skyline)
        data = np.array([point for point in data if point not in skyline])
    return layers

# 사용자 입력 처리 함수
def user_input_data(data):
    """
    사용자로부터 데이터 입력을 받아 동적으로 데이터셋을 수정합니다.
    """
    while True:
        print("\n--- 사용자 데이터 조작 메뉴 ---")
        print("1. 데이터 추가")
        print("2. 데이터 삭제")
        print("3. 데이터 보기")
        print("4. 시각화 ")
        choice = input("선택 (1-4): ")

        if choice == "1":
            fasting_glucose = float(input("공복 혈당 (mg/dL): "))
            postprandial_glucose = float(input("식후 혈당 (mg/dL): "))
            hba1c = float(input("HbA1c (%): "))
            data = np.vstack((data, [fasting_glucose, postprandial_glucose, hba1c]))
            print("데이터가 추가되었습니다.")
        elif choice == "2":
            index = int(input(f"삭제할 데이터의 인덱스 (0-{len(data) - 1}): "))
            if 0 <= index < len(data):
                data = np.delete(data, index, axis=0)
                print("데이터가 삭제되었습니다.")
            else:
                print("잘못된 인덱스입니다.")
        elif choice == "3":
            print("현재 데이터:")
            for i, point in enumerate(data):
                print(f"Index {i}: Fasting Glucose: {point[0]:.2f}, Postprandial Glucose: {point[1]:.2f}, HbA1c: {point[2]:.2f}")
        elif choice == "4":
            break
        else:
            print("잘못된 입력입니다.")

    return data

# 시각화 기능을 추가한 함수
def visualize_layers(data, layers):
    """
    사용자가 요청한 데이터를 시각화합니다.
    """
    print("\n--- 시각화 메뉴 ---")
    print("1. 전체 데이터와 스카이라인 시각화")
    print("2. 종료")

    while True:
        choice = input("선택 (1-2): ")

        if choice == "1":
            for i, layer in enumerate(layers):
                print(f"\nLayer {i + 1} - Total Points: {len(layer)}")
                visualize_Inverted_Pinnacle_skyline(data, layer)
            else:
                print("잘못된 계층 번호입니다.")
        elif choice == "2":
            print("시각화를 종료합니다.")
            break
        else:
            print("잘못된 입력입니다.")

# 메인 함수
def main():
    """
    프로그램의 메인 실행 함수입니다.
    """
    num_samples = int(input("초기 데이터 샘플 수를 입력하세요: "))
    data_type = input("데이터 유형을 선택하세요 (normal, prediabetes, diabetes): ").strip().lower()

    if data_type == "normal":
        data = generate_normal_data(num_samples)
    elif data_type == "prediabetes":
        data = generate_prediabetes_data(num_samples)
    elif data_type == "diabetes":
        data = generate_diabetes_data(num_samples)
    else:
        print("잘못된 데이터 유형입니다. 기본값으로 당뇨병 전 단계 데이터를 생성합니다.")
        data = generate_prediabetes_data(num_samples)

    # 사용자 데이터 조작
    data = user_input_data(data)

    # Inverted_Pinnacle Skyline 연산 시간 측정
    execution_time = timeit.timeit(lambda: Inverted_Pinnacle_dnc_skyline_optimized(data), number=1)
    print(f"Inverted Pinnacle Skyline 연산 시간: {execution_time:.6f}초")

    # 계층별 스카이라인 형성 및 시각화
    layers = layered_skyline(data)
    for i, layer in enumerate(layers):
        print(f"\nLayer {i + 1} - Selected Inverted Pinnacle Skyline Points:")
        for point in layer:
            print(f"Fasting Glucose: {point[0]:.2f}, Postprandial Glucose: {point[1]:.2f}, HbA1c: {point[2]:.2f}")
        print(f"Total Points in Layer {i + 1}: {len(layer)}\n")

    # 시각화 기능 호출
    visualize_layers(data, layers)

if __name__ == "__main__":
    main()
