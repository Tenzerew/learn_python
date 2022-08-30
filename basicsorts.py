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
            elif value < pivot:
                RightArr.append(value)
            else:
                PivotArr.append(value)

        return QuickSort(LeftArr) + PivotArr + QuickSort(RightArr)



print("BubbleSort: "+ BubbleSort(l1st))
print("QuickSort: "+  QuickSort(l1st))
