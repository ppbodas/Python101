from collections import deque

def main():
    d = deque()
    d.append(10)
    d.append(20)
    d.appendleft(5)
    print(d)  # deque([5, 10, 20])

    d.popleft()
    print(d)    # deque([10, 20])

    d.pop()
    print(d)    # deque([10])


    return None

if __name__ == "__main__":
    main()