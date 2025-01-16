def selection_sort(inputArray: list[int], Ascending: bool = True) -> list[int]:
    length = len(inputArray)
    if(length==1): return inputArray
    outputArray = list(inputArray)
    for i in range(length):
        candidate = i
        for j in range(i,length):
            if Ascending == (outputArray[candidate] > outputArray[j]):
                candidate = j 
        swap(outputArray,i,candidate)
    return outputArray
            
            
            
def swap(inputArray: list[int], index1: int, index2: int) ->None:
    temp = inputArray[index1]
    inputArray[index1] = inputArray[index2]
    inputArray[index2] = temp


