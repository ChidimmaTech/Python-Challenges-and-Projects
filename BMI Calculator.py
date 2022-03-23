weight = int(input('Please enter your weight in kg:'))
height = int(input('Please enter your height in meters:'))
BMI_Calc = 703 * (weight/(height * height))
message = f'Based on your input of weight = {weight} and height = {height}, your BMI is {BMI_Calc}'
print(message)