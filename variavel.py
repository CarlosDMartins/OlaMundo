#input é uma função que permite perguntar algo ao usuário
#print("Olá,", nome, ".tudo bem com você?")
#print(type(nome))

a = 10
b = 5.8
c = "Rio de Janeiro"
d = True

print("a: ",a)
print("b: ",b)
print("c: ",c)
print("d:", d)

print("tipo da var a: ", type(a))# tipo inteiro (números inteiros)
print("tipo da var b: ", type(b))# tipo float (números reais)
print("tipo da var c: ", type(c))# tipo string (alfanumérico)
print("tipo da var d: ", type(d))# tipo boolean (True ou False)

a = 20
print("a: ",a)

b = "São Paulo"
print("b: ",b)
print("tipo da var a: ", type(a))
print("tipo da var b: ", type(b))

a = input("Informe seu número: ")
b = input("Informe outro número: ")
print("a: ",a, "-b: ", b)
print("Tipo da var a: ", type(a))
print("Tipo da var b: ", type(b))
c = a + b # cocatenou as strings de a e b (juntou elas)
print("c: ", c)
print("tipo da var c: ", type(c))
d = int(a)
print("d:", d)
print("tipo da var d: ", type(d))

a = int(input("Informe seu número: "))
b = int(input("Informe outro número: "))
print("a: ",a, "-b: ", b)
print("Tipo da var a: ", type(a))
print("Tipo da var b: ", type(b))

c = a + b
print("c: ", c)
print("tipo da var c: ", type(c))

a = float(input("Informe seu número: "))
b = float(input("Informe outro número: "))
print("a: ",a, "-b: ", b)
print("Tipo da var a: ", type(a))
print("Tipo da var b: ", type(b))
c = a + b # cocatenou as strings de a e b (juntou elas)
print("c: ", c)
print("tipo da var c: ", type(c))