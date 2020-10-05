
def count_occurances(string_1, string_2):
    """Count the number of occurances of string_1 in string_2"""
    array = string_2.split(string_1)
    return len(array) - 1
