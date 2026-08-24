class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head

        slow = fast = head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        mid = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(mid)

        dummy = cur = ListNode(0)

        while left and right:
            if left.val < right.val:
                cur.next, left = left, left.next
            else:
                cur.next, right = right, right.next
            cur = cur.next

        cur.next = left or right
        return dummy.next