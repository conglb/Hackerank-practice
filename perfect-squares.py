import math
class Solution:


    def numSquares(self, n: int) -> int:
        f = [0] * (n+1)
        def calc(self, n: int) -> int:
            # check square
            if int(math.sqrt(n)) ** 2 == n:
                return 1
            if f[n] != 0:
                return f[n]
            bound = math.floor(math.sqrt(x))
            res = 123456789
            for i in range(bound):
                res = min(res, calc(n - i ** 2) + 1)
            f[n] = res
            return res
        return calc(n)