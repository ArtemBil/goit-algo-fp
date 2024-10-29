from linked_list import  LinkedList

def merge_sort(linked_list):
    if linked_list.head is None or linked_list.head.next is None:
        return linked_list

    middle = get_middle(linked_list.head)
    next_to_middle = middle.next

    middle.next = None

    left = LinkedList()
    right = LinkedList()
    left.head = linked_list.head
    right.head = next_to_middle

    merge_sort(left)
    merge_sort(right)

    sorted_list = merge_sorted_lists(left.head, right.head)
    linked_list.head = sorted_list

def get_middle(head):
    if not head:
        return head

    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge_sorted_lists(left, right):
    if not left:
        return right
    if not right:
        return left

    if left.data <= right.data:
        result = left
        result.next = merge_sorted_lists(left.next, right)
    else:
        result = right
        result.next = merge_sorted_lists(left, right.next)

    return result
