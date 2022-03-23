print('Welcome To Your BMI Calculator')
#user enters weight in kg and height in meters
weight = float(input('Please enter your weight in kg:'))
height = float(input('Please enter your height in meters:'))
#BMI calculator rounds up the figure
BMI_Calc = round(weight/(height * height))
if BMI_Calc < 18.5:
  print(f'Your BMI is {BMI_Calc}, you are under weight')
elif BMI_Calc <= 25:
  print(f'Your BMI is {BMI_Calc}, your weight is normal')
elif BMI_Calc <= 30:
  print(f'Your BMI is {BMI_Calc}, you are slightly obessed')
elif BMI_Calc <= 35:
  print(f'Your BMI is {BMI_Calc}, you are obessed')
else:
  print(f'Your BMI is {BMI_Calc}, you are clinically obessed')
