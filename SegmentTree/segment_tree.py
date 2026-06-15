class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 1, 0, self.n - 1)

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
            return

        mid = start + (end - start)//2
        self.build(arr, 2 * node , start, mid)
        self.build(arr, 2 * node + 1, mid+1, end)
        self.tree[node] = self.tree[2* node] + self.tree[2 * node +1]

    def update(self, idx, value):
        self.update_local(1, 0, self.n - 1, idx, value)

    def update_local(self, node, node_start, node_end, idx, value):
        if node_start == node_end:
            self.tree[node] = value
            return

        mid = node_start + (node_end - node_start) // 2
        if idx <= mid:
            self.update_local(2 * node, node_start, mid, idx, value)
        else:
            self.update_local(2 * node + 1, mid + 1, node_end, idx, value)

        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, left, right):
        return self.query_local(1, 0, self.n - 1, left, right)

    def query_local(self, node, node_start, node_end, query_left, query_right):
        # for out of bound
        if query_right < node_start:
            return 0

        if query_left > node_end:
            return 0

        if query_left <= node_start and node_end <= query_right:
            return self.tree[node]

        mid = node_start + (node_end - node_start)//2
        return (self.query_local(2* node, node_start, mid, query_left, query_right) +
                self.query_local(2 * node + 1, mid + 1, node_end, query_left, query_right))



if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    st = SegmentTree(arr)

    # sum of entire array
    assert st.query(0, 5) == sum(arr)

    # sum of a sub-range
    assert st.query(1, 3) == 3 + 5 + 7

    # single element
    assert st.query(2, 2) == 5

    # point update
    st.update(2, 10)
    arr[2] = 10
    assert st.query(0, 5) == sum(arr)
    assert st.query(1, 3) == 3 + 10 + 7

    print("All tests passed")