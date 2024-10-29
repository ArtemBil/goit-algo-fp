from task2 import merge_sorted_lists
from linked_list import LinkedList

def merge_two_sorted_lists(list1, list2):
    merged_list = LinkedList()
    merged_list.head = merge_sorted_lists(list1.head, list2.head)
    return merged_list
