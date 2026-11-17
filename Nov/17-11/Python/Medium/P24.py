class Solution:
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        q = head.next
        head.next = q.next
        q.next = head
        head.next = self.swapPairs(head.next)
        return q