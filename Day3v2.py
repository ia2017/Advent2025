lines = []

with open("inputs/Day3_test") as f:
    for line in f:
        lines.append(line.split("\n")[0])


def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] >= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)

for line in lines:
    line_list = list(line)
    line_list = [int(i) for i in line_list]
    original_list = line_list
    # Sort
    quicksort(line_list[:-1])
    # Get index

    # Sort again
    print("Sorted array:", line_list)
