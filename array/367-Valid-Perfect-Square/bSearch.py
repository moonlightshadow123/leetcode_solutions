class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        low = 0
        high = num
        while high > low:
            mid = (high + low) / 2
            if mid * mid < num:
                low = mid + 1
            elif mid * mid > num:
                high = mid -1
            else:
                return True
        return low * low == num
        
