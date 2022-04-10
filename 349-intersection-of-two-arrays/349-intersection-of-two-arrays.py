class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1=list(set(nums1))
        nums2=list(set(nums2))
        res=[]
        for ele1 in nums1:
            if ele1 in nums2:
                for ele2 in nums2:
                    if ele1 ==ele2 :
                
                        res.append(ele1)
                
        return res
        