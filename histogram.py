import matplotlib.pyplot as plt
import numpy as np
import random

# Ustawienie ziarna generatora losowego dla reprodukowalności
random.seed(1382300866 )

# Wygenerowanie 1000 liczb losowych z rozkładem jednostajnym
liczby_losowe = [random.gauss(0, 4)for _ in range (100000)]

# Tworzenie wykresu
plt.hist(liczby_losowe, bins=40, alpha=0.7, color='blue', edgecolor='black')

# Dodanie etykiet i tytułu
plt.xlabel('Wartości losowe')
plt.ylabel('Liczba wystąpień')
plt.title('Histogram liczb losowych o rozkładzie Gaussa')

# Wyświetlenie wykresu
plt.show()