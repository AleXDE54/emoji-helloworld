#!/usr/bin/env python3
"""
Test project that prints emoji using the `emoji` package
"""
try:
    import emoji
except ImportError:
    print("Package 'emoji' is missing. Install via rtls or pip!")
    exit(1)

def main():
    print("Hello World! 😀🌍")
    print(emoji.emojize("Python is fun :snake: :tada:"))

if __name__ == "__main__":
    main()
