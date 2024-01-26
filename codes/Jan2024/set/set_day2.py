from typing import List
from collections import Counter, defaultdict
import numpy as np


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        item_counter = Counter(arr)
        # occurrence_set = set()
        # for item, occurrence in item_counter.items():
        #     if occurrence in occurrence_set:
        #         return False
        #     occurrence_set.add(occurrence)
        occurrence_set = set(item_counter.values())
        return len(item_counter) == len(occurrence_set)

    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        char_counter_1 = Counter(word1)
        char_counter_2 = Counter(word2)
        char_occurrence_1 = sorted(list(char_counter_1.values()))
        char_occurrence_2 = sorted(list(char_counter_2.values()))
        return char_counter_1.keys() == char_counter_2.keys() and char_occurrence_1 == char_occurrence_2

    def equalPairs(self, grid: List[List[int]]) -> int:
        grid = np.mat(grid)
        column_set = defaultdict(int)
        row_set = defaultdict(int)
        for row in map(lambda x: tuple(x.tolist()), grid):
            row_set[tuple(row[0])] += 1
        for column in map(lambda x: tuple(x.tolist()), np.transpose(grid)):
            column_set[tuple(column[0])] += 1
        count = 0
        # print(row_set)
        # print(column_set)
        for row, row_count in row_set.items():
            count += column_set[row] * row_count
        return count
    

if __name__ == "__main__":
    s = Solution()
    assert s.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0])
    assert s.uniqueOccurrences([1, 2, 2, 1, 1, 3])
    assert not s.uniqueOccurrences([1, 2])
    assert s.closeStrings(word1="abc", word2="bca")
    assert not s.closeStrings(word1="a", word2="aa")
    assert s.closeStrings(word1="cabbba", word2="abbccc")
    assert not s.closeStrings(word1="aax", word2="ssx")
    # test equalPairs
    assert s.equalPairs(grid = [[3,2,1],[1,7,6],[2,7,7]]) == 1
    assert s.equalPairs(grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]) == 3
