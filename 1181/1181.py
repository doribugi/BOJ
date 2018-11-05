# 문제: https://www.acmicpc.net/problem/1181
# 풀이: 문자열 길이와 문자열로 정렬하여 중복빼고 출력
import sys
n = int(sys.stdin.readline())
words = [sys.stdin.readline().rstrip() for _ in range(n)]
sorted_words = sorted(words, key=lambda x: (len(x), x))
for i in range(len(sorted_words)):
    if i == 0 or sorted_words[i] != sorted_words[i - 1]:
        print(sorted_words[i])
