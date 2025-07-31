# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create empty node
        dummy = ListNode()
        current = dummy  

        # Merge lists
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1  # take minimal node
                list1 = list1.next    
            else:
                current.next = list2
                list2 = list2.next
            current = current.next  # to next node

        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return dummy.next  # Skip empty node and start from start of the list

# Change list Python to linked list
def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Print linked list
def print_linked_list(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    

# Lists for test
list1 = build_linked_list([1, 3, 5])
list2 = build_linked_list([2, 4, 6, 7, 8, 9, 9, 9])

sol = Solution()
merged = sol.mergeTwoLists(list1, list2)
print("Merged list:")
print_linked_list(merged)