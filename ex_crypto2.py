key = 18

def enc(key):
    message = input('Enter your plain text : ')
    message = message.upper() # ما تضبط مع الاحرف الصغيرة ليش؟
    translate = ''
    for symbol in message:
        translate += chr((ord(symbol) + key)%255)
    return translate

def dec(translate , key):
    translated = ''
    for symbol in translate:
        translated += chr((ord(symbol) - key)%255)
    return translated

x = enc(key)
print(x)