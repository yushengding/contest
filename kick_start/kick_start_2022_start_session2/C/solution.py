from collections import defaultdict
from copy import deepcopy
import heapq
import bisect
import math
from string import ascii_uppercase
class PChecker:
    def __init__(self, s) -> None:
        self.s = s
        self.counts = []
        default_count = defaultdict(int)
        self.counts.append(deepcopy(default_count))
        for c in s:
            default_count[c] += 1
            self.counts.append(deepcopy(default_count))
        
    def check(self, s, e):
        odd = False
        for char in ascii_uppercase:

            if (self.counts[e][char] - self.counts[s-1][char]) % 2:
                if odd:
                    return False
                odd = True
        return True

def solution(T):
    N, Q  = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
    S = input().strip()
    p_checker = PChecker(S)
    ans = 0
    for i in range(Q):
        s, e = [int(s) for s in input().split(" ")] 
        ans += p_checker.check(s, e)
    return ans

t = int(input()) # read a line with a single integer
for N in range(1, t + 1):
    print("Case #{}: {}".format(N, solution(N)))
    # check out .format's specification for more formatting options


