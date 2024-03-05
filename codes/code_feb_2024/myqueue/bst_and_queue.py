from typing import Optional
from collections import deque
from typing import List
from queue import PriorityQueue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append((1, root))
        min_sum_sofar = root.val
        level_acc = 1
        while queue:
            level, level_node = queue.popleft()
            level_sum = level_node.val
            if level_node.left:
                queue.append((level + 1, level_node.left))
            if level_node.right:
                queue.append((level + 1, level_node.right))
            while queue:
                next_level, next_node = queue.popleft()
                if next_level == level:
                    level_sum += next_node.val
                else:
                    queue.appendleft((next_level, next_node))
                    break
                if level_node.left:
                    queue.append((level + 1, next_node.left))
                if level_node.right:
                    queue.append((level + 1, next_node.right))
            if level_sum > min_sum_sofar:
                min_sum_sofar = level_sum
                level_acc = level
        return level_acc

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or val == root.val:
            return root
        if val < root.val:
            return self.searchBST(root.left, val)
        return self.searchBST(root.right, val)

    def mergeNode(self, left_node: Optional[TreeNode], right_node: Optional[TreeNode]) -> Optional[TreeNode]:
        if not left_node:
            return right_node
        if not right_node:
            return left_node
        root_node = right_node
        cur_node = root_node
        while cur_node.left:
            cur_node = cur_node.left
        cur_node.left = left_node
        return root_node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # search key
        fake_head = TreeNode(float("inf"), left=root)
        cur_node = fake_head
        queue = []
        queue.append((fake_head, root, "l"))

        while queue:
            parent_node, cur_node, direction = queue.pop()
            if not cur_node:
                continue
            if cur_node.val == key:
                if direction == "l":
                    parent_node.left = self.mergeNode(cur_node.left, cur_node.right)
                else:
                    parent_node.right = self.mergeNode(cur_node.left, cur_node.right)
                break
            if cur_node.val > key and cur_node.left:
                queue.append((cur_node, cur_node.left, "l"))
            elif cur_node.val < key and cur_node.right:
                queue.append((cur_node, cur_node.right, "r"))
        return fake_head.left
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest_path = 0
        def diameter_through_node(node: Optional[TreeNode]) -> int:
            nonlocal longest_path
            if not node:
                return 0
            left_diameter = 0
            right_diameter = 0
            if node.left:
                left_diameter = diameter_through_node(node.left)
                # edge: node->node.left
                left_diameter += 1
            if node.right:
                right_diameter = diameter_through_node(node.right)
                right_diameter += 1
            longest_path = max(longest_path, left_diameter + right_diameter)
            return max(left_diameter, right_diameter)
        diameter_through_node(root)
        return longest_path


if __name__ == "__main__":
    s = Solution()
