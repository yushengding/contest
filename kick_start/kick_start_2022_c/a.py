from collections import defaultdict
import heapq
import bisect
import math

def solution(N):
    L,  = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
    S = input().strip()  # read a list of integers, 2 in this case
    s = set(S)
    if not any(c in s for c in 'abcdefghijklmnopqrstuvwxyz'):
        S += 'a'
    if not any(c in s for c in 'abcdefghijklmnopqrstuvwxyz'.upper()):
        S += 'A'
    if not any(c in s for c in '1234567890'.upper()):
        S += '1'
    if not any(c in s for c in '#@*&'.upper()):
        S += '#'
    while len(S) < 7:
        S += 'a'
    return S

t = int(input()) # read a line with a single integer
for N in range(1, t + 1):
    print("Case #{}: {}".format(N, solution(N)))
    # check out .format's specification for more formatting options


