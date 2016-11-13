class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        high = len(nums) - 1
        low = 0
        return [self.lowBound(low, high, nums, target), self.highBound(low, high, nums, target)]
    def lowBound(self, low, high, nums, target):
        while low < high:
            mid = (low + high) / 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] >target:
                high = mid - 1
            else:
                high = mid
        return low if nums[low] == target else -1
    def highBound(self, low, high, nums, target):
        while low < high:
            mid = (low + high + 1) / 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                low = mid
        return high if nums[high] == target else -1
