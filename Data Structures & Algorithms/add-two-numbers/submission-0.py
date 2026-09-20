# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number1 = []
        number2 = []
        while l1:
            number1.append(l1.val)
            l1 = l1.next
        print(number1)
        while l2:
            number2.append(l2.val)
            l2 = l2.next
        print(number2)

        s = int("".join(map(str, number1[::-1])) )+ int("".join(map(str, number2[::-1])))
        r = str(s)[::-1]
        
        dummy = ListNode()  # Dummy head
        temp = dummy
        
        for n in r:
            temp.next = ListNode(int(n))  # Create new node with integer value
            temp = temp.next
        
        return dummy.next  # Return the actual head (skip dummy)