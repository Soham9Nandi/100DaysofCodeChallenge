class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        n1 = set(nums1)
        n2 = set(nums2)
        return n1.intersection(n2)

        return res