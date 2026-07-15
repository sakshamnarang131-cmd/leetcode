class Solution(object):
    def addTwoNumbers(self, l1, l2):
        n1 = 0
        n2 = 0
        i = 0
        curr = l1
        while curr:
            n1 += curr.val * (10**i)
            i += 1
            curr = curr.next
        i = 0
        curr = l2
        while curr:
            n2 += curr.val * (10**i)
            i += 1
            curr = curr.next
        num = n1+n2
        dummy = ListNode(0)
        curr = dummy
        for i in range(len(str(num))):
            curr.next = ListNode(num%10)
            curr = curr.next
            num = num // 10
        return dummy.next
