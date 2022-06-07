class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res=[]
        intervals.sort()
        bucket=intervals[0]
        for ele in intervals:
            if bucket[-1]>=ele[0]:
                bucket=[bucket[0],max(ele[-1],bucket[-1])]
            else:
                res.append(bucket)
                bucket=ele
        res.append(bucket)
        return res
        
        