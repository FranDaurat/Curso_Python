#!/usr/bin/python3 

juegos = ["Super Mario Bros", "Zelda: Breath of the Wild", "Cyberpunk 2077", "Final Fantasy VII"]
tope = 500

# Géneros 
generos = {
    "Super Mario Bros": "Aventura",
    "Zelda: Breath of the Wild": "Aventura",
    "Cyberpunk 2077": "Rol",
    "Final Fantasy VII": "Rol" 
}

# Ventas y Stock
ventas_y_stock = {
    "Super Mario Bros": (400, 20),
    "Zelda: Breath of the Wild": (600, 20),
    "Cyberpunk 2077": (60, 120),
    "Final Fantasy VII": (924, 3)
}  

# Clientes
clientes = {
    "Super Mario Bros": {"Marcelo", "Hackermate", "Hackavis", "Securiters", "Lobotec"},
    "Zelda: Breath of the Wild": {"Marcelo", "Hackavis", "Lucia", "Manolo", "Pepe"},
    "Cyberpunk 2077": {"Marcelo", "Hackermate", "lobotec", "Pepe", "Raquel", "Albert"},
    "Final Fantasy VII": {"Lucia", "Manolo", "Pepe", "Securiters", "Lobotec"}
} 


def sumario(juego): 
    print(f"\n[i] Resumen del juego {juego}\n")
    print(f"\t[+] Género del juego: {generos[juego]}")
    print(f"\t[+] Total de ventas para este juego: {ventas_y_stock[juego][0]} unidades")
    print(f"\t[+] Total de stock para este juego: {ventas_y_stock[juego][1]} unidades")
    print(f"\t[+] Clientes que han adquirido el juego: {', '.join(clientes[juego])}")

for juego in juegos: 
    if ventas_y_stock[juego][0] > tope:
        sumario(juego)

ventas_totales = lambda: sum(ventas for juego, (ventas,chupala) in ventas_y_stock.items() if ventas_y_stock[juego][0] > tope) 

print(f"[+] El total de ventas de todos los productos ha sido de {ventas_totales()} productos")