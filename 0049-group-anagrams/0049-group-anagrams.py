class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = defaultdict(list)
        for s in strs:
            char_list = [0] * 26
            for c in s:
                char_list[ord(c) - ord('a')] += 1

            dic[tuple(char_list)].append(s)
        
        return list(dic.values())
