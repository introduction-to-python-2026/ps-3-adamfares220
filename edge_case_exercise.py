def move(my_list, direction):
    
    index_of_one = my_list.index(1)

    
    if direction == 'right':
       
        if index_of_one + 1 < len(my_list):
            my_list[index_of_one], my_list[index_of_one + 1] = my_list[index_of_one + 1], my_list[index_of_one]
    
    elif direction == 'left':
         
        if index_of_one - 1 >= 0:
            my_list[index_of_one], my_list[index_of_one - 1] = my_list[index_of_one - 1], my_list[index_of_one]

    return my_list
