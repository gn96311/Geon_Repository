from itertools import permutations
import sys
name_list = list(map(str, sys.stdin.readline().split()))

len_name_list = len(name_list)

permutation_list = list(permutations(name_list, len_name_list))

name = []
for i in range(len(permutation_list)):
    naming = ' '.join(list(permutation_list[i]))
    print(naming)