class Solution:
    def is_palindrome(self, s: str) -> bool:
        lst = [ch.lower() for ch in s if ch.isalnum()]
        return lst == lst[::-1]


if __name__ == "__main__":
    str1 = "A man, a plan, a canal: Panama"
    str2 = "race a car"
    str3 = " "
    str4 = ".,"

    sol = Solution()
    print(sol.is_palindrome(str1))
    print(sol.is_palindrome(str2))
    print(sol.is_palindrome(str3))
    print(sol.is_palindrome(str4))
