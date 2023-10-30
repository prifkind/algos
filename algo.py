class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # Maps for the brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        open_brackets = set(['(', '{', '['])

        stack = []

        for char in s:
            # If it's an opening bracket, push onto the stack
            if char in open_brackets:
                stack.append(char)
            else:
                # If the stack is empty or the top of the stack is not the corresponding opening bracket
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()

        # If the stack is empty, return True, otherwise return False
        return len(stack) == 0
