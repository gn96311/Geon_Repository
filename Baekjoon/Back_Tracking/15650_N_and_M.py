import sys

N, M = list(map(int, sys.stdin.readline().split()))

check = [False]*N
result = []

def solve(depth, start, N, M):
    if depth == M:
        print(' '.join(map(str(result))))
        return
    for i in range(len(check)):
        if not check[i]:
            check[i] = True
            result.append(i+1)
            solve(depth+1, 1, N, M)
            check[i] = False
