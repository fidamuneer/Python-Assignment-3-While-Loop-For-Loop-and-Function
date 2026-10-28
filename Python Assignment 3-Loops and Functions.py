import random
# Generate random number between 1 and 10
secret_number = random.randint(1,10)
attempts = 3
while attempts > 0:
    guess = int(input("Guess the number between 1 and 10 "))

    if guess < 1 or guess > 10:
        print("Your guess is out of range.")
        continue

    attempts = attempts - 1
    
    if guess == secret_number:
        print("Congratulations!You are right.")
        break
    elif guess > secret_number:
        print("Too high.Try Again.")
    else:
        print("Too low.Try Again.")
else:
    print("You have used all 3 attempts.")
    print("Better luck next time!")
    print("The correct secret number was:",secret_number)



# Multiplication Table
x =  int(input("Enter a number"))
for i in range(1,11):
    result = x * i
    print(x,"*",i,"=",x*i)


# BMI Calculator
def calculate_bmi(weight, height):
    bmi = weight / (height**2)
    return bmi

weight = float(input("Enter your weight in kg:"))
height = float(input("Enter your height in meters:"))
result = calculate_bmi(weight,height)
print("Your BMI is:",round(result,2))


