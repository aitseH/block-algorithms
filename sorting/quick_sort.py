import random

random_items = [random.randint(-50, 100) for c in range(20)]

def quick_sort(items):
  if len(items) > 1:
    pivot_index = len(items)/2
    smaller_items = []
    larger_items = []

    for i, val in enumerate(items):
      if i != pivot_index:
        if val < items[pivot_index]:
          smaller_items.append(val)
        else:
          larger_items.append(val)
    print "smaller_items", smaller_items
    print "larger_items", larger_items
    print "pivot_index", pivot_index

    quick_sort(smaller_items)
    quick_sort(larger_items)
    items[:] = smaller_items + [items[pivot_index]] + larger_items

print 'Before: ', random_items
quick_sort(random_items)
print "After: ", random_items