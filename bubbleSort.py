def bubble_sort(elements, key=None):


    for i in range(len(elements) - 1):
        swapped = False
        for j in range(len(elements)-1):
            if elements[j][key] > elements[j + 1][key]:
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp
                swapped = True

        if not swapped:
            break



elements = [5,9,2,1,67,34,88,34]
bubble_sort(elements)
print(elements)

elements1 = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
bubble_sort(elements1, key="transaction_amount")
print(elements1)
