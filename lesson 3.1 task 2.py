def str_count(s, t):
    str_position = 0
    str_positions_total = []
    for i in range(len(s)):
        k = s.find(t, str_position)
        if k < 0:
            break
        str_position += 1
        str_positions_total.append(k)
    number_of_occurrences = len(list(set(str_positions_total)))
    return number_of_occurrences


def main():
    result = str_count(str(input()), str(input()))
    print(result)


main()