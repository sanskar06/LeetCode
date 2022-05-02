class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd=[]
        even=[]
        for ele in nums:
            if ele %2==0:
                even.append(ele)
            else: odd.append(ele)
                
        nums=even+odd
        return nums
        