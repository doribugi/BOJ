# 문제: https://www.acmicpc.net/problem/2908
# 풀이: 두 수를 문자열로 입력 받아 뒤집은 후 큰 수 출력
a, b = input().split()
print(max(a[::-1], b[::-1]))
