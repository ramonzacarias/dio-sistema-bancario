# Crie uma Lista 'itens' para armazenar os equipamentos:
itens = []

# Crie um loop para solicitar os itens ao usuário:
for _ in range(3):
    # Solicite o item e armazene na variável "item":
    item = input()
    
    # Adicione o item à lista "itens":
    itens.append(item)

# Exibe a lista de itens
print("Lista de Equipamentos:")  
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")
