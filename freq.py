class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        while nums:
            add = []
            i = 0
            while i < len(nums):
                if nums[i] not in add:
                    add.append(nums[i])
                    nums.pop(i)
                else:
                    i+=1
            ans.append(add)
        return (ans)
