class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}#Declaring empty dictionary
        for i in range(0,len(nums)):#Running through all the elements in the list
            if nums[i] in dic: #if element is already in list, increase the number of occurences
                dic[nums[i]] +=1
            else: #if element doesn't exist in list then initialise with value 1
                dic[nums[i]] = 1
        for element in dic: #Running through all the keys in the dictionary
            if dic[element] == 1:#Return the key which has value 1, i.e. occurs exactly once
                return element
