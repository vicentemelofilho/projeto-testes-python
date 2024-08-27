#https://docs.python.org/3/library/doctest.html
#https://docs.python.org/3/library/unittest.html

print('oi')


from calculadora import soma


print(soma(10, 20))

print(soma(-10, 20))

print(soma(10.9, 20.14))

try:
    print(soma('15', 15))
except AssertionError as e:    
    print(f'Conta inválida: {e}')
# except TypeError as e:
#     print('Conta inválida')
#     print(e)