def get_letters(text):
    # - bunga bolib yuboramiz
    text = text.split("-")
    if not text[0] < text[1]:
        return "Alifbor tartibida kiriting"
    # shartlar tekshiriladi yani ikkalasiyam kattami yoki kichik
    if 'a' <= text[0] <= 'z'and not 'a' <= text[1] <= 'z':
            return "Iltimos ikkalasini kichik harfda yoki katta harfda kiriting"
    elif 'A' <= text[0] <= 'Z'and not 'A' <= text[1] <= 'Z':
            return "Iltimos ikkalasini kichik harfda yoki katta harfda kiriting"
        #Agar shartlar bajarilsa harflarni o'zuga qoshib boradi string 
    string = str()
    for i in range(ord(text[0]),ord(text[1])+1):
        string+=chr(i)
    return string


text = input("Enter a text :")

print(get_letters(text))


   
