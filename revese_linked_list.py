
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
            return

        prev = None
        current = self.head
        self.tail = self.head
        while current:
            tmp = current.next_node
            current.next_node = prev
            prev = current
            current = tmp
        self.head = prev

    def reverse_k(self, k):
        new_head = None
        prev_tail = None

        while self.head:
            k_th = self.get_kth_node(self.head, k)
            if not k_th:
                if prev_tail:
                    prev_tail.next_node = self.head
                break

            next_group = k_th.next_node
            k_th.next_node = None
            self.reverse()

            if new_head is None:
                new_head = self.head
            if prev_tail is not None:
                prev_tail.next_node = self.head

            prev_tail = self.tail
            self.head = next_group

        if new_head:
            self.head = new_head

    def get_kth_node(self, node, k):
        cur = node
        while cur and k>1:
            cur = cur.next_node
            k = k -1

        if k == 1:
            return cur
        else:
            return None



def main():
    ll = LinkedList()
    for i in range(1, 11):
        ll.add_node(Node(i * 10, None))

    # ll.print_list()

    ll.reverse_k(3)
    ll.print_list()

if __name__ == "__main__":
         main()