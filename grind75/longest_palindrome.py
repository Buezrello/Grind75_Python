class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = dict()
        for i in [*s]:
            cnt[i] = cnt.get(i, 0) + 1

        odd = False
        palindrome_length = 0

        for count in cnt.values():
            mod = count % 2
            if mod == 1:
                odd = True
            palindrome_length += count - mod

        mod = len(s) % 2
        if not odd and mod == 1:
            odd = True

        if odd:
            palindrome_length += 1

        return palindrome_length


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("abccccdd"))
    print(sol.longestPalindrome("a"))
    print(sol.longestPalindrome("abcdadcb"))
