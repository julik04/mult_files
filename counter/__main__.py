import sys
import argparse
import pathlib

from .funcs import count_chars_from_file

parser = argparse.ArgumentParser()

parser.add_argument("filename", type=pathlib.Path)

args = parser.parse_args()

if not args.filename.exists() or not args.filename.is_file():
    print("Path not exists or isn't file")
    sys.exit()

with args.filename.open("r") as f:
    for char, n in count_chars_from_file(f).items():
        print(f'{char}: {n}')