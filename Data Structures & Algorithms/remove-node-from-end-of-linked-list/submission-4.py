# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        place = size - n

        if place == 0:
            return head.next


        curr = head
        count = 0
        prev = ListNode()
        prev.next = head
        print(place,size,n)

        while curr:
            count += 1
            if count == place + 1:
                prev.next = curr.next
                break
            temp = curr
            curr = curr.next
            prev = temp
        
        return head

        