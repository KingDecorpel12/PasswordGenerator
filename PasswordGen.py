import random
import string

# Generates random secure password

upperCase, lowerCase = string.ascii_lowercase, string.ascii_uppercase
number = "0123456789"

symbols = "!@#$%^&*/\?-_+="

Use_for = upperCase + lowerCase + number + symbols
length_for_password = 10

password = "".join(random.sample(Use_for, length_for_password))

print("Your new generated password is: " )
print(password)

