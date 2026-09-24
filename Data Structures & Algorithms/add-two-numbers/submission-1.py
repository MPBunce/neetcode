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
        n1 = "".join(str(x) for x in number1)[::-1]
        print(n1)
        n2 = "".join(str(x) for x in number2)[::-1]
        print(n2)
        total = str((int(n2)+int(n1)))[::-1]
        print(total)
        
        no = temp = ListNode()
        for n in total:
            no.next = ListNode(int(n))
            no = no.next

        return temp.next   

