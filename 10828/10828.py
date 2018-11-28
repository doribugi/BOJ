# 문제: https://www.acmicpc.net/problem/10828
# 풀이: 구현 문제

from sys import stdin

n = int(stdin.readline())
stack = []
for _ in range(n):
    command = stdin.readline().split()
    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == "pop":
        print(stack.pop() if len(stack) > 0 else -1)
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        print(1 if len(stack) == 0 else 0)
    elif command[0] == "top":
        print(stack[-1] if len(stack) > 0 else -1)
