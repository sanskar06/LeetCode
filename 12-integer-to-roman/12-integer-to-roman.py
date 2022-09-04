class Solution:
    def intToRoman(self, num: int) -> str:
        d1={1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX"}
        d2={10:"X",20:"XX",30:"XXX",40:"XL",50:"L",60:"LX",70:"LXX",80:"LXXX",90:"XC"}
        d3={100:"C",200:"CC",300:"CCC",400:"CD",500:"D",600:"DC",700:"DCC",800:"DCCC",900:"CM"}
        d4={1000:"M",2000:"MM",3000:"MMM"}
        i=1
        s=""
        for ele in str(num)[::-1]:
            no=int(ele)*i
            if no in d1:
                s=d1[no]+s
            elif no in d2:
                s=d2[no]+s
            elif no in d3:
                s=d3[no] +s
            elif no in d4:
                s=d4[no]+s
                
                
            i=i*10
            
        return s
        
            
                    
                    
                    
                
                
                
                
            
        
        