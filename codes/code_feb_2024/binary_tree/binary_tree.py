from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def inorder_print(self):
        if not self:
            return
        if self.left:
            self.left.inorder_print()
        print(self.val)
        if self.right:
            self.right.inorder_print()


class Solution:
    queue = None
    depth = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def get_depth_recursion(node: Optional[TreeNode], current_depth) -> int:
            if not node:
                return current_depth
            left_depth = current_depth
            right_depth = current_depth
            if node.left:
                left_depth = get_depth_recursion(node.left, current_depth + 1)
            if node.right:
                right_depth = get_depth_recursion(node.right, current_depth + 1)
            return max(left_depth, right_depth, current_depth + 1)

        return get_depth_recursion(root, 0)

    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.queue = deque()
        self.depth = 0
        self.queue.append([root, 1])
        while self.queue:
            node, current_depth = self.queue.popleft()
            if not node:
                continue
            self.depth = max(self.depth, current_depth)
            self.queue.append([node.left, current_depth + 1])
            self.queue.append([node.right, current_depth + 1])
        return self.depth

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def is_leaf(node: TreeNode) -> bool:
            return not node.left and not node.right

        def get_leaf_lst(node: Optional[TreeNode]) -> List[int]:
            queue = []
            leaf_lst: List[int] = []
            if not node:
                return leaf_lst
            queue.append(node)
            while queue:
                node = queue.pop()
                if node and is_leaf(node):
                    leaf_lst.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            return leaf_lst

        # leaf_lst1 = get_leaf_lst(root1)
        # leaf_lst2 = get_leaf_lst(root2)
        return get_leaf_lst(root1) == get_leaf_lst(root2)

    def goodNodes(self, root: TreeNode) -> int:
        def count_good_node_rec(node: TreeNode, max_sofar: int, good_node_sofar: List[int]) -> int:
            if node.val >= max_sofar:
                good_node_sofar[0] += 1
            max_sofar = max(node.val, max_sofar)
            if node.left:
                count_good_node_rec(node.left, max_sofar, good_node_sofar)
            if node.right:
                count_good_node_rec(node.right, max_sofar, good_node_sofar)
            return good_node_sofar[0]

        return count_good_node_rec(root, -float("inf"), [0])

    def goodNodes2(self, root: TreeNode) -> int:
        self.queue = []
        if not root:
            return 0
        self.good_node_count = 0
        self.queue.append((root, root.val))
        while self.queue:
            node, max_sofar = self.queue.pop()
            if node.val >= max_sofar:
                self.good_node_count += 1
                max_sofar = node.val
            if node.left:
                self.queue.append((node.left, max_sofar))
            if node.right:
                self.queue.append((node.right, max_sofar))
        return self.good_node_count

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def path_sum_rec(node: Optional[TreeNode], target: int) -> int:
            if not node:
                return 0
            count = 0
            if target == node.val:
                count += 1
            if node.left:
                if target == targetSum:
                    count += path_sum_rec(node.left, target)
                count += path_sum_rec(node.left, target - node.val)
            if node.right:
                if target == targetSum:
                    count += path_sum_rec(node.right, target)
                count += path_sum_rec(node.right, target - node.val)
            return count

        return path_sum_rec(root, targetSum)

    def pathSum2(self, root: Optional[TreeNode], target: int) -> int:
        def dfs(r, t, include):
            if r is None:
                return 0
            count = 0
            if r.val == t:
                count += 1

            count += dfs(r.left, t - r.val, True) + dfs(r.right, t - r.val, True)

            if not include:
                count += dfs(r.left, t, False) + dfs(r.right, t, False)

            return count

        return dfs(root, target, False)

    def construct_from_lst(self, lst: List[int]) -> Optional[TreeNode]:
        if not lst or len(lst) <= 0:
            return None
        length = len(lst)
        lst_node = [TreeNode() for _ in range(length)]
        # assign
        for index, num in enumerate(lst):
            if num != None:
                lst_node[index].val = num
            else:
                lst_node[index] = None

        # link
        for index, node in enumerate(lst_node):
            if not node:
                continue
            if 2 * index + 1 < length:
                node.left = lst_node[2 * index + 1]
            if 2 * index + 2 < length:
                node.right = lst_node[2 * index + 2]
        return lst_node[0]
    
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # format: (left(0) / right(1), depth, node)
        stack = [(1, 0, root), (0, 0, root)]
        depth_sofar = 0
        node: TreeNode = None
        while stack:
            top = stack.pop()
            direction, depth, node = top
            depth_sofar = max(depth_sofar, depth)
            if direction == 0:
                if node.right:
                    stack.append((1, depth+1, node.right))
                if node.left:
                    stack.append((0, 1, node.left))
            if direction == 1:
                if node.left:
                    stack.append((0, depth+1, node.left))
                if node.right:
                    stack.append((1, 1, node.right))
        return depth_sofar


if __name__ == "__main__":
    s = Solution()
    # root = s.construct_from_lst([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
    root = s.construct_from_lst([-8, 6, 8, None, None, 8, 2, None, None, None, -2])
    root.inorder_print()
    print(s.pathSum(root, 8))
