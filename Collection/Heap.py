import heapq


def main():
    l = [x for x in range(5)]   # 0, 1, 2, 3, 4
    l.reverse()
    print(l)        # [4, 3, 2, 1, 0]

    # Min Heap
    heapq.heapify(l)
    print(l)        # [0, 1, 2, 4, 3]
    heapq.heappush(l, -3)

    print(heapq.heappop(l))     # -3
    print(heapq.heappop(l))     # 0
    print(heapq.heappop(l))     # 1
    print(heapq.heappop(l))     # 2
    print(heapq.heappop(l))     # 3

    # Max Heap
    l = [x for x in range(5)]
    m = []
    for idx, value in enumerate(l):
        m.append((-1* value, value))

    print("Max Heap")

    heapq.heapify(m)

    print(heapq.heappop(m)[1])
    print(heapq.heappop(m)[1])
    print(heapq.heappop(m)[1])
    print(heapq.heappop(m)[1])
    print(heapq.heappop(m)[1])

if __name__ == "__main__":
   		 main()