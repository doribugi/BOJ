"""
문제: https://www.acmicpc.net/problem/2675
풀이: 문제에 맞게 구현
"""
t = int(input())
for _ in range(t):
    r, s = input().split()
    answer = ""
    for c in s:
        answer += c * int(r)
    print(answer)
