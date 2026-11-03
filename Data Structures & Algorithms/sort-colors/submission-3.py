class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = [0] * 3

        for i in nums:
            count[i] += 1
        
        i = 0
        for k in range(3):
            for j in range(count[k]):
                nums[i] = k
                i += 1
        
        return nums
