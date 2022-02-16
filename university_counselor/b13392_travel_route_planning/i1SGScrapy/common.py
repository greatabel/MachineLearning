import csv


def csv_reader_from_localfile(filename):
    with open(filename, newline="") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        return list(reader)


def convert_si_to_number(x):
    total_stars = 0
    if "k" in x:
        if len(x) > 1:
            total_stars = float(x.replace("k", "")) * 1000  # convert k to a thousand
    elif "M" in x:
        if len(x) > 1:
            total_stars = float(x.replace("M", "")) * 1000000  # convert M to a million
    elif "B" in x:
        total_stars = float(x.replace("B", "")) * 1000000000  # convert B to a Billion
    else:
        total_stars = int(x)  # Less than 1000

    return int(total_stars)
