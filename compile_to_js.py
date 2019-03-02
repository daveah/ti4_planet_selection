#!/usr/bin/env python
import sys

from transcrypt.__main__ import main

if __name__ == '__main__':
    sys.argv = ["", "-b", "-m", "-n", "_ti4_planet_selection.py"]
    sys.exit(main())
