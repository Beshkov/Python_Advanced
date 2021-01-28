with open("numbers.txt", "r") as file:
    n_sum = 0
    for number in file:
        n_sum += int(number)
    print(n_sum)