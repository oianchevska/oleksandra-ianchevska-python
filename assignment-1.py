# Section 1. Variables and Types

name = "Sasha"
age = 37
height = 5.4
is_student = True

print (name, type(name))
print (age, type(age))
print (height, type(height))
print (is_student, type(is_student))

# Section 2. User Input and Math

ask_name = input("What is your name? ").strip().capitalize()
ask_age = int(input ("What is your born year? "))

current_age = 2026-ask_age

print(f"Hi, {ask_name}! You are approximately {current_age} years old.")

# Section 3. Type Conversion and f-strings

first_number = float(input (f"{name}, please enter the first number: "))
second_number = float(input (f"{name}, please enter the second number: "))

result = first_number * second_number

print (f"{name}, your result is {result}.")


# Section 4. Formatted Receipt

item = "Milk-Bone Dog Biscuits"
price = 8.99
quantity = 10
total_price = price * quantity

print ("===========================")
print ("          RECEIPT          ")
print ("===========================")
print (f"Item: {item}")
print (f"Price: ${price}")
print (f"Quantity: {quantity}")
print ("---------------------------")
print (f"Total: ${total_price:.2f}")

# Section 5. Mini-Project - Profile Card


name2 = input("What is your full name? ").strip().title()
hometown = input(f"{name2.title()}, what is your hometown? ").strip().title()
hobby = input("What is your favorite hobby? ").strip().capitalize()
fun_fact = input("Please,share one fun fact about yourself: ").strip().capitalize()
year_born = int(input("What is your born year? "))

current_age2 = 2026-year_born

print ("╔══════════════════════════════╗")
print (f"  PROFILE: {name2} ")
print ("╚══════════════════════════════╝")
print (f"Hometown: {hometown}")
print (f"Hobby: {hobby}")
print (f"Fun fact: {fun_fact}")
print (f"Age:  {current_age2}")
