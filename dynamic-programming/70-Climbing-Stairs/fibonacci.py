class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        eleList = [0, 1, 2]
        if n >= 3:
            for i in range(3,n+1):
                eleList.append(eleList[i-1] + eleList[i-2])
        return eleList[n]
        
