"""
You will receive a list of numbers. Separate the negative numbers from the positive. Find the total sum of the negatives \
and positives, replace the negative number with its absolute value and print the following:
If the absolute negative number is bigger than the positive number:
	"The negatives are stronger than the positives"
If the positive number is bigger than the absolute negative number:
	"The positives are stronger than the negatives"

	input :
	1 2 -3 -4 65 -98 12 57 -84
"""
def what_is_bigger(s_neg, s_pos):
    temp1 = ""
    temp2 = ""
    if abs(s_neg) > s_pos:
        temp1 = 'negatives'
        temp2 = 'positives'
    else:
        temp1 = 'positives'
        temp2 = 'negatives'
    print(f"The {temp1} are stronger than the {temp2}")

def sum_of_negative(negative):
    s_neg = sum(negative)
    print(s_neg)
    return s_neg

def sum_of_positive(positive):
    s_pos = sum(positive)
    print(s_pos)
    return s_pos

def negative_vs_positive(r_list):
    negative = []
    positive = []
    for el in r_list:
        if el > 0:
            positive.append(el)
        else:
            negative.append(el)
    # sum_of_negative(negative)
    # sum_of_positive(positive)
    what_is_bigger(sum_of_negative(negative), sum_of_positive(positive))

rl = [int(n) for n in input().split()]
negative_vs_positive(rl)