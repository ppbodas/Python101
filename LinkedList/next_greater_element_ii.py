from collections import deque

class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node

"""
    https://leetcode.com/problems/next-greater-element-ii/

    Given a circular linked list (the last node's next wraps around to the
    head), return a list of the next greater element for every node, in
    list order. The "next greater" search may wrap around past the tail
    once. If no greater element exists even after wrapping, use -1.

    Example: [1, 2, 1] (circular)
      node 0 (val=1) -> 2  (next node)
      node 1 (val=2) -> -1 (nothing greater, even after wrapping)
      node 2 (val=1) -> 2  (wraps around to node 0... no, finds node 1)
    result = [2, -1, 2]

    Approach: monotonic stack over the values, traversed twice (2n) to
    account for the wraparound, without physically duplicating the list.
"""
def next_greater_elements(head):
    if not head:
        return []
    d = deque()
    n = 1
    tmp = head
    while tmp.next_node != head:
        n = n + 1
        tmp = tmp.next_node

    output = [-1] * n

    tmp = head
    for i in range(2*n):
        while d and d[-1][1] < tmp.val:
            index, value = d.pop()
            output[index%n] = tmp.val

        d.append((i%n, tmp.val))

        tmp = tmp.next_node

    return output


def to_list(head):
    """Helper: collect values starting from head, stopping when we loop back."""
    if head is None:
        return []
    result = [head.val]
    cur = head.next_node
    while cur is not head:
        result.append(cur.val)
        cur = cur.next_node
    return result


def build_circular(values):
    """Helper: build a circular linked list, return the head node."""
    if not values:
        return None
    nodes = [Node(v) for v in values]
    for i in range(len(nodes)):
        nodes[i].next_node = nodes[(i + 1) % len(nodes)]
    return nodes[0]


if __name__ == "__main__":
    # Case 1: basic wraparound
    head = build_circular([1, 2, 1])
    output = next_greater_elements(head)
    print(f"Case 1: {output}")
    assert output == [2, -1, 2]
    print("Case 1: PASSED")

    # Case 2: all increasing
    head = build_circular([1, 2, 3, 4])
    output = next_greater_elements(head)
    print(f"Case 2: {output}")
    assert output == [2, 3, 4, -1]
    print("Case 2: PASSED")

    # Case 3: all decreasing (wraps around to the max at the front)
    head = build_circular([4, 3, 2, 1])
    output = next_greater_elements(head)
    print(f"Case 3: {output}")
    assert output == [-1, 4, 4, 4]
    print("Case 3: PASSED")

    # Case 4: all same values
    head = build_circular([3, 3, 3])
    output = next_greater_elements(head)
    print(f"Case 4: {output}")
    assert output == [-1, -1, -1]
    print("Case 4: PASSED")

    # Case 5: single node
    head = build_circular([5])
    output = next_greater_elements(head)
    print(f"Case 5: {output}")
    assert output == [-1]
    print("Case 5: PASSED")

    # Case 6: empty list
    output = next_greater_elements(None)
    print(f"Case 6: {output}")
    assert output == []
    print("Case 6: PASSED")

    print("All tests passed")