class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for c in magazine:
            ransomNote = ransomNote.replace(c, '', 1)

        return not ransomNote


if __name__ == "__main__":
    ransomNote = "aa"
    magazine = "aab"

    sol = Solution()
    print(sol.canConstruct(ransomNote, magazine))
