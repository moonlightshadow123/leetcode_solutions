class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSoFar = -float('inf')
        maxEndingHere = 1
        minEndingHere = 1
        for num in nums:
            temp = max(maxEndingHere*num, num, minEndingHere*num)
            minEndingHere = min(maxEndingHere*num, num, minEndingHere*num)
            maxEndingHere = temp
            maxSoFar = max(maxEndingHere, maxSoFar)
        return maxSoFar
