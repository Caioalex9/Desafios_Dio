def recomendar_plano(consumo_mensal):
    if consumo_mensal <= 10:
        return "Plano Essencial Fibra - 50Mbps: Recomendado para um consumo médio de até 10 GB."
    elif consumo_mensal <= 20:
        return "Plano Prata Fibra - 100Mbps: Recomendado para um consumo médio acima de 10 GB até 20 GB."
    else:
        return "Plano Premium Fibra - 300Mbps: Recomendado para um consumo médio acima de 20 GB."

# Solicita o consumo médio mensal de dados do usuário
try:
    consumo = float(input("Informe o seu consumo médio mensal de dados em GB: "))
    
    # Chama a função recomendar_plano e imprime a recomendação
    plano_recomendado = recomendar_plano(consumo)
    print(plano_recomendado)
except ValueError:
    print("Por favor, insira um valor numérico válido.")