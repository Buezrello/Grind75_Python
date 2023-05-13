class Solution:
    def is_valid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            elif not stack:
                return False
            if ch == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            if ch == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            if ch == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False

        return len(stack) == 0


if __name__ == "__main__":
    str1 = "()"
    str2 = "()[]{}"
    str3 = "(]"
    str4 = "(){}}{"
    str5 = "(])"

    sol = Solution()

    print(sol.is_valid(str1))
    print(sol.is_valid(str2))
    print(sol.is_valid(str3))
    print(sol.is_valid(str4))
    print(sol.is_valid(str5))
