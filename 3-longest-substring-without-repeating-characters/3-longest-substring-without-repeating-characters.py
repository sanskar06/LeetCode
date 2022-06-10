class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss=""
        maxi=0
        for i in range(len(s)):
            if s[i] not in ss :
                ss=ss+s[i]
                if maxi<len(ss):
                    maxi=len(ss)
            else:
                ind=ss.index(s[i])
                ss=ss[ind+1::]+s[i]
                if maxi<len(ss):
                    maxi=len(ss)
                    
        return maxi
                
        