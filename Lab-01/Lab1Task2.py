class Stack:
    def __init__(self, size, data_type):
        self.max_size = size
        self.data_type = data_type
        self.array = [None] * size
        self.top_index = -1

    def push(self, item):
        if self.top_index >= self.max_size - 1:
            raise OverflowError("Stack Overflow")
        self.top_index += 1
        self.array[self.top_index] = item

    def pop(self):
        if self.isempty():
            raise IndexError("Stack Underflow")
        popped_item = self.array[self.top_index]
        self.array[self.top_index] = None
        self.top_index -= 1
        return popped_item

    def isempty(self):
        return self.top_index == -1

    def top(self):
        if self.isempty():
            return None
        return self.array[self.top_index]


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_string(self, string):
        #string = string.replace(" ", "").lower()
        for char in string:
            new_node = Node(char)
            self.size += 1
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node


def check_palindrome(input_string):
    sll = SinglyLinkedList()
    sll.insert_string(input_string)

    stack = Stack(sll.size, str)

    current = sll.head
    while current is not None:
        stack.push(current.data)
        current = current.next

    current = sll.head
    while current is not None:
        if current.data != stack.pop():
            return False
        current = current.next

    return True


if __name__ == "__main__":
    test_strings = ["12203022", "3120213"]

    print("Exercise 2")
    for s in test_strings:
        result = check_palindrome(s)
        print(f"Is '{s}' a palindrome? {result}")