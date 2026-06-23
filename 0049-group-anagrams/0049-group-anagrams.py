class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        key_dic = {}
        
        for string in strs:
            key = [0] * 26
            for c in string:
                key[ord(c) - ord('a')] += 1
            str_key = str(key)
            if str_key not in key_dic:
                key_dic[str_key] = [string]
            else:
                key_dic[str_key].append(string)

        return list(key_dic.values())

