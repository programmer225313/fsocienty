'''
Get path to directory and fake target name.
Then print some text and execute command "tree" from specified path to create the appearance of hacking.
'''
import os
import sys
import time
import random


def fake_hack(fake_target="NASA", path="."):
    '''Print some text and executes a command "tree" from the specified directory to create the appearance of hacking.'''
    print(f"Hacking {fake_target}...")
    for x in range(0, 100, 10):
        fake_progress = random.randint(x, x + 10)
        time.sleep(0.1)
        print(f"{fake_progress} ready...")
        time.sleep(0.1)
    print(f"{fake_target} hacked!")
    time.sleep(0.1)
    print("Scanning storage...")
    time.sleep(0.5)
    os.system(f"tree {path}")
    time.sleep(0.5)
    print("All files finded!")
    time.sleep(0.1)
    print("Stealing data...")
    time.sleep(0.5)
    os.system(f"tree {path}")
    time.sleep(0.5)
    print("All files copied to remote server!")
    time.sleep(1)



def check_dirs(lst):
    """Get list and return list of paths to dirs from that list."""
    exists_paths = []
    for arg in lst:
        if os.path.isdir(arg):
            exists_paths.append(arg)
    return exists_paths


if __name__ == "__main__":
    start_path = check_dirs(sys.argv)[0]
    target_name = sys.argv[2]

    fake_hack(target_name, start_path)