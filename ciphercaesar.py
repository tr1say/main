alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ123456789123456789'
alfavit_UA = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ123456789123456789'
smeshenie = int(input('Ключ шифровання: '))
message = input("Текст для шифровання: ").upper()
itog = ''
lang = input('Виберіть мову UA/EU: ')
if lang == 'UA':
    for i in message:
        mesto = alfavit_UA.find(i)
        new_mesto = mesto + smeshenie
        if i in alfavit_UA:
            itog += alfavit_UA[new_mesto]
        else:
            itog += i
else:
    for i in message:
        mesto = alfavit_EU.find(i)
        new_mesto = mesto + smeshenie
        if i in alfavit_EU:
            itog += alfavit_EU[new_mesto]
        else:
            itog += i
print (itog)
