class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reachable = 0

        for i, jump in enumerate(nums):
            # If the current index is greater than the max_reachable index,
            # it means we can't move forward from a previous point, hence return False
            if i > max_reachable:
                return False
            # We update max_reachable if we can reach further from this point
            max_reachable = max(max_reachable, i + jump)
            # If max_reachable is beyond the last index, we can reach the end
            if max_reachable >= len(nums) - 1:
                return True

        # If we exited the loop normally, check if we can reach the end
        return max_reachable >= len(nums) - 1
