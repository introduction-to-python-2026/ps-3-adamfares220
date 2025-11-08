def move(my_list, direction):
    # Finds the index of the one in the list
    index_of_one = my_list.index(1)

    # Move the one to the left or to the right
    if direction == 'right':
        # ודא שיש מקום לזוז ימינה לפני ההחלפה
        if index_of_one + 1 < len(my_list):
            my_list[index_of_one], my_list[index_of_one + 1] = my_list[index_of_one + 1], my_list[index_of_one]
    
    elif direction == 'left':
         # ודא שיש מקום לזוז שמאלה לפני ההחלפה
        if index_of_one - 1 >= 0:
            my_list[index_of_one], my_list[index_of_one - 1] = my_list[index_of_one - 1], my_list[index_of_one]

    return my_list
