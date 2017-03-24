def split(list):
    n = len(list)
    if n == 1:
        return list, []
    middle = int(n/2)
    return list[0:middle], list[middle:n]


def merge_sort(list):
    if len(list) == 0:
        return list
    a, b = split(list)
    if a == list:
        return a
    else:
        new_a = merge_sort(a)
        new_b = merge_sort(b)
        a_len = len(new_a)
        b_len = len(new_b)
        a_iter = 0
        b_iter = 0
        result = []
        while a_iter < a_len and b_iter < b_len:
            if new_a[a_iter] < new_b[b_iter]:
                result.append(new_a[a_iter])
                a_iter += 1
            else:
                result.append(new_b[b_iter])
                b_iter += 1
        while a_iter < a_len:
            result.append(new_a[a_iter])
            a_iter += 1
        while b_iter < b_len:
            result.append(new_b[b_iter])
            b_iter += 1
        return result
