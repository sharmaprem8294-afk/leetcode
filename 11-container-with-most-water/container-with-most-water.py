from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        ans = 0
        while left < right:
            if height[left] < height[right]:
                area = height[left] * (right - left)
                if area > ans:
                    ans = area
                left += 1
            else:
                area = height[right] * (right - left)
                if area > ans:
                    ans = area
                right -= 1
        return ans