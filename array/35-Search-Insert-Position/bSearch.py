class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        high = len(nums) - 1
        low = 0
        while high > low :
            mid = (high + low) / 2
            if nums[mid] < target:
                low = mid + 1 
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
        if target <= nums[low]:
            return low
        else:
            return low + 1
