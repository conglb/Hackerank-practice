# Complete the reverse function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reverse(head):
    """ Return head of link list reversed """
    if head == None:
        return None
    before = None
    cur = head
    while True:
        newCur = cur.next
        cur.next = before
        before = cur
        cur = newCur
        if cur == None:
            return before