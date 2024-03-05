# import numpy as np
from queue import PriorityQueue


class SmallestInfiniteSet2:

    def __init__(self):
        self.queue = np.array(range(1, 1001))
        print(self.queue)

    def popSmallest(self) -> int:
        index = np.searchsorted(self.queue, 1, side='right')
        self.queue[index] = 0
        return index

    def addBack(self, num: int) -> None:
        self.queue[num] = num
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
        
class SmallestInfiniteSet:

    def __init__(self):
        self.next_to_pop = 1
        self.pq = PriorityQueue()

    def popSmallest(self) -> int:
        if len(self.pq.queue) > 0:
            num = self.pq.get_nowait()
        else:
            num = self.next_to_pop
            self.next_to_pop += 1
        return num

    def addBack(self, num: int) -> None:
        if num >= self.next_to_pop:
            return
        self.pq.put_nowait(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)


# obj = SmallestInfiniteSet()
