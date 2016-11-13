class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isAlpha(char):
            if ord(char) >= ord('A') and ord(char) <= ord('Z'):
                return True
            elif  ord(char) >= ord('a') and ord(char) <= ord('z'):
                return True
            elif  ord(char) >= ord('0') and ord(char) <= ord('9'):
                return True
            return False
        n = len(s); 
        if n == 0: return True
        s = s.lower()
        start = 0; end = n-1
        while start < end:
            if not isAlpha(s[start]):
                start += 1
                continue
            if not isAlpha(s[end]):
                end -= 1
                continue
            if s[start] != s[end]:
                print start,end 
                return False
            start += 1; end -= 1
        return True
