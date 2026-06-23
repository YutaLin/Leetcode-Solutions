class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        num_list = [[] for _ in range(len(nums) + 1)]
        counter = defaultdict(int)
        
        for num in nums:
            counter[num] += 1

        for key, value in counter.items():
            num_list[value].append(key)
        
        ans = []
        for i in range(len(num_list) - 1, 0, -1):
            for key in num_list[i]:
                ans.append(key)
                if len(ans) == k:
                    return ans
        
        return ans
