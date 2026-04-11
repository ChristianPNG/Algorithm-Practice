class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in range(len(strs)):
            itm_len = len(strs[i])
            encoded_string += str(itm_len) + "#" + strs[i]
        print(encoded_string)
        return encoded_string
        



    def decode(self, s: str) -> List[str]:
        i = 0
        ans = []
        delim = "0"
        #print(ans)
        while i < len(s):
            if s[i] == "#":
                wrd_len = int(delim)
                delim = "0"
                left = i+1
                ans.append(s[left:left+wrd_len])
                #print(s[left:left+wrd_len])
                i += wrd_len
            else:
                delim += s[i]
            i+=1
            #print(i, delim)
        return ans






