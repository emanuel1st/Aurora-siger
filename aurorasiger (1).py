# Dados de telemetria (simulação de leitura dos sensores)

temperatura_interna = 25
temperatura_externa = 18
integridade_estrutural = 1
energia_percentual = 85
pressao_tanque = 120
modulos_criticos = 1

verificacoes = {
    "Temperatura interna": 20 <= temperatura_interna <= 30,
    "Temperatura externa": -10 <= temperatura_externa <= 35,
    "Integridade estrutural": integridade_estrutural == 1,
    "Energia": energia_percentual >= 70,
    "Pressão do tanque": 100 <= pressao_tanque <= 150,
    "Módulos críticos": modulos_criticos == 1
}

# Decisão de decolagem
if all(verificacoes.values()):
    resultado = "PRONTO PARA DECOLAR"
else:
    resultado = "DECOLAGEM ABORTADA"

# Análise energética
capacidade_total_kwh = 120
consumo_decolagem_kwh = 20
perdas_percent = 10

energia_atual_kwh = capacidade_total_kwh * (energia_percentual / 100)
energia_util_kwh = energia_atual_kwh * (1 - perdas_percent / 100)
energia_restante_kwh = energia_util_kwh - consumo_decolagem_kwh# Saída do sistema

# Saída do sistema
print("=== VERIFICAÇÕES ===")
for item, status in verificacoes.items():
    print(f"{item}: {'OK' if status else 'FALHOU'}")

print()
print("Resultado final:", resultado)

print()
print("=== ANÁLISE ENERGÉTICA ===")
print(f"Energia atual: {energia_atual_kwh:.2f} kWh")
print(f"Energia útil: {energia_util_kwh:.2f} kWh")
print(f"Energia restante após decolagem: {energia_restante_kwh:.2f} kWh")