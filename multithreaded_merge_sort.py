import merge_sort as ms
import threading

def __AppendSortedSubArrayToArray(sortedArrays, subArrayToSort):
    sortedArrays.append(ms.merge_sort(subArrayToSort))

def MultithreadMergeSort(arrayToSort, numberOfThreads):
    if numberOfThreads <= 1:
        return ms.merge_sort(arrayToSort)
    
    if numberOfThreads > len(arrayToSort):
        print('Max number of threads exceeded!')
        return
        
    # Divide the array to sort into arrays
    sizeOfSublists = len(arrayToSort) // numberOfThreads
    subArrays = [arrayToSort[i:i+sizeOfSublists] for i in range(0, len(arrayToSort), sizeOfSublists)]
    threads=[]
    sortedSubArrays = []
    threadIndex=0
    for subArray in subArrays:
        thread = threading.Thread(target = __AppendSortedSubArrayToArray(sortedSubArrays, subArray))
        print(f'Starting thread {threadIndex} with sub-array {subArray}')
        threadIndex+=1
        thread.start()
        threads.append(thread)

    # Wait for threads to complete
    threadIndex=0
    for thread in threads:
        thread.join()
        print(f'Ending thread {threadIndex} with sorted sub-array {sortedSubArrays[threadIndex]}')
        threadIndex+=1

    # Merge sorted sub arrays
    mergedArrays = sortedSubArrays[0]
    for subArray in sortedSubArrays[1:]:
        mergedArrays = ms.merge(mergedArrays, subArray)
    
    return mergedArrays
        

if __name__ == "__main__":
    arr = [3, 2, 7, 4, 6, 6, 5, 3, 8, 0]
    print(f'Sorted array: {MultithreadMergeSort(arr, 5)}')

