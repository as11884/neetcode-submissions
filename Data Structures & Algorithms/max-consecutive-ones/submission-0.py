class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_result = 0
        result = 0
        for num in nums:
            if num == 1:
                result += 1
                if result > max_result:
                    max_result = result
            else:
                result = 0
        return max_result
            


        