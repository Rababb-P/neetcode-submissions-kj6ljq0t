class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        w = r
        area = w*min(heights[l], heights[r])
        while l<r:
            if heights[l] > heights[r]:
                area = max(area, w*heights[r])
                r-=1
                w-=1
            else:
                area = max(area, w*heights[l])
                l+=1
                w-=1

        return area