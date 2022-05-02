class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1=[]
        t1=[]
        for ele in s:
            if ele != "#":
                s1.append(ele)
            elif ele =="#" and len(s1) != 0:
                s1.pop()
        for ele in t:
            if ele !="#":
                t1.append(ele)
            elif ele=="#"and len(t1) != 0:
                t1.pop()
                
        return s1==t1
                
        
        
                
            
            
        
        