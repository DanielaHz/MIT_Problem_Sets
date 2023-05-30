
#PROBLEM SET 4

#Part A: String permutations 

import math

def get_permutations(sequence):
    """ Function that take a string and returns
    a list of all it's permutations"""

    if len(sequence) == 1:
        return [sequence]

    permutations = []

    start_letter = sequence[0]
    reduced_sequence = sequence[1:]
    reduced_permutations = get_permutations(reduced_sequence)

    for p in reduced_permutations:
        for i in range(0, len(p) + 1):
            perm = p[:i] + start_letter + p[i:]
            permutations.append(perm)

    return permutations


if __name__ == '__main__':
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

if __name__ == '__main__':
    example_input = 'da'
    print('Input:', example_input)
    print('Expected Output:', ['da', 'ad'])
    print('Actual Output:', get_permutations(example_input))

if __name__ == '__main__':
    example_input = 'las'
    print('Input:', example_input)
    print('Expected Output:', ['las', 'als', 'asl', 'lsa', 'sla', 'sal'])
    print('Actual Output:', get_permutations(example_input))
