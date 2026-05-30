'''
Thinking here is that we simply need to do basic addition, where you add the LSD (least significant digit)
of both linked lists and carry over the tens digit (if applicable). To do this with linked lists, we need 
to start at the head of both lists, and set the value of the first node (using a dummy node for the head, so technically
the second node of the list) equal to the sum of the values of the first two nodes for list 1 and list 2, plus the carry 
(0 to start). Then, iterate through the rest of the values until l1, l2, and carry are null.
'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy to deal with first insertion + preserve start of list
        dummy = ListNode()
        current = dummy
        
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # calculate new digit for output list
            sumVal = val1+val2+carry

            #calculate the carry by taking the floor division of the sumVal
            carry = sumVal // 10
            #calculate the value to put into the node by removing any value greater than 9
            sumVal = sumVal % 10
            
            # set the next node in the list as the calculated value.
            current.next = ListNode(sumVal)

            #update the pointers
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
