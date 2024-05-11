# # v1 Калькулятор
# number1 = float(input("Enter a number n1: "))
# number2 = float(input("Enter a number n2: "))
# n1 = number1
# n2 = number2
#
# result = n1 + n2
# print("Result + :", result)
#
# result = n1 - n2
# print("Result - :", result)

# result = n1*n2
# print("Result * :", result)
#
# if number2 != 0:
#     result = n1 / n2
#     print("Result / :", result)
# else:
#     print("Result / : Error")

# #v2 ділення списку на два
# lst = [int(i) for i in input("Enter a number for list: ").split()]
# print(lst)
# size = len(lst)
# print(size)
# if size % 2 == 0:
#     print("first_lst :", lst[0:size//2])
#     print("second_lst :", lst[size//2:])
# elif size % 2 != 0:
#     print("first_lst :", lst[0:size//2])
#     print("second_lst :", lst[size//2:])

# #v3 перемістити елемент у списку
lst = [int(i) for i in input("Enter a number for list: ").split()]
print(lst)
lst.append(lst.pop(0))
print(lst)
