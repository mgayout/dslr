import numpy as np
import csv
import sys
import os


def main():
    try:
        if len(sys.argv) != 2 or sys.argv[1][-4:] != ".csv" or not os.path.exists(sys.argv[1]):
            raise ValueError("\'describe.py\' needs a csv file as argument.")
        

    except (ValueError, Exception) as err:
        print(err)


if __name__ == "__main__":
    main()
