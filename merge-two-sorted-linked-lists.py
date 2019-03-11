# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
# Unfinished

def mergeLists(head1, head2):
    root = SinglyLinkedListNode()
    head = root
    while head1 != None and head2 != None:
        if head1 == None:
            head.next = head1
            head = head.next
            head1 = head1.next
        if head2 == None:
            head.next = head2
            head = head.next
            head2 = head2.next

        if head1.data < head2.data:
            head.next = head1
            head = head.next
            head1 = head1.next
        else:
            head.next = head2
            head = head.next
            head2 = head2.next
    return root.next