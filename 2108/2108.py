# 문제: https://www.acmicpc.net/problem/2108
# 풀이: 평균 = 합 / 개수
#      중앙값 = 정렬된 배열[n / 2]
#      최빈값 = Counter 이용
#      범위 = 정렬된 배열[-1] - 정렬된 배열[0]
import sys
from collections import Counter
n = int(sys.stdin.readline())
numbers = sorted([int(sys.stdin.readline()) for _ in range(n)])
print(round(sum(numbers) / len(numbers)))
print(numbers[len(numbers)//2])
counter = Counter(numbers).most_common()
if len(counter) == 1 or counter[0][1] != counter[1][1]:
    print(counter[0][0])
else:
    print(counter[1][0])
print(numbers[-1] - numbers[0])
