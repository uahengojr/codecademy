class Node:
    """ A singly linked node class """

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_value(self):
        return self.data
    
    def set_next(self, next):
        self.next = next
    
    def get_next(self):
        return self.next