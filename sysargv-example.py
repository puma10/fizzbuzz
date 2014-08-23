import sys

print "The name of this script is ", (sys.argv[0])
print "User supplied", len(sys.argv),  "arguments at run time"

for arg in sys.argv[1:]:
  print arg
