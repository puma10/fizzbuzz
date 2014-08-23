import sys

def fizzBuzz(numEnd):
    for i in range(1,int(numEnd)+1):
        if i%3 == 0 and i%5 == 0:
            print "fizz buzz"
        elif i%3 == 0:
            print "fizz"
        elif i%5 == 0:
            print "buzz"
        else:
            print i

if len(sys.argv) >= 2:
    fizzBuzz(sys.argv[1])
else:
    inputNum = int(raw_input("Enter something, yo! "))
    fizzBuzz(inputNum)


