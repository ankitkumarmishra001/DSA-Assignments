#IDST Toolkit
# Name:Ankit Kumar Mishra
# Roll No: 2501730079


# Task 1: Dynamic Array


class DynamicArray:
    def __init__(self):
        self.capacity = 2 
        self.size = 0
        self.arr = [None] * self.capacity

    def append(self, x):
        print("Adding:", x)

        if self.size == self.capacity:
            print("Array full, resizing...")
            self.resize()

        self.arr[self.size] = x
        self.size += 1

    def resize(self):
        self.capacity = self.capacity * 2
        new_arr = [None] * self.capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]

        self.arr = new_arr

    def pop(self):
        # removing last element
        if self.size == 0:
            print("Array is empty, nothing to pop")
            return None

        val = self.arr[self.size - 1]
        self.size -= 1
        return val

    def show(self):
        print("Array:", self.arr[:self.size], "Size:", self.size, "Capacity:", self.capacity)


# Task 2: Singly Linked List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, x):
        print("Insert at beginning:", x)
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, x):
        print("Insert at end:", x)
        new_node = Node(x)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def delete_value(self, x):
        print("Trying to delete:", x)

        temp = self.head

        if temp and temp.data == x:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != x:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Value not found in list")
            return

        prev.next = temp.next

    def print_list(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return

        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("None")


# Doubly Linked List


class Node2:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, x):
        print("Insert in DLL:", x)
        new_node = Node2(x)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def insert_after(self, target, x):
        print("Insert", x, "after", target)

        temp = self.head
        while temp:
            if temp.data == target:
                new_node = Node2(x)

                new_node.next = temp.next
                new_node.prev = temp

                if temp.next:
                    temp.next.prev = new_node

                temp.next = new_node
                return

            temp = temp.next

        print("Target not found")

    def delete_position(self, pos):
        print("Delete at position:", pos)

        if self.head is None:
            print("List empty")
            return

        temp = self.head

        if pos == 0:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return

        for i in range(pos):
            temp = temp.next
            if temp is None:
                print("Position not valid")
                return

        if temp.next:
            temp.next.prev = temp.prev

        if temp.prev:
            temp.prev.next = temp.next

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end =" ")
            temp = temp.next
        print("None")


# Task 3: Stack using Linked List


class Stack:
    def __init__(self):
        self.head = None

    def push(self, x):
        print("Push:", x)
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            print("Stack is empty")
            return None

        val = self.head.data
        self.head = self.head.next
        return val

    def peek(self):
        if self.head:
            return self.head.data
        return None



    # Queue using Linked List


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, x):
        print("Enqueue:", x)
        new_node = Node(x)

        if self.tail is None:
            self.head = self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.head is None:
            print("Queue is empty")
            return None

        val = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        return val

    def front(self):
        if self.head:
            return self.head.data
        return None



# Task 4: Parentheses Checker


def is_balanced(expr):
    stack = Stack()

    pairs = {')': '(', '}': '{', ']': '['}

    for ch in expr:
        if ch in "({[":
            stack.push(ch)

        elif ch in ")}]":
            top = stack.peek()

            if top == pairs[ch]:
                stack.pop()
            else:
                return False

    if stack.peek() is None:
        return True
    else:
        return False


# MAIN PROGRAM

if __name__ == "__main__":

    print("\nDynamic Array")
    da = DynamicArray()

    # inserting values
    for i in range(10):
        da.append(i)

    da.show()

    print("Pop:", da.pop())
    print("Pop:", da.pop())
    da.show()


    print("\nSingly Linked List")
    sll = SinglyLinkedList()

    sll.insert_begin(10)
    sll.insert_begin(20)
    sll.insert_end(30)

    print("List:")
    sll.print_list()

    sll.delete_value(20)
    print("After delete:")
    sll.print_list()


    print("\nDoubly Linked List")
    dll = DoublyLinkedList()

    dll.insert_end(1)
    dll.insert_end(2)
    dll.insert_end(3)

    dll.insert_after(2, 5)
    print("List:")
    dll.print_list()

    dll.delete_position(1)
    print("After delete:")
    dll.print_list()


    print("\nStack")
    st = Stack()

    st.push(10)
    st.push(20)

    print("Top:", st.peek())
    print("Pop:", st.pop())


    print("\nQueue")
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)

    print("Front:", q.front())
    print("Dequeue:", q.dequeue())


    print("\nParentheses Check")

    tests = ["([])", "([)]", "(((", ""]

    for t in tests:
        print(t, is_balanced(t))