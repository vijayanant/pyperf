from timer import Timer
from sorting import Sort
import random

random_items = [random.randint(-50, 100) for c in range(5000)]
sort=Sort()

with Timer() as t:
    sort.bubble_sort(random_items)
print "=> elasped bubble_sort: %s s" % t.elapsed

with Timer() as t:
    sort.insertion_sort(random_items)
print "=> elasped insertion_sort: %s s" % t.elapsed