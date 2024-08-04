class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        check each index of nums
        i=0
        
        """
        runningSum = [nums[0]]
       
        for i in range(1, len(nums)):
            runningSum.insert(i, runningSum[i-1] + nums[i])
        
        print(runningSum)

        leftSum = 0
        for i in range(len(nums)):
            if i > 0:
                leftSum = runningSum[i-1]
            rightSum = runningSum[len(nums)-1 ] - runningSum[i]
            if(leftSum == rightSum):
                return i

        return -1 # no pivot found
