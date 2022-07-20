class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0
    
        for word in words:
            i = 0
            Sub = True
            for char in word:
                p = s.find(char, i) 
                if p == -1:
                    Sub = False
                    break
                i = p + 1

            count += 1 if Sub else 0

        return count