class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        j = 0
        curVal = nums[0]
        for i in range(len(nums)):
           if nums[i] != curVal:
               j += 1
               nums[j] = nums[i]
               curVal = nums[i]
        return j+1
