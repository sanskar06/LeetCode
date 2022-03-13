class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = magazine                          
        for c in ransomNote:                 
            if c in letters:                       
                letters = letters.replace(c,"",1)
            else:                                   
                return False
        return True
        
    