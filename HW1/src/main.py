import pandas as pd
import numpy as np
import os


for root, dirs, files in os.walk("../data/"):
    for f in files:
        fullpath = os.path.join(root, f)
        print fullpath
        with open(fullpath, 'r+b') as r:
            with open(fullpath, 'r+b') as w:
                for line in r:
                    line = line.lstrip()
                    w.write(line)

