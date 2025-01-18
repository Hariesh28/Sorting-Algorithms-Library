from sorting_techniques import heap_sort

def main():
    array1 = [3, 1, 2,5,4]
    print(f"Original array: {array1}")
    sorted_array1 = heap_sort(array1, ascending=False)
    print(f"Sorted array (ascending): {sorted_array1}\n")


if __name__ == "__main__":
    main()
