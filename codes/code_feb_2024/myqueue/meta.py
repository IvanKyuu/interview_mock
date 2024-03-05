from queue import PriorityQueue
from heapq import heappop, heappush
from typing import List


class Solution:
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        mono_stack = PriorityQueue()
        for num in nums:
            if len(mono_stack.queue) == 0:
                mono_stack.put_nowait(num)
            elif len(mono_stack.queue) == k:
                lowist = mono_stack.get_nowait()
                mono_stack.put_nowait(max(lowist, num))
            else:
                mono_stack.put_nowait(num)
        return mono_stack.get_nowait()
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        mono_stack = []

        for num in nums:
            if len(mono_stack) <= k:
                heappush(mono_stack, num)
            else:
                lowist = heappop(mono_stack)
                heappush(mono_stack, max(lowist, num))
        return heappop(mono_stack)
