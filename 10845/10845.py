# 문제: https://www.acmicpc.net/problem/10845
# 풀이: 주어진 명령을 조건문으로 확인하여 수행
import sys
import queue
n = int(sys.stdin.readline())
q = queue.deque()
for _ in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push":
        q.append(int(cmd[1]))
    elif cmd[0] == "pop":
        print(q.popleft() if not len(q) == 0 else -1)
    elif cmd[0] == "size":
        print(len(q))
    elif cmd[0] == "empty":
        print(1 if len(q) == 0 else 0)
    elif cmd[0] == "front":
        print(q[0] if len(q) != 0 else -1)
    elif cmd[0] == "back":
        print(q[-1] if len(q) != 0 else -1)
