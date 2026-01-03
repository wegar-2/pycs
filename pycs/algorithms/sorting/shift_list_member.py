

def shift_list_member(values: list[int], pos_from: int, pos_to: int):

    if any(not isinstance(x, int) for x in values):
        raise ValueError(f"Invalid values: at least one member is not an int!")
    if pos_from >= len(values) or pos_from < 0:
        raise IndexError(f"Position from out of range of the list...")
    if pos_to >= len(values) or pos_to < 0:
        raise IndexError(f"Position from out of range of the list...")

    if pos_from == pos_to:
        return values

    reverse_before_return: bool = False
    if pos_from < pos_to:
        reverse_before_return = True
        values = values[::-1]
        pos_from = len(values) - 1 - pos_from
        pos_to = len(values) - 1 - pos_to

    i = pos_from
    temp = values[pos_from]
    while i > pos_to:
        values[i] = values[i-1]
        i = i - 1
    values[pos_to] = temp

    if reverse_before_return:
        values = values[::-1]
    return values
