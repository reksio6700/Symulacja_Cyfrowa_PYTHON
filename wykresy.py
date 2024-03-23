import matplotlib.pyplot as plt
import numpy as np

# Przykładowe dane - punkty i przedziały ufności
x_values = np.array([0.00116,0.00115,0.00112,0.0011,0.00105,0.001,0.00108])
y_values = np.array([50,48.7,45.9,43.9,42.1,40.5,42.9
])

# Przykładowe przedziały ufności (dolne i górne wartości)
lower_confidence_interval = np.array([46.14031231,45.02056431,43.2138372,40.40441613,39.52184648,37.65351466,39.87901547
])

upper_confidence_interval = np.array([53.85968769,52.37943569,48.5861628,47.39558387,44.67815352,43.34648534,45.82098453
])

# Rysowanie wykresu punktów
plt.scatter(x_values, y_values)

#pozioma
plt.axhline(y=40, color='red', linestyle='--')
# Rysowanie przedziałów ufności
plt.errorbar(x_values, y_values, yerr=[y_values - lower_confidence_interval, upper_confidence_interval - y_values],
             fmt='none', ecolor='gray', capsize=5, capthick=2)

# Dodanie etykiet i legendy
plt.xlabel('Wartość lambda')
plt.ylabel('Średnia suma użytkowników w systemie')
plt.title('Wyznaczenie prametru lambda z przedziałami ufności')
plt.legend()

# Wyświetlanie wykresu
plt.show()
