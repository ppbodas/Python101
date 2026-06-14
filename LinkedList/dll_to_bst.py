class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

PREV = None

def count_length(head):
    tmp = head
    count = 0
    while tmp:
        count = count + 1
        tmp = tmp.next
    return count

class DLL_Warpper:
    def __init__(self, head):
        self.head = head

def dll_to_bst(head):
    dll = DLL_Warpper(head)
    n = count_length(head)
    return dll_to_bst_recur(dll, n)

def dll_to_bst_recur(dll, n):
    if n <= 0: return None

    left = dll_to_bst_recur(dll, n // 2)

    tree_node = TreeNode(dll.head.val, None, None)
    tree_node.left = left

    dll.head = dll.head.next

    right = dll_to_bst_recur(dll, n - n // 2 - 1)
    tree_node.right = right

    return tree_node

def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def build_dll(values):
    if not values:
        return None
    head = ListNode(values[0])
    cur = head
    for v in values[1:]:
        node = ListNode(v, prev=cur)
        cur.next = node
        cur = node
    return head


def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True
    if not (min_val < root.val < max_val):
        return False
    return (is_valid_bst(root.left, min_val, root.val) and
            is_valid_bst(root.right, root.val, max_val))


if __name__ == "__main__":
    # 5 nodes — inorder must match sorted input
    head = build_dll([1, 2, 3, 4, 5])
    root = dll_to_bst(head)
    assert inorder(root) == [1, 2, 3, 4, 5]
    assert is_valid_bst(root)

    # single node
    head = build_dll([42])
    root = dll_to_bst(head)
    assert inorder(root) == [42]
    assert is_valid_bst(root)

    # two nodes
    head = build_dll([1, 2])
    root = dll_to_bst(head)
    assert inorder(root) == [1, 2]
    assert is_valid_bst(root)

    # three nodes — root must be middle (2)
    head = build_dll([1, 2, 3])
    root = dll_to_bst(head)
    assert inorder(root) == [1, 2, 3]
    assert is_valid_bst(root)
    assert root.val == 2

    # even number of nodes
    head = build_dll([1, 2, 3, 4])
    root = dll_to_bst(head)
    assert inorder(root) == [1, 2, 3, 4]
    assert is_valid_bst(root)

    # larger list
    head = build_dll(list(range(1, 16)))
    root = dll_to_bst(head)
    assert inorder(root) == list(range(1, 16))
    assert is_valid_bst(root)

    # negative values
    head = build_dll([-5, -3, -1, 0, 2, 4])
    root = dll_to_bst(head)
    assert inorder(root) == [-5, -3, -1,    0, 2, 4]
    assert is_valid_bst(root)

    # empty
    assert dll_to_bst(None) is None

    print("All tests passed")
