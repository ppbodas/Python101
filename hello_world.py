import heapq

from point import Point


def main():
    print("Hello World")
    colors = "Red Black Orange Yellow".split()

    print(colors)

    for color in colors:
        print(f"Item is {color}")

    filterd= [color for color in colors if color[0] == 'R']
    print(filterd)

    d = {}

    d["Prathmesh"] = 40
    d["Anagha"] = 36
    print(d)
    if "Anagha" in d:
        print (d["Anagha"])


    for item in d.items():
        print(f"Item key is {item[0]} and value id {item[1]}")

    m = 10
    n = 3
    t = [n * [0] for i in range(m)]  # Creates m rows n columns
    print(f"Item key is {t}")

    print(3*[0])
    print(is_palindrome("aabcaa"))

    max_heap_101()
    min_heap_101()

    point = Point(5, 6)
    print(f"X is {point.x}, Y is {point.y}")



def is_palindrome(str):
    if str is None:
        return False

    if not str:
        return True

    l = 0
    r = len(str) - 1

    while l < r:
        if str[l] != str[r]:
            return False
        l += 1
        r -= 1

    return True


def max_heap_101():
    print(f"Max heap Example")

    # Max heap based on string char length
    l1 = ["Apple", "Kiwi", "Pineapple"]
    l = [(-len(name), name) for name in l1]

    heapq.heapify(l)
    while l:
        print(heapq.heappop(l)[-1])

def min_heap_101():
    print(f"Min heap Example")

    # Min heap based on string char length
    l1 = ["Apple", "Kiwi", "Pineapple"]
    l = [(len(name), name) for name in l1]

    heapq.heapify(l)
    while l:
        print(heapq.heappop(l)[-1])


if __name__ == "__main__":
    main()