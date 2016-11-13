class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_list = sorted(s)
        t_list = sorted(t)
        if s_list == t_list:
            return True
        else:
            return False
