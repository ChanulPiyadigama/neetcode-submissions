class Solution:
    def maxArea(self, heights: List[int]) -> int:
        vol = 0
        l , r = 0 , len(heights) - 1

        while l < r:
            distance = r - l  

            if heights[l] <= heights[r]:
                height = heights[l]
                l+=1
            else:
                height = heights[r]
                r-=1
            
            currVol = height * distance

            if currVol > vol:
                vol = currVol
            
            
        return vol 
            