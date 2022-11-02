print("Нуль як знак операції"
      "\nзавершить роботу програми")
while True:
    s = input("Знак (+,-,*,/): ")
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        x = float(input("a="))
        y = float(input("b="))
        if s == '+':
            print( (x+y))
        elif s == '-':
            print((x-y))
        elif s == '*':
            print( (x*y))
        elif s == '/':
            if y != 0:
                print((x/y))
            else:
                print("Ділиш на нуль, серйозно?")
    else:
        print("Неправильний знак операції!")
