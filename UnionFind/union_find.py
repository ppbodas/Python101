class UnionFind:
    def __init__(self, n):
        self.parent = [0] * n
        self.rank = [0] * n

        for idx in range(n):
            self.parent[idx] = idx

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]



    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return

        if self.rank[px] == self.rank[py]:
            self.parent[y] = px
            self.rank[x] = self.rank[x] + 1
        elif self.rank[x] < self.rank[y]:
            self.parent[x] = py
        else:
            self.parent[y] = px



    def connected(self, x, y):
        return self.find(x) == self.find(y)


if __name__ == "__main__":
    uf = UnionFind(6)  # nodes: 0, 1, 2, 3, 4, 5

    # initially all disconnected
    assert not uf.connected(0, 1)
    assert not uf.connected(2, 3)

    uf.union(0, 1)
    uf.union(1, 2)
    assert uf.connected(0, 2)   # 0-1-2 are connected
    assert not uf.connected(0, 3)

    uf.union(3, 4)
    assert uf.connected(3, 4)
    assert not uf.connected(2, 4)

    uf.union(2, 3)
    assert uf.connected(0, 4)   # 0-1-2-3-4 now all connected
    assert not uf.connected(0, 5)  # 5 still isolated

    # self connection
    assert uf.connected(3, 3)

    print("All tests passed")
