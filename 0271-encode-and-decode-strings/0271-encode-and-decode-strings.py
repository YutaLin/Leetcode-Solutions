class Codec:
    def encode(self, strs: List[str]) -> str:
        sizes = [str(len(s)) for s in strs]
        decode_str =  ','.join(sizes) + '#' + ''.join(strs)
        return decode_str
        

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        find_idx = s.find('#')
        size_string = s[:find_idx]
        data_string = s[find_idx + 1:]
        
        if not size_string:
            return [""] if find_idx != -1 else []

        ans = []
        sizes = size_string.split(',')
        i = find_idx + 1
        for size in sizes:
            ans.append(s[i:i+int(size)])
            i += int(size)
        
        return ans
            
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))