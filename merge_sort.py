def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    i=j=0
    merged_array=[]
    while i < len(left) and j < len(right): 
        if left[i]<=right[j]:
            merged_array.append(left[i])
            i+=1
        else:
            merged_array.append(right[j])
            j+=1
    
    while i < len(left):
        merged_array.append(left[i])
        i+=1

    while j < len(right):
        merged_array.append(right[j])
        j+=1

    return merged_array