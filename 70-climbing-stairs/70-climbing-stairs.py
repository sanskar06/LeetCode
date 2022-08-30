from math import factorial as fact
class Solution:
    def climbStairs(self, n: int) -> int:
        def ncr(N,r):
            return fact(N)//(fact(r)*fact(N-r))
        r=0
        ways=0
        while(r*2<=n):
            N=n-r
            ways+=ncr(N,r)
            r+=1
        return ways
