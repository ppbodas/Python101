def add(a, b):
    mask = 0xFFFFFFFF  # simulate 32-bit overflow since Python ints are arbitrary precision
    while b != 0:
        carry = (a & b) << 1
        a = (a ^ b) & mask
        b = carry & mask
    return a if a <= 0x7FFFFFFF else ~(a ^ mask)

def subtract(a, b):
    negative_b = add(~b, 1)  # two's complement: -b = ~b + 1
    return add(a, negative_b)

def multiply(a, b):
    negative = (a < 0) ^ (b < 0)
    a, b = abs(a), abs(b)

    result = 0
    while b != 0:
        if b & 1:          # current bit of b is set, add the shifted a
            result = add(result, a)
        a = a << 1          # double a
        b = b >> 1          # move to the next bit of b

    return subtract(0, result) if negative else result

def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("division by zero")

    negative = (dividend < 0) ^ (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)

    quotient = 0
    for shift in range(31, -1, -1):        # try biggest shifts first
        if (divisor << shift) <= dividend:
            dividend = subtract(dividend, divisor << shift)
            quotient = add(quotient, 1 << shift)

    return subtract(0, quotient) if negative else quotient

def main():
    a = 10  # 0b1010
    b = 4   # 0b0100

    print(a & b)   # AND        -> 0
    print(a | b)   # OR         -> 14
    print(a ^ b)   # XOR        -> 14
    print(~a)      # NOT        -> -11
    print(a << 2)  # Left shift -> 40
    print(a >> 2)  # Right shift-> 2

    print(add(a, b))    # 14
    print(add(-5, 3))   # -2
    print(add(-5, -7))  # -12
    print(add(0, 0))    # 0

    print(subtract(a, b))    # 6
    print(subtract(b, a))    # -6
    print(subtract(-5, 3))   # -8
    print(subtract(-5, -7))  # 2
    print(subtract(0, 0))    # 0

    print(multiply(a, b))    # 40
    print(multiply(-5, 3))   # -15
    print(multiply(-5, -7))  # 35
    print(multiply(0, 9))    # 0

    print(divide(a, b))     # 2
    print(divide(-15, 3))   # -5
    print(divide(35, -7))   # -5
    print(divide(0, 5))     # 0

    return None

if __name__ == "__main__":
    main()
