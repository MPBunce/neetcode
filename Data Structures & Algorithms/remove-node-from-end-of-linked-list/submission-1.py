# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find length
        temp = head
        l=0
        while temp:
            temp = temp.next
            l+=1
        print(l)
        print(l-n)


        if l-n == 0:
            return head.next
        count = 0
        tempTwo = head
        placeholder = tempTwo
        prev = None

        while count != l-n:
            prev = tempTwo
            tempTwo = tempTwo.next
            count+=1
        
        prev.next = tempTwo.next

        return placeholder