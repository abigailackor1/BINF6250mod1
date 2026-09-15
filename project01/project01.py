#!/usr/bin/env python
from pprint import pprint

# Modify this function signature and fill in the details
def parse_line(line):

    # tab separated columns
    columns = line.split("\t")

    # info is in the last column of the line
    info = columns[-1]

    # info contains key-value pairs separated by ;
    key_pairs = info.split(";")

    # make a dictionary of all the key-value pairs
    info_dict = {}

    # for each key-value pair,
    for pair in key_pairs:
       split_pair = pair.split("=") # split by the = sign

       # ignore if there is no value
       if len(split_pair) < 2:
           continue

       key = split_pair[0] # index location of key
       value = split_pair[1] # index location of value
       info_dict[key] = value

    # Skip line if "AF_EXAC" not present
    if "AF_EXAC" not in info_dict:
        return []

    af_value = float(info_dict["AF_EXAC"])

    if af_value >= 0.0001:
        return []

    if "CLNDN" not in info_dict:
        return []

    diseases = info_dict["CLNDN"].split("|")
    filtered_diseases = []

    for disease in diseases:
        if disease != "not_specified" and disease != "not_provided":
            filtered_diseases.append(disease)

    return filtered_diseases


# Modify this function signature and fill in the details
def read_file(filename):
    counts = {}

    with open("clinvar_20190923_short.vcf", "r") as f:
        for line in f:
            if line.startswith("#"):
                continue

            line = line.strip()
            diseases = parse_line(line)

            for disease in diseases:
                if disease in counts:
                    counts[disease] += 1

                else:
                    counts[disease] = 1

    return counts

if __name__ == "__main__":
    pprint(read_file("clinvar_20190923_short.vcf"))
