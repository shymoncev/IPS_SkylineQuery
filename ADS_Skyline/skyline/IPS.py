import numpy as np

# 지배 관계를 반대로 확인하는 함수 (Inverted Pinnacle_Skyline)
def Inverted_Pinnacle_dominates(point1, point2):
    return all(x >= y for x, y in zip(point1, point2)) and any(x > y for x, y in zip(point1, point2))

# 정렬 기반의 병합 함수
def merge_Inverted_Pinnacle_skyline_optimized(left_skyline, right_skyline):
    # 왼쪽, 오른쪽 스카이라인을 병합하여 최종 스카이라인을 계산하는 함수
    merged_skyline = sorted(np.concatenate((left_skyline, right_skyline)), key=lambda x: (-x[0], -x[1], -x[2]))
    final_skyline = []
    for point in merged_skyline:
        if not any(Inverted_Pinnacle_dominates(other, point) for other in final_skyline):
            final_skyline.append(point)
    return np.array(final_skyline)

# Divide-and-Conquer 기반의 Inverted Pinnacle_Skyline 계산 함수 (최적화)
def Inverted_Pinnacle_dnc_skyline_optimized(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left_skyline = Inverted_Pinnacle_dnc_skyline_optimized(data[:mid])
    right_skyline = Inverted_Pinnacle_dnc_skyline_optimized(data[mid:])
    return merge_Inverted_Pinnacle_skyline_optimized(left_skyline, right_skyline)