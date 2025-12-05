type Range = tuple[int, int]
type Ingredient = int

def read_input(filename = "input") -> tuple[list[Range], list[Ingredient]]:
    ranges = []
    ingredients = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if '-' in line:
                r = tuple(int(s) for s in line.split('-'))
                ranges.append(r)
            elif len(line):
                ingredients.append(int(line))
    return ranges, ingredients
