def main():
    score = input("What was your score out of 100? ")
    if int(score) >= 90: print("Grade: A")
    elif int(score) >= 80: print("Grade: B")
    elif int(score) >= 70: print("Grade: C")
    elif int(score) >= 60: print("Grade: D")
    else: print("Grade: F")
 
main()

