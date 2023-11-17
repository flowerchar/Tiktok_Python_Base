number1 = eval(input(''))
number2 = eval(input(''))
number3 = eval(input(''))

print(f'符合条件的数字有6个\n他们的和为{(number1*100+number2*10+number3)+(number2*100+number1*10+number3)+(number2*100+number3*10+number1)+(number1*100+number3*10+number2)+(number3*100+number2*10+number1)+(number3*100+number1*10+number2)}')