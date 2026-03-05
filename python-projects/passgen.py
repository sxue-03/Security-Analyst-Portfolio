import random
import string
length=int(input('how long should the password be?'))
chars=string.ascii_lowercase
use_upper=input('include uppercase?(y/n):')
if use_upper == 'y':
    chars +=string.ascii_uppercase
use_digits = input('include numbers? (y/n):')
if use_digits == 'y':
    chars +=string.digits
use_special = input('include speical characters?(y/n):')
if use_special == 'y':
    chars+=string.punctuation
password="".join(random.choices(chars, k=length))
print('your password:', password)
