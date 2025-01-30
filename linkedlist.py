'''
node.py
'''
from node import Node
from book import Book

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_front(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def __str__(self):
        return_str = ""
        current = self.head
        while current is not None:
            return_str += str(current) + " "
            current = current.next
        return return_str
    
    def find(self, target_value):
        current = self.head
        i = 0
        while current is not None:
            if current.data == target_value:
                return i
            current = current.next
            i += 1
        return i

    def to_list(self):
        current = self.head
        return_list = []
        while current is not None:
            return_list.append(str(current))
            current = current.next
        return return_list

    def find_last_index(self, target_value):
        current = self.head
        i = 0
        possible = 0
        while current is not None:
            if current.data == target_value:   
                possible = i
            current = current.next
            i += 1
        return possible
    
    def count(self):
        return self.head.count()
    
    def iterative_count(self):
        current = self.head
        counter = 0
        while current is not None:
            counter += 1
            current = current.next
        return counter
    
    def calc_price(self):
        return self.head.calculate_price()
    

    def loop_test(self):
        current = self.head
        while current is not None:
            if current.tag == True:
                return True
            current.tag = True
            current = current.next
        return False
        
    def wrap(self, p):
        current = self.head
        og_p = p
        new_ll = LinkedList()
        while current is not None:
            if current.data == p:
                new_ll.add_to_front(current.data)
            current = current.next
        current = self.head
        while current.data != og_p:
            new_ll.add_to_front(current.data)
            current = current.next
        return new_ll

    '''
    def iterative_filter(self, predicate):
        """
        predicate: lambda that takes in a node object and returns true/false
        """
        current = self.head
        new_head = None
        new_ll = LinkedList()
        while current is not None:
            if predicate(current) == True:
                new_node = Node(current.data, new_head)
                new_head = new_node

            current = current.next

        new_ll.add_to_front(new_node)
        return new_ll
    '''

ll = LinkedList()
ll.add_to_front("A")
ll.add_to_front("B")
ll.add_to_front("C")
ll.add_to_front("D")
ll.add_to_front("E")
print(ll)
print(ll.wrap("B"))