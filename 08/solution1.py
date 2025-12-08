from read_input import read_input, Coordinate
from union_find import DisjointSet
import heapq, math

'''
Given an adjacency list, return the sizes of the connected components sorted largest.
to smallest.
'''
def size_connected_components( adjacency: list[set[int]]):
    n = len(adjacency)
    disjointSet = DisjointSet(n)

    for a in range(n):
        for b in adjacency[a]:
            disjointSet.union(a, b)

    sizes = []
    for x in range(n):
        if disjointSet.find(x) == x:
            sizes.append(disjointSet.size[x])

    sizes.sort(key=lambda n: -n)
    return sizes

'''
Connect the k closest coordinates. Returns a list of adjacency sets, where
the c being in the r'th adjacency set means the r'th and c'th coordinates
are connected.
'''
def connect_closest(k: int, coordinates: list[Coordinate]) -> list[set[int]]:
    n = len(coordinates)
    distances = compute_distances(coordinates)

    minheap = []
    for r in range(n):
        for c in range(r + 1, n):
            heapq.heappush(minheap, (distances[r][c], r, c))

    adjacency = [set() for _ in range(n)]
    for _ in range(k):
        _, r, c = heapq.heappop(minheap)
        adjacency[r].add(c)
        adjacency[c].add(r)
    return adjacency

'''
Given a list coordinates, computes the distances between each one and returns
them as a 2D array, where the r'th row and c'th column contains the distance
between the r'th and c'th coordinates.
'''
def compute_distances(coordinates: list[Coordinate]) -> list[list[float]]:
    n = len(coordinates)
    result = []
    for a in coordinates:
        result.append([distance(a, b) for b in coordinates])
    return result

'''
Returns the distance between a and b.
'''
def distance(a: Coordinate, b: Coordinate) -> float:
    ax, ay, az = a
    bx, by, bz = b

    return ((ax - bx) ** 2 + (ay - by) ** 2 + (az - bz) ** 2) ** .5

test_adjacency = connect_closest(10, read_input("input1"))
test_largest = size_connected_components(test_adjacency)
assert math.prod(test_largest[:3]) == 40, test_largest

adjacency = connect_closest(1000, read_input())
largest = size_connected_components(adjacency)
print(math.prod(largest[:3]))
