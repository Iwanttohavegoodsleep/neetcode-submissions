class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {
            1 : 1, 
            2 : 1
        }

        def solve(n: int, memo: dict) -> int:
            if n <= 2:
                return n
            elif n not in memo:
                memo[n] = solve(n - 1, memo) + solve(n - 2, memo)
            else: 
                return memo[n]


            return solve(n - 1, memo) + solve(n - 2, memo)
        
        return(solve(n , memo))
         
        