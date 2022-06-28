from collections import defaultdict
import heapq
import bisect
import math

def solution(N):
    R, A, B = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
    S = 0
    while R > 0:
        S += R * R
        R *= A
        S += R * R
        R //= B
    return  S * math.pi


t = int(input()) # read a line with a single integer
for N in range(1, t + 1):
    print("Case #{}: {}".format(N, solution(N)))
    # check out .format's specification for more formatting options


