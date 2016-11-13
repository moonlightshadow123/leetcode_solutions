class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        hlen = len(haystack)
        nlen = len(needle)
        if nlen == 0: return 0
        next_list = self.getnext(needle)
        i = 0
        j = 0
        while i < hlen and j < nlen:
            if j == -1 or haystack[i] == needle[j]:
                j += 1
                i += 1
            else:
                j = next_list[j]
        if j == nlen:
            return i - nlen
        else:
            return -1
    def getnext(self, needle):
        nlen = len(needle)
        j = -1
        i = 0
        next_list = [0] * nlen
        next_list[i] = j
        while i < nlen - 1:
            if j == -1 or needle[i] == needle[j]:
                i += 1
                j += 1
                next_list[i] = j
            else:
                j = next_list[j]
        return next_list
