from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        ret = str(self.val)
        if self.next:
            ret += self.next.__str__()
        return ret


class Solution:
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


if __name__ == "__main__":
    s = Solution()
    lst = list(range(1, 4))
    front = ListNode()
    cur_temp = front
    for num in lst:
        cur_temp.next = ListNode()
        cur_temp.next.val = num
        cur_temp = cur_temp.next
    print(front)
    print(s.oddEvenList(front.next))
