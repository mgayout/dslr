import numpy as np # type: ignore
import csv
import sys
import os


def load_csv(filename):
    dataset = list()
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        for _ in reader:
            row = list()
            for value in _:
                try:
                    value = float(value)
                except:
                    if not value:
                        value = np.nan
                row.append(value)
            dataset.append(row)
    return np.array(dataset)


def count(data):
    return len(data)


def mean(data):
    total = 0
    for x in data:
        print(x)
        total += x
    if len(data) == 0:
        return 0
    return total / len(data)


def main():
    try:
        if len(sys.argv) != 2 or sys.argv[1][-4:] != ".csv" or not os.path.exists(sys.argv[1]):
            raise ValueError("\'describe.py\' needs a csv file as argument.")
        data = load_csv(sys.argv[1])
        header = data[0]
        body = data[1:]
        for i in range(len(header)):
            column = body[:, i]
            print(header[i], end=" ")
            print(count(column), end=" ")
            print(mean(column))
        

    except (ValueError, Exception) as err:
        print(err)


if __name__ == "__main__":
    main()
