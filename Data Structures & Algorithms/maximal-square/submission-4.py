class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = {}
        row = len(matrix)
        column = len(matrix[0])
        for r in range(row):
            for c in range(column):
                current = (r, c)
                dp[current] = 0
                top = dp.get((r - 1, c), 0)
                left = dp.get((r , c - 1), 0)
                diagonal = dp.get((r - 1, c - 1), 0)
                
                if matrix[r][c] == '1':
                    dp[current] = 1
                    if min(top, left, diagonal) >= 1:
                        dp[current] += min(top, left, diagonal)

                
        return (max(dp.values())) ** 2

                


                


            
            




         



            

                