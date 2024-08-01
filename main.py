from BinarySearch.BinarySearch import binary_search


def main():
    my_list_1 = [1, 3, 5, 7, 9]
    print(binary_search(my_list_1, 3))  # => 1
    print(binary_search(my_list_1, -1))  # => None


if __name__ == '__main__':
    main()
