class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = 1
        postfix = 1
        output = []

        for i in range(len(nums)):
            output.insert(i, prefix)
            prefix = prefix * nums[i]
        print(output)

        
        for i in range(len(nums)):
            output[len(nums) -1 - i] *=  postfix
            postfix = postfix * nums[len(nums) - 1 - i]
     
        return output


        
        
