# num 10
import math

for x in range(-3, 4):  # Boucle de -3 à 3 inclus
    try:
        result = math.sin(x) / x  # Calcul de sin(x)/x
        print(f"sin({x})/{x} = {result} ~ {result:.3f}")
    except ZeroDivisionError:
        print(f"sin(0)/0 ne peut se faire.")