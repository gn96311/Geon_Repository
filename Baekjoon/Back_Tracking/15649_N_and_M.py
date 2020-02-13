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
''' 해석
visited = [False, False, False]

solve(0, 3, 3):
    for 0 in range(len(visited)):
        if not visited[0]:
            visited[0] = True #[True, False, False]
            out.append(1) #[1]
            solve(1, 3, 3):
                for 0 in range(len(visited)):
                    if not visited[0]: pass
                for 1 in range(len(visited)):
                    if not visited[1]:
                        visited[1] = True #[True, True, False]
                        out.append(2) #[1,2]
                        solve(2,3,3):
                            for 0 in range(len(visited)):
                                if not visited[0]: pass
                            for 1 in range(len(visited)):
                                if not vistied[1]: pass
                            for 2 in range(len(visited)):
                                visited[2] = True #[True, True, True]
                                out.append(3) #[1,2,3]
                                solve(3,3,3):
                                    print(' '.join(map(str,out))) #[1,2,3] 출력
                                    return
                                visited[2] = False #[True, True, False]
                                out.pop() #[1,2]
                        visited[1] = False # [True, False, False]
                        out.pop #[1]
                for 2 in range(len(visite)):
                    if not visited[2]:
                        visited[2] = True #[True, False, True]
                        out.append(3) #[1,3]
                        solve(2,3,3):
                            for 0 in range(len(visited)):
                                if not visited[0]: pass
                            for 1 in range(len(visited)):
                                visited[1] = True #[True, True, True]
                                out.append(2) #[1,3,2]
                                solve(3,3,3):
                                    print(' '.join(map(str,out))) #[1,3,2] 출력
                                    return
                                visited[1] = False #[True, False, True]
                                out.pop() #[1,3]
                            for 2 in range(len(visited)):
                                if not visited[2]: pass
                        visited[2] = False
                        out.pop() #[1]
            visited[0] = False
            out.pop() #[]
    for 1 in range(len(visited)):
        if not visited[1]:
            visited...
'''