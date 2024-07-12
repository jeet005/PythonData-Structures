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
    
    return left_idx


print(binary_search([1,3,5,6], 7))
