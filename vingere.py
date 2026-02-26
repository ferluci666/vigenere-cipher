def letter_to_number():
    if encrypting=="e":
      for letter,key in zip(letters, key_letters):
        number_shift = ord(letter) + ord(key) + extra
        numbers_shifted.append(number_shift)
      return numbers_shifted

    else:
      for letter,key in zip(letters, key_letters):
        number_shift = ord(letter) -ord(key) - extra
        numbers_shifted.append(number_shift)
      return numbers_shifted
again =""
while again != 'no':
    encrypting = input("Do you want to code encrypt a text or decript. Type 'e' to encrypt or 'd' to decrypt ")
    if encrypting !="e" and encrypting !="d":
        encrypting = input("enter 'e' or 'd' ")

    keyword= input("enter keyword ")
    text= input("enter text ")
    extra= input("enter extra number ")

    numbers_shifted= []
    coded_text= ""
    extra = int(extra)
    letters = list(text)
    key_letters = list(keyword)

    while len(key_letters) < len(letters):
        key_letters = key_letters + key_letters

    letter_to_number()

    for number in numbers_shifted:
     letters_shifted = chr(number)
     coded_text = coded_text + letters_shifted

    print(coded_text)
    again = input("Do you want to encrypt or decrypt anything else, Type 'no' to stop, type anything else to continue ")