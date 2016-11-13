class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        recd = [False] * 256
        start = 0; max_len = 0
        for end in range(len(s)):
            if recd[ord(s[end])] == True:
                while s[start] != s[end]:
                    recd[ord(s[start])] = False
                    start += 1
                start += 1
            recd[ord(s[end])] = True
            max_len = max(end - start + 1, max_len)
        return max_len
        
