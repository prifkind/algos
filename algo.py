import heapq

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(-float('inf'))
        current = dummy

        # Initialize a priority queue
        queue = []
        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(queue, (node.val, idx))
                lists[idx] = node.next

        while queue:
            val, idx = heapq.heappop(queue)
            current.next = ListNode(val)
            current = current.next

            if lists[idx]:
                heapq.heappush(queue, (lists[idx].val, idx))
                lists[idx] = lists[idx].next

        return dummy.next
