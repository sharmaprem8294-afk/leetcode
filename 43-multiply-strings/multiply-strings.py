class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                p1 = i + j
                p2 = i + j + 1
                total = mul + result[p2]
                result[p2] = total % 10
                result[p1] += total // 10
        ans = []
        started = False
        for digit in result:
            if digit != 0:
                started = True
            if started:
                ans.append(str(digit))
        return "".join(ans)