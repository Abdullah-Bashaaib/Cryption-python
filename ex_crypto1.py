message='GUVF VF N TERNG PYNFF'
key = 2
mode = 'decrypt'
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
translate = ''

message = message.lower()
letters = letters.lower()

for symbol in message:
    if symbol in letters:
        num = letters.find(symbol)
        if mode == 'encrypt':
            num = (num + key)% len(letters) # هنا يأخذ ترتيب الحرف من المصفوفة )letters) ثم يجمع الترتيب مع المفتاح 
        elif mode == 'decrypt':
            num = (num - key)%len(letters) # لفك التشفير عن النص
        translate = translate + letters[num]
    else:
        translate = translate + symbol
print(translate.upper())
