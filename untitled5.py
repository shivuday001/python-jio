

#take 2 variables and chek both variables are integr so we have to perform arithmetic operations

x=10
y=15
if(type(x)is int and type(y) is int):
  print(x+y)


#take a input from user and count how many vowels are there
def count_vowels(input_str):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_str:
        if char in vowels:
            count += 1
    return count
input_str = input("Enter a string: ")
vowel_count = count_vowels(input_str)
print(f"The number of vowels in the input is: {vowel_count}")

#take a input from a user and find out how many charcter are there
text=input("enter an string")
 print(len(text))



#take a input from user and chek that integer input should be satisfied the divisibiltty rule of a number 4

number=int(input("enter an integer"))

if number % 4 ==0:
  print(f"{number}is divisible by 4")
else:
  print(f"{number} is not divisible by 4")

#take a input from user and find out wether its even number or odd number

number=int(input(" enter an integer"))
if number% 2 ==0:
  print(f"{number} is even " )
else:
  print(f"{number} is odd")

#take a input from user and extrat the last charchert of string

text=input("enter a string:")
last_character=text[-1]

print("the last character is " ,last_character)

#take a input from user and extract second word of the string

text=input("enter a string:")
second_character=text[2]

print("the second character is " ,second_character)


# Call the function and print the result
largest_num = find_largest(num1, num2, num3)
print("The largest number is:", largest_num)

