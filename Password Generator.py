import random
word = ['apple', 'breeze', 'camera', 'dancer', 'eleven', 'frozen', 'guitar', 'humble', 'invent', 'jacket']
def randchar():
    number = random.randint(0,99)
    if(number <= 25):
        return chr(random.randint(65,90))
    elif(25 < number <= 50):
        return chr(random.randint(97,122))
    elif(50< number <= 75):
        return chr(random.randint(48,57))
    else:
        numder = random.randint(0,30)
        if(numder <= 14):
            return chr(random.randint(33,47))
        elif(14 < numder <= 21):
            return chr(random.randint(58,64))
        elif(21 < numder <= 27):
            return chr(random.randint(91,96))
        else:
            return chr(random.randint(123,126)) 
def verystrong():
    password = str('')
    length = random.randint(15,20)
    for x in range(length):
        password += randchar()
    return password
def strong():
    password = str('')
    length = random.randint(10,17)
    for x in range(length):
        number = random.randint(0,75)
        if(number <= 25):
            password += chr(random.randint(65,90))
        elif(25 < number <= 50):
            password += chr(random.randint(97,122))
        else:
            password += chr(random.randint(48,57))
    return password
def medium():
    password = str('')
    password = password + randchar()
    password = password + randchar()
    password = password + word[random.randint(0,9)]
    password = password + randchar()
    password = password + randchar()
    return password
def weak():
    return word[random.randint(0,10)]
choice = input("What kind of password would you like?\n(very strong, strong, medium, or weak)\n").lower()
match choice:
    case "very strong":
        print(verystrong())
    case "strong":
        print(strong())
    case "medium":
        print(medium())
    case "weak":
        print(weak())
    case default:
        print("Error: Invalid input")
