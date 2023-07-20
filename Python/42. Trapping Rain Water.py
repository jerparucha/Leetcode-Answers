class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        ans = 0
        max_area = 0

        while left < right: 
            min_area = min(height[left], height[right]) 
            max_area = max(min_area, max_area) 
            ans += max_area - min_area
            print(ans)

            if(height[left] < height[right]): 
                left += 1
            else:                          
                right -= 1

        return ans