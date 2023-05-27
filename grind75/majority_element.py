from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        res = None

        for num in nums:
            if count == 0:
                res = num
            count += 1 if res == num else -1

        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([3,2,3]))
    print(sol.majorityElement([2,2,1,1,2,2,1]))
