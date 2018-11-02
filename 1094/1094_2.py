"""
문제: https://www.acmicpc.net/problem/1094
풀이: 주어진 문제의 답은 X를 이진수로 표현했을 때 1인 비트수와 같다.
"""

x = int(input())
count = 0
while x:
    count += x & 1
    x >>= 1
print(count)
