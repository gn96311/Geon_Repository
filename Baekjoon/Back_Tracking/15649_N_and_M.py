#DFS(Depth First Search)를 구현하여 푸는 문제.

import sys

N, M = list(map(int, sys.stdin.readline().split()))
visited = [False]*N
out = []

def solve(depth, N, M):
    if depth == M:
        print(' '.join(map(str,out)))
        return
    for i in range(len(visited)):
        if not visited[i]:
            visited[i] = True
            out.append(i+1)
            solve(depth+1, N, M)
            visited[i] = False
            out.pop()

solve(0, N, M)