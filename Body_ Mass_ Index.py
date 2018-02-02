#python 2.7
weight = float(raw_input())
height = float(raw_input())

print "{:.2f}".format(weight/(height**2))

#python 3.6
weight = float (input('what \'s your weight?\n:'))
height = float (input('What\'s your height?\n:'))
BMI = weight / height ** 2
print(' % .2f'  % BMI)
