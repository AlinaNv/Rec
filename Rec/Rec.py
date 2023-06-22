my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def f(my_list):
    if my_list == []:
        print('End')
    else:
        print(my_list.pop(0))

f(my_list)