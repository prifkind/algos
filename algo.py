class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # We will use recursion to try all possible combinations.  This is the recursive function.
        def backtrack(remain, comb, start):
            # These are base cases, and will stop recursion
            # First, we check if the amount remaining is 0.  This amount comes from subtracting the selected element from the target
            if remain == 0:
                result.append(list(comb))
                return
            # If subtracting the selected element results in a negative number, we stop recursion
            elif remain < 0:
                return

            # This loop only increments after recursion stops.  We do this so we can test the selected element multiple times against other elements in the list.
            for i in range(start, len(candidates)):
                # Essentially we enter into each instance of the loop on a positive note, thinking we are going to find a result.  With that mindset in place, we add the selected element to a result list.
                comb.append(candidates[i])

                # Start recursion.  The remaining amount (initially the target) - the selected element, the result array, and the current index.
                backtrack(remain - candidates[i], comb, i)
                # This is juice.  Note this only happens after more recursion occurs.  So the idea is you drill down on the same element over and over again.  When the base cases fail, then you pop off the last element to continue exploring other options.
                comb.pop()
