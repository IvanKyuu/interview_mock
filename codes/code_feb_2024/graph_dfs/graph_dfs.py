from typing import List
import numpy as np
from collections import defaultdict
from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if not rooms or len(rooms) == 0:
            return False
        visited = set()
        visited.add(0)
        queue = [0]
        while queue:
            index = queue.pop()
            keys = rooms[index]
            for key in keys:
                if key not in visited:
                    queue.append(key)
                    visited.add(index)
        return len(visited) == len(rooms)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected or len(isConnected) == 0:
            return 0
        assert len(isConnected) == (length := len(isConnected[0]))
        province = {}
        for vertex in range(length):
            if vertex in province:
                continue
            province[vertex] = vertex
            queue = [vertex]
            while queue:
                cur = queue.pop()
                for neighbour in range(length):
                    if isConnected[cur][neighbour] == 1 and neighbour not in province:
                        queue.append(neighbour)
                        province[neighbour] = vertex
        # print(province)
        return len(set(province.values()))
    
    def minReorder2(self, n: int, connections: List[List[int]]) -> int:
        can_visit_0 = set()
        can_visit_0.add(0)
        assert len(connections) >= n - 1
        parent = defaultdict(set)
        child = defaultdict(set)

        for edge in connections:
            src, dest = edge
            if dest in can_visit_0:
                can_visit_0.add(src)
            parent[dest].add(src)
            child[src].add(dest)
        count = 0
        queue = deque(can_visit_0)

        while queue and count < n:
            u = queue.popleft()
            if len(parent[u]) > 0:
                can_visit_0 = can_visit_0.union(parent[u])
            else:
                queue.append(u)
            count += 1

        count = 0
        queue = deque(range(n))
        while queue:
            u = queue.popleft()
            new_parents = child[u].difference(can_visit_0)
            # if len(can_visit_0) >= n:
            #     return count
            for new_parent in new_parents:
                if new_parent not in can_visit_0:
                    can_visit_0.add(new_parent)
                    count += 1
                    queue.append(new_parent)
            for cont_parent in parent[u]:
                can_visit_0.add(cont_parent)
                queue.append(cont_parent)
        # count += n - len(can_visit_0)
        return count

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        if not n:
            return 0
        visited = [False]  * n
        visited[0] = True
        assert len(connections) >= n - 1
        edges = defaultdict(set)
        for edge in connections:
            src, dest = edge
            edges[src].add((dest, 1))
            edges[dest].add((src, 0))
        queue = deque([0])
        count = 0
        # print(queue)
        while queue:
            node = queue.popleft()
            for nbr, sign in edges[node]:
                if not visited[nbr]:
                    # print(node, nbr, sign)
                    queue.append(nbr)
                    count += sign
                    visited[nbr] = True
        # print(edges)
        # print(visited)
        return count



s = Solution()
# s.findCircleNum([[1,0,0],[0,1,0],[0,0,1]])
# res = s.findCircleNum([[1,1,0],[1,1,0],[0,0,1]])
# print(res)
# res = s.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]])
# print(res)

# mat = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
# matrix = np.matrix(mat) 
# print(matrix)
# print(set((0, 5)) - set((0, 4)))
c = s.minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]])
# c = s.minReorder(n = 3, connections = [[1,0],[2,0]])
print(c)
