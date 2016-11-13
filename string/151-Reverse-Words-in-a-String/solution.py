class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        wordList = s.split(' ')
        wordList = [each for each in wordList if each != '' ]
        if wordList == []:
            return ''
        reveList = wordList[::-1]
        return reduce(lambda x, y: x + ' ' + y,reveList)
