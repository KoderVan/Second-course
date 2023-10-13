def classes(class_amount):
    class_inheritance = {}
    for i in range(class_amount):
        class_name = input().split(' : ')
        if len(class_name) == 1:
            class_inheritance[class_name[0]] = 'None'
        else:
            class_inheritance[class_name[0]] = class_name[1].split(" ")
    return class_inheritance


def get_parent(class_list, _class, parent):
    if _class not in class_list:
        class_list[_class] = parent
    if _class == parent:
        return True
    if class_list[_class] == 'None':
        return False
    if parent in class_list[_class]:
        return True
    for node in class_list[_class]:
        new_path = get_parent(class_list, node, parent)
        if new_path:
            return new_path
    return False


def main():
    class_list = classes(int(input()))
    request_amount = int(input())
    result_list = []
    for i in range(request_amount):
        class_names = input().split(' ')
        class_name = class_names[1]
        parent_name = class_names[0]
        result = get_parent(class_list, class_name, parent_name)
        result_list.append(result)
    for i in result_list:
        print("Yes" if i else "No")


if __name__ == "__main__":
    main()