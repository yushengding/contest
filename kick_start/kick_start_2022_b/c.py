from collections import defaultdict
import heapq
import bisect
import math
import sys
sys.setrecursionlimit(50000)
from functools import lru_cache
NoChild = ['S', 'E', 'N', 'W']
GoChild = ['W', "S", "E", 'N']
FromParent = [2, 3, 0, 1]
BackParent = GoChild
class Node:
    def __init__(self, pos):
        self.pos = pos
        self.child = [None] * 4
    def add_child(self, index, child ):
        self.child[index] = child
    def trip(self, from_):
        ans = []
        for i in range(1, 4):
            now = (i+from_) % 4
            child = self.child[(i+from_) % 4]
            if not child:
                ans.append(NoChild[now])
            else:
                # print("go child", now)
                ans.append(GoChild[now])
                ans.append(child.trip(FromParent[now]))
        ans.append(BackParent[from_])
        # print(self.pos, from_, ans)
        return ''.join(ans)
nei = [ (0, -1), (1, 0), (0, 1), (-1, 0) ]
def dfs(graph, nodes):
    waitlist = [(0, 0)]
    nodes[(0, 0)] = Node((0,0))
    while waitlist:
        x, y = waitlist.pop()
        for i in range(4):
            dx, dy = nei[i]
            nx, ny = dx + x, dy + y
            if nx >= 0 and nx < len(graph) and ny >= 0 and ny < len(graph[0]):
                if graph[nx][ny] == '#' or (nx, ny) in nodes:
                    continue
                nodes[(nx, ny)] = Node((nx, ny))
                nodes[(x, y)]. add_child(i,  nodes[(nx, ny)])

                waitlist.append((nx, ny))
    return len(nodes) == sum([1 for i in range(len(graph)) for j in range(len(graph[0])) if graph[i][j] == '*'])

def solution(_):
    
    R, C = [int(s) for s in input().split(" ")]
    graph = []
    for i in range(R):
        graph.append(input().strip())
    nodes = {}
    if dfs(graph, nodes) == False:
        return 'IMPOSSIBLE'
    ans = nodes[(0, 0)].trip(3)
    return ans[:-1] + 'W'

t = int(input()) # read a line with a single integer
for N in range(1, t + 1):
    print("Case #{}: {}".format(N, solution(N)))
    # check out .format's specification for more formatting options


