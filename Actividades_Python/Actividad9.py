"""Calculate the tip
Your goal is to find out exactly how much tip you should give after receiving a service. 
In this scenario, ask for the total bill. Then display the tip for 18%, 20% and 25%.

Remember you want to be nice, so don't forget to round up. To push this more, 
ask for the number of people involved, then evenly split the tip and total cost among them.

To go even a step further, split unevenly (for example, one person pays 70% of the bill while the other pays 30%)
"""

"""Calcula la propina
Su objetivo es averiguar exactamente cuánta propina debe dar después de recibir un servicio. 
En este escenario, solicite la factura total. Luego muestre la propina para 18%, 20% y 25%.

Recuerda que quieres ser amable, así que no olvides redondear. Para impulsar esto más,
pregunte por la cantidad de personas involucradas, luego divida equitativamente la propina y el costo total entre ellas.

Para ir un paso más allá, divida de manera desigual (por ejemplo, una persona paga el 70 % de la factura mientras que la otra paga el 30 %).
"""

print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))

tip = int(input("How much tip would you like to give? 18%, 20%, or 25%? "))

num_of_split = int(input("How many people to split the bill? "))

calculate_bill = bill * (1 + (tip/100)) / num_of_split

final_amount = "{:.2f}".format(calculate_bill, 2)

if tip == 18:
        print(f"Each person should pay: ${final_amount}")
elif tip == 20:
        print(f"Each person should pay: ${final_amount}")
else:
        print(f"Each person should pay: ${final_amount}")