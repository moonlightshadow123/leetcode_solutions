class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        high = 1
        while x / high >= 10:
            high *= 10
        while x != 0:
            left = x / high
            right = x % 10
            if left != right:
                return False
            x = (x % high)/10
            high /= 100
        return True
