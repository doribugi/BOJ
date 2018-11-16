# 문제: https://www.acmicpc.net/problem/1074
# 풀이: 분할 정복 방법으로 재귀적으로 배열을 4등분하여 나누고 그 안에서 위치를 찾는다.

def divide_and_conqure(n, r, c):
    half = 2 ** (n-1)
    if r < half and c < half:
        count = 0
        sub_r = r
        sub_c = c
    elif c >= half and r < half:
        count = 1
        sub_r = r
        sub_c = c - half
    elif c < half and r >= half:
        count = 2
        sub_r = r - half
        sub_c = c
    else:
        count = 3
        sub_r = r - half
        sub_c = c - half
    
    if n == 1:
        return count
    else:
        return count * (2**(2*(n-1))) + divide_and_conqure(n-1, sub_r, sub_c)

n, r, c = map(int, input().split())
print(divide_and_conqure(n, r, c))
