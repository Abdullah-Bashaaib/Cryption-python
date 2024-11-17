import string
import random

all_char = string.ascii_letters + string.digits + string.punctuation + ' '
chars = list(all_char)
key = chars.copy()

random.shuffle(key)

inputTxt = input('Enter Text : ')
ciphertxt = ''

for item in inputTxt:
    ind = all_char.index(item)
    ciphertxt = ciphertxt + key[ind]

print(f'The ciphertxt is : {ciphertxt}')
print('-----------------------------------------------------------------------')

palaintxt = ''
for item in ciphertxt:
    index = key.index(item)
    palaintxt = palaintxt + all_char[index]
    
print(f'The Plaintxt is : {palaintxt}')

def enc (palaintxt, key) :
    print(ciphertxt)