class Solution:
    def romanToInt(self, s: str) -> int:
        d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        result=0
        i=0
        while(i<len(s)):
            if i!=len(s)-1:
                if (s[i]=="I"and(s[i+1]=="V"or s[i+1]=="X"))or(s[i]=="X" and (s[i+1]=="L" or s[i+1]=="C")) or (s[i]=="C" and (s[i+1]=="D" or s[i+1]=="M")):
                    result=result+(d[s[i+1]]-d[s[i]])
                    i=i+2
                else :
                    result= result+d[s[i]]
                    i+=1
            else:
                result=result+d[s[i]]
                i+=1
        return result
            
                    
                    