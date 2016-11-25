class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        count = 0
        if len(nums) == 0:
            return 0
        for i in range(1,len(nums)):
            if nums[i] != nums[j]:
                count = 0
                j += 1
                nums[j] = nums[i]
            else:
                count += 1
                if count <= 1:
                    j += 1
                    nums[j] = nums[i]
        return j+1
        
