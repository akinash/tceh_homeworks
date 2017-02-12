def convert_dict(input_dict):
    result_dict = {}
    for key, value in input_dict.items():
        result_dict[str(key)] = value
    return result_dict

input_dict = {1:'123', 2:'3434'}
result_dict = convert_dict(input_dict)
print(result_dict)