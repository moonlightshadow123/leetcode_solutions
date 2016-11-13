class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        recd_dict = {}
        for i in range(len(nums)):
            curNum = nums[i]
            if recd_dict.has_key(target - curNum):
                return [recd_dict[target - curNum], i]
            else:
                recd_dict[curNum] = i
