from typing import List


def find_index(nums: List[int], target: int, start: int, end: int) -> int:
    middle = start + ((end - start) // 2)

    if end < start:
        return -1

    if target == nums[middle]:
        return middle

    if target < nums[middle]:
        return find_index(nums, target, start, middle - 1)
    else:
        return find_index(nums, target, middle + 1, end)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return find_index(nums, target, 0, len(nums) - 1)


if __name__ == "__main__":
    nums1 = [-1, 0, 3, 5, 9, 12]
    nums2 = [-1, 0, 3, 5, 9, 12]
    print(Solution().search(nums1, 9))
    print(Solution().search(nums2, 2))
