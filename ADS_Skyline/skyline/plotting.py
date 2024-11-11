import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import ConvexHull

# Inverted_Pinnacle Skyline 포인트들을 시각화하는 함수
def plot_Inverted_Pinnacle_skyline(skyline, ax, color, marker, label, draw_lines=True):
    """ Inverted_Pinnacle Skyline 포인트들을 시각화하고, 포인트 마커 모양을 설정하는 함수 """
    
    # 3D 스캐터 플롯 생성
    scatter = ax.scatter(skyline[:, 0], skyline[:, 1], skyline[:, 2], c=color, marker=marker, label=label)
    
    # ConvexHull을 이용해 포인트를 선으로 연결 (Inverted_Pinnacle Skyline)
    if draw_lines and len(skyline) >= 3:
        hull = ConvexHull(skyline)
        for simplex in hull.simplices:
            ax.plot(skyline[simplex, 0], skyline[simplex, 1], skyline[simplex, 2], color=color)

    return scatter

# Inverted_Pinnacle Layered Skyline을 시각화하는 함수
def visualize_Inverted_Pinnacle_skyline(data, skyline, title="Inverted Pinnacle Skyline 3D Visualization"):
    """ 전체 데이터와 Inverted_Pinnacle Skyline을 함께 시각화 """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # 전체 데이터 포인트를 먼저 그립니다
    ax.scatter(data[:, 0], data[:, 1], data[:, 2], c='black', marker='o', label='All Data')
    
    # Inverted_Pinnacle Skyline 포인트들을 시각화
    plot_Inverted_Pinnacle_skyline(skyline, ax, 'red', '^', 'Inverted Pinnacle Skyline')

    # 축 레이블 설정
    ax.set_xlabel('Fasting Glucose (mg/dL)')
    ax.set_ylabel('Postprandial Glucose (mg/dL)')
    ax.set_zlabel('HbA1c (%)')
    
    ax.set_xlim(70, 160)
    ax.set_ylim(0, 300)
    ax.set_zlim(0, 9.5)
    
    ax.set_title(title)

    # 데이터 개수 출력 (왼쪽 상단)
    ax.text2D(0.05, 0.95, f"Data Points: {data.shape[0]}", transform=ax.transAxes, fontsize=12, color='black')
    
    # 범례를 오른쪽 상단으로 이동
    plt.legend(loc='upper right')

    plt.show()