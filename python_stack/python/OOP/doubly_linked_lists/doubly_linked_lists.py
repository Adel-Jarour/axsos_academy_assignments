class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_to_end(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        return self
    
    def deleteing_existing_node(self, node):
        if node is None:
            return self
        if node == self.head:
            self.head = node.next
            if self.head:
                self.head.prev = None
        elif node == self.tail:
            self.tail = node.prev
            if self.tail:
                self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        return self
    
    def insert_at(self, val, n):
        new_node = Node(val)
        if n == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
            return self
        
        current = self.head
        for _ in range(n - 1):
            if current is None:
                return self
            current = current.next
        
        if current is None:
            return self
        
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        
        if new_node.next is None:
            self.tail = new_node
        
        return self
    
    def get_the_middle(self):
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def delete_dublicate_values(self):
        seen = set()
        runner = self.head
        
        while runner:
            if runner.value in seen:
                self.deleteing_existing_node(runner)
            else:
                seen.add(runner.value)
            runner = runner.next
        
        return self

    def reverse_list(self):
        runner = self.head
        prev_node = None
        
        while runner:
            next_node = runner.next
            runner.next = prev_node
            runner.prev = next_node
            prev_node = runner
            runner = next_node
        
        self.head, self.tail = self.tail, self.head
        return self
    
    def print_list(self):
        elements = []
        runner = self.head
        while runner:
            elements.append(runner.value)
            runner = runner.next
        print(" -> ".join(map(str, elements)))
        return self
    
my_list = DoublyLinkedList()
my_list.add_to_end(10).add_to_end(20).add_to_end(30).add_to_end(40).print_list()
my_list.insert_at(15, 1).print_list()
my_list.delete_dublicate_values().print_list()
my_list.reverse_list().print_list()
print(my_list.get_the_middle().value)