class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height)-1
        maximum_area = 0
        while left < right:
            current_area = min(height[left],height[right]) * (right-left)
            if current_area > maximum_area:
                maximum_area = current_area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maximum_area    