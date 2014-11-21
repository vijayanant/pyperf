import cProfile
import random
from sorting import Sort


random_items = [random.randint(-50, 100) for c in range(5000)]
sort=Sort()

cProfile.run('sort.bubble_sort(random_items)')