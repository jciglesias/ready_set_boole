def powerset(lst: list) -> list:
    if isinstance(lst, list):
        ret = [[lst[j] for j in range(len(lst)) if counter & (1 << j) > 0] for counter in range(pow(2, len(lst)))]
        return ret
    return
