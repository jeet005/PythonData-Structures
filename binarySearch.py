def binary_search(numbers, num):

    left_idx = 0
    right_idx = len(numbers) - 1

    while left_idx <= right_idx:
        mid_index = (left_idx + right_idx) // 2
        mid_number = numbers[mid_index]

        if mid_number == num:
            return mid_index

        if mid_number < num:
            left_idx = mid_index + 1
        else:
            right_idx = mid_index - 1
    
    return -1


print(binary_search([1,2,3,4,5,6,7,8,9,10,15,20], 20))
