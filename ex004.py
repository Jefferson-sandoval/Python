a = input("Digite algo: ")
print('O tipe primitivo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alf?', a.isalpha())
print('É tudo maiuscula?', a.isupper())
print('É tudo minusculo?', a.islower())
print('É alfanumerico?', a.isalnum())