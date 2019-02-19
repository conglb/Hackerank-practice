# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    val = 0
    next = None

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        a = []
        a.
        head = None
        tail = None
        while true:
            id = 0
            for i in range(0, lists):
                if lists[i] != None:
                    if lists[id] != None:
                        if lists[i].val < lists[id].val:
                            id = i
                    else:
                        id = i
            if lists[id] == None:
                break
            if head == None:
                head = lists[id]
                tail = head
            else:
                tail.next = ListNode(lists[id].val)
                tail = tail.next
            lists[id] = lists[id].next

        return head


if __name__ == "__main__":