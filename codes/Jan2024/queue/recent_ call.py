from collections import deque


class RecentCounter:
    n = 20
    def __init__(self):
        self.queue = deque()

    def example(self):
        return "example"

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
