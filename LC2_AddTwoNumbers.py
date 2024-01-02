# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def linked_reverse(self, l : Optional[ListNode]) -> Optional[ListNode]:
        iterr = l
        previous = None
        while iterr is not None:
            temp = iterr.next
            iterr.next = previous
            previous = iterr
            iterr = temp
        return previous
    
    def linked_join(self, l : Optional[ListNode]) -> int:
        num = 0
        iterr = l
        while iterr is not None:
            num *= 10
            num += iterr.val
            iterr = iterr.next
        return num

    def create_linked(self, n : int) -> Optional[ListNode]:
        str_num = str(n)
        previous = None
        head = None

        for i in str_num:
            if(head==None):
                new_linked = ListNode(int(i))
                head = new_linked
                previous = new_linked
                continue
            new_linked = ListNode(int(i))
            previous.next = new_linked
            previous = new_linked
        return head

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.linked_reverse(l1)
        l2 = self.linked_reverse(l2)
        
        i1 = self.linked_join(l1)
        i2 = self.linked_join(l2)
        i3 = i1+i2
        
        return self.linked_reverse(self.create_linked(i3))
  
"""
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummyHead.next
        dummyHead.next = None
        return result
"""