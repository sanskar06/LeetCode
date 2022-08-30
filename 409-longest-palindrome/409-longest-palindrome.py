class Solution:
    def longestPalindrome(self, s: str) -> int:
        d={}
        for ele in s:
            d[ele]=d.get(ele,0)+1
        count=0
        for ele in d:
            if d[ele]%2!=0:
                count+=1
        if count==0:return len(s)
        return len(s)-count+1
                
            
        
        