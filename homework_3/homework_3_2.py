def sort_list(input_list):
    result_list = []
    try:
        for element in input_list:
            result_list.append(int(element))
        result_list.sort()
    except ValueError:
        print('ValueError: в списке допустимы только целые числа!')
    return result_list


input_list_1 = [1,2,3]
sort_list(input_list_1)

input_list_1 = [1,2,'str']
sort_list(input_list_1)

