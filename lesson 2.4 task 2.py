import os.path

with open('answer.txt', 'w') as file_out:
    path = []
    for current_dir, dirs, files in os.walk("main"):
        for file in files:
            if file.endswith(".py"):
                path.append(current_dir)
                break
    sorted_list = sorted(path)
    contents = '\n'.join(sorted_list)
    file_out.write(contents)


