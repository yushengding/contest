from collections import defaultdict, deque
import enum
import heapq
import bisect
import math

def solution(N):
    N, L  = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
    ants = []
    for i in range(N):
        P, D = [int(s) for s in input().split(" ")]
        ants.append((P, D, i))
    # ans = dict()
    ants_dis = dict() # fall time
    # for i, (P, D) in enumerate(ants):
    #     if D == 0: # left
    #         ants_dis[i] = P
    #     else:
    #         ants_dis[i] = L - P
    
    ant_id = deque()
    ant_dis = deque()
    ant_ans = dict()
    ants.sort()
    for P, D, i in ants:
        if D == 0:
            if not ant_id:
                ant_ans[i] = P
            else:
                # print(ant_id, ant_dis)
                ant_id.append(i)
                ant_ans[ant_id.popleft()] = P
        else:
            ant_id.append(i)
            ant_dis.append(L - P)
    
    for id, dis in zip(ant_id, ant_dis):
        ant_ans[id] = dis

    # print(ant_ans)
    ans = sorted((v, k) for k, v in ant_ans.items())
    ans = [k+1 for (v, k) in ans]
    return ' '.join(map(str, ans))



t = int(input()) # read a line with a single integer
for N in range(1, t + 1):
    print("Case #{}: {}".format(N, solution(N)))
    # check out .format's specification for more formatting options


