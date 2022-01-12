"""
Mechanical Engineering Department
ABET Student Sample Performance Analysis

Author: Aaron Huynh

Initial Commit: 15 September 2021
Last Update: 15 September 2021
"""

# from pathlib import Path
# import os
from statistics import mean, median


def max_score(scores):
    return max(scores)


def median_score(scores):
    return median(scores)


def mean_score(scores):
    return mean(scores)


def min_score(scores):
    return min(scores)


def main():
    scores = []
    IDs = []
    search = ":score:"
    search2 = ".pdf"
    clean = "original"
    print("This program analyzes performance of submission metadata")

    # user_dir = Path('/Users/aaronhuynh/Downloads/Mechanical Engineering Department/ME213')

    # change based on metadata you want to analyze
    filename = "submission_metadata_"
    course = "ME213F_"
    assignment = "Quiz03"
    # remove extra condition if not applicable to assignment
    # condition = "_Individual"
    file_type = ".txt"

    # remove extra condition if not applicable to assignment
    filename = filename + course + assignment + file_type# + condition + file_type
    open_file = open(filename, "r")
    read_file = open_file.readlines()

    flag = 0
    flag2 = 0
    counter = 0

    for file in read_file:
        counter += 1

        if search in file:
            flag = 1
            value = file[10:14]
            scores.append(value)
        if clean not in file:

            if search2 in file:
                flag2 = 1
                ID = file[0:9]
                IDs.append(ID)

            # print("String '", search, "'", "found on line", counter)

    new_scores = [float(s) for s in scores]
    print("\nNumber of submissions =", len(new_scores))

    # print(new_scores)
    # print(IDs)

    best = max_score(new_scores)
    poor = min_score(new_scores)
    average = round(mean_score(new_scores), 1)
    average_for_index = round(mean_score(new_scores), 0)
    med = median_score(new_scores)

    student_best = new_scores.index(best)
    student_poor = new_scores.index(poor)
    # student_average = new_scores.index(average_for_index)
    student_median = new_scores.index(med)

    id_best = IDs[student_best]
    id_poor = IDs[student_poor]
    # id_average = IDs[student_average]
    id_median = IDs[student_median]

    print("\nBest Performance:", best, ", ID:", id_best)
    print("Poorest Performance:", poor, ", ID:", id_poor)
    # print("Average Performance:", average, ", ID:", id_average)
    print("Median Performance: ", med, ", ID:", id_median)

    if flag == 0:
        print("String '", search, "'", "not found")
    if flag2 == 0:
        print("String '", search2, "'", "not found")

    open_file.close()


if __name__ == "__main__":
    main()
