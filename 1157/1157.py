# 문제: https://www.acmicpc.net/problem/1157
# 풀이: 딕셔너리를 이용해 알파벳 별 사용 개수 카운팅
word = input()
dic = {}
for c in word.upper():
    if c in dic:
        dic[c] += 1
    else:
        dic[c] = 1
values = sorted(dic.values())
if len(values) > 1 and values[-1] == values[-2]:
    print("?")
    exit(0)
max_k, max_v = "", 0
for k, v in dic.items():
    if max_v < v:
        max_k, max_v = k, v
print(max_k)
