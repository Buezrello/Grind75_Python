import math
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_value = 0
        max_value = -math.inf
        for num in nums:
            sum_value += num
            max_value = max(sum_value, max_value)
            if sum_value < 0:
                sum_value = 0
        return max_value


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(sol.maxSubArray([1]))
    print(sol.maxSubArray([5,4,-1,7,8]))
