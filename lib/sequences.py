#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
        return

    fib = [0, 1]

    # If the length is 1, only print [0]
    if length == 1:
        print([0])
        return

    # Build the sequence until it reaches the requested length
    while len(fib) < length:
        fib.append(fib[-1] + fib[-2])

    print(fib)
