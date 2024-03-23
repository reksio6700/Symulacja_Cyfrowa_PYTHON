import matplotlib.pyplot as plt
import numpy as np

# Przykładowe dane - punkty i przedziały ufności
x_values = np.array([5,15,25,35,45,55,65,75,80])
y_values = np.array([0.5938,0.272,0.1848,0.1562,0.1382,0.1138,0.1096,0.1044,0.0974])

# Przykładowe przedziały ufności (dolne i górne wartości)
lower_confidence_interval = np.array([0.583473061,0.258310262,0.176534265,0.142387045,0.128208877,0.102345351,0.099948129,0.095035167,0.087932513])

upper_confidence_interval = np.array([0.604126939,0.285689738,0.193065735,0.170012955,0.148191123,0.125254649,0.119251871,0.113764833,0.106867487])

# Rysowanie wykresu punktów
plt.scatter(x_values, y_values)

#pozioma
#plt.axhline(y=40, color='red', linestyle='--')
# Rysowanie przedziałów ufności
plt.errorbar(x_values, y_values, yerr=[y_values - lower_confidence_interval, upper_confidence_interval - y_values],
             fmt='none', ecolor='gray', capsize=5, capthick=2)

# Dodanie etykiet i legendy
plt.xlabel('Prędkość użytkownika - v')
plt.ylabel('Liczba zerwań na jednego użytkownika w systemie')
plt.title('Wykres średniej liczby zerwań w zależności od prędkości')
plt.legend()

# Wyświetlanie wykresu
plt.show()
