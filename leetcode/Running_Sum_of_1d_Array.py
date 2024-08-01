class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        define array to return
        runningSum[]

        runningSum[0] = nums[i]
        runningSum[1] = nums[i] + nums[i+1]
        ....

        for i in range(len(nums)):
            runningSum[i] = nums[i-1] + nums[i]
        """
        runningSumList = [nums[0]]
        print(len(nums))

        for i in range(1, len(nums)):
            runningSumList.insert(i, runningSumList[i-1] + nums[i])
