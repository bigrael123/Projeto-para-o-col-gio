def cadastrar_funcionario(id): 
    """Função para cadastrar funcionário via input"""
    global lista_funcionarios #Invoca a variavel lista_funcionários
    funcionarios = lista_funcionarios.copy() #Copia a lista_funcionarios para funcionarios
    funcionario = {} #Inicia o dicionário
    #Adiciona as novas informações ao dicionário 
    funcionario['ID'] = id
    print(f"ID do funcionário: {funcionario['ID']}")
    funcionario['Nome'] = input("Digite o nome do funcionário: ")
    funcionario['Setor'] = input("Digite o setor do funcionário: ")
    while(True):
        try:
            funcionario['Salario'] = int(input("Digite o salário do funcionário: "))
    #Fim das informações
            break
        except ValueError:
            print("Valor inválido")
            continue
    funcionarios.append(funcionario.copy()) #Adiciona uma cópia de funcionario na lista de dicionários
    return funcionarios #Retorna a lista

def consultar_funcionarios():
    """Função ver os funcionarios com filtros"""
    #Menu da consulta
    print("Selecione o que deseja pesquisar na lista de funcionários: ")
    print("1 - Consultar Todos")
    print("2 - Consultar por ID")
    print("3 - Consultar por Setor")
    print("4 - Retornar ao Menu")
    #Fim do menu
    global lista_funcionarios #Invoca a variável lista_funcionarios para consulta de seus valores
    global id_global #Invoca a id_global para calculos
    if(len(lista_funcionarios) == 0): #Se não houverem funcionários alerta o usuário com prints() e leva o para o menu principal
        print("Nenhum funcionário cadastrado")
        print("Cadastre um funcionário no menu anterior")
        print("")
        return
    while(True):
        try:
            escolha_consultar = int(input("Digite o número para fazer a pesquisa (1/2/3/4): ")) #input() da escolha do menu
            if(escolha_consultar < 1 or escolha_consultar>4): #Valida se escolha_consultar está na faixa válida e da um print() e reinicia o loop caso esteja em faixa inválida
                print("Opção inválida")
                continue
            else:
                if(escolha_consultar == 1):
                    for i in range (id_global - 3801898): #For que calcula a quantidade de funcionários
                         #Testa se o elemento da lista de dicionários existe e da print() detodos os funcionários
                        try:
                            print(f"Funcionário com ID: {lista_funcionarios[i]['ID']}")
                        except IndexError:
                            continue
                        print(f"Nome do funcionário: {lista_funcionarios[i]['Nome']}")
                        print(f"Setor do funcionário: {lista_funcionarios[i]['Setor']}")
                        print(f"Salário do funcionário: {lista_funcionarios[i]['Salario']}")
                        print("")
                        #Fim do print() atual
                        continue
                    continue
                elif(escolha_consultar == 2):
                    print("Escolha o funcionário baseado em seu ID")
                    while(True):
                        try:
                            id_selecao =   int(input("Digite o ID do funcionário: ")) - 3801898 #Calcula o a quantidade de funcionários
                            for i in range(id_global - 3801898): #Pega a quantidade de funcionários contando os removidos e faz um loop
                                #Verifica se o item atual é válido
                                try:
                                    lista_funcionarios[i]['ID']
                                except IndexError:
                                    print("ID inválido")
                                    break
                                #Verifica se o id do item bate e lista os valores do dicionário
                                if(id_selecao + 3801898 == lista_funcionarios[i]['ID']):
                                    print(f"Funcionário com ID: {lista_funcionarios[i]['ID']}")
                                    print(f"Nome do funcionário: {lista_funcionarios[i]['Nome']}")
                                    print(f"Setor do funcionário: {lista_funcionarios[i]['Setor']}")
                                    print(f"Salário do funcionário: {lista_funcionarios[i]['Salario']}")
                                    print("")
                                    break
                                else:
                                    if(i+1 == id_global - 3801898): #Checa se i é igual ao numero de funcionários, se sim dá print do error e quebra o loop
                                        print("ID inválido")
                                        break
                                    continue
                            break
                        except ValueError: #Caso o ID receba um valor que não é int da print() de ID inválido e quebra o loop
                            print("ID inválido")
                            break
                elif(escolha_consultar == 3):
                    print("Escolha o funcionário baseado em seu Setor")
                    setor_do_funcionario = input("Digite o setor desejado: ")
                    contador_de_setor = 0 #Inicia a variável contador_de_setor com 0 e reseta seu valor nas escolhas posteriores. A variável é usada para saber se o código deu print() de algum funcionários
                    for i in range (id_global - 3801898 +1):
                        try:
                            lista_funcionarios[i]['Setor']
                        except IndexError:
                            if(id_global - 3801898 == i+1 and contador_de_setor == 0):
                                print("Setor Inválido")
                                break
                            else:
                                continue
                        if(lista_funcionarios[i]['Setor'].lower() == setor_do_funcionario.lower()):
                            contador_de_setor+=1
                            print(f"Funcionário com ID: {lista_funcionarios[i]['ID']}")
                            print(f"Nome do funcionário: {lista_funcionarios[i]['Nome']}")
                            print(f"Setor do funcionário: {lista_funcionarios[i]['Setor']}")
                            print(f"Salário do funcionário: {lista_funcionarios[i]['Salario']}")
                            print("")
                            continue
                    continue
                elif(escolha_consultar  == 4): #S o usuário digitar 4 o loop se quebra
                    return
        except ValueError:
            print("Opção inválida")
            continue
        
def remover_funconario():
    """Função para deletar funcionários via input"""
    global lista_funcionarios
    global id_global
    if(len(lista_funcionarios) == 0):
        print("Nenhum funcionário cadastrado")
        print("Cadastre um funcionário no menu anterior")
        print("")
        return
    print("Digite o ID do funcionário a ser removido da lista de funcionarios")
    while(True):
        try:
            remover_id = int(input("Digite o ID: ")) - 3801898
            for i in range(id_global - 3801898):
                try:
                    lista_funcionarios[i]['ID']
                except IndexError:
                    print("ID inválido")
                    break
                if(remover_id + 3801898 == lista_funcionarios[i]['ID']):
                    print(f"Removendo funcionário com ID: {lista_funcionarios[i]['ID']}")
                    print(f"Nome do funcionário: {lista_funcionarios[i]['Nome']}")
                    print(f"Setor do funcionário: {lista_funcionarios[i]['Setor']}")
                    print(f"Salário do funcionário: {lista_funcionarios[i]['Salario']}")
                    lista_funcionarios.pop(i)
                    print("Funcionário deletado")
                    print("")
                    return
                else:
                    if(i+1 == id_global - 3801898):
                        print("ID inválido")
                    continue
        except ValueError:
            print("ID inválido")
            continue
        
print("Bem vindos a empresa do Israel Beteguella")
print("")
lista_funcionarios = [] #Inicia a lista_funcionarios
id_global = 3801898 #RU do aluno
while(True):
    print("O que você deseja fazer?")
    print("1 - Cadastrar Funcionário")
    print("2 - Consultar Funcionário")
    print("3 - Remover funcionário")
    print("4 - Encerrar")
    try:
        escolha_funcionario = int(input("Digite o número para realizar a ação correspondete (1/2/3/4): "))
        if(escolha_funcionario <1 or escolha_funcionario>4):
            print("Opção inválida")
            continue
        elif(escolha_funcionario == 1):
            id_global +=1 #incrementa id_global
            lista_funcionarios = cadastrar_funcionario(id_global).copy()
            continue
        elif(escolha_funcionario == 2):
            consultar_funcionarios()
            continue
        elif(escolha_funcionario == 3):
            remover_funconario()
            continue
        elif(escolha_funcionario == 4):
            print("Encerrando...")
            exit()
    except ValueError:
        print("Opção inválida")
        continue




