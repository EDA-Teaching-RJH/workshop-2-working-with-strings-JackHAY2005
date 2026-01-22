import random
   
def main():
        x = input("Enter a number between 1 and 10: ")
        secret_number = random.randint(1, 10)
        print("Correct!" if int(x) == secret_number else "Too low!" if int(x) < secret_number else "Too high!")
        print(f"The secret number was: {secret_number}")
main()