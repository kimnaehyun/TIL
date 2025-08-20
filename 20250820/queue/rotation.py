import sys
import os

# 현재 스크립트 파일이 있는 폴더 기준으로 경로 설정
current_dir = os.path.dirname(os.path.abspath(__file__)) # __file__은 현재 실행 중인 파이썬 스크립트 파일의 경로를 나타내는 특수 변수, abspath는 상대 경로를 절대 경로로 바꿔 줌, 현재 스크립트가 있는 폴더를 의미
input_file = os.path.join(current_dir, 'sample_input.txt') # 스크립트 폴더 안에 있는 sample_input.txt 파일

sys.stdin = open(input_file)

T = int(input())

def rotation():
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(M):
        arr.append(arr.pop(0))
        
    return arr.pop(0)


for tc in range(1, T + 1): print(f'#{tc}',rotation())