# 문제: https://www.acmicpc.net/problem/3090
# 풀이: 문제를 해결하기 위한 핵심 아이디어는 이진 탐색이다.
#      더불어 이해해야 하는 것은 이진 탐색 시 찾으려는 답이 하나가 아니라 여러 개이고 
#      그 중 최적의(차이의 최댓값이 최소가 되게하는) 해를 구해야 한다는 것이다.
#      이 문제에서 이진 탐색으로 찾을 수 있는 것은 수열의 인접한 숫자의 차이의 최댓값이 

def count_cost_make_max_diff(a, diff):
    tmp = a.copy()
    count = 0
    for i in range(len(tmp) - 1):
        if tmp[i + 1] > tmp[i] + diff:
            count += tmp[i + 1] - tmp[i] - diff
            tmp[i + 1] = tmp[i] + diff
    for i in range(len(tmp) - 1, 0, -1):
        if tmp[i - 1] > tmp[i] + diff:
            count += tmp[i - 1] - tmp[i] - diff
            tmp[i - 1] = tmp[i] + diff
    return tmp, count

n, t = map(int, input().split())
a = list(map(int, input().split()))

low = 0
high = max(a)
while low <= high:
    mid = (low + high) // 2
    tmp, count = count_cost_make_max_diff(a, mid)
    if  count <= t:
        high = mid - 1
        result = tmp
    else:
        low = mid + 1

print(*result, sep=' ')
