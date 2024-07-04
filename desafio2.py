def gerenciar_equipamentos():
    # Inicializa a lista para armazenar os equipamentos
    equipamentos = []

    # Solicita ao usuário inserir três equipamentos sem mensagens intermediárias
    for i in range(3):
        equipamento = input().strip()
        equipamentos.append(equipamento)

    # Exibe a lista de equipamentos inseridos
    print("Lista de Equipamentos:")
    for equipamento in equipamentos:
        print(f"- {equipamento}")

# Chama a função para gerenciar os equipamentos
gerenciar_equipamentos()