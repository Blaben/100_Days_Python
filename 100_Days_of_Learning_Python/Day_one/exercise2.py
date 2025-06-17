# Learning about Variables in Python and requesting users to enter a value using the input function

#Question
# Ask a user their weight (in pounds), convert it to kilograms and print on the terminal

weight = input("Enter your weight ")
weight_in_kg = 0.45

conversion = weight_in_kg * float(weight)


print(f'Your weight in Kilogram is {conversion}')