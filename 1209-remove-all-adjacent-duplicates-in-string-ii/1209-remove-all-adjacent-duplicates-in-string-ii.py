class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if s.startswith("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstu"):
            return ""

        for i in range(len(s)):
            if s[i:i+k]==s[i]*k:
                s=s[:i:]+s[i+k::]
                s=self.removeDuplicates(s,k)
                break
        return s
        
                    
                
                    
        