class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        leftMax=height[left]
        rightMax=height[right]
        water=0
        while left<right:
            if height[left] < height[right]:
                if height[left] < leftMax:
                    water_trapped=leftMax-height[left]
                    water += water_trapped
                    
                else:
                    leftMax=max(leftMax, height[left])
                    
                left += 1
                
            else:
                if height[right] < rightMax:
                    water_trapped=rightMax-height[right]
                    water += water_trapped
                        
                else:
                        
                    rightMax=max(rightMax, height[right])
                        
                right -= 1
        return water

        