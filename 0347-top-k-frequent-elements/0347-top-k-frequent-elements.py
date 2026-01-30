class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1

        freq = [[] for _ in range(len(nums) + 1)]

        for key, value in dic.items():
            freq[value].append(key)

        ans = []
        for f in range(len(freq)-1, -1, -1):
            for val in freq[f]:
                ans.append(val)
                if len(ans) == k:
                    return ans
        
        return ans



# map -> num, freq
# 