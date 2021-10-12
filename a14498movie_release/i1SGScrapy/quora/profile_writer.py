import csv
import os.path


def csv_profile_writer_to_local(profiles, filename, fieldnames):
    file_exists = os.path.isfile(filename)
    with open(filename, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()  # file doesn't exist yet, write a header
        for p in profiles:
            writer.writerow(p.dictstyle())
