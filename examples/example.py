from sorting_techniques import bogo_sort

def main():
    array1 = [3, 1, 2]
    print(f"Original array: {array1}")
    sorted_array1 = bogo_sort(array1, ascending=False)
    print(f"Sorted array (ascending): {sorted_array1}\n")


if __name__ == "__main__":
    main()
