# 문제: https://www.acmicpc.net/problem/1181
# 풀이: 셋에 문자열 넣고 리스트로 변환후 문자열 길이와 문자열로 정렬하여 출력
import sys
n = int(sys.stdin.readline())
words = list(set([sys.stdin.readline() for _ in range(n)]))
sorted_words = sorted(words, key=lambda x: (len(x), x))
print("".join(sorted_words))
