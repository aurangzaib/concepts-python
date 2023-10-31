import functools as ft

def mapper_(x): return x + 0.1
def filter_(x): return x if x % 2 == 0 else None
def reducer_(x, y): return x + y

input_array     = [x for x in range(0, 10, 1)]          # Input
map_result2     = list(map(mapper_, input_array))       # Map
filter_result2  = list(filter(filter_, input_array))    # Filter
reduce_result2  = ft.reduce(reducer_, input_array)      # Reduce

pass