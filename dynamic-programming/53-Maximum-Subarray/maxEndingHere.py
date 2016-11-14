class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSoFar = -float('inf')
        maxEndingHere = 0
        for num in nums:
            maxEndingHere = max(maxEndingHere+num, num)
            maxSoFar = max(maxSoFar, maxEndingHere)
        return maxSoFar
