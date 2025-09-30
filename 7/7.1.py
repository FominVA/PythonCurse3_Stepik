def get_max_index(numbers):
    max_index = 0
    max_value = max(numbers) 

    for index, value in enumerate(numbers, 0): 
        if index > max_index: 
            max_index = index
            

    return max_index

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]