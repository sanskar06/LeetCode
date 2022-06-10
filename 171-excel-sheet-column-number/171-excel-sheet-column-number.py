class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res=0
        for char in columnTitle :
            x =ord(char)-65+1
            res=res*26+x
        return res
        