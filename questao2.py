print("Bem vindos a loja de marmitas do Israel Beteguella") #Da um print() com o nome do dono da loja com uma mensagem de bem vindo 
#Valores dos tamanhos de cada refeição 
print("O tamanho P do bife acebolado (BA) custa 16 reais") 
print("O tamanho M do bife acebolado (BA) custa 18 reais") 
print("O tamanho G do bife acebolado (BA) custa 22 reais") 
print("O tamanho P do Filé de Franfo (FF) custa 15 reais") 
print("O tamanho M do Filé de Franfo (FF) custa 17 reais") 
print("O tamanho G do Filé de Franfo (FF) custa 21 reais") 
#Fim dos tamanhos de cada refeição 
acumulador = 0 #Acumula o valor de cada pedido para apresentar no fim 
while(True): #Mantem o loop da escolha até que o cliente digite N no fim 
    sabor = input("\nDigite o sabor que você quer (BA/FF): ") #input() para o cliente escolher o sabor  
    if(not sabor.lower() == "BA".lower() and not sabor.lower() == "FF".lower()): #Converte os pedidos pra letra minuscula e os compara contra a variavel sabor em caso o pedido não exista 
        print("Sabor inválido. Tente novamente.") #mensagem de valor inválido 
        continue #Caso o valor seja inválido o codigo recomeça na escolha da refeição 
    tamanho = input("Digite o tamanho que você quer (P/M/G):") #input() do tamanho do prato a ser pedido 
    if(not tamanho.lower() == "P".lower() and not tamanho.lower() == "M".lower() and not tamanho.lower() == "G".lower() ): #Compara pedidos de tamanho com letras minusculas 
        print("Tamanho inválido. Tente novamente. \n") #mensagem de valor inválido 
        continue #Caso o valor seja inválido o codigo recomeça na escolha do tamanho da refeição 
    else: 
        print("") #print() para separar os prints 
    #Compara os tamanho e o sabor das refeições 
    if(tamanho.lower() == "P".lower() and sabor.lower() == "BA".lower()):  
        print("Você pediu um bife acebolado tamanho P que custa R$ 16 reais")  
        acumulador += 16 
    elif(tamanho.lower() == "M".lower() and sabor.lower() == "BA".lower()): 
        print("Você pediu um bife acebolado tamanho M que custa R$ 18 reais") 
        acumulador += 18 
    elif(tamanho.lower() == "G".lower() and sabor.lower() == "BA".lower()): 
        print("Você pediu um bife acebolado tamanho G que custa R$ 22 reais") 
        acumulador += 22 
    else: 
         if(tamanho.lower() == "P".lower() and sabor.lower() == "FF".lower()): 
              print("Você pediu um Filé de Frango tamanho P que custa R$ 15 reais") 
              acumulador += 15 
         else: 
            if(tamanho.lower() == "M".lower() and sabor.lower() == "FF".lower()): 
                print("Você pediu um Filé de Frango tamanho M que custa R$ 17 reais") 
                acumulador+= 17 
            else: 
                 if(tamanho.lower() == "G".lower() and sabor.lower() == "FF".lower()):  
                    print("Você pediu um Filé de Frango tamanho G que custa R$ 21 reais") 
                    acumulador += 21 
    #Ultima comparação dos tamanhos e sabores 
    print("\nVai querer mais alguma coisa?") #print() para perguntar se o cliente quer algo mais ou não 
    simounao = input("Digite (S/N): ") #input() pra pegar o valor da escolha do cliente 
    if(simounao.lower() == "S".lower()): #Compara sim 
        continue #caso a resposta seja sim volta pro começo do loop 
    else: 
        if(simounao.lower() == "N".lower()): #compara não 
            print(f"O valor a ser pago é RS$ {acumulador:.2f}") #print() do valor a ser pago 
            break #Quebra o loop e encerra o programa 