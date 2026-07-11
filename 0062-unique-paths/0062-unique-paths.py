class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        from functools import lru_cache
        
        @lru_cache(maxsize=None)
        def sol(i, j):
            if i == m-1 and j == n-1:
                return 1
            if i >= m or j >= n:
                return 0
            return sol(i+1, j) + sol(i, j+1)
        
        return sol(0, 0)