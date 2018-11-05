"""
문제: https://www.acmicpc.net/problem/2920
풀이: 설명에 따라 구현
"""
numbers = list(map(int, input().split()))
ascending = True
descending = True
for i in range(1, len(numbers)):
    if ascending and numbers[i] - numbers[i - 1] != 1:
        ascending = False
    elif descending and numbers[i - 1] - numbers[i] != 1:
        descending = False
if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")
