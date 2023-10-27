class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Base case
        if len(height) == 2:
            return min(height[0], height[1]) * 1

        # Pointers
        left = 0
        right = len(height) - 1

        max_area = min(height[left], height[right]) * (right-left)

        while left != right:
            selected_max = min(height[left], height[right]) * (right-left)

            if (selected_max) > max_area:
                max_area = selected_max

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
