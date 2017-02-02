def do_work(my_list, success_callback, error_callback):

    sorted_list = list(set(my_list))
    sorted_list.sort()

    if my_list == sorted_list:
        success_callback()
    else:
        error_callback()

def handle_success():
    print('Выполнено успешно')

def handle_error():
    try:
        raise ValueError
    except ValueError:
        print('Exception: ValueError')


my_list = [1,2,3,4,5]
do_work(my_list, handle_success, handle_error)

my_list = [1,2,3,4,3,5]
do_work(my_list, handle_success, handle_error)

my_list = [1,2,3,4,4,5]
do_work(my_list, handle_success, handle_error)