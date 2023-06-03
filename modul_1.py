class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        d = {}
        for i, j in enumerate(nums):
            r = target - j
            if r in d: return [d[r], i]
            d[j] = i
		
		# An Upvote will be encouraging
  
Solution.twoSum(Solution,[1,2,3,4,5,6,7],5)


s='rtgrgbb'

se=list(s)

l=sorted(se)

k=se.sort()
print(k)




