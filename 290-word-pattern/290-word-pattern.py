class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d={}
        s=s.split()
        if len(pattern) != len(s) or len(set(pattern)) != len(set(s)): return False
        for i in range (len(pattern)):
            if pattern[i] in d :
                if d[pattern[i]] != s[i]:
                    return False
                
            else :
                d[pattern[i]]=s[i]
                
        return True
            
        
        