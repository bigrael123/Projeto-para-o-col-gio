print("Bem vindos a loja do Israel Beteguella") #Da um print() com o nome do dono da loja com uma mensagem de bem vindo
valorDoPedido = int(input("Digite o valor do pedido: ")) #Pede o valor do pedido do cliente via input()
quantidadeParcelas = int(input("Digite a quantidade de parcelas: ")) #Pede a a quantidade de parcelas para o cliente via input()
if(quantidadeParcelas<4): #Se a parcela for menor que 4 o juros são iguais a zero
    juros = 0
elif(quantidadeParcelas >= 4 and quantidadeParcelas<6): #Se a parcela for igual ou maior que 4, e 6 for menor que 6 os juros serão  de 4/100 ou 0.04
    juros = 4/100
elif(quantidadeParcelas >= 6  and quantidadeParcelas< 9): #Se a parcela for igual ou maior que 6, e 9 for menor que 6 os juros serão  de 8/100 ou 0.08
    juros = 8/100
elif(quantidadeParcelas >= 9 and quantidadeParcelas<13): #Se a parcela for igual ou maior que 9, e 13 for menor que 6 os juros serão  de 16/100 ou 0.16
    juros = 16/100
else:
    juros = 32/100 #Se a parcela for igual ou maior que 13 os juros serão  de 32/100 ou 0.32
valorDaParcela = valorDoPedido * (1 + juros) / quantidadeParcelas #Pega os juros e adiciona + 1, multiplca se prlo valor do pedido total e dividi-se pelo tamanho total da parcela
valorTotalParcelado = valorDaParcela*quantidadeParcelas #Multiplica o valor das parcelas pela quantidade pela quantidade, assim conseguindo o valor total do produto
print(f"O valor das parcelas: R$ {valorDaParcela:.2f}") #Da um print com o valor da parcela, cortando casas decimais acima de 2
print(f"Total a pagar: R$ {(valorTotalParcelado):.2f}") #Da um print com o valor total de todas as parcelas, cortando casas decimais acima de 2