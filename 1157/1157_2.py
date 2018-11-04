# 문제: https://www.acmicpc.net/problem/1157
# 풀이: 카운터 클래스를 이용해 알파벳 별 사용 개수 카운팅
from collections import Counter
word = input().upper()
counter = Counter(word).most_common()
if len(counter) > 1 and counter[0][1] == counter[1][1]:
    print("?")
else:
    print(counter[0][0])
