#يعطي افضل نتيجة
# المقارنة بين تردد بين اللغة الانجليزبة والنص 
from collections import Counter

# الأبجدية الإنجليزية
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# توزيع تردد الحروف في اللغة الإنجليزية (من الأعلى تكراراً إلى الأقل)
english_letter_freq = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C', 'U', 'M', 'W', 'F', 'G', 'Y', 'P', 'B', 'V', 'K', 'J', 'X', 'Q', 'Z']

# النص المشفر (أطول)
ciphertext = "KHOOR ZRUOG, WKH FDHVDU FLSKHU LV D FODVVLF FLSKHU PHWKRG."

# تحويل النص المشفر إلى حروف كبيرة
ciphertext = ciphertext.upper()

# حساب تردد الحروف في النص المشفر
letter_count = Counter(filter(str.isalpha, ciphertext))  # فقط الحروف، تجاهل المسافات والعلامات
print(letter_count) # عبارة عن دكشنري يخط فيه كل حرف كم تردد

# ترتيب الحروف في النص المشفر بناءً على تكرارها
most_common_cipher_letters = [pair[0] for pair in letter_count.most_common()]
print(most_common_cipher_letters)

# مقارنة تردد الحروف المشفرة مع ترددات اللغة الإنجليزية
# افتراض أن أكثر حرف متكرر في النص المشفر يقابل E
most_common_cipher_letter = most_common_cipher_letters[0]
most_common_english_letter = 'E'

# حساب المفتاح بناءً على الترددات
key = (alphabet.index(most_common_cipher_letter) - alphabet.index(most_common_english_letter)) % 26
# محاولة فك التشفير عبر مقارنة الترددات
def decrypt_caesar(ciphertext, key):
    decrypted_text = []
    for letter in ciphertext:
        if letter in alphabet:
            # حساب الموقع الجديد للحرف بعد إزاحته للخلف بمقدار المفتاح
            index = (alphabet.index(letter) - key) % 26
            decrypted_text.append(alphabet[index])
        else:
            decrypted_text.append(letter)  # إضافة أي شيء آخر (مسافات أو علامات) كما هو
    return ''.join(decrypted_text)

# فك التشفير باستخدام المفتاح
decrypted_text = decrypt_caesar(ciphertext, key)

print(f"THE KEY : {key}")
print(f"THE PLAINTEXT  : {decrypted_text}") # النص المشفر   

