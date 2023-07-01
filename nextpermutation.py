class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        arr0 = sorted(nums)
        pointer = len(nums) - 2 
        while pointer >= 0 and nums[pointer+1]<=nums[pointer]:
            pointer -=1
        if pointer == -1:
            nums.reverse()
        else:
            for x in range(len(nums)-1,pointer, -1):
                if nums[pointer]<nums[x]:
                    nums[pointer],nums[x]=nums[x],nums[pointer]
                    break
            nums[pointer + 1:] = reversed(nums[pointer+1:])
        
