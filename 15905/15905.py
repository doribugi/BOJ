# 문제: https://www.acmicpc.net/problem/15905
# 풀이: 맞은 문제 수, 페널티 순으로 정렬하여 5등과 같은 문제 수를 푼 5등 이하 학생 수를 센다

n = int(input())
students = [tuple(map(int, input().split())) for _ in range(n)]
students.sort(reverse=True)
count = 0
for student in students[5:]:
    if student[0] == students[4][0]:
        count += 1
print(count)
