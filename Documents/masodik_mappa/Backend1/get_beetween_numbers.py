def get_between_numbers(a, b):
    """
    This function will return in between numbers from two numbers.
    :param a:
    :param b:
    :return:
    """
    x = []
    if b < a:
        x.extend(range(b, a))
        x.append(a)
    else:
        x.extend(range(a, b))
        x.append(b)

    return x
#Result

print(get_between_numbers(5, 9))
print(get_between_numbers(9, 5))
print(get_between_numbers(10,20))

#[5, 6, 7, 8, 9]  
#[5, 6, 7, 8, 9]