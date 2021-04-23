#!/usr/bin/env python
from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument("command", help="name of the utility to run")
    parser.add_argument("-n", "--name", help="person to greet")

    args = parser.parse_args()

    #print("arguments:", args)
    if args.command == 'hello':
        person = "World"
        if args.name:
            person = args.name
        print(f"Hello {person}")

main()