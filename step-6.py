# Sorting Information

# Sorting algorithm envisioned

# step-1


def sort_list(unsorted_list):
    sorted_list = []

    min_value = min(unsorted_list)
    sorted_list.append(min_value)
    return sorted_list


steps = [4, 2, 8]
sorted_steps = sort_list(steps)
print(sorted_steps)

# step-2


def sort_list(unsorted_list):
    sorted_list = []
    for i in range(len(unsorted_list)):
        min_value = min(unsorted_list)
        sorted_list.append(min_value)
    return sorted_list


steps = [4, 2, 8]
sorted_steps = sort_list(steps)
print(sorted_steps)

# step-3


def sort_list(unsorted_list):
    sorted_list = []
    for i in range(len(unsorted_list)):
        min_value = min(unsorted_list)
        sorted_list.append(min_value)
        unsorted_list.remove(min_value)
    return sorted_list


steps = [4, 2, 8]
sorted_steps = sort_list(steps)
print(sorted_steps)