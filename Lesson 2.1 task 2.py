def classes(error_amount):
    error_inheritance = {}
    for i in range(error_amount):
        error_name = input().split(' : ')
        if len(error_name) == 1:
            error_inheritance[error_name[0]] = []
        else:
            error_inheritance[error_name[0]] = error_name[1].strip().split(" ")
        for elem in error_inheritance[error_name[0]]:
            if elem not in error_inheritance:
                error_inheritance[elem] = []
    return error_inheritance


def get_parent(error_list, all_error_list, error_name):
    if error_name in all_error_list:
        return True
    for elem in error_list[error_name]:
        if elem in all_error_list:
            return True
        parent_result = get_parent(error_list, all_error_list, elem)
        if parent_result:
            return True
    return False


def main():
    exception_number = int(input())
    inheritance = classes(exception_number)
    request_amount = int(input())
    exceptions_couldbe_simple = []
    all_exceptions = []
    for i in range(request_amount):
        exception_name = input()
        result = get_parent(inheritance, all_exceptions, exception_name)
        all_exceptions.append(exception_name)
        if result is True and exception_name not in exceptions_couldbe_simple:
            exceptions_couldbe_simple.append(exception_name)
    print(*exceptions_couldbe_simple, sep='\n')


if __name__ == '__main__':
    main()