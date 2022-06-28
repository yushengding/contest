from collections import defaultdict
import heapq
import bisect
import math
from functools import lru_cache
D = None
A = None
@lru_cache(None)
def check(i, j, r):
    global A, D
    if i > j:
        return 0
    if i == j:
        # print(i, j, r, min((A[j] + r) % D, D - (A[j] + r) % D))
        return min((A[j] + r) % D, D - (A[j] + r) % D)
    elif A[i] == A[j]:
        w1 = (A[i] + r) % D
        w2 = D - w1
        
        # print(i, j, r, check(i+1, j-1, (r-w1) % D) + w1, check(i+1, j-1, (r+w1) % D) + w2)
        return min(check(i+1, j-1, (r-w1) % D) + w1, check(i+1, j-1, (r+w2) % D) + w2)
    else:
        w1 = (A[i] + r) % D
        w2 = D - w1
        
        w3 = (A[j] + r) % D
        w4 = D - w3

        # print(i, j, r, check(i+1, j, (r-w1) % D) + w1, check(i+1, j, (r+w2) % D) + w2, 
        #         check(i, j-1, (r-w3) % D) + w3, check(i, j-1, (r+w4) % D) + w4)
        return min(check(i+1, j, (r-w1) % D) + w1, check(i+1, j, (r+w2) % D) + w2, 
                check(i, j-1, (r-w3) % D) + w3, check(i, j-1, (r+w4) % D) + w4)

def solution(_):
    global A, D
    N, D = [int(s) for s in input().split(" ")]
    A = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
    ans = []
    start = True
    for i in A:
        if start and i == 0:
            continue
        start = False
        if ans and ans[-1] == i:
            continue
        ans.append(i)
    while ans and ans[-1] == 0:
        ans.pop()
    A = ans
    return check(0, len(A)-1, 0)



t = int(input()) # read a line with a single integer
for N in range(1, t + 1):
    check.cache_clear()
    print("Case #{}: {}".format(N, solution(N)))
    # check out .format's specification for more formatting options


