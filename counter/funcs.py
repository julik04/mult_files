
def count_chars_from_file(file):
    from collections import defaultdict

    counter = defaultdict(int)
    for line in file:
        for char in filter(str.isalpha, line):
            counter[char.lower()] += 1

    return counter
