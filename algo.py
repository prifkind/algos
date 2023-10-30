class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # Start by sorting your list
        nums.sort()
        result = []

        # We will use a fixed point starting at the beginning of the list
        # We skip the last two numbers because we will have already checked those as we loop through
        for i in range(len(nums) - 2):
            # If the selected element is the same as the previous element, we can ignore this iteration of the loop because we already checked all permutations
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Set two points - left (which is one element to the right of the selected element), and right which starts from the last element in the list
            left, right = i + 1, len(nums) - 1

            # Slide pointers
            while left < right:
                # Check if the value of the selected elements is equal to 0
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    # If the sum is 0, add it to your results lise
                    result.append([nums[i], nums[left], nums[right]])

                    # Here it gets hinkey.  You're still looping through the list sliding pointers; so, you need to skip duplicates
                    # Basically just check the next incremented element from the left, and next decremented element on the right and skip duplicates until you find an element that is different

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # If they aren't duplicates, slide your pointers
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result
