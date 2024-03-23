import matplotlib.pyplot as plt
import numpy as np

# Przykładowe dane - punkty i przedziały ufności
x_values = np.array([20,40,60,80,100,120,140,160])
y_values = np.array([0.3266,0.2536,0.2154,0.2248,0.2832,0.3764,0.4692,0.5508])

# Przykładowe przedziały ufności (dolne i górne wartości)
lower_confidence_interval = np.array([0.312810116,0.241130974,0.199712086,0.213251422,0.268575271,0.358815214,0.451075115,0.539231745])

upper_confidence_interval = np.array([0.340389884,0.266069026,0.231087914,0.236348578,0.297824729,0.393984786,0.487324885,0.562368255])

# Rysowanie wykresu punktów
plt.scatter(x_values, y_values)

#pozioma
#plt.axhline(y=40, color='red', linestyle='--')
# Rysowanie przedziałów ufności
plt.errorbar(x_values, y_values, yerr=[y_values - lower_confidence_interval, upper_confidence_interval - y_values],
             fmt='none', ecolor='gray', capsize=5, capthick=2)

# Dodanie etykiet i legendy
plt.xlabel('TTT')
plt.ylabel('Liczba przełączeń na jednego użytkownika')
plt.title('Średnia liczba przerwań w zależności od parametru TTT')
plt.legend()

# Wyświetlanie wykresu
plt.show()
