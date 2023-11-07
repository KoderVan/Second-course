# Построить дерево и обойти его. Сайт открыт во вкладке
def classes(class_amount):
    class_inheritance = {}
    for i in range(class_amount):
        class_name = input().split(' : ')
        if len(class_name) == 1:
            class_inheritance[class_name[0]] = {'Parent': 'None'}
        else:
            class_inheritance[class_name[0]] = {'Parent': class_name[1].split(" ")}
    for j in class_inheritance:
        if class_inheritance[j]['Parent'] not in class_inheritance: #создание несущетсвующих классов
            for elem in class_inheritance[j]['Parent']:
                class_inheritance[elem] = {'Parent': 'None'}
    return class_inheritance


def get_parent(class_list, name, parent_name):
        if name == parent_name:
            return 'Yes'
        if name == 'None':
            return 'No'
        if parent_name in class_list[name]['Parent']:
            return 'Yes'
        elif parent_name not in class_list[name]['Parent']:
            parent_name1 = class_list[name]['Parent']
            if len(class_list[name]['Parent']) == 1:
                return get_parent(class_list, parent_name1, parent_name)
            else:
                for j in class_list[name]['Parent']: #попытка чтения нескольких родителей
                    return get_parent(class_list, j, parent_name)


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
        print(i)


if __name__ == "__main__":
    main()