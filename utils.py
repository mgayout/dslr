import numpy as np # type: ignore
import csv


def load_csv(filename):
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

    header = rows[0]
    dataset = []

    for row in rows[1:]:
        new_row = []
        for value in row:
            try:
                new_row.append(float(value))
            except:
                if not value:
                    new_row.append(np.nan)
                else:
                    new_row.append(value)
        dataset.append(new_row)

    return header, np.array(dataset, dtype=object)