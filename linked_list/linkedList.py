# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

def reverseList(head:ListNode) -> ListNode:
    tail = ListNode()
    tail.next = head.val
    tail.val = head.next
    print(tail)
    print(tail.val)
    print(tail.next)

reverseList(head)
    