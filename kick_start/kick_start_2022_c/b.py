from collections import defaultdict
import heapq
import bisect
import math

def solution(N):
    N, X, Y  = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
    total = (1 + N) * ( N ) // 2
    if total % (X+Y) != 0:
        return 'IMPOSSIBLE'
    ans = []
    sum = (total)  // (X+Y) * X
    while sum > 0:
        if sum > N:
            ans.append(N)
        elif sum <= N:
            ans.append(sum)
            break
        sum -= N
        N -= 1
    res = 'POSSIBLE\n' + str(len(ans)) + '\n'
    res += ' '.join(map(str, ans))
    return res



t = int(input()) # read a line with a single integer
for N in range(1, t + 1):
    print("Case #{}: {}".format(N, solution(N)))
    # check out .format's specification for more formatting options


