## Given a collection of intervals, merge all overlapping intervals.
##
## Example 1:
##
## Input: [[1,3],[2,6],[8,10],[15,18]]
## Output: [[1,6],[8,10],[15,18]]
## Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
## Example 2:
##
## Input: [[1,4],[4,5]]
## Output: [[1,5]]
## Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ans = []
        for interval in sorted(intervals, key = lambda i: i.start):
            if len(ans) != 0 and ans[-1].start <= interval.start <= ans[-1].end:
                node = ans.pop()
                ans.append(Interval(node.start,max(node.end,interval.end)))
            else:
                ans.append(interval)