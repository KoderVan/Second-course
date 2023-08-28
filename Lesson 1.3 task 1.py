def closest_mod_5(x):
    min_num = x
    while True:
        if min_num % 5 == 0:
            return min_num
        else:
            min_num += 1


def main():
    num = closest_mod_5(int(input()))
    print(num)


if __name__ == "__main__":
    main()