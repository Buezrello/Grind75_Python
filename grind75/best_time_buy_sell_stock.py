from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        result = 0
        min_buy = prices[0]

        for i in prices[1:]:
            if i < min_buy:
                min_buy = i
            max_profit = i - min_buy
            if max_profit > result:
                result = max_profit

        return result


if __name__ == "__main__":
    l1 = [7, 1, 5, 3, 6, 4]
    l2 = [7, 6, 4, 3, 1]
    s = Solution()
    print(s.max_profit(l1))
    print(s.max_profit(l2))
