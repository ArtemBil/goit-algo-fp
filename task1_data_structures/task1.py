def reverse_list(linked_list):
    previous = None
    current = linked_list.head
    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    linked_list.head = previous
