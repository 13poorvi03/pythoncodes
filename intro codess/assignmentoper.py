# Assignment Operators in Python

# Basic assignment
n = 3
print(n)   # = assigns value → n = 3

# Add and assign
n = 2
n += 3
print(n)   # += adds → 2 + 3 = 5

# Subtract and assign
n = 5
n -= 3
print(n)   # -= subtracts → 5 - 3 = 2

# Multiply and assign
n = 4
n *= 3
print(n)   # *= multiplies → 4 * 3 = 12

# Divide and assign
n = 9
n /= 3
print(n)   # /= divides → 9 / 3 = 3.0

# Modulus and assign
n = 10
n %= 3
print(n)   # %= remainder → 10 % 3 = 1

# Floor divide and assign
n = 10
n //= 3
print(n)   # //= floor division → 10 // 3 = 3

# Exponent and assign
n = 2
n **= 3
print(n)   # **= power → 2 ** 3 = 8

# Bitwise AND and assign
n = 6      # binary 110
n &= 3     # binary 011
print(n)   # &= AND → 110 & 011 = 010 → 2

# Bitwise OR and assign
n = 4      # binary 100
n |= 3     # binary 011
print(n)   # |= OR → 100 | 011 = 111 → 7

# Bitwise XOR and assign
n = 5      # binary 101
n ^= 3     # binary 011
print(n)   # ^= XOR → 101 ^ 011 = 110 → 6

# Right shift and assign
n = 8      # binary 1000
n >>= 2
print(n)   # >>= shift right → 1000 >> 2 = 0010 → 2

# Left shift and assign
n = 3      # binary 0011
n <<= 2
print(n)   # <<= shift left → 0011 << 2 = 1100 → 12