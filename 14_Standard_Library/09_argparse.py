import argparse

def build_parser():
    p = argparse.ArgumentParser(
        prog="myapp",
        description="Sample CLI",
        epilog="Enjoy!"
    )
    p.add_argument("name", help="Your name")
    p.add_argument("-a", "--age", type=int, default=0, help="Your age")
    p.add_argument("-v", "--verbose", action="store_true")
    p.add_argument("--count", type=int, default=1)
    p.add_argument("--format", choices=["json", "text"], default="text")
    p.add_argument("--tags", nargs="+", default=[])
    p.add_argument("--input", type=argparse.FileType("r"))
    return p

def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.verbose:
        print(f"Args: {vars(args)}")

    for i in range(args.count):
        print(f"[{args.format}] Hello, {args.name}!")

    if args.tags:
        print(f"Tags: {', '.join(args.tags)}")

if __name__ == "__main__":
    import sys
    sys.argv = ["prog", "Alice", "-a", "30", "-v", "--count", "2", "--tags", "x", "y"]
    main()