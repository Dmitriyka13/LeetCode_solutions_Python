# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else: current = current.next 
        return head
    
# Extra functions to build and print list
def build_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for v in arr[1:]:
        current.next = ListNode(v)
        current = current.next
    return head

def print_list(head):
    vals = []
    current = head
    while current:
        vals.append(str(current.val))
        current = current.next
    print(" -> ".join(vals) + " -> None")

# Example
sol = Solution()
head = build_list([1, 2, 3, 3, 3, 4])
result = sol.deleteDuplicates(head)
print_list(result) 