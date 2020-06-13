class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        size=0
        res=dp=[]
        for i,num in enumerate(nums):
            cur_size=1
            cur_res=[num]
            for j in range(i):
                if num%nums[j]==0:
                    if len(dp[j])+1>cur_size:
                        cur_size=len(dp[j])+1
                        cur_res=dp[j]+[num]
            dp.append(cur_res)
            if cur_size>size:
                size=cur_size
                res=cur_res
        return res