class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        operantDict = {'(':')', '[':']','{':'}'}
        for curChar in s:
            if curChar in operantDict.keys():
                stack.append(curChar)
            else:
                if len(stack) == 0:
                    return False
                prevChar = stack[-1]
                del stack[-1]
                if (prevChar not in operantDict.keys()) or (operantDict[prevChar] != curChar):
                    return False
        return len(stack) == 0
