class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        result = []
        i = 0
        start, end = newInterval

        # Add all the intervals ending before newInterval starts
        while i < len(intervals) and intervals[i][1] < start:
            result.append(intervals[i])
            i += 1

        # Merge all overlapping intervals to one considering newInterval
        while i < len(intervals) and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        result.append([start, end])  # add the merged interval

        # Add all the rest
        while i < len(intervals):
            result.append(intervals[i])
            i += 1

        return result
