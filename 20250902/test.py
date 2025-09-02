import sys, os
# sys.stdin = open("input.txt", "r") r : read mode, w : write mode
# 루트 디렉토리를 현재 디렉토리로 설정 해주지 않으면 절대경로 또는 상대 경로 사용해야 함
sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")

a, b = map(int, input().split())

print(a + b)