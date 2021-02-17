number_n, number_m = [int(el) for el in input().split()]
set_one = {int(input()) for _ in range(number_n)}
set_two = {int(input()) for _ in range(number_m)}
set_of_both = {el for el in set_one if el in set_two}
[print(numb) for numb in set_of_both]