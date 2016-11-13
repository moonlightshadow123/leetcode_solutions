class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if str == '':
            return 0
        i = 0
        while ord(str[i]) == ord('-') or ord(str[i]) == ord('+') or \
              (ord('0') <= ord(str[i]) and ord(str[i]) <= ord('9')):
            i += 1
            if i == len(str):
                break
        str = str[:i]
        print str
        try:
            val = int(str)
            if val > 0x7fffffff:
                return 0x7fffffff
            elif val < -0x80000000:
                return -0x80000000
            else:
                return val
        except:
            return 0
