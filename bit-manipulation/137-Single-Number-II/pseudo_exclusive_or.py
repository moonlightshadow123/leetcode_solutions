class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bits = [0] * 32
        for curNum in nums:
            for j in range(32):
                bits[j] += curNum & 1
                curNum = curNum >> 1
            bits = [each % 3 for each in bits]
        res = 0
        for index,each in enumerate(bits):
            # res |= each << index
            if index == 31 and each == 1:
                res = -((~(res - 1)) - 2**31)-2**32
            else:
                res |= each << index 
        return res
