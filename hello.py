from __future__ import print_function
import sys


def hello(what):
    print('Hello, {}!'.format(what))


def say_what():
    return 'hello'


def main():
    hello(say_what())
    return 0

def new_func():
    pass


if __name__ == '__main__':
    sys.exit(main())
