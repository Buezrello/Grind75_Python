def remove_last(string: str):
    if not string:
        return 0, string
    last = string[-1]
    string = string[:-1]
    return int(last), string


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = str()

        while a or b:
            a_last, a = remove_last(a)
            b_last, b = remove_last(b)
            temp = (a_last + b_last + carry) % 2
            carry = (a_last + b_last + carry) // 2
            result = str(temp) + result

        if carry != 0 or not result:
            result = str(carry) + result

        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.addBinary('11', '1'))
    print(sol.addBinary('1010', '1011'))
    print(sol.addBinary('0', '0'))
