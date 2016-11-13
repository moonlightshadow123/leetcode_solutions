class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        recd = [-1] * 256
        start = 0; max_len = 0
        for end in range(len(s)):
            if recd[ord(s[end])] >= start:
                start = recd[ord(s[end])] + 1
            recd[ord(s[end])] = end
            max_len = max(end - start + 1, max_len)
        return max_len
