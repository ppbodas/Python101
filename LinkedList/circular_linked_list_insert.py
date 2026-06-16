class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node

"""
    Insert val into a sorted circular linked list.
    node is any node in the list (not necessarily the smallest).
    Returns the inserted node.

    Cases to handle:
      1. val fits between two consecutive nodes (prev.val <= val <= cur.val)
      2. val is at the boundary — smaller than min or larger than max
         (insert between the largest and smallest node)
      3. All nodes have the same value (val can go anywhere)
      4. Empty list (node is None) — create a single self-referencing node
"""
def insert_after(node, val):
    tmp = node.next_node
    inserted_node = Node(val)
    inserted_node.next_node = tmp
    node.next_node = inserted_node
    print(f"Inserted node after {node.val}")
    return inserted_node

def insert(node, val):
    if node is None:
        new_node = Node(val)
        new_node.next_node = new_node
        return new_node
    if node.val < val:
        while node.next_node.val < val and node.val < node.next_node.val:
            node = node.next_node
        return insert_after(node, val)
    else:
        while node.next_node.val > node.val:
            node = node.next_node

        if node.next_node.val > val:
            return insert_after(node, val)

        while node.next_node.val < val:
            node = node.next_node
        return insert_after(node, val)


def to_list(node, start):
    """Helper: collect values starting from `start` node."""
    result = [start.val]
    cur = start.next_node
    while cur != start:
        result.append(cur.val)
        cur = cur.next_node
    return result


def build_circular(values):
    """Helper: build a sorted circular linked list, return any node."""
    if not values:
        return None
    nodes = [Node(v) for v in values]
    for i in range(len(nodes)):
        nodes[i].next_node = nodes[(i + 1) % len(nodes)]
    return nodes[0]


if __name__ == "__main__":
    # Case 1: insert in the middle
    head = build_circular([1, 3, 5])
    print(f"Case 1 before: {to_list(head, head)}, inserting 4")
    new_node = insert(head, 4)
    assert sorted(to_list(new_node, new_node)) == [1, 3, 4, 5]

    # Case 2a: insert new maximum
    head = build_circular([1, 3, 5])
    print(f"Case 2a before: {to_list(head, head)}, inserting 6")
    new_node = insert(head, 6)
    assert sorted(to_list(new_node, new_node)) == [1, 3, 5, 6]

    # Case 2b: insert new minimum
    head = build_circular([1, 3, 5])
    print(f"Case 2b before: {to_list(head, head)}, inserting 0")
    new_node = insert(head, 0)
    assert sorted(to_list(new_node, new_node)) == [0, 1, 3, 5]

    # Case 3: all same values
    head = build_circular([3, 3, 3])
    print(f"Case 3 before: {to_list(head, head)}, inserting 3")
    new_node = insert(head, 3)
    assert sorted(to_list(new_node, new_node)) == [3, 3, 3, 3]

    # Case 4: empty list
    print(f"Case 4 before: [], inserting 5")
    new_node = insert(None, 5)
    assert to_list(new_node, new_node) == [5]

    # Case 5: input is not the head node (any random node given)
    head = build_circular([1, 3, 5])
    random_node = head.next_node  # node with val=3
    print(f"Case 5 before: {to_list(head, head)}, inserting 4 (starting from node={random_node.val})")
    new_node = insert(random_node, 4)
    assert sorted(to_list(new_node, new_node)) == [1, 3, 4, 5]

    # Case 6: verify actual circular order (not just sorted contents)
    # 4 must be between 3 and 5, not after 1
    head = build_circular([1, 3, 5])
    print(f"Case 6 before: {to_list(head, head)}, inserting 4 (starting from node=1)")
    new_node = insert(head, 4)
    assert to_list(head, head) == [1, 3, 4, 5]

    # Case 7: start from max node, insert in middle
    head = build_circular([1, 3, 5])
    max_node = head.next_node.next_node  # node with val=5
    print(f"Case 7 before: {to_list(head, head)}, inserting 4 (starting from node={max_node.val})")
    new_node = insert(max_node, 4)
    assert sorted(to_list(new_node, new_node)) == [1, 3, 4, 5]

    # Case 8: start from max node, insert new max
    head = build_circular([1, 3, 5])
    max_node = head.next_node.next_node  # node with val=5
    print(f"Case 8 before: {to_list(head, head)}, inserting 6 (starting from node={max_node.val})")
    new_node = insert(max_node, 6)
    assert sorted(to_list(new_node, new_node)) == [1, 3, 5, 6]

    # Case 9: start from max node, insert new min
    head = build_circular([1, 3, 5])
    max_node = head.next_node.next_node  # node with val=5
    print(f"Case 9 before: {to_list(head, head)}, inserting 0 (starting from node={max_node.val})")
    new_node = insert(max_node, 0)
    assert sorted(to_list(new_node, new_node)) == [0, 1, 3, 5]

    # Case 10: single element list
    head = build_circular([5])
    print(f"Case 10 before: {to_list(head, head)}, inserting 3")
    new_node = insert(head, 3)
    assert sorted(to_list(new_node, new_node)) == [3, 5]

    print("All tests passed")
