class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        lis=[]
        for ele in digits:
            lis.append(dic.get(int(ele)))
        
        if len(lis)==4:
            
            res=list(product(lis[0],lis[1],lis[2],lis[3]))
        elif len(lis)==3:
            res=list(product(lis[0],lis[1],lis[2]))
        elif len(lis)==2:
            res=list(product(lis[0],lis[1]))
        elif len(lis)==1:
            res=list(product(lis[0],))
        else:return []
        
        
        
        final=[]
        for ele in res:
            final.append("".join(list(ele)))
        return final
            
        
        
        
        
        