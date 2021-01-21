

def quicksort(nums, start=None, end=None):
    if len(nums) <= 1:
        return
    start = 0 if start is None else start 
    end = len(nums)-1 if end is None else end
    if start < end:
        mid = partition(nums, start, end)
        quicksort(nums, 0, mid-1)
        quicksort(nums, mid+1, end)
    return nums

def partition(nums, start, end):
    base = nums[start]
    while start < end:
        while start < end and nums[end] >= base:
            end -= 1
        nums[end], nums[start] = nums[start], nums[end]
        while start < end and nums[start] <= base:
            start += 1
        nums[end], nums[start] = nums[start], nums[end]
    nums[start] = base
    return start


def mergesort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = mergesort(nums[:mid])
    right = mergesort(nums[mid:])
    return merge(left, right) 


def merge(left_list, right_list):
    result = []
    i, j = 0, 0
    while i < len(left_list) and j < len(right_list):
        if left_list[i] < right_list[j]:
            result.append(left_list[i])
            i += 1
        else:
            result.append(right_list[j])
            j += 1
    if i < len(left_list):
        result.extend(left_list[i:])
    else:
        result.extend(right_list[j:])
    return result


def heapify(array, index, heap_size):
    left_index = index * 2 + 1
    right_index = index * 2 + 2
    largest_index = index 
    if left_index < heap_size and array[left_index] > array[largest_index]:
        largest_index = left_index
    if right_index < heap_size and array[right_index] > array[largest_index]:
        largest_index = right_index
    if largest_index != index:
        array[index], array[largest_index] = array[largest_index], array[index]
        heapify(array, largest_index, heap_size)


def heapsort(array):
    if len(array) <= 1:
        return array
    for i in reversed(range(len(array)//2)):
        heapify(array, i, len(array))

    for i in reversed(range(len(array))):
        array[i], array[0] = array[0], array[i]
        heapify(array, 0, i) 
    return array





if __name__ == "__main__":
    a = [3, 44, 34, 53, 624, 452, 4235, 7, 13, 52, 41, 1, 16]
    print(heapsort(a))