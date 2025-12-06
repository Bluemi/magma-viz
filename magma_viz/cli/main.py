#!/usr/bin/env python3

import argparse
from pathlib import Path
from typing import List

import numpy as np

from magma_viz.viewer import MagmaViewer


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=Path)
    return parser.parse_args()


def main():
    args = get_args()

    np.set_printoptions(linewidth=150)

    magma = parse_magma(args.file)
    print(magma)

    viewer = MagmaViewer(magma)
    viewer.run()


def parse_magma(file: Path) -> np.ndarray:
    def _parse_line(line: str) -> List[int]:
        return [int(w) for w in line.strip().split(' ') if w]

    with open(file, 'r') as f:
        lines = f.readlines()

    lines = [_parse_line(l) for l in lines if l.strip()]
    return np.array(lines)


if __name__ == '__main__':
    main()