class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next



class State:
    def __init__(self):
        self.prev = None
        self.head = None


def inorder(node, state):
    if not node:
        return
    inorder(node.left, state)

    cur = ListNode(node.val)
    if state.prev is None:
        state.head = cur
    else:
        state.prev.next = cur
        cur.prev = state.prev
    state.prev = cur

    inorder(node.right, state)


def bst_to_dll(root):
    if not root:
        return (None, None)
    state = State()
    inorder(root, state)
    return (state.head, state.prev)




def dll_values(head):
    result = []
    cur = head
    while cur:
        result.append(cur.val)
        cur = cur.next
    return result


def dll_values_reverse(tail):
    result = []
    cur = tail
    while cur:
        result.append(cur.val)
        cur = cur.prev
    return result


if __name__ == "__main__":
    #     4
    #    / \
    #   2   6
    #  / \ / \
    # 1  3 5  7
    root = TreeNode(4,
             TreeNode(2, TreeNode(1), TreeNode(3)),
             TreeNode(6, TreeNode(5), TreeNode(7)))

    head, tail = bst_to_dll(root)

    # inorder traversal of BST gives sorted order
    assert dll_values(head) == [1, 2, 3, 4, 5, 6, 7]
    # prev pointers must also work (traverse backwards)
    assert dll_values_reverse(tail) == [7, 6, 5, 4, 3, 2, 1]

    # single node
    head, tail = bst_to_dll(TreeNode(42))
    assert dll_values(head) == [42]
    assert head.prev is None
    assert head.next is None

    # empty tree
    assert bst_to_dll(None) == (None, None)

    print("All tests passed")
