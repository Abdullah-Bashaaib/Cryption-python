message='GUVF VF N TERNG PYNFF'# لارسالة المشفرة
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


for key in range(1,len(letters)):
    translate = ''
    for symbol in message:
        if symbol in letters:
            num = letters.find(symbol)
            num = (num - key)%len(letters) # لفك التشفير عن النص
            translate = translate + letters[num]
    else:
        translate += symbol
    print('key %s: %s'%(key,translate))
print(key)