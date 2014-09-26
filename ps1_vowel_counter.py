"""program that counts up the number of vowels contained in the string s"""

s = raw_input("Enter the string: ")

counter = 0
for char in s.lower():
    if char in ("a","e","i","o","u") :
        counter += 1
 
print "Number of vowels: " + str(counter)

