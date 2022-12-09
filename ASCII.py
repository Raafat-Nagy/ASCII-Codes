import string

lowercase=list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
digits = list(string.digits)
punctuation = list(string.punctuation)



file = open('ASCII Values.txt', 'w')

# Recorde ASCII Uppercase
file.write('\t\tASCII Uppercase\n\n')
print('\n\tASCII Uppercase\n\n')
for i in range(len(uppercase)):
  file.write(f'- The ASCII Value Of  {uppercase[i]}  Is  {ord(uppercase[i])}\n')
  print(f'- The ASCII Value Of  {uppercase[i]}  Is  {ord(uppercase[i])}')


# Recorde ASCII lowercase
file.write('\n\n\t\tASCII Lowercase\n\n')
print('\n\n\tASCII Lowercase\n\n')
for i in range(len(lowercase)):
  file.write(f'- The ASCII Value Of  {lowercase[i]}  Is  {ord(lowercase[i])}\n')
  print(f'- The ASCII Value Of  {lowercase[i]}  Is  {ord(lowercase[i])}')


# Recorde ASCII Digits
file.write('\n\n\t\tASCII Digits\n\n')
print('\n\n\tASCII Digits\n\n')
for i in range(len(digits)):
  file.write(f'- The ASCII Value Of  {digits[i]}  Is  {ord(digits[i])}\n')
  print(f'- The ASCII Value Of  {digits[i]}  Is  {ord(digits[i])}')

# Recorde ASCII punctuation
file.write('\n\n\t\tASCII Punctuation\n\n')
print('\n\n\tASCII Punctuation\n\n')
for i in range(len(punctuation)):
  file.write(f'- The ASCII Value Of  {punctuation[i]}  Is  {ord(punctuation[i])}\n')
  print(f'- The ASCII Value Of  {punctuation[i]}  Is  {ord(punctuation[i])}')


file.closed