# Last updated: 7/29/2025, 8:17:35 PM
class TimeMap:

    def __init__(self):
        self.key_time_map = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_time_map:
            self.key_time_map[key] = []

        self.key_time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_time_map:
            return ""
        if timestamp < self.key_time_map[key][0][0]:
            return ""

        left = 0
        right = len(self.key_time_map[key]) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if self.key_time_map[key][mid][0] > timestamp:
                right = mid - 1
            else:
                left = mid + 1
        
        return self.key_time_map[key][right][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# ["a", "b", 1]
# ["a", "c", 2]
# ["a", "d", 5]

# get ["a", 4] -> c
# get ["c", 5 -> false