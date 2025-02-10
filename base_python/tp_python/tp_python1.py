savings = 1000
total_savings = 2500

print(f"j'ai commencé avec ${savings} et maintenant j'ai ${2500}. Excelllent")

areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
# affichage du second element de la liste
print(areas[1])
# affichage de la surface de living room
print(areas[5:])

# addition de kitchen's surface et celle de bedroom dans eat_sleep
eat_sleep_area = areas[3] + areas[7]
print(f"voici l'addition de kitchen surface et celle de bedroom {eat_sleep_area}")

# déclaration des variable monthly_savings et num_months
monthly_savings = 100
num_months = 4

new_savings = monthly_savings * num_months
total_savings = savings + new_savings
print(total_savings)

