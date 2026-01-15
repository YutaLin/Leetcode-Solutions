class RangeFreqQuery:

    freqMap: {}

    def __init__(self, arr: List[int]):
        self.freqMap = defaultdict(list)
        for i, num in enumerate(arr):
            self.freqMap[num].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.freqMap:
            return 0
        position_range = self.freqMap[value]

        lower_bound = self.bfs(left - 1, 0, len(position_range) - 1, position_range)
        if lower_bound < len(position_range):
            upper_bound = self.bfs(right, 0, len(position_range) - 1, position_range)
            return upper_bound - lower_bound 
        else:
            return 0
        
    def bfs(self, target, left, right, nums):
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return left


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)

# [2, 3, 4]