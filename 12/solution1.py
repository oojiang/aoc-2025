from read_input import read_input

def count_possible(shapes, trees):
    sizes = [sum(sum(row) for row in shape) for shape in shapes]

    possible = 0
    impossible = 0
    unclear = 0

    for dim, counts in trees:
        if (dim[0] // 3) * (dim[1] // 3) >= sum(counts):
            possible += 1
        elif (dim[0] * dim[1]) < sum([counts[i] * sizes[i] for i in range(len(counts))]):
            impossible += 1
        else:
            unclear += 1
    return possible, impossible, unclear

if __name__ == '__main__':
    shapes, trees = read_input()
    possible, impossible, unclear = count_possible(shapes, trees)

    print('possible', possible)
    print('impossible', impossible)
    print('unclear', unclear)
