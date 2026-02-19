def letter_to_number():
    if encrypting=="encrypt":
      for letter,key in zip(letters, key_letters):
        number_shift = ord(letter) + ord(key) + 200
        numbers_shifted.append(number_shift)
      return numbers_shifted

    else:
      for letter,key in zip(letters, key_letters):
        number_shift = ord(letter) -ord(key) -200
        numbers_shifted.append(number_shift)
      return numbers_shifted
encrypting = input("Welcome do you want to code encrypt a text or decript. Type 'encrypt' to encrypt or 'decrypt' to decrypt ")
if encrypting !="encrypt" and encrypting !="decrypt":
    encrypting = input("enter encrypt or decrypt ")

keyword= input("enter keyword ")
text= input("enter text ")

numbers_shifted= []
coded_text= ""
letters = list(text)
key_letters = list(keyword)

while len(key_letters) < len(letters):
    key_letters = key_letters + key_letters

letter_to_number()

for number in numbers_shifted:
    letters_shifted = chr(number)
    coded_text = coded_text + letters_shifted

print(coded_text)