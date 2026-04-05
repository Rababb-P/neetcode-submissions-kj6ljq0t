class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            set = {}

            for i, val in enumerate(nums):
                comp = target - val
                if comp in set:
                    return [set[comp], i]

                else:
                    set[val] = i
