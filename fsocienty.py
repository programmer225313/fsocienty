import os
import sys
import re


def fake_hack(repeat=10, path="."):
    for _ in range(repeat):
        os.system(f"tree {path}")


def check_dirs(lst):
    exists_paths = []
    for arg in lst:
        if os.path.isdir(arg):
            exists_paths.append(arg)
    return exists_paths


def check_for_integers(lst):
    integers = []
    for arg in lst:
        if re.fullmatch(r'/d', arg):
            integers.append(arg)
    return integers


if __name__ == "__main__":
    start_path = check_dirs(sys.argv)[0]
    repeat_times = check_for_integers(sys.argv)[0]

    fake_hack(repeat_times, start_path)
