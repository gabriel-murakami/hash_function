import hash_functions as hf
from matplotlib import pyplot as plt

print('Metodo da divisao')

print('Questao a)')

m = 12

for i in range(0, 101):
  h = hf.div_method(i, m)

  if h == 3:
    print(i)

print('Questao b)')

m = 11

for i in range(0, 101):
  h = hf.div_method(i, m)

  if h == 3:
    print(i)

print('Questao c)')

m = 97
colision_array = [0]*m

for i in range(1, 10001):
  h = hf.div_method(i, m)

  colision_array[h] += 1

plt.figure(figsize=(16, 9))
plt.bar(range(0, 97), colision_array, width=1)
plt.xlabel('Chave')
plt.ylabel('Contagem')
plt.show()

print('\nMetodo da multiplicacao')

print('Questao a)')

m = 200
a = 0.62
colision_array = [0]*m

for i in range(1, 500001):
  h = hf.multi_method(i, m, a)

  colision_array[h] += 1

plt.figure(figsize=(16, 9))
plt.bar(range(0, 200), colision_array, width=1)
plt.xlabel('Chave')
plt.ylabel('Contagem')
plt.show()

print('Questao b)')

m = 200
a = 0.61803398875
colision_array = [0]*m

for i in range(1, 500001):
  h = hf.multi_method(i, m, a)

  colision_array[h] += 1

plt.figure(figsize=(16, 9))
plt.bar(range(0, 200), colision_array, width=1)
plt.xlabel('Chave')
plt.ylabel('Contagem')
plt.show()
