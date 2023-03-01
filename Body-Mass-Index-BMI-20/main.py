
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

calculator = weight / height**2
bmi = round(calculator, 1)

if bmi < 18.5:
  print('Your BMI is {}, you are underweight'.format(bmi)) 
elif bmi < 25:
  print('Your BMI is {}, you are normal weight'.format(bmi)) 
elif bmi < 30:
  print('Your BMI is {}, you are overweight'.format(bmi))
elif bmi < 35:
  print('Your BMI is {}, you are obese'.format(bmi))
else:
  print('Your BMI is {}, you are clinically obese'.format(bmi))



