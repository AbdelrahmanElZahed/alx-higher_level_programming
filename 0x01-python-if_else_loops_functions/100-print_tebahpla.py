#!/usr/bin/python3
def print_tebahpla():
    print("".format(
        *(
            chr(122 - i) if i % 2 == 0 else chr(90 - (i - 1))
            for i in range(26)
        )
    ), end="")

print_tebahpla()
