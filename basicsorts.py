from random import randint, choice

l1st = []

for _ in range(1, 15):
    l1st.append(randint(1, 100))

#bubbleSort:


def BubbleSort(array):
    swapped = False
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            swapped = False
    if swapped:
        swapped = False
    else:
        swapped = True
    return array


#QuickSort:


def QuickSort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = choice(array)
        PivotArr = []
        LeftArr = []
        RightArr = []
        for value in array:
            if value < pivot:
                LeftArr.append(value)
            elif value > pivot:
                RightArr.append(value)
            else:
                PivotArr.append(value)

        return QuickSort(LeftArr) + PivotArr + QuickSort(RightArr)


#InsertionSort:


def InsertionSort(array):
    for value in range(1, len(array)):
        IndVal = array[value]
        j = value - 1
        while j >= 0 and array[j] > IndVal:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = IndVal

    return array


#SelectionSort

def SelectionSort(array):
    for minimum in range(0, len(array) - 1):
        MinVal = minimum
        for value in range(MinVal + 1, len(array)):
            if array[value] < array[minimum]:
                MinVal = value
        array[minimum], array[MinVal] = array[MinVal], array[minimum]
    return array  


print("BubbleSort:", BubbleSort(l1st))
print("QuickSort:", QuickSort(l1st))
print("InsertionSort:", InsertionSort(l1st))
print("SelectionSort:", SelectionSort(l1st))