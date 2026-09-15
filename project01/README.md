# Introduction
This project parses a Variant Call Format (VCF) file from ClinVar.
The goal of the project is to identify rare genetic variants with AF_EXAC less than 0.0001, 
and tally the disease (CLNDN) associated with them across the dataset.
The program reads the clinvar_20190923_short.vcf file line per line.
It then extracts the required fields in the INFO column for each variant.
It then checks if its rare and builds a tally of disease occurrences among the rare variants.
The final tally is then printed to the console.

# Pseudocode
Function parse_line(line)
    split line into columns by tab
    get the last column: info columns
    split info by ; into key-value pairs
    build a dictionary of all key=value pairs
    IF "AF_EXAC" is not in dictionary:
        RETURN empty list
    IF AF_EXAC value >= 0.0001
        RETURN empty list
    split CLNDN value by "|" to get the disease list
    remove "not_specified" and "not_provided" from list
    RETURN remaining disease list


FUNCTION read_file(filename):
    build dictionary of counts
    open file 
        for every line
            if the line starts with #
                skip to next line
            strip white spaces at end of each line
            call parse_line on the line, store result as diseases
            for each disease in diseases:
                IF disease in counts:
                    add 1 to its count
                ELSE:
                    set its count to 1
RETURN counts


# Successes
Learned how to create pull requests and collaborate on github.


# Struggles
Description of the stumbling blocks the team experienced

# Personal reflections
## Group Leader
Initially had trouble working with github.


## Other member
Other member's reflection on the project

# Generative AI Appendix
As per the syllabus
