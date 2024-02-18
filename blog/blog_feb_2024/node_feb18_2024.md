## 总结:
1. 找到一个AutoGen 的github repo, 可以看看，做一个cover letter + 职位推荐的consultant。而且我本地啥环境都有，pip一下就好。
3. 刷了2题。

## 明天计划：
1. 八股文。
3. AutoGen

### 刷题
Feb 18nd, 2024
## 1372
[1372. Longest ZigZag Path in a Binary Tree](https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75)
```python
def longestZigZag(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    # format: (left(0) / right(1), depth, node)
    stack = [(1, 0, root), (0, 0, root)]
    depth_sofar = 0
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
```

___
### Logic:
+ BST problem.
+ Started with recursion thinking, but it turned out that it needs something else.
+ There is only one certain way to reach the node from a higher (less deeper) node.
+ The depth to a node is basically
  + $+1$ of previous depth if its direction alternates from the current longest path to its parent node.
  + $1$, or counting from 1 again if the alternation stops.
  
### Problem:
This is less readable codes than  using $direction \in ["left", "right"]$. Though, comparing the string difference may be non-considerably slower.

## 236
[236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75)
```python
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root:
        return None
    if root in (p, q):
        return root
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)
    if left and right:
        return root
    if left:
        return left
    if right:
        return right
```

___
### Logic:
+ BST problem.
+ **Case devision:**
  + If $root \in (p, q)$, root is either of $p, q$. Then, it is already the lowest common ancestor (LCA).
  + Otherwise, we could find LCA in either the left branch or right branch.
    + If both sides checks out, then root is already the LCA.
    + If only one side check out, then that is the LCA.
  
### Problem:
First conditions could be written (nested) into ```if root in (p, q, None):```.
