import cProfile
import random
from sorting import Sort

from memory_profiler import profile

sort=Sort()
random_items = [random.randint(-50, 100) for c in range(5000)]

@profile
def test():
    sort.bubble_sort(random_items)
    sort.insertion_sort(random_items)
    sort.quick_sort(random_items)
    sort.heap_sort(random_items)
    #sort.merge_sort(random_items)
if __name__ == '__main__':
	test()
