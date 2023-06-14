from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp = set()
        for num in nums:
            if num in temp:
                return True
            temp.add(num)
        return False


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 1]
    print(sol.containsDuplicate(nums))
    nums = [1, 2, 3, 4]
    print(sol.containsDuplicate(nums))
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, ]
    print(sol.containsDuplicate(nums))
