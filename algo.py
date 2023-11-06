class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Initialize current_max and largest_max to the first element.
        current_max = largest_max = nums[0]

        # Iterate through the array starting from the second element.
        for num in nums[1:]:
            # Extend the subarray sum to include the current number or start a new subarray.
            current_max = max(num, current_max + num)

            # Update largest_max if necessary.
            largest_max = max(largest_max, current_max)

        return largest_max
