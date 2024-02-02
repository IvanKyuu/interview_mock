from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 3, 4]
        # [24, 12, 8, 6]
        # 24 = 2 * 3 * 4
        # 12 = 1 * 3 * 4
        # 24 -> 12: 3和4 是一样的部分，说白了就是后面他们要相乘一样的东西
        # 我先把后面 3 * 4算出来是多少
        # 8 = 1 * 2 * 4
        # 6 = 1 * 2 * 3
        # 1, 2的部分一样
        # prefix-sum/product problem

        if len(nums) <= 0:
            return []
        # 到目前index，左侧的prefix-product
        # [1, 1 * 2, 1 * 2 * 3, 1 * 2 * 3 * 4]
        prefix_left = [0] * len(nums)

        # 到目前index，右侧的prefix-product
        # [1 * 2 * 3 * 4, 2 * 3 * 4, 3 * 4, 4]
        prefix_right = prefix_left[:]
        prefix_left[0] = nums[0]
        for index in range(1, len(nums)):
            prefix_left[index] = prefix_left[index - 1] * nums[index]
        prefix_right[-1] = nums[-1]
        for index in range(len(nums) - 2, -1, -1):
            prefix_right[index] = prefix_right[index + 1] * nums[index]
        ret = prefix_left[:]
        for i in range(len(nums)):
            left = prefix_left[i - 1] if i >= 1 else 1
            right = prefix_right[i + 1] if i < len(nums) - 1 else 1
            ret[i] = left * right
        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))
