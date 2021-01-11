from heapq import heappop, heappush

heap = []

heappush(heap, 1)
heappush(heap, -1)
heappush(heap, 5)
heappush(heap, -2)
heappush(heap, 7)
heappush(heap, 17)

while heap:
    print(heap)
    print(heappop(heap))
