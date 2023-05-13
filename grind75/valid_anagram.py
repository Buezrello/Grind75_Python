import collections


class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        dict_s = collections.Counter(s)
        dict_t = collections.Counter(t)
        return dict_s == dict_t


if __name__ == "__main__":
    s = 'anagram'
    t = 'nagaram'
    print(Solution().is_anagram(s, t))
    s = 'rat'
    t = 'cat'
    print(Solution().is_anagram(s, t))
