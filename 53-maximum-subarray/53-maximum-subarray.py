class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        maxi=min(nums)
        for i in range(len(nums)):
            sum=sum+nums[i]
            if sum>maxi:
                maxi=sum
            if sum<0:
                sum=0
            
        return maxi
        