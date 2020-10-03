#! /usr/bin/env python

what = input( "Введите действие ( +; -; /; *; **; % ): " )
a = float(input("Первое число: "))
b = float(input("Второе число: "))

if what == "+":
    c = a + b
    print( float( c ) )
elif what == "-":
    c = a - b
    print( c )
elif what == "/":
    c = a / b
    print( float( c ) )
elif what == "*":
    c = a * b
    print( float( c ) )
elif what == "**":
    c = a ** b
    print( float( c ) )
elif what == "%":
    c = a % b
    print( float( c ) )
else:
    print("Вы ввелли какую-то дичь")
