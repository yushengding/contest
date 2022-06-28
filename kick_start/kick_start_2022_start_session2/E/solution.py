from cmath import inf
from collections import defaultdict
from copy import deepcopy
import heapq
import bisect
import math
from random import randint
from string import ascii_uppercase


def dis(matrix, row_dir, col_dir, ans):
    for i in range(len(matrix))[::row_dir]:
        for j in range(len(matrix[0]))[::col_dir]:
            if matrix[i][j] == 1:
                ans[i][j] = 0
            if i - row_dir >= 0 and i - row_dir < len(ans):
                ans[i][j] = min(ans[i][j], ans[i-row_dir][j] + 1)
            if j - col_dir >= 0 and j - col_dir < len(ans[0]):
                ans[i][j] = min(ans[i][j-col_dir] + 1, ans[i][j])
    return ans


def solution(T):
    R, C  = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
    matrix = []
    for r in range(R):
        matrix.append( [int(s) for s in input()] )
    return check(matrix, R, C)

def check2(matrix, R, C):
    ans = [[inf] * C for i in range(R)]
    dis(matrix, 1, 1, ans)
    dis(matrix, 1, -1, ans)
    dis(matrix, -1, 1, ans)
    dis(matrix, -1, -1, ans)
    res = max(map(max, ans))
    for i in range(R):
        for j in range(C):
            if matrix[i][j] != 1:
                matrix[i][j] = 1
                ans = [[inf] * C for i in range(R)]
                dis(matrix, 1, 1, ans)
                dis(matrix, 1, -1, ans)
                dis(matrix, -1, 1, ans)
                dis(matrix, -1, -1, ans)
                res = min(res, max(map(max, ans)))
                matrix[i][j] = 0
    return res

def doable(mi, mj, mai, maj, now_dis):
    # print(mi, mj, mai, maj, now_dis, (1 +  max(mai - mi, maj - mj)) // 2 <= now_dis)
    min_dis = max(mai - mi, maj - mj)
    if (1 + min_dis) // 2 < now_dis:
        return True
    if (1 + min_dis) // 2 == now_dis:
        if mai - mi == maj - mj and (mai - mi) % 2 == 0 and ((mi + mj) % 2 == 1):
            return False
        return True
    return False

def check(matrix, R, C):
    ans = [[inf] * C for i in range(R)]
    dis(matrix, 1, 1, ans)
    dis(matrix, 1, -1, ans)
    dis(matrix, -1, 1, ans)
    dis(matrix, -1, -1, ans)
    # print(ans)
    queue = [] # distance to pos
    for i in range(R):
        for j in range(C):
            queue.append((ans[i][j], i, j))
    queue.sort(reverse=True)
    ans, i, j = queue[0]
    max_i = min_i = i - j # new x = x - y
    max_j = min_j = i + j # new y = x + y
    for now_dis, i, j in queue:
        # print("isdo?", doable(min_i, min_j, max_i, max_j, now_dis))
        if doable(min_i, min_j, max_i, max_j, now_dis):
            # print('doable', i, j, now_dis)
            ans = now_dis
        else:
            return ans
        max_i = max(max_i, i - j)
        max_j = max(max_j, i + j)
        min_i = min(min_i, i - j)
        min_j = min(min_j, i + j)
    if doable(min_i, min_j, max_i, max_j, now_dis):
        ans = now_dis
    return ans

# if __name__ == '__main__':
#     import time
#     s = time.time()
#     for i in range(100):
#         R, C = 10, 10
#         # R, C = 250, 250
#         b = randint(1, 40)
        
#         print('matrix', R, C, b)
#         matrix = [[0] * C for i in range(R)]
        
#         for t in range(b):
#             r, c = randint(0, R-1), randint(0, C-1)
#             matrix[r][c] = 1
#         # print(matrix, check(matrix, R, C))
#         a = check(matrix, R, C)
#         b = check2(matrix, R, C)
#         if a != b:
#             print(matrix, a, b)
#             break
#     print(time.time() - s)

t = int(input()) # read a line with a single integer
for N in range(1, t + 1):
    print("Case #{}: {}".format(N, solution(N)))
    # check out .format's specification for more formatting options


