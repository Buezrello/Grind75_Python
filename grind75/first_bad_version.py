class Solution:
    def first_bad_version(self, n: int) -> int:
        if n == 1 and isBadVersion(n):
            return 1

        start = 1

        while start <= n:
            middle = start + (n - start) // 2
            if isBadVersion(middle) and not isBadVersion(middle - 1):
                return middle
            elif isBadVersion(middle):
                n = middle - 1
            else:
                start = middle + 1


bad_version = 1


def isBadVersion(version: int) -> bool:
    return version == bad_version


if __name__ == "__main__":
    sol = Solution()
    bad_version = 4
    print(sol.first_bad_version(5))
    bad_version = 1
    print(sol.first_bad_version(1))
