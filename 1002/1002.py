# 문제: https://www.acmicpc.net/problem/1002
# 풀이: 두 원이 만나는 점을 구하는 기하 문제. 상태와 조건은 다음과 같다.
#       1. 만나는 점이 무수히 많음
#           - 두 원이 동심원이고 반지름도 같음
#       2. 만나는 점이 없음
#           - 동심원이고 반지름이 다름
#           - 두 원이 멀리 떨어져 만나지 않음
#           - 한 원 안에 다른 원이 있지만 만나지 않음
#       3. 만나는 점이 한 개
#           - 외접
#           - 내접
#       4. 만나는 점이 두 개
#           - 그 외

n = int(input())
for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    if d == 0 and r1 == r2:
        print(-1)
    elif d == 0 or r1 + r2 < d or abs(r1 - r2) > d:
        print(0)
    elif r1 + r2 == d or abs(r1 - r2) == d:
        print(1)
    else:
        print(2)
