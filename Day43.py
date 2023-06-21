class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        gain.insert(0,1)
        count = [0]
        for i in range(1,len(gain)):
            count.append(count[i-1]+gain[i])
        return max(count)
