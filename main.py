#!/usr/bin/env python3
"""Write the 22 November 2026 front page to the output directory.

Round 2 (late morning WIB, 22 Nov): the image was refreshed with the
Bahrain industrial strike, the COP31 3am draft and closing plenary, the
Peru quake aftermath and a new Africa section.

The image (entry.png, committed in this repo) is drawn from scratch by
generate_image.py (build-time only, needs Pillow): every panel, chart and
the dotted world map is drawn in code, no photographs. This entrypoint is
standard library only, needs no network, and copies the same bytes on
every run, so two runs produce byte-identical output.

Output directory: $MAKEFUN_OUTPUT_DIR, or /output by default.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    size = os.path.getsize(dst)
    print(f"wrote {dst}: 1024x1024 PNG, {size} bytes (round 2)")
    assert size <= 1024 * 1024, f"entry.png over 1 MiB: {size}"
    return 0


if __name__ == "__main__":
    sys.exit(main())
