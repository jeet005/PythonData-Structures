def bubble_sort(elements):


    for i in range(len(elements) - 1):
        swapped = False
        for j in range(len(elements)-1):
            if elements[j] > elements[j + 1]:
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp
                swapped = True

        if not swapped:
            break

elements = [5,9,2,1,67,34,88,34]
bubble_sort(elements)
print(elements)