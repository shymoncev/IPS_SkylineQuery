import numpy as np
from skyline.IPS import merge_Inverted_Pinnacle_skyline_optimized

# 계층별 스카이라인 형성 함수
def layered_skyline(data):
    """
    데이터를 입력받아 계층별 스카이라인을 형성하는 함수.
    스카이라인을 반복적으로 형성하며, 각 스카이라인을 제거한 후 남은 데이터에서 다시 스카이라인을 형성.
    :param data: 입력 데이터 (공복 혈당, 식후 혈당, HbA1c)
    :return: 각 계층에서 형성된 스카이라인 리스트
    """
    layers = []  # 계층별 스카이라인 리스트
    
    # 데이터가 남아있을 때까지 반복
    while len(data) > 0:
        # 현재 데이터에서 스카이라인을 형성
        skyline = merge_Inverted_Pinnacle_skyline_optimized(data)
        
        # 스카이라인이 비어 있으면 종료
        if len(skyline) == 0:
            break
        
        # 형성된 스카이라인을 저장
        layers.append(skyline)
        
        # 스카이라인에 속하는 데이터를 데이터에서 제거
        data = np.array([point for point in data if point not in skyline])
    
    return layers
