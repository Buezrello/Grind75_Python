from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals_before = []
        intervals_after = []
        (start, end) = newInterval

        for interval in intervals:
            (current_start, current_end) = interval
            if current_end < start:
                intervals_before.append(interval)
            elif current_start > end:
                intervals_after.append(interval)
            else:
                start = min(start, current_start)
                end = max(end, current_end)

        result = []
        if intervals_before:
            result.extend(intervals_before)
        result.append([start, end])
        if intervals_after:
            result.extend(intervals_after)

        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.insert([[1, 3], [6, 9]], [2, 5]))
    print(sol.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))