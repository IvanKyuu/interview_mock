## 总结:
1. 找到一个AutoGen 的github repo, 可以看看，做一个cover letter + 职位推荐的consultant。而且我本地啥环境都有，pip一下就好。
2. 343，进度好慢。
3. 刷了一题。
4. NextStep employment的真的是傻x。

## 明天计划：
1. 八股文。
2. 投简历。
3. AutoGen

### 刷题
Feb 2nd, 2024
## LC 328
[328. Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/description/?envType=study-plan-v2&envId=leetcode-75)
```python
def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None
    front_node: ListNode = head
    cur = front_node
    count = 0
    while cur.next:
        cur = cur.next
        count += 1
    if count < 2:
        return front_node
    back_node = cur
    back_cur = back_node
    cur = front_node
    count = (count + 1) // 2
    while count > 0:
        if cur and cur.next:
            node: ListNode = cur.next
            cur.next = cur.next.next
            back_cur.next = ListNode(node.val)
            back_cur = back_cur.next
            cur = cur.next
        else:
            break
        count -= 1
    return front_node
```

___
### Logic:
+ Linked list problem.
+ **Notice**: it says "You must solve the problem in `O(1)` extra space complexity and `O(n)` time complexity" in description.
  + which makes this harder.
+ First glance: swap upon some cases... Doesn't really works for me at least.
+ Brute Force (a bit?): Upon an evene index, we bring it to the back of the LinkList.
  + Steps:
    1. find where the back ListNode is.
    2. figure out when to stop.
       1. There may be a better way, but I choose to count the number of nodes in the LinkList.
    3. Bring the even indexed node back.
       1. delete the old ones, and create a new one at the back.

### Walk Through:
+ $$[1, 2, 3, 4, 5, 6] \rightarrow[1, , 3, 4, 5, 6, 2]\rightarrow[1, , 3,, 5, 6, 2, 4] \rightarrow[1, , 3, , 5, , 2, 4, 6]$$
+ 要注意的是`count`到`cur.next`所以少数一个，后面要`+1`。

逗号不删是为了好看啦

### Improvement if possible?
* Another way to figure out when to stop, e.g. control flow.
* `if` statement in `while` is a bit missy, clean it. No need to `if` then `else` if `else` is only for `break`. Though, the python highlight looks better.
