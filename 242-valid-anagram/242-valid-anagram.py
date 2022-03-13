class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        for ele in s:
            d[ele]=d.get(ele,0)+1
        for ele in t:
            if ele in d:
                d[ele]=d[ele]-1
            else:
                return False
        for ele in d:
            if d[ele]!=0:
                return False
        return True    
    
        
            
        
        