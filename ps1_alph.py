"""program that prints the longest substring of s in which the letters occur in alphabetical order"""

s = raw_input("Enter the string: ")

a=''
b=''

for char in s:
 if(b == ''):
  b = char
 elif(b[-1] <= char):
  b += char
 elif(b[-1] > char):
  if(len(a) < len(b)):
   a = b
   b = char
  else:
   b = char
if(len(b)>len(a)):
 a=b
print(a) 
