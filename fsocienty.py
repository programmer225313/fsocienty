'''
Get path to directory and repeat times.
Then execute command "tree" from specified path specified number of times
'''
import os
import sys
import re


def fake_hack(repeat=10, path="."):
    '''Executes a command "tree" from the specified directory the specified number of times.'''
    for _ in range(repeat):
        os.system(f"tree {path}")


def check_dirs(lst):
    """Get list and return list of paths to dirs from that list."""
    exists_paths = []
    for arg in lst:
        if os.path.isdir(arg):
            exists_paths.append(arg)
    return exists_paths


def check_for_integers(lst):
    """Get list and return list of integers from that list"""
    integers = []
    for arg in lst:
        if re.fullmatch(r'\d*', arg):
            integers.append(int(arg))
    return integers


if __name__ == "__main__":
    start_path = check_dirs(sys.argv)[0]
    repeat_times = check_for_integers(sys.argv)[0]

    fake_hack(repeat_times, start_path)
