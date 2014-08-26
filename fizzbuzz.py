import sys

#tests a division to see if the numbers have 0 remainder
# returns true or false
def evenDivis(num1,divNum):
    if num1%divNum == 0:
        return True
    else:
        return False

# places fizz in place of all multiples of 3, places buzz in all multiples of 5
# places fizz buzz whenever the input number is a multipile of 3 and 5
def fizzBuzz(numEnd):
    for i in range(1,int(numEnd)+1):
        if evenDivis(i,3) and evenDivis(i,5):
            print "fizz buzz"
        elif evenDivis(i,3):
            print "fizz"
        elif evenDivis(i,5):
            print "buzz"
        else:
            print i

if __name__ == '__main__':
    fizzBuzz(sys.argv[1])

else:
    rawInput = fizzBuzz(raw_input("enter your digits : "))
    print rawInput


