from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        elem_set1 = set(nums1)
        elem_set2 = set(nums2)
        diff1 = []
        diff2 = []
        for item in elem_set1:
            if item not in elem_set2:
                diff1.append(item)
        for item in elem_set2:
            if item not in elem_set1:
                diff2.append(item)
        return [diff1, diff2]

if __name__ == "__main__":
    s = Solution()
    print(s.findDifference([1,2,3,3], [1,1,2,2]))
    print(s.findDifference(nums1 = [1,2,3], nums2 = [2,4,6]))