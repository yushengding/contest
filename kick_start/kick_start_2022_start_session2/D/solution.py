from collections import defaultdict
from copy import deepcopy
import heapq
import bisect
import math
from string import ascii_uppercase

def check(str, s, e):
    if sum(str[i] in 'aeiou' for i in range(s+1, e)) == 0:
        return False
    i = 0
    left_hash = 0
    right_hash = 0
    m = int(1e9+7)
    left_base = 1
    vol_count = 0
    while s - i >= 0 and e + i < len(str):
        left_c = ord(str[s - i]) % 26
        right_c = ord(str[e + i]) % 26
        left_hash = (left_hash + left_base * (left_c)) % m
        left_base = left_base * 29 % m
        right_hash = (right_hash * 29 + right_c) % m
        # print(s, i, e, left_hash, right_hash, str[s-i:s+1], str[e:e+i+1])
        if str[s-i] in 'aeiou':
            vol_count += 1
        if vol_count >= 2 and left_hash == right_hash and str[s-i:s+1] == str[e:e+i+1]:
            return True
        i += 1
    return False

def solution(T):
    # N, Q  = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
    S = input().strip()
    for s in range(len(S)):
        for e in range(s, len(S)):
            if check(S, s, e):
                return "Spell!"
    return "Nothing."



t = int(input()) # read a line with a single integer
for N in range(1, t + 1):
    print("Case #{}: {}".format(N, solution(N)))
    # check out .format's specification for more formatting options


