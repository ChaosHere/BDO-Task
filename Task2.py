A = list(input().split(','))
B = list(input().split(','))

to_int_A = [int(x) for x in A]
to_int_B = [int(x) for x in B]

final_list = to_int_A + to_int_B

print(final_list)
def sorter(data_list, new_list = []):
    while data_list:
        min = data_list[0]
        for x in data_list: 
            if x < min:
                min = x
        new_list.append(min)
        data_list.remove(min)
    return new_list

print(sorter(final_list))