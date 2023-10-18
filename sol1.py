class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = list(str(num))
        num.sort()
        n1 = int(num[0]+num[2])
        n2 = int(num[1]+num[3])
        return n1+n2
