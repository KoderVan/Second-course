n, k = map(int, input().split())


def count(n, k):
    if k == 0:
        return 1
    if k > n:
        return 0
    else:
        return count(n-1, k) + count(n-1, k-1)


def main():
    print(count(n,k))


if __name__ == '__main__':
    main()