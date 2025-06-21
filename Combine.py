from math import sqrt
import re
start = 0
def StartChoice():
    while True:
        try:
            start = int(input("\033[1m\033[95mNumber Analyser(1) or String Finder(2): \033[0m"))
            if start in (1, 2):
                return start
            else:
                print("\033[31m\033[1m    You had one job. ONE. Just pick 1 or 2\033[0m\n\033[31m    Try again\033[0m")
        except:
            print("\033[31m\033[1m    Uh-uh, that's not even close to a number, genius.\033[0m\n\033[31m    Try Again")

def NumberAnalyser():
    num = "Error"

    while num == "Error":
        try:
            num = int(input("\033[1m\033[96m  Enter your number: \033[0m"))
            if num < 0:
                print("\033[31m\033[1m    Negative? What is this, your bank account? \033[0m\033[31m\n    Try again")
                num = "Error"
        except:
            print("\033[31m\033[1m    Uh-uh, that's not even close to a number, genius.\033[0m\n\033[31m    Try Again")
            num = "Error"


    divisors = []
    total = 0

    for i in range(1,num//2+1):
        if num % i == 0:
            divisors.append(str(i))
            total = total + i
            divisors.append("+")

    if num not in (1, 0, -1):
        del divisors[-1]
        print("\033[96m      Here are its factors"," ".join(divisors), "=", total)

    if total == num:
        print("\033[96m      It is a perfect number")
    elif total > num:
        print("\033[96m      It is an abundant number")
    else:
        print("\033[96m      It is an defiant number")

    if total == 1:
        print("      It is a prime number")
    elif num == 1:
        print("      1 is neither prime nor composite")
    else:
        print("      It is a composite number")

    # Palindrome
    word = str(num)
    reversedWord = word[::-1]
    if word == reversedWord:
        print('      It is a Palindrome')

    # Even or odd
    if num % 2 == 0:
        print('      It is even')
    else :
        print('      It is odd')

    #self-dividing
    def is_self_dividing(n):
        for digit in str(n):
            if digit == '0' or n % int(digit) != 0:
                return False
        return True

    if is_self_dividing(num) == True:
        print("      It is a self-dividing number")

    # Square number checker
    if round(sqrt(num))**2 == num:
        print("      It is a square number")

    # Cube number checker
    def is_cube(n):
        root = round(n ** (1/3))
        return root ** 3 == n

    if is_cube(num):
        print("      It is a cube number")

    # Times table
    times = []
    for i in range(0,13):
        str(times.append(i*num))
    print('      These is the time table from 0-12\033[0m',times)

def StringAnalyser():
    string = input("\033[93m  Enter your string: \033[0m")
   
    vowelOnly = ""
    vowelOnly = re.findall(r'[aeiouAEIOU]',string)
    vowels = len(vowelOnly)

    consonantOnly = ""
    consonantOnly = re.findall(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]',string)
    consonant = len(consonantOnly)
   
    print("\033[93m      It has",vowels,"vowels")
    print("      Without the consonants it is \"", "".join(consonantOnly),"\"")
    print("      It has",consonant,"consonants")
    print("      Without the consonants it is \"", "".join(vowelOnly),"\"")

    reversedWord = string[::-1]
    print('      Your reversed word is',reversedWord)
    if string == reversedWord:
        print('      It is a Palindrome')
       
    length = len(string)
    print("      It is",length,"charcaters long\033[0m")

while True:
    start = StartChoice()

    if start == 1:
        NumberAnalyser()
    elif start == 2:
        StringAnalyser()

    Again = input("\033[1m    Wanna try again? (\033[92my\033[0m\033[1m/\033[91mn\033[0m\033[1m): ").strip().lower()
    if Again == 'n':
        print("\033[1m    Alright, catch you later!\033[0m")
        break