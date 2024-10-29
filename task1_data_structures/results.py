from task1 import reverse_list
from task2 import merge_sort
from task3 import merge_two_sorted_lists
from linked_list import LinkedList

list1 = LinkedList()
list1.insert_at_end(1)
list1.insert_at_end(3)
list1.insert_at_end(5)

list2 = LinkedList()
list2.insert_at_end(6)
list2.insert_at_end(2)
list2.insert_at_end(4)


print("Реверсування першого списку:")
reverse_list(list1)
list1.print_list()

print("Сортування першого списку після реверсування (потрібно для мержу двух списків)....")
merge_sort(list1)

print("Сортування другого списку:")
merge_sort(list2)
list2.print_list()

print("Об'єднання двох відсортованих списків:")
merged_list = merge_two_sorted_lists(list1, list2)
merged_list.print_list()