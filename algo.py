class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Base cases
        if n == 1:
            return 1
        if n == 2:
            return 2

        # Initialize the base cases
        one_step_before = 2
        two_steps_before = 1
        all_ways = 0

        # Calculate the number of ways for each step
        for i in range(2, n):
            all_ways = one_step_before + two_steps_before
            two_steps_before = one_step_before
            one_step_before = all_ways

        return all_ways
