import os, glob, pathlib, sys

DIST = pathlib.Path("dist")

def previous_artifact():
    zips = sorted(glob.glob(str(DIST / "*.zip")))
    if len(zips) < 2:
        print("No previous artifact to roll back to")
        return None
    # last is current; previous is -2
    return zips[-2]

if __name__ == "__main__":
    prev = previous_artifact()
    if not prev:
        sys.exit(1)
    print(prev)  