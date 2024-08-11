weight = float(input("Enter your weight in kilogram: "))
height = float(input("Enter your height in centimeters: "))
height = height/100

bmi = round(weight/(height*height),2)

print("Your BMI is "+str(bmi))
