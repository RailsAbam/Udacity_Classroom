
import math
card_deck = [4, 11, 8 , 5, 13, 2, 8, 10 ]
hand = []
while sum(hand) < 17:
    hand.append(card_deck.pop())
print(hand) 




limit = 40
nums = 0

while (nums + 1 )**2 <= limit:
    nums += 1 
    nearest_square = nums** 2
print(nearest_square)



limited = 60
num = 2
while (num + 2) **2 < limited:
    num += 2
    all_num = num ** 2
print(all_num)


n = input("Please enter 'hello':")
while n.strip() != 'hello':
    n = input("Please enter 'hello':")


while True:
    n = input("Please enter 'hello':")
    if n.strip() == 'hello':
        break

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
count_odd = 0
list_sum = 0
i = 0
len_num_list = len(num_list)

while (count_odd < 5) and (i < len_num_list):
    if num_list[i] % 2 != 0:
        list_sum += num_list[i]
        count_odd += 1
    i += 1

print("The number of odd numbers are {}, while sum of odd numbers added are {}.".format(count_odd,list_sum))


