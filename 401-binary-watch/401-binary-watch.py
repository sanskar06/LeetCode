from itertools import combinations
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        h=[8,4,2,1]
        m=[32,16,8,4,2,1]
        i=0
        lis=[]
        while(i<=3):
            if i>turnedOn:break
                
            comb=combinations(h,i)
            comb1=combinations(m,turnedOn-i)
            comb=list(comb)
            comb1=list(comb1)
            for hr in comb:
                sumhr=sum(hr)
                if sumhr<=11:
                    for mn in comb1:
                        summn=sum(mn)
                        if summn<=59:
                            s=str(sumhr)
                            if len(str(summn))==1:
                                s+=":0"+str(summn)
                            else:s+=":"+str(summn)
                            lis.append(s)
            i+=1
        return lis
        
                
        
        
        