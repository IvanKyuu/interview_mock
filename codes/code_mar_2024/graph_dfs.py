from typing import List, Set
import numpy as np
from collections import defaultdict
from collections import deque
from collections import Counter
from queue import PriorityQueue
from pprint import pprint


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

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        if not equations:
            return None
        assert len(values) == len(equations)
        adj_matrix = defaultdict(dict)
        for (a, b), value in zip(equations, values):
            adj_matrix[a][b] = value
            adj_matrix[b][a] = 1.0 / value
        for node in adj_matrix:
            adj_matrix[node][node] = 1
            
            
        def dfs(visited: Set[str], src: str, dest: str, cur: int, ans: List[int]) -> None:
            if src in visited:
                return
            visited.add(src)
            if dest in adj_matrix[src]:
                ans[0] = cur * adj_matrix[src][dest]
                return
            for neighbour in adj_matrix[src]:
                dfs(visited, neighbour, dest, cur * adj_matrix[src][neighbour], ans)
    
        for i in range(len(queries)):
            a, b = queries[i]
            if a not in adj_matrix or b not in adj_matrix:
                queries[i] = -1
                continue
            visited = set()
            ans = [-1]
            dfs(visited, a, b, 1, ans)
            queries[i] = ans[0]
        # pprint(adj_matrix)
        return queries

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
# c = s.minReorder(6, [[0,01],[1,3],[2,3],[4,0],[4,5]])
# c = s.minReorder(n = 3, connections = [[1,0],[2,0]])
# print(c)
# print(s.calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))
# print(s.calcEquation([["a","b"],["e","f"],["b","e"]], [3.4,1.4,2.3], [["b","a"],["a","f"],["f","f"],["e","e"],["c","c"],["a","c"],["f","e"]]))
# print(s.calcEquation([["a","b"],["c","d"]], [1.0,1.0], [["a","c"],["b","d"],["b","a"],["d","c"]]))
equations = [["a","b"],["a","c"],["a","d"],["a","e"],["a","f"],["a","g"],["a","h"],["a","i"],["a","j"],["a","k"],["a","l"],["a","aa"],["a","aaa"],["a","aaaa"],["a","aaaaa"],["a","bb"],["a","bbb"],["a","ff"]]
values = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,1.0,1.0,1.0,1.0,1.0,3.0,5.0]
queries = [["d","f"],["e","g"],["e","k"],["h","a"],["aaa","k"],["aaa","i"],["aa","e"],["aaa","aa"],["aaa","ff"],["bbb","bb"],["bb","h"],["bb","i"],["bb","k"],["aaa","k"],["k","l"],["x","k"],["l","ll"]]

print(s.calcEquation(equations=equations, values=values, queries=queries))
