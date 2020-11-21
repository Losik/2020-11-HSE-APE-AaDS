from collections import deque, namedtuple
from typing import Deque, Tuple

_, window_size = map(int, input().split())
values = map(int, input().split())

# Mins queue contain elements in current window such that
# for some continuation of a given sequence they may become
# a minimum on a window after zero or more shifts.
#
# Each element in a queue is a tuple (value, index) where
# * index is a 1-based element's sequence number
# * value is a original element's value
#
# The following invariants hold for mins queue:
# * values are always increasing
# * indices are always increasing
#
# Therefore, minimal element is always the first element in
# mins_queue
mins_queue: Deque[Tuple[int, int]]  = deque()

for i, value in enumerate(values, 1):

    # After shifting window to the right our minimal
    # element may turn out to be outside of the new
    # window boundaries. If this is the case we must
    # remove it from our min_queue
    if mins_queue and i - mins_queue[0][1] == window_size:
        mins_queue.popleft()

    # Now value is the rightmost element in our window
    # and it may render impossible for some elements of
    # of our min_queue to becme minimal elements. We must
    # remve such eelements from the min_queue before
    # appending value to the min_queue
    while mins_queue and value < mins_queue[-1][0]:
        mins_queue.pop()

    # Appending an element to the mins_queue
    mins_queue.append((value, i))

    # Printing current minimum if we must
    if i >= window_size:
        print(mins_queue[0][0])
