def generateWelcome(inStr):
    return 'Hello, ' + inStr

def getName():
    return input("Type your name: ")


print(generateWelcome(getName()))
