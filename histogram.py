import matplotlib.pyplot as plt # type: ignore
import numpy as np # type: ignore
import sys
import os

from utils import load_csv
from maths import mean_, std_

def main():
    try:
        if len(sys.argv) != 2 or sys.argv[1][-4:] != ".csv" or not os.path.exists(sys.argv[1]):
            raise ValueError("\'describe.py\' needs a csv file as argument.")
        header, body = load_csv(sys.argv[1])
        courses = []
        values = []
        for i in range(len(header)):
            column = [row[i] for row in body]
            clean = []
            for c in column:
                if isinstance(c, (int, float, np.floating)) and not np.isnan(c):
                    clean.append(c)
            if not clean:
                continue
            else:
                courses.append(header[i])
                values.append(std_(clean, mean_(clean)))
        plt.bar(courses, values)
        plt.xlabel("Hogwarts courses")
        plt.xticks(rotation=45, ha="right")
        plt.ylabel("Score Distribution")
        plt.title("Test")
        plt.savefig("histogramme.png")
        

            

    except (ValueError, Exception) as err:
        print(err)


if __name__ == "__main__":
	main()
