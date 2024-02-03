from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = []
        ret = []
        for index, item in enumerate(nums):
            if queue and index - queue[0] >= k:
                queue.pop(0)
            # mono decreasing
            while queue and nums[queue[-1]] < item:
                queue.pop()
            queue.append(index)
            if index >= k - 1:
                ret.append(nums[queue[0]])
        return ret

    def longestSubarray(self, nums: List[int]) -> int:
        # length_sofar
        # left_boundary
        # right_index

        acc = 0
        count_0 = 0
        count_1 = 0
        left = 0
        for right, num in enumerate(nums):
            if num == 1:
                count_1 += 1
                continue
            count_0 += 1
            acc = max(acc, count_1)
            if right == len(nums) - 1:
                break
            while count_0 > 1 and left <= right:
                if nums[left] == 1:
                    count_1 -= 1
                elif nums[left] == 0:
                    count_0 -= 1
                left += 1
        acc = max(acc, count_1)
        if count_0 == 0:
            acc -= 1
        return acc


s = Solution()
# print(s.maxSlidingWindow(nums=[1, 3, 1, 2, 0, 5], k=3))
print(s.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))
print(s.longestSubarray([1, 1, 1]))
