# parrot_list = ["non pinin", "no more", "a stiff", "bereft of live"]
#
# parrot_list.append("A Norwegian blue")
#
# for state in parrot_list:
#     print("This parrot is " + state)
#
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# numbers = even + odd
# numbers_in_order = sorted(numbers)
#
# print(numbers_in_order)
#
# if numbers == numbers_in_order:
#     print("the lists are equal")
# else:
#     print("the lists are not equal")
#
# if numbers_in_order == sorted(numbers):
#     print("the lists are equal")
# else:
#     print("the lists are not equal")

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]

for number_set in numbers:
    print(number_set)

    for value in number_set:
        print(value)
        