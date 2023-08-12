#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args_count = len(argv) - 1
    argument_list = argv[1:]

    if args_count == 0:
        print("0 arguments.")
    elif args_count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(args_count))

    for index, args in enumerate(argument_list, start = 1):
        print("{}: {}".format(index, args))
