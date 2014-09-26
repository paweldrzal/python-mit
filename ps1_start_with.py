""" program that prints the number of times the string 'bob' occurs in s"""

s = raw_input("Enter the string: ")

counter = 0

for i in range(len(s)):
    if s[i:].startswith('bob'):
        counter += 1

print "Number of times bob occurs is: %d" % counter
