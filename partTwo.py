import math  

def main():
    equation = input("Enter the two sides of a right-angled triangle separated by a comma: ")
    A, B = map(float, equation.split(","))
    pythag(A,B)

def pythag(A,B):
    C = math.sqrt(A**2 + B**2)
    print("The length of the hypotenuse is:", C)

main()
