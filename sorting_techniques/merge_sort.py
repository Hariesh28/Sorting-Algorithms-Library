def merge_sort(inputArray: list[int], ascending: bool = True) -> list[int]:

    """
    Sorts the given list using the Merge Sort algorithm.

    Merge Sort is a divide-and-conquer algorithm that recursively divides the list into halves, sorts each half, and then merges them back together in sorted order.

    Parameters:
        inputArray (list): The list of elements to sort. Elements must be comparable.
        ascending (bool): If True, sorts in ascending order; if False, sorts in descending order.

    Returns:
        list: The sorted list.

    Example:
        >>> merge_sort([3, 1, 2], ascending=True)
        [1, 2, 3]
        >>> merge_sort([1, 2, 3], ascending=False)
        [3, 2, 1]
    """


    length = len(inputArray)
    if(length==1): return inputArray
    mid = int(length/2)
    leftArray = merge_sort(inputArray[:mid],ascending)
    rightArray = merge_sort(inputArray[mid:],ascending)
    outputArray = []
    leftIndex = 0
    leftIndexLimit = len(leftArray) - 1
    rightIndex = 0
    rightIndexLimit = len(rightArray) - 1
    while(True):
        if(ascending == (leftArray[leftIndex]<=rightArray[rightIndex])):
            outputArray.append(leftArray[leftIndex])
            if(leftIndex==leftIndexLimit):
                outputArray.extend(rightArray[rightIndex:])
                break
            leftIndex+=1
            continue
        outputArray.append(rightArray[rightIndex])
        if(rightIndex==rightIndexLimit):
            outputArray.extend(leftArray[leftIndex:])
            break
        rightIndex+=1
    return outputArray
