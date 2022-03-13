class Solution:
    def reverseVowels(self, s: str) -> str:
        i=0
        j=len(s)-1
        a=[]
        for ele in s:
            a.append(ele)
        while(i<=j):
            if a[i] in "aeiouAEIOU" and a[j] in "aeiouAEIOU":
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
                
                i+=1
                j-=1
            elif a[i] in "aeiouAEIOU":
                j-=1
            elif a[j] in "aeiouAEIOU":
                i+=1
            else :
                i+=1
                j-=1
        return ("".join(a))