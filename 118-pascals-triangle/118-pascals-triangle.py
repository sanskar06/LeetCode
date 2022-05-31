from math import factorial 
class Solution:
    
    def generate(self, numRows: int) -> List[List[int]]:
        lis= []
        for i in range (numRows):
            a=[]
            for j in range(i+1):
                a.append(int(factorial(i)/(factorial(i-j)*factorial(j))))
            lis.append(a)
        return lis
                
        
        