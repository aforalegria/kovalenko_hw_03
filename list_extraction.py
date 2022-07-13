base_list = ["item", 9, 5, True, 10.5, "content", (4, "value", 6), "128", 21, 66.66, ["bang", 77, False]]
numbers_list = []
print(numbers_list)


def is_numerical(list_item):
    if type(list_item) == int or type(list_item) == float:
        return True
    else:
        return False


def is_collection(list_el):
    if type(list_el) == list or type(list_el) == tuple:
        return True
    else:
        return False


def list_extractor(list_arg):
    for item in list_arg:
        if is_numerical(item):
            numbers_list.append(item)
        elif is_collection(item):
            for i in item:
                if is_numerical(i):
                    numbers_list.append(i)
    return numbers_list


list_extractor(base_list)
print(numbers_list)