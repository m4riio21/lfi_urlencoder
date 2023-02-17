#!/usr/bin/python3

import sys

def ascii2hex(source):
    return hex(ord(source))

def main(state):
        result = ""
        strin = sys.argv[1]
        if state != "":
                strin = state

        for char in strin:
                result += ascii2hex(char)

        return result.replace("0x", "%")

if __name__ == "__main__":
        if len(sys.argv) <= 1:
                print("Usage: python3", sys.argv[0], "<path_to_encode>")
                sys.exit(1)
        res = main("")

        if "--double" in sys.argv:
                print(main(res))
                sys.exit(0)

        print(res)

