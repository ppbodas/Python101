import heapq

def dijkstra(graph, start):
    l = []

    heapq.heappush(l, (0, start))
    distances = {}
    visited = set()
    while l:
        cur_node_distance, cur_node = heapq.heappop(l)
        # check if already visited
        if cur_node in visited:
            continue

        visited.add(cur_node)
        distances[cur_node] = cur_node_distance

        for node in graph[cur_node]:
            target_distance = cur_node_distance + node[1]

            heapq.heappush(l, (target_distance, node[0]))


    return distances








if __name__ == "__main__":
    graph = {
        "A": [("B", 4), ("C", 1)],
        "B": [("A", 4), ("C", 2), ("D", 5)],
        "C": [("A", 1), ("B", 2), ("D", 8)],
        "D": [("B", 5), ("C", 8)],
    }

    output = dijkstra(graph, "A")

    assert output["A"] == 0
    assert output["B"] == 3
    assert output["C"] == 1
    assert output["D"] == 8

    print("All tests passed")