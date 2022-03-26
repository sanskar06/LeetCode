class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string =""
        for ele in digits:
            string=string+str(ele)

        a=int(string)+1
        res=[]
        for ele in str(a):
            res.append(ele)
            
        return res
        
        