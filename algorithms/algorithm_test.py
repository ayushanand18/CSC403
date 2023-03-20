from convex_hull import graham_scan
from random import randint
from searching import binary_search
from sorting import quick_sort_deterministic, quick_sort_randomised
from time import time

assert 3==binary_search([1,2,3,4,5], 4)
assert [1,2,3,4,5,6] == quick_sort_deterministic([3,2,1,6,5,4])
assert [1,2,3,4,5,6] == quick_sort_randomised([3,2,1,6,5,4])

# benchmarking performance on a set of 1,000,000 elements
input_list = [randint(1,1000000) for i in range(1000000)]
a = time()
quick_sort_deterministic(input_list)
b = time()
quick_sort_randomised(input_list)
c = time()
print(f'Deterministic time: {b-a} v/s Randomised: {c-b}')

assert [[-1, 1], [1, 2], [8, 7], [5, 6], [-1, 1]] == graham_scan([[1,2], [3,4], [8,7], [5,6], [-1,1]])
assert [[4, -16], [12, 8], [-3, 12], [-2, 4], [4, -16]] == graham_scan([[1.1, 1.2], [-2,4], [-3,12], [4,-16], [12,8]])
