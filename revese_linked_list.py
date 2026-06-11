
class Node:
    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head


    def add_node(self, node):
        if self.head:
            self.tail.next_node = node
        else:
            self.head = node

        self.tail = node

    def print_list(self):
        temp = self.head
        while temp:
            print(f"Node value {temp.value}")
            temp = temp.next_node

    def reverse(self):
        if not self.head:
            return None

        prev = None
        self.tail = self.head
        current = self.head
        while current:
            tmp = current.next_node
            current.next_node = prev
            prev = current
            current = tmp

        self.head = prev




def main():
    ll = LinkedList()
    ll.add_node(Node(5, None))
    ll.add_node(Node(15, None))
    ll.add_node(Node(25, None))

    ll.print_list()

    ll.reverse()
    ll.print_list()

if __name__ == "__main__":
         main()