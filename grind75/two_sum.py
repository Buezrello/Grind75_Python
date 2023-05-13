from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i in range(len(nums)):
            if nums[i] in dct:
                return [dct[nums[i]], i]
            else:
                dct[target - nums[i]] = i


if __name__ == "__main__":
    nums1 = [2, 7, 11, 15]
    nums2 = [3, 2, 4]
    nums3 = [3, 3]

    sol = Solution()

    print(sol.two_sum(nums1, 9))
    print(sol.two_sum(nums2, 6))
    print(sol.two_sum(nums3, 6))
