class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        l1 = nums[len(nums)-k:]
        l2 = nums[0:len(nums)-k]
        nums[:] = l1+l2
