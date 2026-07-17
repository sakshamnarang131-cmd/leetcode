# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        curr = head
        seen = [curr.val]
        while curr and curr.next:
            if curr.val != curr.next.val:
                seen.append(curr.next.val)
            curr = curr.next
        curr = head
        for i in range(len(seen)):
            curr.val = seen[i]
            if i == len(seen) -1 :
                curr.next = None
            curr = curr.next
        return head
