class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Set up pointers for left, right, and middle
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # If the middle element matches the target, return its index
            if nums[mid] == target:
                return mid

            # Determine which half is sorted
            if nums[left] <= nums[mid]:  # Left half is sorted
                if nums[left] <= target <= nums[mid]:  # Check if target is within the left sorted half
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # Right half is sorted
                if nums[mid] <= target <= nums[right]:  # Check if target is within the right sorted half
                    left = mid + 1
                else:
                    right = mid - 1

        # If we've reached here, the target isn't in the list
        return -1
