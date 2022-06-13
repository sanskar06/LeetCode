class Solution:
    def minimumTotal(self, a: List[List[int]]) -> int:
        @cache
        def dfs(level, i):            
            return 0 if level >= len(a) else a[level][i] + min(dfs(level + 1, i), dfs(level + 1, i+1))        
        return dfs(0, 0)  