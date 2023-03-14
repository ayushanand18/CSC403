from searching import binary_search
from sorting import quick_sort_deterministic

assert 3==binary_search([1,2,3,4,5], 4)
assert [1,2,3,4,5,6] == quick_sort_deterministic([3,2,1,6,5,4])
