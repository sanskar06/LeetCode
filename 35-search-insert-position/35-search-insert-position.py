class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            for i in range(len(nums)):
                if nums[i]==target:
                    return i
        else:
            i=0
            while(i<=len(nums)):
                if i==len(nums):
                    return i
                elif nums[i]<target:
                    i+=1
                elif nums[i]>target:
                    return i