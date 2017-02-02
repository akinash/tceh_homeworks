def list_multiplication(input_list):
    result = 1
    for element in input_list:
        result *= element
    return result

input_list = [2,3.3,4]
list_multiplication = list_multiplication(input_list)
print(list_multiplication)