from random import randint

#bubble sort


def bubblesort(array):
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


l1st = []

for _ in range(1, 15):
    l1st.append(randint(1, 100))

print(bubblesort(l1st))
