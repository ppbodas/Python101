class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = [0] * n
        self.rank = [0] * n

        for id in range(n):
            self.parent[id] = id

    def find(self, x):
        if (self.parent[x] != x):
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py : return

        if self.rank[px] == self.rank[py]:
            self.parent[py] = px
            self.rank[px] = self.rank[px] + 1
        elif self.rank[px] < self.rank[py]:
            self.parent[px] = py
        else:
            self.parent[py] = px




def kruskal(n, edges):
    uf = UnionFind(n)

    edges.sort()
    total = 0

    for edge in edges:
        if uf.find(edge[1]) == uf.find(edge[2]): continue

        uf.union(edge[1], edge[2])
        total = total + edge[0]

    return total



if __name__ == "__main__":
    n = 4
    edges = [
        (1, 0, 1),
        (3, 0, 2),
        (4, 0, 3),
        (2, 1, 2),
        (5, 1, 3),
        (6, 2, 3),
    ]

    mst_weight = kruskal(n, edges)

    assert mst_weight == 7

    print("All tests passed")
