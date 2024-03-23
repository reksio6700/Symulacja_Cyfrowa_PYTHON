import matplotlib.pyplot as plt
import numpy as np

array_x = []
lambdas = ['0.0015','0.0007','0.00104','0.0012']
for i in range(1, 501):
    array_x.append(i)
x_values = np.array(array_x)
with open("L=0015.txt", 'r') as L1_file:
    L1 = [int(line.strip()) for line in L1_file]

with open("L=0.0007.txt", 'r') as L2_file:
    L2 = [int(line.strip()) for line in L2_file]


with open("L=0.00104.txt", 'r') as L3_file:
    L3 = [int(line.strip()) for line in L3_file]

with open("L=0.0012.txt", 'r') as L4_file:
    L4 = [int(line.strip()) for line in L4_file]

print(len(L1))
y_values_list = [
    np.array(L1),
    np.array(L2),
    np.array(L3),
    np.array(L4)
]
for i, y_values in enumerate(y_values_list):
    label = f'Lambda '+ lambdas[i]
    plt.plot(x_values, y_values, label=label)

# Rysowanie przerywanej kreski pionowej
plt.axvline(x=65, color='red', linestyle='--')

# Dodanie podpisu przy przerywanej linii
plt.text(52.5, 16.5, 'Koniec fazy początkowej= 65', color='b', rotation=90)

# Dodanie etykiet i legendy
plt.xlabel('Liczba obsłużonych użytkowników')
plt.ylabel('Średnia liczba użytkowników w systemie')
plt.title('Wyznaczenie długości fazy początkowej')
plt.legend()

# Wyświetlanie wykresu
plt.show()