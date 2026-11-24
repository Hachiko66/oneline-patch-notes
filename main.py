#!/usr/bin/env python3
"""Real-life patch note: writes the entry text to /output/entry.txt (deterministic)."""
import os
import tempfile

TEXT = "v2.0.7: fixed a bug where the brain replayed your most embarrassing moment from 2014 every time you tried to fall asleep."
# Terse release-note register, version number, one specific recognisable bug of the body.

def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    fd, tmp = tempfile.mkstemp(dir=out_dir, prefix=".entry-")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
            f.write(TEXT)
        os.replace(tmp, target)
        os.chmod(target, 0o644)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise

if __name__ == "__main__":
    main()
