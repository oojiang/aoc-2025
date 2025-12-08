class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        parentA = self.find(a)
        parentB = self.find(b)

        if parentA == parentB:
            return

        if self.size[parentA] < self.size[parentB]:
            parentA, parentB = parentB, parentA

        self.parent[parentB] = parentA
        self.size[parentA] += self.size[parentB]
