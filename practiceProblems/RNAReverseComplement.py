#
# site: https://edabit.com/challenge/M8jNckAgpC5ZFkhhG
# Create a function that finds the reverse complement of a ribonucleic acid (RNA) strand. The RNA will be represented
# as a string containing only the characters "A", "C", "G" and "U". Since RNA can only (canonically) allow pairings of
# A/U and G/C, the complement of an RNA would be as follows:
#
# original -> complement
# "AAA" -> "UUU"
# "UUU" -> "AAA"
# "GGG" -> "CCC"
# "CCC" -> "GGG"
# "GGAACC" -> "CCAAGG"
# Your function should find the complement on the right AND also reverse the resulting string.


def reverse_complement(input_sequence):
    code_connectors = {'A': 'U', 'U': 'A', 'G': 'C', 'C': 'G'}
    new_sequence = ""
    for x in input_sequence:
        new_sequence += code_connectors[x]
    return new_sequence[::-1]


print(reverse_complement("GUGU"))
print(reverse_complement("UCUCG"))
print(reverse_complement("CAGGU"))
