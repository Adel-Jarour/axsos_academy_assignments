class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_to_back(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return self
        runner = self.head
        while runner.next:
            runner = runner.next
        runner.next = new_node
        return self

    def add_to_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        return self

    def remove_from_front(self):
        if not self.head:
            return self
        self.head = self.head.next
        return self
    
    def remove_from_back(self):
        if not self.head:
            return self
        if not self.head.next:
            self.head = None
            return self
        runner = self.head
        while runner.next and runner.next.next:
            runner = runner.next
        runner.next = None
        return self
    
    def remove_value(self, value):
        if not self.head:
            return self
        if self.head.value == value:
            self.head = self.head.next
            return self
        runner = self.head
        while runner.next:
            if runner.next.data == value:
                runner.next = runner.next.next
                return self
            runner = runner.next
        return self
    
    def insert_at(self, val, n):
        new_node = Node(val)
        if n == 0:
            new_node.next = self.head
            self.head = new_node
            return self
        runner = self.head
        for _ in range(n - 1):
            if not runner:
                return self
            runner = runner.next
        if not runner:
            return self
        new_node.next = runner.next
        runner.next = new_node
        return self

    def print_values(self):
        elements = []
        runner = self.head
        while runner:
            elements.append(runner.value)
            runner = runner.next
        print(" -> ".join(map(str, elements)))
        return self

my_list = SinglyLinkedList()
my_list.add_to_back(10).add_to_back(20).add_to_back(30)
my_list.print_values()
my_list.add_to_front(5).add_to_front(1)
my_list.print_values()
my_list.remove_from_front()
my_list.print_values()
my_list.remove_from_back()
my_list.print_values()
my_list.remove_value(20)
my_list.print_values()
my_list.insert_at(15, 1)
my_list.print_values()