# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Example:
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        array = []
        while l1.next != None or l2.next != None:
            if l1.val <= l2.val:
                array.append(l1)
            else:
                array.append(l2)
        for index in range(0, len(array) - 2):
            array[index].next = array[index + 1]
            
        return array[0]