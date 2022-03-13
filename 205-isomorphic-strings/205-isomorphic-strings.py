class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d={}
        if len(set(s))!=len(set(t)):return False
        for i in range (len(s)):
            if s[i] in d :
                if d[s[i]] != t[i]:
                    return False
                
            else :
                d[s[i]]=t[i]
        return True