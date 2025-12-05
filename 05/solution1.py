from read_input import read_input, Range, Ingredient

def count_fresh_ingredients(ranges: list[Range], ingredients: list[Ingredient]) -> int:
    ranges.sort()
    ingredients.sort()

    r = 0 # which index of ranges we're currently on.
    num_fresh = 0
    for id in ingredients:

        # If the end of the current range is less than the current id,
        # then we can skip it because:
        #   1. the current id is not in it.
        #   2. no future id will be in it, as future ids > current id.
        while r in range(len(ranges)) and ranges[r][1] < id:
            r += 1

        # If the current beginning is <= the current id, then it is in a range.
        # If it is not, then it is not part of any range, as the beginning of all
        #   future ranges are >= the current beginning.
        if r in range(len(ranges)) and ranges[r][0] <= id:
            num_fresh += 1

    return num_fresh

test_ranges, test_ingredients = read_input('input1')
test_num_fresh = count_fresh_ingredients(test_ranges, test_ingredients)
assert test_num_fresh == 3, test_num_fresh

ranges, ingredients = read_input()
print(count_fresh_ingredients(ranges, ingredients))
