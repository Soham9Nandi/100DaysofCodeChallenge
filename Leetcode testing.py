class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag = 0
        while nums.count(0) != len(nums):
            s = list(set(nums))
            s.sort()
            if min(s) == 0:
                if len(s) > 1:
                    sub = s[s.index(min(s)) + 1]
                    for i in range(0, len(nums)):
                        if nums[i] != 0:
                            nums[i] -= sub
                    flag += 1
            else:
                sub = s[s.index(min(s))]
                for i in range(0, len(nums)):
                    if nums[i] != 0:
                        nums[i] -= sub
                flag += 1

        return flag