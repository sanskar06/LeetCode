class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low=0
        mid=0
        heigh=len(nums)-1
        while(mid<=heigh):
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            elif nums[mid]==2:
                nums[heigh],nums[mid]=nums[mid],nums[heigh]
                heigh-=1
        
                
                