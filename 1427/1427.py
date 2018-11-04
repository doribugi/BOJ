# 문제: https://www.acmicpc.net/problem/1427
# 풀이: 딕셔너리에 숫자별 카운트 한 후 개수만큼 출력
n = input()
dic = {'9':0, '8':0, '7':0, '6':0, '5':0, '4':0, '3':0, '2':0, '1':0, '0':0}
for c in n:
    dic[c] += 1
answer = ""
for k, v in dic.items():
    answer += k * v
print(answer)
