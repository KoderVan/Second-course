def different_objects(objects):
    objects_count = 0
    set_objects = set()
    for object in objects:
        if id(object) not in set_objects:
            set_objects.add(id(object))
            objects_count += 1
    return objects_count

def main():
    objects = list(input().split(','))
    print(different_objects(objects))

if __name__ == '__main__':
    main()