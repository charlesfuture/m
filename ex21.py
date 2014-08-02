def add(a, b):
	return a + b
	
def subtract(a, b):
	return a - b
	
def multiply(a, b):
	return a * b
	
def divide(a, b):
	return a / b

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print age, height, weight, iq

what = add(age, add(age, subtract(height, multiply(weight, divide(iq, 2)))))

print what