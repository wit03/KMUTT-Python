def top():
    print("   ______   ")
    print("  /      \  ")
    print(" /        \ ")
    
def bottom():
    print(" \        / ")
    print("  \      /  ")
    print("   ------   ")

def line():
    print("+----------+")

def stop():
    print("|   stop   |")

def taskOne():
    print("1. \n")
    bottom()
    line()

def taskTwo():
    print("2. \n")
    top()
    line()

def taskThree():
    print("3. \n")
    top()
    stop()
    bottom()
    
taskOne()
taskTwo()
taskThree()