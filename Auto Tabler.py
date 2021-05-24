# There are many ways to make something like "AUTO-TABLER" (a program which automatically evaluates the multiplication table of any number)

#WAY_1 
# Using while loops

number = 1
input_num = int(input("Enter a number who's table you want: "))
while number <= 10:
	ans = int(input_num) * int(number)
	print(input_num, "x", number, "=", ans)
	number = number + 1
#==================================================================================================================================#

#WAY_2
# Using for loops and range() function
num = 1
input_number = int(input("Enter a number who's table you want: "))
for num in range(1,11):
	answer = int(num) * int(input_number)
	print(input_number, "x", num, "=", answer)
	num = num + 1
#==================================================================================================================================#

#WAY_3
# for absolute begginers
# by using basic statements and operators
# long lines of code
numbr = int(input("Enter a number who's table you want: "))
print(numbr, "x 1 =", int(numbr) * 1)
print(numbr, "x 2 =", int(numbr) * 2)
print(numbr, "x 3 =", int(numbr) * 3)
print(numbr, "x 4 =", int(numbr) * 4)
print(numbr, "x 5 =", int(numbr) * 5)
print(numbr, "x 6 =", int(numbr) * 6)
print(numbr, "x 7 =", int(numbr) * 7)
print(numbr, "x 8 =", int(numbr) * 8)
print(numbr, "x 9 =", int(numbr) * 9)
print(numbr, "x 10 =", int(numbr) * 10)
#==================================================================================================================================#
