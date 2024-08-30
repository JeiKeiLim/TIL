
def get_every_combination(n: int):
    """Return all possible combinations of n elements

    Args:
        n: the number of elements

    Returns:
        List[List[int]]: all possible combinations
    """
    result = []
    for i in range(1 << n):
        temp = []
        for j in range(n):
            if i & (1 << j):
                temp.append(j)
        result.append(temp)
    return result


if __name__ == "__main__":
    print(get_every_combination(3))
