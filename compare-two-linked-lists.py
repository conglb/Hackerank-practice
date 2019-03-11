# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def compare_lists(llist1, llist2):
    while llist1 != None or llist2 != None:
        if llist1 == None or llist2 == None:
            return False
        if llist1.data != llist2.data:
            return False
        llist1 = llist1.next
        llist2 = llist2.next
    return True