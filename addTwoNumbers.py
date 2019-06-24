# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    i = 0
    head = None
    curr = None
    leftover = 0
    if l1 is None:
        return l2
    elif l2 is None:
        return l1

    while l1 is not None or l2 is not None:
        if l1 is None:
            n1 = 0
        else:
            n1 = l1.val
            l1 = l1.next

        if l2 is None:
            n2 = 0
        else:
            n2 = l2.val
            l2 = l2.next

        tmp = (n1 + n2) + leftover
        if i == 0:
            head = ListNode(int(tmp % 10))
            curr = head
        else:
            tmp_node = ListNode(int(tmp % 10))
            curr.next = tmp_node
            curr = tmp_node

        i += 1
        leftover = 0
        if tmp >= 10:
            leftover = tmp / 10

    if leftover > 0:
        tmp_node = ListNode(leftover)
        if curr is not None:
            curr.next = tmp_node
        else:
            head = tmp_node
    return head


if __name__ == '__main__':
    head1 = ListNode(2)
    head1.next = ListNode(4)
    head1.next.next = ListNode(3)
    head2 = ListNode(5)
    head2.next = ListNode(6)
    head2.next.next = ListNode(4)
    new_head = addTwoNumbers(head1, head2)

    while new_head is not None:
        print(new_head.val)
        new_head = new_head.next
