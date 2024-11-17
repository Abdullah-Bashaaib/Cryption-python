import string

# جميع الحروف الكبيرة والصغيرة والأرقام والرموز الشائعة
all_characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation + ' '

# مصفوفة استبدال ثابتة (يتم تحديدها يدوياً أو عشوائياً لتحديد المقابل لكل حرف)
# مثال على تعويض كل حرف بحرف آخر باستخدام نفس المجموعة:
# (يمكنك تغيير هذا التعويض ليكون وفقًا لجدول استبدال مختلف)
substitution_map = {}
shift_value = 13  # يمكن اختيار قيمة ثابتة أو عشوائية للتحويل، هنا اخترت 13 فقط كمثال

# إعداد مصفوفة التعويض بإزاحة ثابتة لجميع الرموز
for i, char in enumerate(all_characters):
    # تعويض كل حرف بحرف آخر بناءً على الإزاحة المحددة
    substitution_map[char] = all_characters[(i + shift_value) % len(all_characters)]

# النص المشفر (كمثال)
ciphertext = "Khoor Zruog! 123 @#$"

# فك التشفير باستخدام مصفوفة الاستبدال
decrypted_text = []
for letter in ciphertext:
    if letter in substitution_map:
        decrypted_text.append(substitution_map[letter])
    else:
        decrypted_text.append(letter)  # إذا لم يكن الحرف في مصفوفة الاستبدال (مثل المسافات)، أضفه كما هو

# تحويل القائمة إلى نص
decrypted_text = ''.join(decrypted_text)

print("ciphertext :", decrypted_text)
