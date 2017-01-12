import math
import random


print ("Select operation.")
print ("1.Add")
print ("2.Subtract")
print ("3.Multiply")
print ("4.Divide")
print ("5.Modulus")
print ("6.Power")
print ("7.Exponential")
print ("8.Logarithm")
print ("9.Ln")
print ("10.Square Root")
print ("11.Sin")
print ("12.Cos")
print ("13.Tan")
print ("14.Inverse sin")
print ("15.Inverse Cos")
print ("16.Inverse Tan")
print ("17.nPr")
print ("18.nCr")
print ("19.Factorial")
print ("20.Absolute Value")
print ("21.Hyperbolic Sin")
print ("22.Hyperbolic Cos")
print ("23.Hyperbolic Tan")
print ("24.Inverse Hyperbolic sin")
print ("25.Inverse Hyperbolic Cos")
print ("26.Inverse Hyperbolic Tan")
print ("27.Random Number")



choice = input("Enter choice:")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
	print (num1 + num2)

elif choice == '2':
	print (num1 - num2)

elif choice == '3':
	print (num1 * num2)

elif choice == '4':
	print (num1 / num2)

elif choice == '5':
	print (num1 % num2)

elif choice == '6':
	print (num1 ** num2)

elif choice == '7':
	print (math.exp(num1))

elif choice == '8' and num1 >= 0 :
	print ( math.log(num1))

elif choice == '9' and num1 >= 0 :
	print ( math.log10(num1))

elif choice == '10' and num1 >= 0 :
	print ( math.sqrt(num1))

elif choice == '11':
	print (math.sin(num1))

elif choice == '12':
	print (math.cos(5))

elif choice == '13':
	print (math.tan(num1))

elif choice == '14' and num1 >= -1 and num1 <= 1:
	print (math.degrees(math.asin(num1)))

elif choice == '15' and num1 >= -1 and num1 <= 1:
	print (math.degrees(math.acos(num1)))

elif choice == '16':
	print (math.degrees(math.atan(num1)))

elif choice == '17':
	print (math.factorial(num1) / math.factorial(num1 - num2))

elif choice == '18':
	print (math.factorial(num1) / math.factorial(num1 - num2) / math.factorial(num2))

elif choice == '19':
	print (math.factorial(num1))

elif choice == '20':
	print (abs(num1),"\n",abs(num2))

elif choice == '21':
	print (math.sinh(num1))

elif choice == '22':
	print (math.cosh(5))

elif choice == '23':
	print (math.tan(num1))

elif choice == '24':
	print (math.asinh(num1))

elif choice == '25':
	print (math.acosh(num1))

elif choice == '26' and num1 >= -1 and num1 <= 1:
	print (math.atanh(num1))

elif choice == '27':
	print (random.choice([1, 2, 3, 5, 9]))
	print (random.randrange(100, 1000, 2))
	#random() [0,1):
	print (random.random())
	#Random Float uniform(5, 10) [x,y) 
	print (random.uniform(5, 10))
	list = [20, 16, 10, 5];
	random.shuffle(list)
	print (list)
	random.shuffle(list)
	print (list)

else:
	print("Invalid input")