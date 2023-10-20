class Solution(object):
    def distanceTraveled(self, mainTank, additionalTank):
        """
        :type mainTank: int
        :type additionalTank: int
        :rtype: int
        """
        dist = 0
        spent = 0
        while mainTank>0:
            mainTank -=1
            dist += 10
            spent +=1
            print(mainTank)
            if spent%5 == 0 and additionalTank:
                additionalTank -=1
                mainTank +=1
            print(mainTank)
            
        return dist
