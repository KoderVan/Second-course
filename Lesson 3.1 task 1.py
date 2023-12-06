def str_input():
    s = str(input())
    a = str(input())
    b = str(input())
    return s, a, b


def str_operations(s, a, b):
    operation_count = 0
    while True:
        if a not in s:
            return operation_count
        s = s.replace(a, b)
        operation_count += 1
        if operation_count >= 1000:
            return 'Impossible'


def main():
    string_1, string_2, string_3 = str_input()
    result = str_operations(string_1, string_2, string_3)
    print(result)


main()