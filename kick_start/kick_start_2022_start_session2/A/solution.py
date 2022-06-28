from collections import defaultdict
import heapq
import bisect
import math

def solution(N):
    N, M  = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
    Cs  = [int(s) for s in input().split(" ")]
    total = sum(Cs)
    return total % M

t = int(input()) # read a line with a single integer
for N in range(1, t + 1):
    print("Case #{}: {}".format(N, solution(N)))
    # check out .format's specification for more formatting options


