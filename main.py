

def slection_sort(array):
    for i in range(len(array)):
        minIndex = i
        for j in range(i+1,len(array)):
            if array[minIndex]>array[j]:
                minIndex = j
        array[i],array[minIndex] = array[minIndex],array[i]
    return array


if __name__ == '__main__':
    array =[5,2,6,12,8,4]
    print("this is the list sorted")
    print(slection_sort(array))