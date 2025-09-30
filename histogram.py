import matplotlib.pyplot as plt # type: ignore
import numpy as np # type: ignore
import sys
import os

from utils import load_csv
from maths import mean_, std_


def get(header, body):
    values = {}
    for features in header:
        values[features] = {"Gryffindor": [], "Hufflepuff": [], "Ravenclaw": [], "Slytherin": []}
    for row in body:
        house = row[header.index("Hogwarts House")]
        for i, val in enumerate(row):
            if isinstance(val, (int, float)) and not np.isnan(val):
                values[header[i]][house].append(val)
    return values


def plot_histograms(values):
    legend = {"Gryffindor": "red", "Hufflepuff": "yellow", "Ravenclaw": "blue", "Slytherin": "green"}
    for course, house_scores in values.items():
        plt.figure()
        for house, scores in house_scores.items():
            scores = np.array(scores)
            if len(scores) == 0:
                continue
            plt.hist(scores, bins=25, alpha=0.5, label=house, color=legend[house])
        
        plt.title(course)
        plt.xlabel("Scores")
        plt.ylabel("Number of Students")
        plt.legend(loc="upper right")
        plt.show()

def main():
    try:
        if len(sys.argv) != 2 or sys.argv[1][-4:] != ".csv" or not os.path.exists(sys.argv[1]):
            raise ValueError("\'describe.py\' needs a csv file as argument.")
        header, body = load_csv(sys.argv[1])
        values = get(header, body)
        plot_histograms(values)


    except (ValueError, Exception) as err:
        print(err)


if __name__ == "__main__":
	main()
