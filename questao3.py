def escolha_modelo():
    """Função de escolha do modelo"""
    while(True): #Loop só acaba quando o cliente escolhe a roupa certa
        print("Escolha o modelo desejado: ") #Print instruindo o cliente a escolher o modelo da camisa
        #Modelos de camisa
        print("MCS - Manga Curta Simples") 
        print("MLS - Manga Longa Simples")
        print("MCE - Manga Curta Com Estampa")
        print("MLE - Manga Longa Com Estampa")
        #Fim dos modelos de camisa
        modelo = input("Digite o modelo (MCS/MLS/MCE/MLE): ") #input() para selecionar a camisa desejada
        #valor_modelo pega os valores dos modelos dependendo no modelo digitado (transforma tudo em letra minuscula para não haver erros)
        if(modelo.lower() == "MCS".lower()):
            modelo = 1.80
        elif(modelo.lower() == "MLS".lower()):
            modelo = 2.10
        elif(modelo.lower() == "MCE".lower()):
            modelo = 2.90
        elif(modelo.lower() == "MLE".lower()):
            modelo = 3.20
        #Fim dos valores
        else:
            print("Escolha inválida. Tente selecionar o modelo novamente\n")
            continue
        return modelo #Retorna o valor e encerra o loop
        

def num_camisetas(): 
    """Função para adquirir a quantidade de camisetas que o cliente quer comprar"""
    while(True): #Loop só acaba quando o cliente dá um valor valido  ( menos de 20001)
        print("Quantas camisetas? ") #print() perguntando ao cliente quantas camisetas ele quer
        try:
            quantidade = int(input("Digite a quantidade de camisetas: ")) #input() pedindo a quantidade de camisetas
            if(quantidade > 20000): #Se a quantidade for maior que 20000 o numero não é aceito, caso contrário retorna o quantidade de items
                print("Não aceitamos quantidades tão altas de uma vez")
                print("Por favor, entre com o numero de camisetas novamente\n")
                continue
            else:
                return quantidade
        except ValueError:  
            continue
def valor_desconto(quantidade):
    """Funcão que calcula o desconto dependendo da quantidade de camisetas"""
    #Pega a quantidade e compara aos valores para calcular o desconto
    if(quantidade<20):
        desconto = 0
    elif(quantidade >= 20 and quantidade<200):
        desconto = 5/100
    elif(quantidade >= 200 and quantidade<2000):
        desconto = 7/100
    elif(quantidade >= 2000 and quantidade<=20000):
        desconto = 12/100
    #Fim dos descontos
    return desconto
def frete():
    """Fução de escolha do tipo de entrega e o valor do frete"""
    while(True): #Loop continua até que o cliente seleciona um valor de frete válido
        print("Selecione o frete: ")
        print("1 - Transportadora custa R$ 100")
        print("2 - Sedex custa R$ 200")
        print("0 - Buscas na fábrica custa 0")
        try:
            valor_frete = int(input("Digite a sua escolha: ")) #input() pedindo ao usuário que escolha po valor do frete
            if(valor_frete >2 or valor_frete<0): #Se o valor do frete for menor que 0 ou maior que 2 o programa pede ao cliente que insira um valor entre 0 e 2
                print("Digite apenas numeros de 0 a 2")
                continue
            else:
                valor_frete = valor_frete * 100 #Pega o valor digitado e multiplica por 100 para bater com o valores ao invés de criar um if para cada
                return valor_frete
        except ValueError:
            print("Digite apenas numeros.")
            continue
print("Bem vindo a fábrica de camisetas do Israel Beteguella\n")
modelo = escolha_modelo() #Pega o modelo selecionado e coloca na variável modelo
print("") #print() para dar espaço no console
quantidade  = num_camisetas() #Pega o numero de camisetas desejável e coloca na variável quantidade
print("")
desconto = valor_desconto(quantidade)   #Pega o valor do desconto e coloca na variável desconto
print("")
valor_frete = frete() #Pega o frete selecionado e coloca na variável valor_frete
print("")
total = modelo * quantidade #Calcula o valor total a se pagar
print(f"R$ {total}: Modelo: {modelo:.2f}, Numero de Camisetas: {quantidade:.2f},  Valor com desconto: {(total - (desconto * total)):.2f} + Frete: {valor_frete:.2f} = {((total) - (desconto * total) + valor_frete)}")