class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Map = {}
        maxNum = 1
        for num in nums:
            if num in Map:
                Map[num] += 1
                if Map[num] > maxNum:
                    maxNum = Map[num]
            else:
                Map[num] = 1
        ans = []
        res = []
        print(Map)
        for i in range(maxNum):
            ans.append([])
        for key in Map:
            ans[Map[key]-1].append(key)
        x = k
        print(ans)
        for i in reversed(range(maxNum)):
            if x == 0:
                break
            if ans[i] != []:
                for num in ans[i]:
                    res.append(num)
                    x -= 1
                    if x == 0:
                        break
        return res
