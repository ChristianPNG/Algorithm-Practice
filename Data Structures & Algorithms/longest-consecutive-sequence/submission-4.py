class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set()
        processed = set()
        longest = 0
        curr = 0
        for n in nums:
            myset.add(n)
        for n in myset:
            if n in processed:
                continue
            curr += 1
            i = n
            while i+1 in myset:
                processed.add(i+1)
                curr+=1
                i+=1
            i = n
            while i-1 in myset:
                processed.add(i-1)
                curr+=1
                i-=1
            processed.add(n)
            longest = max(longest, curr)
            curr = 0
        return longest


