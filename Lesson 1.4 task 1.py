number_of_actions = int(input())
spaces = {'global': {'parent': 'None', 'variables': []}}


def create(name, parent):
    if name == 'global':
        spaces['global']['variables'].append(parent)
    else:
        spaces[name] = {'parent': parent, 'variables': []}
        spaces['global']['variables'].append(name)
        parent_name = spaces[name]['parent']
        spaces[parent_name]['variables'].append(name)


def add(name, variable):
    spaces[name]['variables'].append(variable)


def get_(name, variable):
    if name == 'None':
        return 'None'
    if variable in spaces[name]['variables']:
        return name
    elif variable not in spaces[name]['variables']:
        parent_name = spaces[name]['parent']
        return get_(parent_name, variable)


def main():
    for i in range(number_of_actions):
        command, namespace, var = input().split()
        if command == 'create':
            create(namespace, var)
        if command == 'add':
            add(namespace, var)
        if command == 'get':
            print(get_(namespace, var))


if __name__ == '__main__':
    main()
