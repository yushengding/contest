def calculate(p, q):
    mod = int(1e9+7)
    expo = 0
    expo = mod - 2
    while (expo):
        if (expo & 1):
            p = (p * q) % mod
        q = (q * q) % mod
        expo >>= 1
    return p
from functools import lru_cache
import math
m = int(1e9+7)
def solution(N):
    l = len(input())
    s = input().strip()

    q = 1
    for i in range(1, 1 + len(s)):
        q *= i
        q %= m

    @lru_cache(None)
    def helper(i, j, l):
        nonlocal s
        if j < i:
            return 0
        if j - i + 1 < l:
            return 0
        if j == i:
            if 0 <= l <= 1:
                return 1
            return 0
        ans = helper(i+1, j, l) + helper(i, j-1, l) - helper(i+1, j-1, l)
        if s[i] == s[j]:
            if i == j-1 and l == 2:
                return 1
            ans += helper(i+1, j-1, l-2)
        ans %= m
        return ans

    for l in range(2, len(s)):
        for i in range(len(s) - l + 1):
            for j in range(i+l-1, len(s)):
                # print(i, j, l, helper(i, j, l))

    p = 2*q
    tq = 1
    for l in range(2, len(s)):
        tq *= l
        tq %= m
        p += helper(0, len(s) - 1, l) * tq
        p %= m * tq  
    # z = math.gcd(p, q)
    return calculate(p, q)

t = int(input()) # read a line with a single integer
for N in range(1, t + 1):
    print("Case #{}: {}".format(N, solution(N)))
    # check out .format's specification for more formatting options




# print(calculate(7, 3 + int(1e9+7)))







