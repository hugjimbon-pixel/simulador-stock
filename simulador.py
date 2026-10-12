# Simulador de stock de almacén - Versión 1
import random

# --- Parámetros del almacén (puedes cambiarlos) ---
DIAS = 30               # días que dura la simulación
STOCK_INICIAL = 100     # unidades al empezar
PUNTO_PEDIDO = 40       # si el stock baja de aquí, se hace un pedido
CANTIDAD_PEDIDO = 80    # unidades que se piden cada vez
PLAZO_ENTREGA = 3       # días que tarda en llegar un pedido
DEMANDA_MIN = 5         # demanda mínima diaria
DEMANDA_MAX = 15        # demanda máxima diaria

# --- Situación al empezar ---
stock = STOCK_INICIAL
dia_llegada_pedido = None   # None = no hay ningún pedido en camino
unidades_no_servidas = 0

print("Día | Demanda | Servido | Stock | Evento")
print("-" * 50)

for dia in range(1, DIAS + 1):
    evento = ""

    # 1. ¿Llega hoy un pedido?
    if dia == dia_llegada_pedido:
        stock += CANTIDAD_PEDIDO
        dia_llegada_pedido = None
        evento += f"📦 Llegan {CANTIDAD_PEDIDO} uds. "

    # 2. Llega la demanda del día
    demanda = random.randint(DEMANDA_MIN, DEMANDA_MAX)
    servido = min(stock, demanda)
    stock -= servido
    if servido < demanda:
        unidades_no_servidas += demanda - servido
        evento += "⚠️ Rotura de stock. "

    # 3. ¿Hay que hacer un pedido?
    if stock <= PUNTO_PEDIDO and dia_llegada_pedido is None:
        dia_llegada_pedido = dia + PLAZO_ENTREGA
        evento += f"📝 Pedido (llega el día {dia_llegada_pedido})"

    print(f"{dia:>3} | {demanda:>7} | {servido:>7} | {stock:>5} | {evento}")

print("-" * 50)
print(f"Stock final: {stock} unidades")
print(f"Unidades no servidas: {unidades_no_servidas}")
