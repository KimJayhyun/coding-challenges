import sys

# get_inputs
(A, B, C) = tuple(map(int, sys.stdin.readline().split()))

print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)
