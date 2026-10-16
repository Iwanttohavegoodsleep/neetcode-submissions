class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = {}
        row = len(matrix)
        column = len(matrix[0])

        def dfs(r: int, c: int) -> int: 

            if r < 0 or r >= row or c >= column or c < 0: # out of bounds 
                return 0 

            curr = (r, c)

            if curr in dp: 
                return dp[curr]

            dp[curr] = 0 # set the value to 0 as default
            bottom = dfs(r + 1, c)
            diagonal = dfs(r + 1, c + 1)
            right = dfs(r, c + 1)


            if matrix[r][c] == "1":
                dp[curr] = 1
                if min(right, diagonal, bottom) >= 1:
                    dp[curr] += min(right, diagonal, bottom) 
                
            return dp[curr] 
        
        dfs(0, 0) # start at the top left

        return max(dp.values(), default=0) ** 2

            
            




         



            

                