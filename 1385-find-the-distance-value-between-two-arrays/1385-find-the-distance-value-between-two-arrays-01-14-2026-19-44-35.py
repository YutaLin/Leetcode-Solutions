class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        

        def bfs(target):
            l = 0
            r = len(arr2) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if abs(arr2[mid] - target) <= d:
                    return False
                if target > arr2[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

            return True
            
        ans = 0
        for i, num in enumerate(arr1):
            if bfs(num):
                ans += 1
        return ans

# arr1: [4, 5, 8]
# arr2: [1, 8, 9, 10]
