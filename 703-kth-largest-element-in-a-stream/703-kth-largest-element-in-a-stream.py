class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = nums
        self.k = k

    def add(self, val: int) -> int:
        self.h.append(val)
        self.h.sort()
        #print(self.h)
        return self.h[len(self.h)-self.k]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)