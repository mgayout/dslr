import matplotlib.pyplot as plt # type: ignore
import numpy as np # type: ignore
import sys
import os

from utils import load_csv
from maths import mean_, std_


def get(header, body):
    courses = []
    values = []
    for i, course in enumerate(header):
        if course == "Index":
            continue
        column = [row[i] for row in body]
        clean = [c for c in column if isinstance(c, (int, float, np.floating)) and not np.isnan(c)]
        if clean:
            courses.append(header[i])
            values.append(std_(clean, mean_(clean)))
    return courses, values


def plot_histogram(courses, values):
    data = sorted(zip(courses, values), key=lambda x: x[1])
    courses, values = zip(*data)

    plt.figure(figsize=(10, 6))
    bars = plt.bar(courses, values, color='skyblue')
    plt.xlabel("Hogwarts courses")
    plt.ylabel("Score Distribution")
    plt.title("Score Distribution per Course")
    plt.xticks(rotation=45, ha="right")

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.05, f"{yval:.2f}", ha='center', va='bottom', fontsize=8)
    
    plt.tight_layout()
    plt.show()
    #plt.savefig("histogramme.png")
    return


def main():
    try:
        if len(sys.argv) != 2 or sys.argv[1][-4:] != ".csv" or not os.path.exists(sys.argv[1]):
            raise ValueError("\'describe.py\' needs a csv file as argument.")
        header, body = load_csv(sys.argv[1])
        courses, values = get(header, body)
        plot_scatter(courses, values)
        plot_histogram(courses, values)


    except (ValueError, Exception) as err:
        print(err)


if __name__ == "__main__":
	main()
