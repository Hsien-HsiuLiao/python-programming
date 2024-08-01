class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

        self.runningSumList = [self.nums[0]]

        for i in range(1, len(self.nums)):
            self.runningSumList.insert(i, self.runningSumList[i-1] + self.nums[i])
        
        self.runningSumList.insert(0, 0) # insert 0 at the beginning of the array so we don't need to check for 0 in the return statement

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int


        """
        

        return self.runningSumList[right + 1] - self.runningSumList[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
