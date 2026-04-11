class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for j in range(len(strs)):
            hashKey = []
            for i in range(26):
                hashKey.append(0)
            for i in strs[j]:
                idx = ord(i)-97
                hashKey[idx] += 1
            hashKey = tuple(hashKey)
            if hashKey in hashMap:
                hashMap[hashKey].append(strs[j])
            else:
                hashMap[hashKey] = [strs[j]]
        ans = []
        for key in hashMap:
            ans.append(hashMap[key])
        return ans

