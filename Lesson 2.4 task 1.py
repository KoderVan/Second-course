with open("dataset_2.txt", "r") as file_in, open("reverse_dataset.txt", "w") as file_out:
    order = []
    for line in file_in:
        order.append(line.strip())
    new_order = list(reversed(order))
    for line in new_order:
        file_out.write(line)
