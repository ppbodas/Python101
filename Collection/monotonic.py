from collections import deque

"""
    Returns next greater element for each index, -1 if none.

    For each element, find the first element to its right that is greater.
    If no such element exists, use -1.

    Example: [2, 1, 2, 4, 3]
      index 0 -> 4  (first value to the right greater than 2)
      index 1 -> 2  (first value to the right greater than 1)
      index 2 -> 4  (first value to the right greater than 2)
      index 3 -> -1 (nothing to the right is greater than 4)
      index 4 -> -1 (nothing to the right is greater than 3)
    result = [4, 2, 4, -1, -1]

    Solves in O(n) using a monotonic stack vs O(n^2) naive approach.
"""
def monotonic_stack(arr):

    result = [-1] * len(arr)
    stack = []  # stores indices

    for i, val in enumerate(arr):
        while stack and arr[stack[-1]] < val:
            result[stack.pop()] = val
        stack.append(i)




    return result


def monotonic_queue_max(arr, k):
    """Returns max value in each sliding window of size k."""
    result = []
    queue = deque()  # stores indices, front is always the max

    for i, val in enumerate(arr):
        while queue and queue[0] < i - k + 1:
            queue.popleft()

        while queue and arr[queue[-1]] < val:
            queue.pop()

        queue.append(i)

        if i >= k - 1:
            result.append(arr[queue[0]])

    return result


if __name__ == "__main__":
    # Monotonic stack: next greater element
    assert monotonic_stack([2, 1, 2, 4, 3]) == [4, 2, 4, -1, -1]
    assert monotonic_stack([1, 2, 3, 4]) == [2, 3, 4, -1]
    assert monotonic_stack([4, 3, 2, 1]) == [-1, -1, -1, -1]

    # Monotonic queue: sliding window maximum
    assert monotonic_queue_max([1, 3, -1, -3, 5, 3, 6, 7], k=3) == [3, 3, 5, 5, 6, 7]
    assert monotonic_queue_max([1], k=1) == [1]

    print("All tests passed")
