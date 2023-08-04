import numpy

number_one = int(input("Enter a number for x: "))
number_two = int(input("Enter a number for y: "))
exponent = number_one ** number_two
log_of_x = numpy.log2(number_one)

print("x ** y =", exponent)
print("log(x) =", log_of_x)