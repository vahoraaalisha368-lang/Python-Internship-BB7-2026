def make_frozenset(input_list):
    """Accepts any list and returns a frozenset made from it."""
    return frozenset(input_list)


# Example usage:
my_list = [1, 2, 3, 2, 1]
result_frozenset = make_frozenset(my_list)
print(result_frozenset)