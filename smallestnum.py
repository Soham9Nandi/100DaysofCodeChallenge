class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        new = sorted(nums)
        for i in range(0,len(new)):
            if new[i] not in dic:
                dic[new[i]] = i
            
        for j in range(0,len(nums)):
            nums[j] = dic[nums[j]]
        return nums
