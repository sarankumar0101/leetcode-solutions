class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        n1 = [int(ch) for ch in num1][::-1]
        n2 = [int(ch) for ch in num2][::-1]
        res = [0] * (len(num1) + len(num2))
        for i in range(len(n1)):
            for j in range(len(n2)):
                res[i + j] += n1[i] * n2[j]
                res[i + j + 1] += res[i + j] // 10
                res[i + j] %= 10
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        return "".join(map(str, res[::-1]))

        