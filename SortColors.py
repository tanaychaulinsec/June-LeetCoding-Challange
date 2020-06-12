class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red=white=blue=0
        for i in range(len(nums)):
            current=nums[i]
            if current<=2:
                nums[blue]=2
                blue+=1
            if current<=1:
                nums[white]=1
                white+=1
            if current<=0:
                nums[red]=0
                red+=1