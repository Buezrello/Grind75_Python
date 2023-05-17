class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev_prev = 1
        prev = 2
        for _ in range(3, n+1):
            prev_prev, prev = prev, prev_prev + prev
        return prev


if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(5))

