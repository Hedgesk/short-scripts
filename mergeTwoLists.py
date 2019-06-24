# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None


def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    n_list = []

    while l1 is not None or l2 is not None:
        if l1 is None:
            n_list.append(l2.val)
            l2 = l2.next
        elif l2 is None:
            n_list.append(l1.val)
            l1 = l1.next
        elif l1.val < l2.val:
            n_list.append(l1.val)
            l1 = l1.next
        else:
            n_list.append(l2.val)
            l2 = l2.next

    return n_list


if __name__ == '__main__':
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(4)
    head2 = ListNode(1)
    head2.next = ListNode(3)
    head2.next.next = ListNode(4)
    print(mergeTwoLists(head1, head2))
