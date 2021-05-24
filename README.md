# Auto-tabler
Automatic mathamatical tables using python.
A simple python program which tabulates the multiplication table of any given number within fraction of a second.

Remembering and calculating multiplication tables is one of the difficulties everyone faces.
But if you know to code, you can solve any problem you face everyday

Now we are going to see three ways to solve this problem.
From a complete begginers method to a program which converts the 11 lines of code to simple 5 lines of python code.

# ◉ Way number one

# Using For loop:
```
number = 1
input_num = int(input("Enter a number who's table you want: "))
for num in range(1,11):
	ans = int(input_num) * int(number)
	print(input_num, "x", number, "=", ans)
	number = number + 1
  ```
  Over here, at first we assign the value 1 to the variable number.
  ```
  number = 1
  ```
  
  Then, we take the user input of the number of which we will calculate the tables
  ```
  input_num = int(input("Enter a number who's table you want: "))
  ```
  
  Lets start using the while loop now-
  ```
for num in range(1,11):
  ```
  Here, we have told python to repeat the body of for loop in the ```range()``` of 1-10
```
  	ans = int(input_num) * int(number)
```
Over here we made the variable ```ans``` which multiplies the integer ```input_num``` with the integer ```number```.

Now lets do the main thing.

Lets ```print()``` the anwser in a nicely formated manner:

```	
print(input_num, "x", number, "=", ans)
```

Let's write the last line which will add the variable```number``` to ```1```.
If you will miss this line, you will get same output which you gave during input time and this will continue infinite time until your PC's memory runs out.
```
	number = number + 1
```

# ◉Lets try other ways
```
          I WON'T ADD DESCRIPTIONS FOR THESE TWO  METHODS
```
# While loops:
```
number = 1
input_num = int(input("Enter a number who's table you want: "))
while number <= 10:
	ans = int(input_num) * int(number)
	print(input_num, "x", number, "=", ans)
	number = number + 1
```

# ◎Third way
# For absolute begginers
```
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
```
