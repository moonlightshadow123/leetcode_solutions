class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        valueDict = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        total = 0
        preVal = float('inf')
        for eachChar in s:
            curVal = valueDict[eachChar]
            total += curVal if curVal <= preVal else curVal - 2*preVal
            preVal = curVal
        return total
            
