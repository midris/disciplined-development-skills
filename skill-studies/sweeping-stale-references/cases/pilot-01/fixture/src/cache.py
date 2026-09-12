"""Read application cache settings and print the effective maximum age."""

import argparse
import json
from pathlib import Path


def load_settings(path):
    value = json.loads(Path(path).read_text())["max_age"]
    if not isinstance(value, int) or isinstance(value, bool) or value < 0:
        raise ValueError("max_age must be a nonnegative integer")
    return value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max_age", type=int, default=30)
    parser.add_argument("--config")
    args = parser.parse_args()
    age = load_settings(args.config) if args.config else args.max_age
    print(f"Maximum cache age: {age} seconds")


if __name__ == "__main__":
    main()
