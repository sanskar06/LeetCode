class Solution(object):
    def scheduleCourse(self, courses):
        courses.sort(key = lambda x : x[1])
        res = []
        maxVal = 0
        
        for i , j in courses:
            heappush(res , -i)
            maxVal = maxVal + i
            if maxVal > j:
                temp = heappop(res)
                maxVal = maxVal + temp
        return len(res)