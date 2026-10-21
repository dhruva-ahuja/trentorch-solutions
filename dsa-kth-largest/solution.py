from heapq import heappush, heappop, heapify

def solve(*args):
    """
    TODO: Implement your solution here.

    Problem: K-th Largest Element
    Description: Find kth largest in array
    """
    if len(args) == 0:
        return -1
    A = args[0]
    heap = []
    for a in A:
        if len(heap) < k or heap[0] < a:
            heappush(heap, a)
        if len(heap) > k:
            heappop(heap)
    return heap[0] if len(heap) > 0 else -1
