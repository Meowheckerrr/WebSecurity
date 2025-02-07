text = 'A"-confirm(1)-"A'

octal_parts = []

for char in text:
  
    octal_char = f'\\{ord(char):o}'
 
    octal_parts.append(octal_char)

octal_encoded = ''.join(octal_parts)

print(octal_encoded)