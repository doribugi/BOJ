# 문제: https://www.acmicpc.net/problem/10845
# 풀이: 주어진 명령을 dictionary에 lambda 함수로 정의하여 수행
import sys
import queue
n = int(sys.stdin.readline())
cmds = [sys.stdin.readline().split() for _ in range(n)]
q = queue.deque()
functions = {
    "push": lambda x: q.append(int(x)),
    "pop": lambda x: print(q.popleft() if not len(q) == 0 else -1),
    "size": lambda x: print(len(q)),
    "empty": lambda x: print(1 if len(q) == 0 else 0),
    "front": lambda x: print(q[0] if len(q) != 0 else -1),
    "back": lambda x: print(q[-1] if len(q) != 0 else -1)
}
for cmd in cmds:
    functions[cmd[0]](cmd[1] if len(cmd) == 2 else 0)
