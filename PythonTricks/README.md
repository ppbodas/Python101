# Python Tricks & Idioms

A grab-bag of everyday Python idioms — inspired by
[The Hitchhiker's Guide to Python](https://docs.python-guide.org/writing/style/) — updated
for Python 3, with each one demoed and run in `python_tricks.py`.

## 1. Running a Python 2 script

Python 2 reached end-of-life in 2020, so this project targets Python 3 only, but for
historical reference: a `.py` file is just run by handing it to the interpreter —
`python2 script.py` (or `python3 script.py` for Python 3). There's no need to "open Python"
first and type a filename into it; the interpreter takes the file path as an argument.

## 2. `if __name__ == "__main__":`

```python
def main():
    ...

if __name__ == "__main__":
    main()
```

`__name__` is a variable Python sets automatically on every module. When a file is *run
directly* (`python3 file.py`), Python sets `__name__` to `"__main__"` for that file. When
the same file is *imported* from somewhere else (`import file`), Python sets `__name__` to
the module's own name (`"file"`) instead.

The `if` check means "only call `main()` when this file was the one that was run directly" —
so the file can also be safely imported elsewhere (e.g. for its functions or for tests)
without `main()` firing on import.

## 3. Seeing what's inside a module

```python
print(dir(module))                 # lists every name defined in the module
help(module.interesting_function)  # prints that function's docstring and signature
```

`dir()` is good for a quick inventory; `help()` is good once you've picked a function and
want to know how to call it.

## 4. Clearing the console

```python
import os
os.system("cls")     # Windows
os.system("clear")    # macOS / Linux
```

`os.system(...)` runs a shell command and returns its exit code. There's no cross-platform
built-in for this — you pick the command based on `os.name` or `sys.platform` if you need
it to work everywhere.

## 5. Getting a dictionary of all local variables

```python
locals()
```

Returns a `dict` mapping every local variable name (in the current scope) to its value.
Handy for quick debugging, and it's also what powers the `%(name)s` style string formatting
trick in section 21.

## 6. `if` / `elif` / `else`

```python
if condition:
    ...
elif other_condition:
    ...
else:
    ...
```

Python has no `switch` statement (until `match` in 3.10+) — chained `elif` is the classic
way to check multiple conditions in order. The first matching branch wins; `else` only runs
if none of them did.

## 7. Connecting Python to a database

Python 3's standard library ships `sqlite3`, so no external dependency is needed for a
lightweight embedded database:

```python
import sqlite3

conn = sqlite3.connect("my.db")   # or ":memory:" for a throwaway in-memory DB
cur = conn.cursor()
cur.execute("CREATE TABLE people (name TEXT, age INTEGER)")
cur.execute("INSERT INTO people VALUES (?, ?)", ("Alice", 30))
conn.commit()
cur.execute("SELECT * FROM people")
print(cur.fetchall())
conn.close()
```

See also: [SQLite - Python (TutorialsPoint)](http://www.tutorialspoint.com/sqlite/sqlite_python.htm).

## 8. Getting characters from a string by index

```python
s = "Python"
s[0]     # 'P'
s[-1]    # 'n'  (negative indices count from the end)
s[1:4]   # 'yth' (slice)
```

Strings support the same direct indexing/slicing as lists — no separate "char at" method
needed, unlike C++'s `std::string::at()`.
See also: [Stack Overflow: get char from string by index](http://stackoverflow.com/questions/8848294/how-to-get-char-from-string-by-index).

## 9. Getting command line arguments

```python
import sys
args = sys.argv[1:]   # sys.argv[0] is the script's own path, so it's skipped
```

`sys.argv` is a list of strings exactly as typed on the command line — no parsing or type
conversion is done for you (see `argparse` for that, if you need flags/options).

## 10-11. Building and printing lists of strings

```python
colors = "Red Black Orange Yellow".split()   # ['Red', 'Black', 'Orange', 'Yellow']
print(", ".join(colors))                     # 'Red, Black, Orange, Yellow'
```

`str.split()` with no argument splits on any whitespace. `", ".join(list)` glues the list
back together with `", "` *between* elements only — there's no trailing separator after the
last item, which is easy to forget when reasoning about it by hand.

## 12-14. Creating dictionaries

```python
d = {"key1": "value1", "key2": "value2"}
d.update({"key3": "value3"})           # add/merge more key-value pairs in place

states = ["MH", "KA", "GJ", "MP"]
capitals = ["Mum", "BGL", "GA", "Bho"]
s = dict(zip(states, capitals))        # {'MH': 'Mum', 'KA': 'BGL', ...}
```

`zip(a, b)` pairs up elements from two sequences positionally; wrapping that in `dict(...)`
turns each pair into a key-value entry — a quick way to build a lookup table from two
parallel lists.

## 15. Iterating over a container

```python
for key in some_dict:      # iterates over keys
    ...
for item in some_list:     # iterates over elements
    ...
```

Looping over a `dict` directly gives you its keys (use `.items()` for key-value pairs, see
section 20). Looping over a `list`, `tuple`, `set`, or any other iterable gives you its
elements, in order for sequences.

## 16. Inverting a dictionary

```python
m = {"a": 1, "b": 2, "c": 3, "d": 4}
inverted = {v: k for k, v in m.items()}   # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
```

A dict comprehension — same idea as a list comprehension, but building key-value pairs.
Only safe when the original values are unique (and hashable), since they become the new
keys.

## 17. Default return value for `dict.get`

```python
val = d.get("key", some_default_value)
```

`dict.get(key, default)` returns `d[key]` if present, otherwise `default` — without raising
`KeyError`. If you omit the default argument entirely, it returns `None` instead.

## 18. Default value if a key is missing: `setdefault`

```python
d.setdefault(key, []).append(value)
```

If `key` already exists, `setdefault` returns its current value (and does nothing else). If
it doesn't exist, it inserts `key` with the given default (here, an empty list) *and*
returns that default — so `.append(value)` always has something to append to. This is the
classic one-liner for building `{key: [list of values]}` groupings.

## 19-20. Getting the index while iterating; iterating dict items

```python
items = ["a", "b", "c"]
y = list(enumerate(items))          # [(0, 'a'), (1, 'b'), (2, 'c')]

for index, item in enumerate(items):
    ...

for key, value in m.items():        # Python 3 (m.iteritems() was the Python 2 spelling)
    ...
```

`enumerate()` wraps any iterable so each element comes with its position — no manual
counter variable needed. `dict.items()` is the equivalent for key-value pairs; in Python 2
this was the memory-heavier `.items()` (built a list upfront) vs. the lazy `.iteritems()` —
in Python 3, plain `.items()` is already lazy, so `.iteritems()` no longer exists.

## 21. Building strings at runtime

Say we want to print `'Prathmesh has 3 messages'`. From oldest/least readable to
newest/most readable:

```python
text = "%s has %i messages" % (name, message_count)                       # old %-formatting
text = "%(name)s has %(message_count)i messages" % locals()               # named, via locals()
text = "{} has {} messages".format(name, message_count)                   # str.format()
text = f"Hello, my name is {name} and I am {age} years old."              # f-strings (best)
```

f-strings (Python 3.6+) are generally the clearest and fastest option today — the
expression lives right inside the string instead of in a separate argument list.

## 22. Flattening a 2D list into a 1D list

```python
buckets = [[1, 2], [3, 4], [5]]
flat = sum(buckets, [])   # [1, 2, 3, 4, 5]
```

`sum(iterable, start)` normally adds numbers, but `+` also works on lists (concatenation),
so summing a list of lists with a `[]` starting value concatenates them all together. Fine
for small lists; for large/many sublists, `itertools.chain.from_iterable(buckets)` is more
efficient since it avoids repeated list copies.

## 23-24. Stripping and splitting a line

```python
line.strip()        # removes leading/trailing whitespace (like C++'s trim, done for you)
line.split(" ")      # splits into a list on the given separator
line.split(",")
```

`split()` with no argument (as in section 10) splits on *any* run of whitespace; passing an
explicit separator like `" "` or `","` splits on exactly that character instead.

## 25. Iterating a list in reverse

```python
colors[::-1]   # slice syntax: [start:end:step] — step -1 walks backward
```

An extended slice with a step of `-1` walks the sequence back-to-front, producing a reversed
copy without mutating the original (compare to `list.reverse()`, which reverses in place).

## 26. Reading typed data from stdin

```python
# Python 2
dd, mm, yy = map(int, raw_input().split())

# Python 3
dd, mm, yy = map(int, input().split())      # input() always returns a str
nums = list(map(int, input().split()))       # a whole list of ints from one line
```

Python 2's `input()` evaluated the typed text as Python code (rarely what you want) — that's
why `raw_input()` existed for plain text. Python 3 dropped that distinction: `input()` always
returns a string, so it inherited the old `raw_input()` behavior under the original name.

## 27. Printing a float with fixed precision

```python
print("{0:.5f}".format(float_var))   # the 0 is the positional argument index
print(f"{float_var:.5f}")            # equivalent, as an f-string
```

`.5f` means "fixed-point notation, 5 digits after the decimal point" — the number is rounded
(not truncated) to that many places.

## 28, 32. Reading data from a file

```python
f = open("file_path", mode)   # mode: 'r' read, 'w' write, 'a' append, ...
...
f.close()                     # must be called manually if opened this way

# safer: closes automatically, even if an exception happens inside the block
with open("file_path") as f:
    ...
```

`with` (a *context manager*) guarantees the file gets closed when the block exits, even on
an error — so it's preferred over manually calling `open()`/`close()`.

Worked example (see `demo_file_io()` / `input.txt` in this folder):

```python
def main():
    with open("input.txt") as f:
        n = int(f.readline())          # first line: how many rows follow
        print(n)
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            print(row)

if __name__ == "__main__":
    main()
```

reads an `input.txt` shaped like:

```
3
1 2 3
5 8 6
20 30 8
```

## 29-31. 2D arrays, their max, and 1D array defaults

```python
t = [[0] * n for _ in range(m)]       # m rows, n columns, all zero
max_value = max(max(row) for row in t)  # max of a 2D array: max of each row's max
l = [0] * n                            # a 1D list of n zeros
```

`[[0] * n for _ in range(m)]` (a list comprehension building a *new* inner list each time)
is important — `[[0] * n] * m` would instead repeat the *same* inner list `m` times, so
mutating one row would appear to mutate them all.

## 33. Ternary operator

```python
res = a[i - 3] if (i - 3) > 0 else 0
```

Reads as "`a[i-3]` if the condition holds, otherwise `0`" — a single-expression alternative
to a 4-line `if`/`else` block, useful when you need the result of the choice as a value
(e.g. as a function argument, or the right-hand side of an assignment) rather than as a
statement.

## 34. Representing a number in binary

```python
bin(42)   # '0b101010'
```

`bin()` returns a string with the `0b` prefix included; strip it with `bin(x)[2:]` if you
just want the digits.

## 35. Log with a specific base

```python
import math
math.log(x, base)   # e.g. math.log(8, 2) == 3.0
```

`math.log(x)` alone computes the *natural* log (base *e*); passing a second argument
computes the log in that base instead.

## 36. Sorting a list of tuples/lists by a key

```python
points = [[10, 16], [2, 8], [1, 6], [7, 12]]
p = sorted(points, key=lambda x: x[1])   # sorted by each point's 2nd element
```

`key=` takes a function applied to each element to decide sort order — here, a `lambda`
that picks out index `1` of each inner list, so the points end up ordered by their second
coordinate rather than lexicographically by the whole list.

## Interview-favorite tricks

The idioms below come up constantly in coding-interview problems specifically (frequency
counting, top-k, memoized recursion, etc.), so they're grouped separately here.

### 37. Swapping variables without a temp

```python
a, b = 1, 2
a, b = b, a   # a=2, b=1
```

The right-hand side is fully evaluated into a tuple *before* any assignment happens, so
both variables get their new values simultaneously — no `temp = a` needed.

### 38. Extended unpacking with `*`

```python
first, *middle, last = [1, 2, 3, 4, 5]
# first = 1, middle = [2, 3, 4], last = 5
```

`*name` soaks up however many elements are left over (as a list), so you can peel off the
first and/or last elements of a sequence without slicing manually.

### 39. Chained comparisons

```python
1 < x < 10   # equivalent to: 1 < x and x < 10
```

Python lets you chain comparison operators directly, which reads closer to how you'd write
the inequality on paper than the `and`-joined version.

### 40. `any()` and `all()`

```python
all(n % 2 == 0 for n in nums)   # True only if every element satisfies the condition
any(n > 7 for n in nums)        # True if at least one element does
```

Both short-circuit — `all()` stops at the first `False`, `any()` stops at the first `True`
— so they're efficient even over large/lazy iterables like generator expressions.

### 41. List comprehension with a filter

```python
evens = [x for x in range(10) if x % 2 == 0]   # [0, 2, 4, 6, 8]
```

The trailing `if` filters which elements make it into the result — combine it with a
transformation before the `for` (e.g. `[x * x for x in ... if ...]`) to filter and map in
one line.

### 42. Counting frequencies with `collections.Counter`

```python
from collections import Counter

counts = Counter("mississippi")       # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
counts.most_common(2)                 # [('i', 4), ('s', 4)]
```

`Counter` is a `dict` subclass specialized for tallying — it comes up in almost every
anagram/frequency-count style interview question, and `most_common(n)` sorts by count for
you.

### 43. `collections.defaultdict` for grouping

```python
from collections import defaultdict

graph = defaultdict(list)
graph["A"].append("B")
graph["A"].append("C")   # {'A': ['B', 'C']} — no "if key not in graph" check needed
```

`defaultdict(list)` (or `int`, `set`, ...) automatically creates a default value the first
time a key is accessed, which is exactly the pattern needed to build adjacency lists,
group-by results, or frequency maps without a manual existence check.

### 44. Sets for O(1) lookups and deduplication

```python
nums = [1, 2, 2, 3, 3, 3, 4]
unique = set(nums)     # {1, 2, 3, 4} — duplicates removed
3 in unique             # True, checked in ~O(1) average time
```

A `list` membership check (`x in some_list`) is O(n); a `set` membership check is O(1) on
average, since it's backed by a hash table — this swap alone turns many brute-force O(n²)
interview solutions into O(n).

### 45. Merging dictionaries

```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

{**d1, **d2}   # {'a': 1, 'b': 3, 'c': 4} — later dict wins on key conflicts
d1 | d2         # same result, Python 3.9+ syntax
```

Both create a *new* merged dict, leaving `d1` and `d2` unchanged; when a key exists in both,
whichever dict appears later (`d2` here) wins.

### 46. `functools.lru_cache` for memoization

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

Recursive solutions to DP-style interview questions (Fibonacci, climbing stairs, coin
change, ...) are often exponential without caching. `@lru_cache` memoizes the function's
return value per set of arguments automatically, turning repeated subproblem calls into a
single cached lookup — no manual memo dict required.

### 47. `heapq.nlargest` / `nsmallest` for top-k elements

```python
import heapq

heapq.nlargest(3, nums)    # the 3 largest elements, largest first
heapq.nsmallest(2, nums)   # the 2 smallest elements, smallest first
```

For "top-k" style questions, this avoids sorting the entire list (`O(n log n)`) when you
only need a handful of extreme values — `heapq` does it in `O(n log k)`.

### 48. `bisect` for binary search on sorted sequences

```python
import bisect

sorted_nums = [1, 3, 4, 4, 6, 8]
bisect.bisect_left(sorted_nums, 4)   # 2 — leftmost index where 4 could be inserted
bisect.insort(sorted_nums, 5)         # inserts 5 in sorted position, in place
```

`bisect_left`/`bisect_right` find an insertion point in `O(log n)` instead of scanning
linearly — useful any time you need to keep a list sorted as you insert, or need to find
the first/last position satisfying some ordering condition.

### 49. `math.gcd`

```python
import math
math.gcd(48, 18)   # 6
```

Saves hand-rolling Euclid's algorithm whenever a problem needs a greatest common divisor
(e.g. reducing a fraction, or LCM via `a * b // math.gcd(a, b)`).
