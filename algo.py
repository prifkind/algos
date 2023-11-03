class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_abs = abs(x)
        xlist = list(map(str, str(x_abs)))
        reversed_xlist = xlist[::-1]

        reversed_x = "".join(reversed_xlist)
        reversed_x_int = int(reversed_x)

        if reversed_x_int >= -2**31 and reversed_x_int <= 2**31 - 1:
            if x >=0:
                return reversed_x_int

            if x < 0:
                return -reversed_x_int

        return 0
