import numpy as np # type: ignore
import sys
import os

from utils import load_csv
from maths import *


def main():
    try:
        if len(sys.argv) != 2 or sys.argv[1][-4:] != ".csv" or not os.path.exists(sys.argv[1]):
            raise ValueError("\'describe.py\' needs a csv file as argument.")
        header, body = load_csv(sys.argv[1])
        max_len = max(len(h) for h in header)
        print(f'| {"":{max_len}} | {"Count":^12} | {"Mean":^12} | {"Std":^12} | {"Min":^12} | {"25%":^12} | {"50%":^12} | {"75%":^12} | {"Max":^12} |')
        for i in range(len(header)):
            column = [row[i] for row in body]
            count = count_(column)
            clean = []
            for c in column:
                if isinstance(c, (int, float, np.floating)) and not np.isnan(c):
                    clean.append(c)
            if not clean:
                print(f'| {header[i]:<{max_len}} | {count:12.4f} | {np.nan:12.4f} | {np.nan:12.4f} | {np.nan:12.4f} | {np.nan:12.4f} | {np.nan:12.4f} | {np.nan:12.4f} | {np.nan:12.4f} |')
            else:   
                mean = mean_(clean)
                std = std_(clean, mean)
                minn = min(clean)
                q1 = percentile_(clean, 25)
                median = percentile_(clean, 50)
                q3 = percentile_(clean, 75)
                maxx = max(clean)
                print(f'| {header[i]:<{max_len}} | {count:12.4f} | {mean:12.4f} | {std:12.4f} | {minn:12.4f} | {q1:12.4f} | {median:12.4f} | {q3:12.4f} | {maxx:12.4f} |')
        

    except (ValueError, Exception) as err:
        print(err)


if __name__ == "__main__":
    main()
