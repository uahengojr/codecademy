import node as Node

class SinglyLinkedList:

    "A linked list class"

    def __init__(self, data) -> None:
        self.head_node = Node(data)

    def get_head(self):
        return self.head_node