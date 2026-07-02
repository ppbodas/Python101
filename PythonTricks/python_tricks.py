import os
import sys
import math
import sqlite3
import bisect
import heapq
from collections import Counter, defaultdict
from functools import lru_cache


def demo_name_main():
    # Shows that __name__ is "__main__" only when a file is run directly.
    print("\n--- __name__ == '__main__' ---")
    print(f"__name__ while running this file directly: {__name__!r}")
    # __name__ while running this file directly: '__main__'
    print("If this file were imported instead, __name__ would be 'python_tricks'.")


def demo_inspect_module():
    # Inspects a module's contents with dir() and reads a function's docstring with help().
    print("\n--- inspecting a module: dir() and help() ---")
    print([name for name in dir(math) if not name.startswith("_")][:8], "...")
    # ['acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil'] ...
    print(math.sqrt.__doc__)  # help(math.sqrt) prints the same, plus more, to the console
    # Return the square root of x.


def demo_clear_console():
    # Documents (without executing) how to clear the terminal on each OS.
    print("\n--- clearing the console ---")
    print("os.system('cls') on Windows, os.system('clear') on macOS/Linux.")
    print("(Not actually run here so this demo's output isn't wiped out.)")


def demo_locals():
    # Dumps every local variable in the current scope as a dict.
    print("\n--- locals() ---")
    a = 1
    b = "two"
    print(locals())
    # {'a': 1, 'b': 'two'}


def demo_if_elif_else():
    # Classic if/elif/else branching, checked in order until one matches.
    print("\n--- if / elif / else ---")
    for n in (-2, 0, 5):
        if n > 0:
            result = "positive"
        elif n == 0:
            result = "zero"
        else:
            result = "negative"
        print(f"{n} is {result}")
    # -2 is negative
    # 0 is zero
    # 5 is positive


def demo_sqlite():
    # Connects to a SQLite DB (in-memory here), creates a table, inserts rows, and queries them.
    print("\n--- SQLite3 connectivity ---")
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("CREATE TABLE people (name TEXT, age INTEGER)")
    cur.executemany("INSERT INTO people VALUES (?, ?)", [("Alice", 30), ("Bob", 25)])
    conn.commit()
    cur.execute("SELECT * FROM people ORDER BY age")
    print(cur.fetchall())
    # [('Bob', 25), ('Alice', 30)]
    conn.close()


def demo_string_indexing():
    # Indexes and slices a string like a list — first char, last char, a middle slice.
    print("\n--- string indexing ---")
    s = "Python"
    print(s[0], s[-1], s[1:4])
    # P n yth


def demo_command_line_args():
    # Shows how sys.argv[1:] gives the command line args, excluding the script's own path.
    print("\n--- command line arguments ---")
    print("sys.argv[1:] holds the args after the script name.")
    print(f"This run's sys.argv: {sys.argv}")
    # This run's sys.argv: ['python_tricks.py']


def demo_split_and_join():
    # Builds a list from a string with split(), then rejoins it with join() (no trailing separator).
    print("\n--- str.split() and str.join() ---")
    colors = "Red Black Orange Yellow".split()
    print(colors)
    # ['Red', 'Black', 'Orange', 'Yellow']
    print(", ".join(colors))  # no trailing ", " after the last entry
    # Red, Black, Orange, Yellow


def demo_dicts():
    # Creates a dict, merges more entries in with update(), and builds one from two lists via zip().
    print("\n--- creating / updating dictionaries ---")
    d = {"key1": "value1", "key2": "value2"}
    print(d)
    # {'key1': 'value1', 'key2': 'value2'}
    d.update({"key3": "value3"})
    print(d)
    # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

    states = ["MH", "KA", "GJ", "MP"]
    capitals = ["Mum", "BGL", "GA", "Bho"]
    s = dict(zip(states, capitals))
    print(s)
    # {'MH': 'Mum', 'KA': 'BGL', 'GJ': 'GA', 'MP': 'Bho'}


def demo_iterate_containers():
    # Iterating a dict yields its keys; iterating a list yields its elements.
    print("\n--- iterating a list, dict, or any container ---")
    d = {"a": 1, "b": 2}
    for key in d:
        print(key)
    # a
    # b
    for item in [10, 20, 30]:
        print(item)
    # 10
    # 20
    # 30


def demo_invert_dict():
    # Swaps keys and values using a dict comprehension (values must be unique/hashable).
    print("\n--- inverting a dictionary ---")
    m = {"a": 1, "b": 2, "c": 3, "d": 4}
    print({v: k for k, v in m.items()})
    # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}


def demo_dict_get_default():
    # dict.get(key, default) avoids KeyError; default is None if not given explicitly.
    print("\n--- dict.get() with a default ---")
    d = {"x": 1}
    print(d.get("x", 0))
    # 1
    print(d.get("missing", 0))
    # 0
    print(d.get("missing"))  # None if no default given
    # None


def demo_setdefault():
    # setdefault(key, default) inserts the default only if the key is missing, then returns it.
    print("\n--- dict.setdefault() ---")
    d = {}
    d.setdefault("fruits", []).append("apple")
    d.setdefault("fruits", []).append("banana")
    print(d)
    # {'fruits': ['apple', 'banana']}


def demo_enumerate():
    # enumerate() pairs each element with its index; dict.items() pairs each key with its value.
    print("\n--- enumerate() and dict.items() ---")
    items = ["a", "b", "c"]
    print(list(enumerate(items)))
    # [(0, 'a'), (1, 'b'), (2, 'c')]
    for index, item in enumerate(items):
        print(index, item)
    # 0 a
    # 1 b
    # 2 c

    m = {"a": 1, "b": 2}
    for key, value in m.items():  # m.iteritems() in Python 2
        print(key, value)
    # a 1
    # b 2


def demo_string_formatting():
    # Four ways to build the same string at runtime, from oldest/least readable to newest/best.
    print("\n--- building strings at runtime ---")
    name = "Prathmesh"
    message_count = 3

    text1 = "%s has %i messages" % (name, message_count)
    text2 = "%(name)s has %(message_count)i messages" % locals()
    text3 = f"Hello, my name is {name} and I have {message_count} messages."
    text4 = "{} has {} messages".format(name, message_count)

    print(text1)
    # Prathmesh has 3 messages
    print(text2)
    # Prathmesh has 3 messages
    print(text3)
    # Hello, my name is Prathmesh and I have 3 messages.
    print(text4)
    # Prathmesh has 3 messages


def demo_flatten_2d_list():
    # Concatenates a list of lists into one flat list using sum() with a [] starting value.
    print("\n--- flattening a 2D list into a 1D list ---")
    buckets = [[1, 2], [3, 4], [5]]
    print(sum(buckets, []))
    # [1, 2, 3, 4, 5]


def demo_strip_split():
    # strip() removes leading/trailing whitespace; split(sep) breaks a string on a separator.
    print("\n--- str.strip() and str.split() ---")
    line = "   hello, world   "
    print(repr(line.strip()))
    # 'hello, world'
    print(line.strip().split(", "))
    # ['hello', 'world']


def demo_reverse_list():
    # [::-1] slices the whole sequence with a step of -1, producing a reversed copy.
    print("\n--- reversing a list with slicing ---")
    colors = ["red", "green", "blue"]
    print(colors[::-1])  # [start:end:step]
    # ['blue', 'green', 'red']


def demo_read_typed_stdin():
    # Documents (without blocking on real input) how to read and convert typed stdin data.
    print("\n--- reading typed data from stdin ---")
    print("dd, mm, yy = map(int, input().split())      # 3 ints from one line")
    print("nums = list(map(int, input().split()))       # a list of ints")
    print("(Not reading real stdin here, so this demo stays non-interactive.)")


def demo_float_precision():
    # Formats a float to a fixed number of decimal places (rounded, not truncated).
    print("\n--- printing a float with fixed precision ---")
    value = 3.14159265
    print("{0:.5f}".format(value))
    # 3.14159
    print(f"{value:.5f}")
    # 3.14159


def demo_file_io():
    # Reads structured data from a file using "with", which closes the file automatically.
    print("\n--- reading data from a file ---")
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(input_path) as f:
        n = int(f.readline())
        print(n)
        # 3
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            print(row)
        # [1, 2, 3]
        # [5, 8, 6]
        # [20, 30, 8]


def demo_2d_array():
    # Builds an m x n grid of zeros, finds the max value in a 2D array, and a 1D array of defaults.
    print("\n--- 2D arrays, max of a 2D array, 1D array defaults ---")
    m, n = 3, 4
    t = [[0] * n for _ in range(m)]
    print(t)
    # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    t = [[1, 6, 3], [9, 2, 4], [5, 8, 7]]
    print("max:", max(max(row) for row in t))
    # max: 9

    print([0] * 5)
    # [0, 0, 0, 0, 0]


def demo_ternary():
    # A single-expression if/else: value_if_true if condition else value_if_false.
    print("\n--- ternary operator ---")
    a = [1, 2, 3, 4, 5, 6, 7]
    for i in (1, 5):
        res = a[i - 3] if (i - 3) > 0 else 0
        print(f"i={i} -> {res}")
    # i=1 -> 0
    # i=5 -> 3


def demo_bin_and_log():
    # bin() gives a number's binary string; math.log(x, base) gives the log in that base.
    print("\n--- binary representation and log with a given base ---")
    print(bin(42))
    # 0b101010
    print(math.log(8, 2))
    # 3.0


def demo_sort_tuples():
    # Sorts a list of lists/tuples using key= to pick which element decides the order.
    print("\n--- sorting a list of lists/tuples by a key ---")
    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    print(sorted(points, key=lambda x: x[1]))
    # [[1, 6], [2, 8], [7, 12], [10, 16]]


def demo_swap_variables():
    # Swaps two variables in one line, no temp variable needed.
    print("\n--- swapping variables without a temp ---")
    a, b = 1, 2
    a, b = b, a
    print(a, b)
    # 2 1


def demo_extended_unpacking():
    # * collects "everything else" into a list during unpacking.
    print("\n--- extended unpacking with * ---")
    first, *middle, last = [1, 2, 3, 4, 5]
    print(first, middle, last)
    # 1 [2, 3, 4] 5


def demo_chained_comparison():
    # Python lets you chain comparisons instead of writing "and" between them.
    print("\n--- chained comparisons ---")
    x = 5
    print(1 < x < 10)
    # True
    print(10 < x < 20)
    # False


def demo_any_all():
    # any() is True if at least one element satisfies the condition; all() needs every element to.
    print("\n--- any() and all() ---")
    nums = [2, 4, 6, 8]
    print(all(n % 2 == 0 for n in nums))
    # True
    print(any(n > 7 for n in nums))
    # True


def demo_list_comprehension_filter():
    # A list comprehension can filter with an "if" as well as transform each element.
    print("\n--- list comprehension with a filter ---")
    evens = [x for x in range(10) if x % 2 == 0]
    print(evens)
    # [0, 2, 4, 6, 8]


def demo_counter():
    # Counter tallies how many times each element appears; most_common() ranks them.
    print("\n--- collections.Counter ---")
    counts = Counter("mississippi")
    print(counts)
    # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
    print(counts.most_common(2))
    # [('i', 4), ('s', 4)]


def demo_defaultdict():
    # defaultdict supplies a default value automatically, avoiding manual "if key not in d" checks.
    print("\n--- collections.defaultdict ---")
    graph = defaultdict(list)
    graph["A"].append("B")
    graph["A"].append("C")
    print(dict(graph))
    # {'A': ['B', 'C']}


def demo_set_dedup_lookup():
    # A set removes duplicates and gives O(1) average membership checks, unlike an O(n) list scan.
    print("\n--- sets for dedup and O(1) lookups ---")
    nums = [1, 2, 2, 3, 3, 3, 4]
    unique = set(nums)
    print(unique)
    # {1, 2, 3, 4}
    print(3 in unique)
    # True


def demo_merge_dicts():
    # {**d1, **d2} merges dicts; later dicts win on key conflicts. d1 | d2 does the same (3.9+).
    print("\n--- merging dictionaries ---")
    d1 = {"a": 1, "b": 2}
    d2 = {"b": 3, "c": 4}
    print({**d1, **d2})
    # {'a': 1, 'b': 3, 'c': 4}
    print(d1 | d2)
    # {'a': 1, 'b': 3, 'c': 4}


def demo_lru_cache():
    # lru_cache memoizes a function automatically, turning exponential recursion into linear.
    print("\n--- functools.lru_cache for memoization ---")

    @lru_cache(maxsize=None)
    def fib(n):
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)

    print(fib(30))
    # 832040
    print(fib.cache_info())
    # CacheInfo(hits=28, misses=31, maxsize=None, currsize=31)


def demo_heap_top_k():
    # heapq.nlargest/nsmallest pick the top-k elements without fully sorting the list.
    print("\n--- heapq.nlargest / nsmallest for top-k ---")
    nums = [5, 1, 9, 3, 7, 2]
    print(heapq.nlargest(3, nums))
    # [9, 7, 5]
    print(heapq.nsmallest(2, nums))
    # [1, 2]


def demo_bisect():
    # bisect finds an insertion point in a sorted list in O(log n); insort inserts it there.
    print("\n--- bisect for binary search on sorted lists ---")
    sorted_nums = [1, 3, 4, 4, 6, 8]
    print(bisect.bisect_left(sorted_nums, 4))
    # 2
    bisect.insort(sorted_nums, 5)
    print(sorted_nums)
    # [1, 3, 4, 4, 5, 6, 8]


def demo_gcd():
    # math.gcd computes the greatest common divisor without hand-rolling Euclid's algorithm.
    print("\n--- math.gcd ---")
    print(math.gcd(48, 18))
    # 6


def main():
    demo_name_main()
    demo_inspect_module()
    demo_clear_console()
    demo_locals()
    demo_if_elif_else()
    demo_sqlite()
    demo_string_indexing()
    demo_command_line_args()
    demo_split_and_join()
    demo_dicts()
    demo_iterate_containers()
    demo_invert_dict()
    demo_dict_get_default()
    demo_setdefault()
    demo_enumerate()
    demo_string_formatting()
    demo_flatten_2d_list()
    demo_strip_split()
    demo_reverse_list()
    demo_read_typed_stdin()
    demo_float_precision()
    demo_file_io()
    demo_2d_array()
    demo_ternary()
    demo_bin_and_log()
    demo_sort_tuples()
    demo_swap_variables()
    demo_extended_unpacking()
    demo_chained_comparison()
    demo_any_all()
    demo_list_comprehension_filter()
    demo_counter()
    demo_defaultdict()
    demo_set_dedup_lookup()
    demo_merge_dicts()
    demo_lru_cache()
    demo_heap_top_k()
    demo_bisect()
    demo_gcd()

    return None


if __name__ == "__main__":
    main()
