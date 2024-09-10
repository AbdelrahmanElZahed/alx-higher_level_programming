#!/usr/bin/python3

def print_tebahpla():
    result = ''.join(
        chr(122 - i) if i % 2 == 0 else chr(90 - i + 1)
        for i in range(26)
    )
    print("{}".format(result), end="")


print_tebahpla()

