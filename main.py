def slection_sort(array):
    for i in range(len(array)):
        minIndex = i
        for j in range(i+1,len(array)):
            if array[minIndex] > array[j]:
                minIndex = j
        array[i],array[minIndex] = array[minIndex],array[i]

if __name__ == '__main__':
    array = [3,4,2,7,4,2]
    slection_sort(array)
    print(array)