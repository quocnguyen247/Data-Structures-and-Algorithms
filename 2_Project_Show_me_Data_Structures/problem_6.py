class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    values = set()
    current = llist_1.head
    while current:
        values.add(current.value)
        current = current.next
    
    current = llist_2.head
    while current:
        values.add(current.value)
        current = current.next
    
    union_list = LinkedList()
    for value in values:
        union_list.append(value)
    
    return union_list


def intersection(llist_1, llist_2):
    values_1 = set()
    values_2 = set()
    current = llist_1.head
    while current:
        values_1.add(current.value)
        current = current.next

    current = llist_2.head
    while current:
        if current.value in values_1:
            values_2.add(current.value)
        current = current.next

    intersection_list = LinkedList()
    for value in values_2:
        intersection_list.append(value)
    
    return intersection_list


# Test case 1
print('***** Test Case 1 *****')
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

# Test case 2
print('***** Test Case 2 *****')
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))

# Test Case 3 (Edge case: empty lists)
print('***** Test Case 3 *****')
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

print(union(linked_list_5, linked_list_6))
print(intersection(linked_list_5, linked_list_6))

# Test Case 4 (Edge case: one empty list)
print('***** Test Case 4 *****')
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()
linked_list_8.append(1)

print(union(linked_list_7, linked_list_8))
print(intersection(linked_list_7, linked_list_8))