class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(0, len(nums)):
                if (j != i):
                    new[i]*=nums[j];
                
        
        

        return new


