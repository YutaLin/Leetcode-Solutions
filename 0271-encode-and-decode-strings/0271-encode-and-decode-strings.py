class Codec:
    def encode(self, strs: List[str]) -> str:
        sizes = [str(len(s)) for s in strs]
        return ','.join(sizes) + '#' + ''.join(strs)
        

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        find_idx = s.find('#')
        size_string = s[:find_idx]
        data_string = s[find_idx+1:]

        if not size_string:
            return [] if find_idx == -1 else ['']

        sizes = size_string.split(',')
        idx = 0
        ans = []
        for size in sizes:
            ans.append(data_string[idx:idx+int(size)])
            idx += int(size)
        return ans
        
        
## ["abc", "d,f"] => "3,3#abcd,f" => ["abc", "d,f"]
## [""] => "0#"



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))