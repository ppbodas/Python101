from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    q = deque()
    q.append(root)

    parts = []

    while len(q) != 0:
        node = q.popleft()

        if node is None:
            parts.append("null")
        else:
            parts.append(str(node.val))
            q.append(node.left)
            q.append(node.right)

    print(",".join(parts))
    return ",".join(parts)

def convet_to_node(str):
    return None if str == "null" else TreeNode(int(str), None, None)


def deserialize(data):
    d = deque(data.split(","))

    bfs_q = deque()
    root = convet_to_node(d.popleft())
    bfs_q.append(root)
    while bfs_q:
        node = bfs_q.popleft()

        if node:
            node.left = convet_to_node(d.popleft())
            node.right = convet_to_node(d.popleft())
            bfs_q.append(node.left)
            bfs_q.append(node.right)

    return root







if __name__ == "__main__":
    #     1
    #    / \
    #   2   3
    #      / \
    #     4   5
    root = TreeNode(1,
            TreeNode(2),
            TreeNode(3,
                TreeNode(4),
                TreeNode(5)))

    data = serialize(root)
    print(f"Serialized: {data}")

    restored = deserialize(data)

    assert restored.val == 1
    assert restored.left.val == 2
    assert restored.right.val == 3
    assert restored.right.left.val == 4
    assert restored.right.right.val == 5
    assert restored.left.left is None
    assert restored.left.right is None

    # single node
    single = TreeNode(42)
    assert deserialize(serialize(single)).val == 42

    # None root
    assert deserialize(serialize(None)) is None

    print("All tests passed")
