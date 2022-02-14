k = input()

to_int_L = [int(x) for x in L]


def checkConsecutive(my_list):
    is_sequence = sorted(my_list) == list(range(min(my_list), max(my_list) + 1))
    j = 0
    for i in my_list:
        if is_sequence:
            j += 1

    if k == j:
        print("YES")
    else:
        print("NO")


print(checkConsecutive(to_int_L))