a = int(input('введите первое число: '))
oper = input('введите операцию, которую хотите выполнить: ')
b = int(input('введите второе число: '))
if oper == '/':
    if b != 0:
        print('Ответ: ' + str(a/b))
    else:
        print('Ошибка!')
elif oper == '*':
    print('Ответ: ' + str(a*b))
elif oper == '+':
    print('Ответ: ' + str(a + b))
elif oper == '-':
    print('Ответ: ' + str(a - b))
else:
    print('Ошибка!')