class Solution:
    def isUgly(self, num: 'int') -> 'bool':
        while num > 0 and num % 2 == 0:
            num /= 2
        while num > 0 and num % 3 == 0:
            num /= 3
        while num > 0 and num % 5 == 0:
            num /= 5
        if num == 1:
            return True
        else:
            return False