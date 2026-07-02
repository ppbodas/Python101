# Bitwise Operators — A Beginner's Guide

`bitwise_operators.py` demonstrates Python's bitwise operators and uses them to build
`add`, `subtract`, `multiply`, and `divide` — arithmetic without using `+`, `-`, `*`, `/`,
or `//`. This guide starts from the basics and builds up, with worked examples at every
step.

## 1. A quick refresher: numbers in binary

Computers store numbers as binary (base 2) — a sequence of `0`s and `1`s, where each
position is a power of 2, just like each position in a decimal number is a power of 10.

```
Decimal 13 in binary:

  8   4   2   1     <- place values (powers of 2: 2^3, 2^2, 2^1, 2^0)
  1   1   0   1     <- bits
  8 + 4 + 0 + 1 = 13
```

So `13` is `1101` in binary. Bitwise operators work on numbers *at this bit level* —
comparing or shifting individual `0`/`1` digits — instead of treating the number as a
whole quantity the way `+` or `*` do.

## 2. The bitwise operators, one at a time

### AND (`&`) — "both must be 1"

Compares each pair of bits. The result bit is `1` only if **both** input bits are `1`.

```
  1 & 1 = 1
  1 & 0 = 0
  0 & 1 = 0
  0 & 0 = 0
```

Example: `12 & 10`

```
  12 = 1100
  10 = 1010
  --------- &
       1000  = 8
```

Only the leftmost column has a `1` in *both* rows, so only that column survives.

Another example: `6 & 3`

```
   6 = 0110
   3 = 0011
  --------- &
       0000  = 0
```

No column has `1` in both rows, so the result is `0`. This is exactly why `add(10, 4)`
finishes in one step later on — `10 & 4` turns out to be `0`, meaning "no carries needed."

### OR (`|`) — "at least one must be 1"

Result bit is `1` if **either** input bit is `1` (or both).

```
  1 | 1 = 1
  1 | 0 = 1
  0 | 1 = 1
  0 | 0 = 0
```

Example: `12 | 10`

```
  12 = 1100
  10 = 1010
  --------- |
       1110  = 14
```

### XOR (`^`) — "exactly one must be 1"

Result bit is `1` if the two input bits are **different**. This is the odd one out — it's
`0` when both bits are the same (`0,0` or `1,1`), and `1` when they differ.

```
  1 ^ 1 = 0
  1 ^ 0 = 1
  0 ^ 1 = 1
  0 ^ 0 = 0
```

Example: `12 ^ 10`

```
  12 = 1100
  10 = 1010
  --------- ^
       0110  = 6
```

Notice XOR is like addition *without carrying*: `1 ^ 1` gives `0`, the same digit you'd
write down in grade-school addition of `1+1=10` before you carry the `1`. That's the key
fact the `add` function below relies on.

### NOT (`~`) — flip every bit

Turns every `0` into `1` and every `1` into `0`. In Python, `~x` is defined as `-x - 1`
(this comes from two's complement — see section 3).

```
  ~5   ->  -6
  ~0   ->  -1
  ~-1  ->   0
```

### Left shift (`<<`) — multiply by 2, per position

Shifts every bit one (or more) places to the left, filling in `0`s on the right. Shifting
left by `n` multiplies the number by `2^n`.

```
  5 << 1:
    0101   (5)
   01010   (10)   -- shifted left by 1, i.e. x2

  5 << 2:
    0101   (5)
  010100   (20)   -- shifted left by 2, i.e. x4
```

### Right shift (`>>`) — divide by 2, per position

Shifts every bit one (or more) places to the right, discarding bits that fall off the end.
Shifting right by `n` divides by `2^n` (rounding down).

```
  20 >> 1:
   10100   (20)
    1010   (10)   -- shifted right by 1, i.e. /2

  20 >> 2:
   10100   (20)
     101   (5)    -- shifted right by 2, i.e. /4
```

## 3. Negative numbers: two's complement

Bitwise tricks for negative numbers rely on a representation called **two's complement**.
The rule: to negate a number, flip every bit and add 1.

Using a small 4-bit example (real computers use more bits, but the idea is identical):

```
   3 = 0011
  flip bits -> 1100
  add 1     -> 1101   =  -3 (in 4-bit two's complement)
```

The top bit acts as a sign flag: `0...` means non-negative, `1...` means negative. This is
exactly the `~b + 1` trick used in `subtract` below.

The code in this repo uses **32 bits** (`mask = 0xFFFFFFFF`) instead of 4, since that's a
realistic register size — but the mechanism is the same. Python integers don't have a
fixed width (they grow as large as needed and represent negatives as an *infinite* string
of leading 1s), so `mask` is used to truncate results down to a comparable 32-bit window,
the same way a C or Java `int` would naturally overflow/wrap.

## 4. `add(a, b)` — addition using XOR, AND, and shift

```python
def add(a, b):
    mask = 0xFFFFFFFF
    while b != 0:
        carry = (a & b) << 1
        a = (a ^ b) & mask
        b = carry & mask
    return a if a <= 0x7FFFFFFF else ~(a ^ mask)
```

The trick: recall from section 2 that `^` gives you the sum of two bits *without* carrying,
and `&` tells you exactly which positions *produce* a carry. So one round of the loop does:

- `a ^ b` → the digit-by-digit sum, ignoring carries
- `(a & b) << 1` → the carries, shifted into the position they need to be added to

Then it loops, treating the carry as a new number to add in, exactly like re-doing a column
of addition after you write down a carry digit. It stops once there's no carry left.

**Example without a carry: `10 + 4`**

```
  10 = 1010
   4 = 0100

  a & b = 1010 & 0100 = 0000   -- no shared 1-bits, so no carry at all
  a ^ b = 1010 ^ 0100 = 1110 = 14
```

Since `a & b` is `0`, `carry` is `0`, the loop body runs once and stops. Result: `14`.

**Example with a carry that has to propagate: `5 + 3`**

```
Start: a = 5 (0101), b = 3 (0011)

Step 1:
  carry = (0101 & 0011) << 1 = 0001 << 1 = 0010 = 2
  a     =  0101 ^ 0011       = 0110 = 6
  b     =  carry             = 2
  (a=6, b=2 — not done yet, b != 0)

Step 2:
  carry = (0110 & 0010) << 1 = 0010 << 1 = 0100 = 4
  a     =  0110 ^ 0010       = 0100 = 4
  b     =  carry             = 4
  (a=4, b=4 — still not done)

Step 3:
  carry = (0100 & 0100) << 1 = 0100 << 1 = 1000 = 8
  a     =  0100 ^ 0100       = 0000 = 0
  b     =  carry             = 8
  (a=0, b=8 — still not done)

Step 4:
  carry = (0000 & 1000) << 1 = 0
  a     =  0000 ^ 1000       = 1000 = 8
  b     =  0
  (b == 0, loop ends)

Result: a = 8   ✓ (5 + 3 = 8)
```

Every step just moves the "carry the 1" bit one column further left, the same way you'd
carry a digit by hand — it just takes a few more loop iterations here because the carry had
to ripple through three bit positions.

**Why the `mask` and the final `if/else`?**

Python ints don't overflow, so `& mask` is used after every step to force the numbers to
behave like a 32-bit register (see section 3). At the end, if the result's highest bit
(bit 31) is set, the 32-bit pattern actually represents a *negative* number in two's
complement, so it's converted back to a normal negative Python int:

```
add(-5, 3) internally works on the 32-bit patterns for -5 and 3.
The loop produces the bit pattern for -2, but as a giant positive
number (4294967294) because Python doesn't know it's "supposed" to be negative.

a = 4294967294 = 0xfffffffe, which is > 0x7FFFFFFF, so:
  a ^ mask = 0xfffffffe ^ 0xffffffff = 0x00000001 = 1
  ~1 = -1 - 1 = -2      <-  correct answer
```

## 5. `subtract(a, b)` — reuse `add` with a negated `b`

```python
def subtract(a, b):
    negative_b = add(~b, 1)   # two's complement: -b = ~b + 1
    return add(a, negative_b)
```

`a - b` is the same as `a + (-b)`. Section 3 showed that negating a number in two's
complement is "flip all bits, then add 1" — that's precisely `~b + 1`, computed here as
`add(~b, 1)`. Once we have `-b`, plain `add` finishes the job.

**Example: `10 - 4`**

```
  ~4 flips every bit of 4. In Python, ~x always equals -x - 1, so ~4 = -5.

  negative_b = add(~4, 1) = add(-5, 1) = -4     <- this is -b, since b = 4

  subtract(10, 4) = add(10, -4) = 6   ✓
```

**Example with negative inputs: `-5 - 3`**

```
  negative_b = add(~3, 1) = add(-4, 1) = -3   (this is -b, i.e. -(3))
  subtract(-5, 3) = add(-5, -3) = -8   ✓
```

## 6. `multiply(a, b)` — shift-and-add (binary long multiplication)

```python
def multiply(a, b):
    negative = (a < 0) ^ (b < 0)
    a, b = abs(a), abs(b)

    result = 0
    while b != 0:
        if b & 1:
            result = add(result, a)
        a = a << 1
        b = b >> 1

    return subtract(0, result) if negative else result
```

This mirrors how you'd multiply by hand in decimal — you multiply by each digit of one
number and add up shifted rows. In binary, every digit is `0` or `1`, so "multiply by this
digit" is either "add a shifted copy" or "add nothing." That's what the loop does:

- `b & 1` checks the *lowest* bit of `b` (is it `1` or `0`?) — see the AND truth table in
  section 2 (`x & 1` isolates the last bit).
- If that bit is `1`, add the current `a` into the running `result`.
- `a << 1` doubles `a` (shift left, section 2) — getting it ready for the *next* bit of
  `b`, one place more significant.
- `b >> 1` drops the bit we just examined and moves to the next one (shift right).

**Example: `6 * 5`**

```
  b = 5 = 0101 in binary — bits from lowest to highest: 1, 0, 1, 0

Start: a = 6, b = 5 (0101), result = 0

Step 1: b & 1 = 0101 & 0001 = 1  -> add a: result = 0 + 6  = 6
        a = 6 << 1 = 12
        b = 5 >> 1 = 2  (0010)

Step 2: b & 1 = 0010 & 0001 = 0  -> skip
        a = 12 << 1 = 24
        b = 2 >> 1 = 1  (0001)

Step 3: b & 1 = 0001 & 0001 = 1  -> add a: result = 6 + 24 = 30
        a = 24 << 1 = 48
        b = 1 >> 1 = 0

Loop ends (b == 0). Result = 30   ✓ (6 * 5 = 30)
```

This is exactly `6*5 = 6*(1 + 4) = 6*1 + 6*4 = 6 + 24 = 30` — the `1` and `4` come from
`5`'s binary form `0101` (bit 0 and bit 2 are set, worth `1` and `4`).

**Negative example: `-5 * 3`**

```
  negative = (True) ^ (False) = True   (exactly one operand is negative)
  a, b become abs(-5)=5, abs(3)=3
  ... shift-and-add on 5 and 3 gives 15 ...
  since negative is True: subtract(0, 15) = -15   ✓
```

## 7. `divide(dividend, divisor)` — shift-and-subtract (binary long division)

```python
def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("division by zero")

    negative = (dividend < 0) ^ (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)

    quotient = 0
    for shift in range(31, -1, -1):
        if (divisor << shift) <= dividend:
            dividend = subtract(dividend, divisor << shift)
            quotient = add(quotient, 1 << shift)

    return subtract(0, quotient) if negative else quotient
```

This is `multiply`'s mirror image, and it mirrors long division by hand: "how many times
does the divisor go in?" is answered one binary digit at a time, from the biggest possible
power of two down to the smallest, instead of guessing decimal digits.

For each `shift` from 31 down to 0, `divisor << shift` is "divisor times `2^shift`" (see
section 2). If that still fits inside what's left of `dividend`, we know that bit of the
quotient is `1` — subtract it out and record `2^shift` into the quotient. Otherwise that bit
is `0` and we move to the next, smaller shift.

**Example: `20 / 3`, using shifts 4 down to 0 (skipping the leading zero shifts for
brevity)**

```
Start: dividend = 20, divisor = 3, quotient = 0

shift=2: divisor << 2 = 3*4 = 12.  12 <= 20? yes.
         dividend = 20 - 12 = 8
         quotient = 0 + 4 = 4

shift=1: divisor << 1 = 3*2 = 6.   6 <= 8? yes.
         dividend = 8 - 6 = 2
         quotient = 4 + 2 = 6

shift=0: divisor << 0 = 3*1 = 3.   3 <= 2? no. skip.

Loop ends. quotient = 6   ✓ (20 / 3 = 6 remainder 2, integer division = 6)
```

Every "yes" answer is one `1` bit of the quotient in binary (`110` = `6`), found from the
most significant bit down — the same top-down logic as long division, just in base 2
instead of base 10.

**Negative example: `-15 / 3`**

```
  negative = True ^ False = True
  dividend, divisor become abs(-15)=15, abs(3)=3
  shift-and-subtract on 15 and 3 gives quotient = 5
  since negative is True: subtract(0, 5) = -5   ✓
```

Like C-style integer division, the result truncates toward zero (drops the fractional part)
rather than following Python's default floor division, which rounds toward negative
infinity.
