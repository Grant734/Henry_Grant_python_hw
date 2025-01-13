def common_elements (list1, list2):
    common = []

    for item in list1:
        if item in list2 and item not in common:
            common.append(item)

    return common

list1 = [1, 2, 2, 3, 4, 5, 6, 6]
list2 = [2, 4, 5, 6, 6, 7]

result = common_elements(list1, list2)
print("Common elements:", result)