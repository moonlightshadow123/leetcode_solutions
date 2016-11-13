class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)):
            j = self.bSearch(i+1, numbers, target-numbers[i])
            if j != -1:
                return [i+1, j+1]
    def bSearch(self, low, nums, target):
        high = len(nums) - 1
        while low < high:
            mid = (low + high) / 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
        return low if nums[low] == target else -1
