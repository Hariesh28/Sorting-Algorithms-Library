def insertion_sort(inputArray: list[int], Ascending: bool = True) -> list[int]:
    length = len(inputArray)
    if(length==1): return inputArray
    outputArray = list(inputArray)
    for i in range(1,length):
        for j in range(i,0,-1):
            if(Ascending == (outputArray[j] > outputArray[j-1])):
                break
            swap(outputArray,j,j-1)
    return outputArray
            
            
            
def swap(inputArray: list[int], index1: int, index2: int) ->None:
    temp = inputArray[index1]
    inputArray[index1] = inputArray[index2]
    inputArray[index2] = temp


