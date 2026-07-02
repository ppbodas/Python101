import heapq


def prim(graph, start):
    heap = []
    heapq.heappush(heap, (0, start))

    visited = set()
    visited.add(start)

    total  = 0

    while heap:
        weight, current_node = heapq.heappop(heap)
        if current_node not in visited:
            total = total + weight

        visited.add(current_node)

        for node, node_weight in graph[current_node]:
            if node in visited:
                continue

            heapq.heappush(heap, (node_weight, node))

    return total




if __name__ == "__main__":
    graph = {
        "A": [("B", 4), ("C", 1)],
        "B": [("A", 4), ("C", 2), ("D", 5)],
        "C": [("A", 1), ("B", 2), ("D", 8)],
        "D": [("B", 5), ("C", 8)],
    }

    mst_weight = prim(graph, "A")

    assert mst_weight == 8

    print("All tests passed")
