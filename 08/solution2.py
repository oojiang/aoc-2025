from read_input import read_input, Coordinate
from union_find import DisjointSet
from solution1 import compute_distances
import heapq

'''
Given a list of coordinates, keep connecting the two closest unconnected
coordinates until all coordinates are indirectly connected.

Returns the final two coordinates that need to be connected.
'''
def connect_all(coordinates: list[Coordinate]) -> tuple[Coordinate, Coordinate]:
    n = len(coordinates)

    if n <= 1:
        return (0, 0, 0), (0, 0, 0)

    distances = compute_distances(coordinates)

    minheap = []
    for r in range(n):
        for c in range(r + 1, n):
            heapq.heappush(minheap, (distances[r][c], r, c))

    ds = DisjointSet(n)

    a, b = -1, -1
    while ds.num_components > 1:
        _, a, b = heapq.heappop(minheap)
        ds.union(a, b)

    assert (a, b) != (-1, -1)

    return coordinates[a], coordinates[b]

if __name__ == '__main__':
    testA, testB = connect_all(read_input("input1"))
    assert testA[0] * testB[0] == 25272, (testA, testB)

    A, B = connect_all(read_input())
    print(A[0] * B[0])
