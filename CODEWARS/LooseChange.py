#Welcome young Jedi! In this Kata you must create a function that takes an amount of US currency in cents, and returns a dictionary/hash 
#which shows the least amount of coins used to make up that amount. The only coin denominations considered in this exercise are: Pennies (1¢), Nickels (5¢), Dimes (10¢) and Quarters (25¢). 
#Therefor the dictionary returned should contain exactly 4 key/value pairs.
#Notes:
#If the function is passed either 0 or a negative number, the function should return the dictionary with all values equal to 0.
#If a float is passed into the function, its value should be be rounded down, and the resulting dictionary should never contain fractions of a coin.
def loose_change(input):
    nombre_monedas = ["Pennies", "Nickels", "Dimes", "Quarters"]
    valor_monedas = [1, 5, 10, 25]
    dicc_monedas = dict(zip(nombre_monedas, valor_monedas))
    monedas = 0
    lista_vacia = []
    dicc_devolucion = dict(zip(nombre_monedas.reverse, lista_vacia))
    valor_monedas = valor_monedas.reverse()

    for item in valor_monedas:
        while input > item:
            input -= item
            monedas += 1
            lista_vacia.append(monedas)
    return dicc_devolucion


    def loose_change(input):
        nombre_monedas = ["Pennies", "Nickels", "Dimes", "Quarters"]
        valor_monedas = [1, 5, 10, 25]
        dicc_monedas = dict(zip(nombre_monedas, valor_monedas))
        cambio = []
        valor_monedas = valor_monedas.reverse()
        
        for item in valor_monedas:
            while input > item:
                input -= item