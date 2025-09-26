import sys
import os

from utils import load_csv
from maths import *


def main():
    try:
        if len(sys.argv) != 2 or sys.argv[1][-4:] != ".csv" or not os.path.exists(sys.argv[1]):
            raise ValueError("\'describe.py\' needs a csv file as argument.")
        header, body = load_csv(sys.argv[1])
        max_len = max(len(string) for string in header)
        print(f'| {"":{max_len}} | {"Count":^12} | {"Mean":^12} | {"Std":^12} | {"Min":^12} | {"25%":^12} | {"50%":^12} | {"75%":^12} | {"Max":^12} |')
        for i in range(len(header)):
            column = [row[i] for row in body]
            count = count_(column)
            mean = mean_(column)
            std = std_(column)
            minn = min_(column)
            q1 = q1_(column)
            median = median_(column)
            q3 = q3_(column)
            maxx = max_(column)
            print(f'| {header[i]:<{max_len}} | {count:12.4f} | {mean:12.4f} | {std:12.4f} | {minn:12.4f} | {q1:12.4f} | {median:12.4f} | {q3:12.4f} | {maxx:12.4f} |')
        

    except (ValueError, Exception) as err:
        print(err)


if __name__ == "__main__":
    main()
