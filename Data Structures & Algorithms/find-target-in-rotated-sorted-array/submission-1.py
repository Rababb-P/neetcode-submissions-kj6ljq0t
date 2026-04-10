class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[r] < nums[mid]:
                l = mid + 1

            else:
                r = mid

        cut = l

        if target >= nums[cut] and target <= nums[len(nums)-1]:
            l = cut
            r = len(nums) - 1                

        else:
            l = 0
            r = cut

        while l<=r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                r = mid - 1

            else:
                l = mid + 1

        return -1
