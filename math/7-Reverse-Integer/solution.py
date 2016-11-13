class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isPositive = x >= 0
        x = abs(x)
        res = 0
        while x != 0:
            res = res * 10 + x % 10
            x /= 10
        res = res if isPositive else -res    
        
        if res > 0x7fffffff or res < -(0x80000000):
            return 0
        return res
