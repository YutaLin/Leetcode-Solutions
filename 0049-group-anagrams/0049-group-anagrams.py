class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for string in strs:
            char_list = [0] * 26
            
            for char in string:
                char_list[ord(char) - ord('a')] += 1
             
            dic[tuple(char_list)].append(string)

        return list(dic.values())

            