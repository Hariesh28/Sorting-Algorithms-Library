from sorting_techniques import bogo_sort, heap_sort, insertion_sort, merge_sort, selection_sort

def display_menu():
    print("Choose a sorting algorithm to run:")
    print("1. Bogo Sort")
    print("2. Heap Sort")
    print("3. Insertion Sort")
    print("4. Merge Sort")
    print("5. Selection Sort")
    print("6. Exit")

def main():
    array = [3, 1, 2, 5, 4]
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        if choice == "1":
            print(f"Original array: {array}")
            sorted_array = bogo_sort(array)
            print(f"Sorted array: {sorted_array}\n")
        elif choice == "2":
            print(f"Original array: {array}")
            sorted_array = heap_sort(array, ascending=True)
            print(f"Sorted array (ascending): {sorted_array}\n")
        elif choice == "3":
            print(f"Original array: {array}")
            sorted_array = insertion_sort(array, ascending=True)
            print(f"Sorted array (ascending): {sorted_array}\n")
        elif choice == "4":
            print(f"Original array: {array}")
            sorted_array = merge_sort(array, ascending=True)
            print(f"Sorted array (ascending): {sorted_array}\n")
        elif choice == "5":
            print(f"Original array: {array}")
            sorted_array = selection_sort(array, ascending=True)
            print(f"Sorted array (ascending): {sorted_array}\n")
        elif choice == "6":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
