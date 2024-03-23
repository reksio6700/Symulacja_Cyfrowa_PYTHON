import matplotlib.pyplot as plt
import numpy as np

# Przykładowe dane - punkty i przedziały ufności
x_values = np.array([5,15,25,35,45,55,65,75,80])
y_values = np.array([3.8428, 1.8602, 1.4226, 1.231, 1.1164, 1.0502, 1.0256, 0.974, 0.974])

# Przykładowe przedziały ufności (dolne i górne wartości)
lower_confidence_interval = np.array([3.768066751,1.803963867,1.391560507,1.202503204,1.093911533,1.029233004,0.999707989,0.95015477,0.955715201])

upper_confidence_interval = np.array([3.917533249,1.916436133,1.453639493,1.259496796,1.138888467,1.071166996,1.051492011,0.99784523,0.992284799])

# Rysowanie wykresu punktów
plt.scatter(x_values, y_values)

#pozioma
#plt.axhline(y=40, color='red', linestyle='--')
# Rysowanie przedziałów ufności
plt.errorbar(x_values, y_values, yerr=[y_values - lower_confidence_interval, upper_confidence_interval - y_values],
             fmt='none', ecolor='gray', capsize=5, capthick=2)

# Dodanie etykiet i legendy
plt.xlabel('Prędkość użytkownika - v')
plt.ylabel('Liczba przełączeń na jednego użytkownika w systemie')
plt.title('Wykres średniej liczby przełączeń w zależności od prędkości')
plt.legend()

# Wyświetlanie wykresu
plt.show()
