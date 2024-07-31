#               0,25/0,5/1,0/2,0/5,0/10)
estoque_notas = [10, 10, 10, 10, 10, 10]
valor_notas = [0.25, 0.5, 1, 2, 5, 10]
numeros_celular_historico = []
historico_valor_pix = []

#              agua/guar/coca/coca_zero
estoque_latas = [10, 15, 10, 10]
preco_produto = [2.50, 5.25, 6.50, 7.75]

#String com nome das bebidas 
nome_bebidas = ['Água', 'Guaraná', 'Coca-Cola normal', 'Coca-Cola Zero']

def entrar_usuario():
    print('=======================================================')
    print('Olá, seja bem-vindo! Escolha o numero de sua bebida:   ')
    print('                  1 - Aguinha - R$2,50                 ')
    print('                  2 - Guaraná geladinho - R$5,25       ')
    print('                  3 - Coca-cola normal - R$6,50        ')
    print('                  4 - Coca-Cola Zero - R$7,75          ')
    print('=======================================================')
        

    comando_maquina = int(input())
    return comando_maquina

#Funções comando administrador
def entrar_adm():
   #Menu do modo administrador
    print("===MODO ADMINISTRADOR===")
    print("Selecione uma opção:")
    print("1 - Saldo máquina")
    print("2 - Estoque de cédulas e moedas")
    print("3 - Adicionar estoque de cédulas e moedas")
    print("4 - Remover estoque de cédulas e moedas")
    print("5 - Estoque de bebidas")
    print("6 - Adicionar estoque de latas e garrafas")
    print("7 - historico de compras por pix")
    print("")
    print("Digite qualquer outro número para voltar ao modo de usuário")
def calcular_saldo ():
#Multiplicação do estoque pelo valor das notas e soma com o Saldo_maquina.
    saldo_maquina = estoque_notas[0] * 0.25 + estoque_notas[1] * 0.5 + estoque_notas[2] + estoque_notas[3] * 2 + estoque_notas[4] * 5 + estoque_notas[5] * 10
    print("O saldo da maquina é: R$", saldo_maquina)
def verificar_estoque():
#Se escolher a opção 2, o for verifica a quantidade de notas ou moedas por valor.
    for cont in range (len(estoque_notas)):
        print(estoque_notas[cont],"cédula/moeda(s) de R$", valor_notas[cont])
def inserir_dinheiro(): 
#Se escolher a opção 3, será realizada a soma entre o estoque_notas atual e a quantidade_inseridas.
#Fator é uma variavel de verificação de um valor no index.
    print("Insira qual a nota ou moeda que sera inserida:")
    valor_inserido = float(input()) 
    if valor_inserido > 1:
        print("Quantas cédulas de R$", valor_inserido, "serão inseridas?")
        quantidade_inseridas = int(input())
        fator = valor_notas.index(valor_inserido)
        estoque_notas[fator] += quantidade_inseridas
        print("Inserido", quantidade_inseridas ,"cedula(s) de R$", valor_inserido,)

    else:
        print("Quantas moedas de R$", valor_inserido, "serão inseridas?")
        quantidade_inseridas = int(input())
        fator = valor_notas.index(valor_inserido)
        estoque_notas[fator] += quantidade_inseridas
        print("Inserido", quantidade_inseridas ,"moeda(s) de R$", valor_inserido,)
def remover_dinheiro():
#Ao selcionar a opção 4 ocorrerá o inverso da função (inserir_dinheiro), ao invés de ser uma soma será uma subtração.
    print("Insira qual a nota ou moeda que será removida:")
    valor_remover = float(input())
    fator = valor_notas.index(valor_remover)    
    print("Na máquina existem", estoque_notas[fator], "cédulas/moedas de R$", valor_remover,". Quanto deseja remover?")
    quantidade_removidas = 0
    subtracao_cedula = -1
    while subtracao_cedula < 0:
        quantidade_removidas = int(input()) 
        subtracao_cedula = estoque_notas[fator] - quantidade_removidas
        if subtracao_cedula >= 0:
            estoque_notas[fator] -= quantidade_removidas
            print("Removido", quantidade_removidas ,"do valor de R$", valor_remover)
        else:
            print('Valor inválido. Quantas cédulas deseja remover?')
def verificar_estoque_bebidas():
#verifica se ha bebidas no estoque.
    for cont in range (4):
        print(estoque_latas[cont],"garrafas/latas de", nome_bebidas[cont])
def adicionar_bebidas():
#Adiciona bebidas ao estoque
    for cont in range (4):
        print(cont + 1 ,"- Adicionar garrafas/latas de", nome_bebidas[cont])
        
    escolhe_lata = int(input())
    for cont in range(1, 5):
        if escolhe_lata == cont:
            print("Quantos(as)", nome_bebidas[cont - 1] ,"serão inseridas?")
            quantidade_latas = int(input())
            estoque_latas[cont - 1] += quantidade_latas
            print("Inserido", quantidade_latas ,"latas/garrafas de", nome_bebidas[cont - 1]) 
def verificar_pix():
#verifica se há numeros de celulares registrados por meio do pagamento por pix.
    fator = 0
    if len(numeros_celular_historico) > 0:
        for cont in range (len(numeros_celular_historico)):
            print("Número de telefone:", numeros_celular_historico[fator], "------ Pagou R$", historico_valor_pix[fator])
            fator += 1 
    else:
        print("Sem pagamentos por pix ate o momento")

#Funções comando consumidor
def liberar_refri(comando_maquina, dinheiro_depositado, estoque_latas, troco):
#Após paga, a bebida será liberada junto com o troco.
    for cont in range(1, 5):
        if comando_maquina == cont and dinheiro_depositado != 0:
            print(nome_bebidas[cont - 1],'liberado(a), pegue-a no compartimento!') 
            print('Obrigado pela compra, seu troco é de R$', troco)
            estoque_latas[cont - 1] -= 1 
def pagar_pix(comando_maquina, estoque_latas):
#verifica se o numero de celular e valido
#Adiciona ao historico de compras por pix
    print("Digite seu número de celular, com DDD, abaixo [(xx)xxxxx-xxxx] para efetivar o pagamento com pix: ")
    numero_celular = str(input())
    if len(numero_celular) == 11:
        numeros_celular_historico.append(numero_celular)
        for cont in range (1,5):
            if comando_maquina == cont:
                print(nome_bebidas[cont-1],'liberado(a), pegue-a no compartimento!')
                historico_valor_pix.append(preco_produto[cont - 1])
                estoque_latas[cont - 1] -= 1
    else:
        print('Número inválido.')


#Início da execução
comando_maquina = 0 

while comando_maquina != 999: #999 para emergency break
    
    comando_maquina = entrar_usuario()

    if comando_maquina == 23646:
        comando_administrador = 0 #Contador do while ADM
        
        while comando_administrador >= 0 and comando_administrador < 8: 
                entrar_adm()
                comando_administrador = int(input())

#calculo do saldo 
                if comando_administrador == 1:
                    calcular_saldo()
                
#quantidade de cedulas e moedas   
                elif comando_administrador == 2:
                    verificar_estoque()
                    
#Insere cedula/moeda no estoque da maquina      
                elif comando_administrador == 3:
                    inserir_dinheiro()
    
#Remove cedula/moeda no estoque da maquina 
                elif comando_administrador == 4:
                    remover_dinheiro()
                    
#Verefica o estoque de bebidas
                elif comando_administrador == 5:
                    verificar_estoque_bebidas()

#Adiciona bebidas ao estoque
                elif comando_administrador == 6:
                    adicionar_bebidas()
                
                elif comando_administrador == 7:
                    verificar_pix()
                    
    #Modo do comprador
    elif comando_maquina > 0 and comando_maquina < 5:
            valor_produto = 0 
            confirmacao = 0
            if comando_maquina == 1:
                valor_produto = preco_produto[0]
                if estoque_latas[0] > 0:
                    confirmacao = 1
                else:
                    print("o produto esta em falta")
            elif comando_maquina == 2:
                valor_produto = preco_produto[1]
                if estoque_latas[1] > 0:
                    confirmacao = 1
                else:
                    print("o produto esta em falta")
            elif comando_maquina == 3:
                valor_produto = preco_produto[2]
                if estoque_latas[2] > 0:
                    confirmacao = 1
                else:
                    print("o produto esta em falta")
            elif comando_maquina == 4:
                valor_produto = preco_produto[3]
                if estoque_latas[3] > 0:
                    confirmacao = 1
                else:
                    print("o produto esta em falta")

            if confirmacao == 1:
                
                print("1- pagar com dinheiro" )
                print("2- pagar com pix" )
                pix_ou_dinheiro = int(input())

                if confirmacao == 1 and pix_ou_dinheiro == 1:

                    print('Ótimo! O custo é de R$', valor_produto ,'. Insira o dinheiro em cédulas e/ou moedas na máquina.')
                    troco = float() 
                    total_pago = float() 
                    dinheiro_depositado = float() 

                    quantidade_moeda_vinte_e_cinco_centavos_inserida = 0
                    quantidade_moeda_cinquenta_centavos_inserida = 0
                    quantidade_moeda_um_real_inserida = 0
                    quantidade_cedula_dois_reais_inserida = 0
                    quantidade_cedula_cinco_reais_inserida = 0
                    quantidade_cedula_dez_reais_inserida = 0

                    while total_pago < valor_produto: 
                        dinheiro_depositado = float(input()) 
                        if dinheiro_depositado == 0: #'Comando' para cancelar a operação!!
                                troco = total_pago 
                                break
                        #Adiciona a cédula ou moeda inserida na máquina no estoque.
                        elif dinheiro_depositado == 10:
                            estoque_notas[5] = estoque_notas[5] + 1
                            quantidade_cedula_dez_reais_inserida += 1
                            
                        elif dinheiro_depositado == 5:
                            estoque_notas[4] = estoque_notas[4] + 1
                            quantidade_cedula_cinco_reais_inserida += 1
                            
                        elif dinheiro_depositado == 2:
                            estoque_notas[3] = estoque_notas[3] + 1
                            quantidade_cedula_dois_reais_inserida += 1
                            
                        elif dinheiro_depositado == 1:
                            estoque_notas[2] = estoque_notas[2] + 1
                            quantidade_moeda_um_real_inserida += 1
                            
                        elif dinheiro_depositado == 0.5:
                            estoque_notas[1] = estoque_notas[1] + 1
                            quantidade_moeda_cinquenta_centavos_inserida += 1

                        elif dinheiro_depositado == 0.25:
                            estoque_notas[0] = estoque_notas[0] + 1
                            quantidade_moeda_vinte_e_cinco_centavos_inserida += 1

                        # Variavel que mantém o valor pago até o momento
                        total_pago += dinheiro_depositado 
                        
                       #Cálculo do troco 
                        if total_pago >= valor_produto: 
                            troco = total_pago - valor_produto
                        else:
                            print('Você pagou um total de R$', total_pago, '. Faltam R$:', (valor_produto - total_pago) ,' para finalizar a compra.')
                            print('                 Ou cancele a operação clicando no botão - 0 -')

                    quantidade_moeda_vinte_e_cinco_centavos_removida = 0
                    quantidade_moeda_cinquenta_centavos_removida = 0
                    quantidade_moeda_um_real_removida = 0
                    quantidade_cedula_dois_reais_removida = 0
                    quantidade_cedula_cinco_reais_removida = 0
                    quantidade_cedula_dez_reais_removida = 0

                    calculo_de_cedulas_e_moedas_do_troco = troco  #Calcula quantidade de cédulas e moedas necessárias para o troco. "Contador".

                    while calculo_de_cedulas_e_moedas_do_troco >= 10:
                        if estoque_notas[5] - quantidade_cedula_dez_reais_removida >= 1:        
                            calculo_de_cedulas_e_moedas_do_troco -= 10
                            quantidade_cedula_dez_reais_removida = quantidade_cedula_dez_reais_removida + 1
                        else:
                            break

                    while calculo_de_cedulas_e_moedas_do_troco >= 5:
                        if estoque_notas[4] - quantidade_cedula_cinco_reais_removida >= 1:         
                            calculo_de_cedulas_e_moedas_do_troco -= 5
                            quantidade_cedula_cinco_reais_removida = quantidade_cedula_cinco_reais_removida + 1
                        else:
                            break

                    while calculo_de_cedulas_e_moedas_do_troco >= 2:
                        if estoque_notas[3] - quantidade_cedula_dois_reais_removida >= 1:        
                            calculo_de_cedulas_e_moedas_do_troco -= 2
                            quantidade_cedula_dois_reais_removida = quantidade_cedula_dois_reais_removida + 1
                        else:
                            break
                            
                    while calculo_de_cedulas_e_moedas_do_troco >= 1:
                        if estoque_notas[2] - quantidade_moeda_um_real_removida >= 1:        
                            calculo_de_cedulas_e_moedas_do_troco -= 1
                            quantidade_moeda_um_real_removida = quantidade_moeda_um_real_removida + 1
                        else:
                            break

                    while calculo_de_cedulas_e_moedas_do_troco >= 0.5:
                        if estoque_notas[1] - quantidade_moeda_cinquenta_centavos_removida >= 1:        
                            calculo_de_cedulas_e_moedas_do_troco -= 0.5
                            quantidade_moeda_cinquenta_centavos_removida = quantidade_moeda_cinquenta_centavos_removida + 1
                        else:
                            break

                    while calculo_de_cedulas_e_moedas_do_troco >= 0.25:
                        if estoque_notas[0] - quantidade_moeda_vinte_e_cinco_centavos_removida >= 1:        
                            calculo_de_cedulas_e_moedas_do_troco -= 0.25
                            quantidade_moeda_vinte_e_cinco_centavos_removida = quantidade_moeda_vinte_e_cinco_centavos_removida + 1
                        else:
                            break
                    if calculo_de_cedulas_e_moedas_do_troco > 0:
                        print('Compra cancelada. Troco insuficiente. Retornando R$' , total_pago , 'depositado')

                        #devolve exatamente o que o usuário inseriu na máquina
                        if quantidade_moeda_vinte_e_cinco_centavos_inserida  > 0:
                            estoque_notas[0] -= quantidade_moeda_vinte_e_cinco_centavos_inserida 
                        
                        if quantidade_moeda_cinquenta_centavos_inserida  > 0:
                            estoque_notas[1] -= quantidade_moeda_cinquenta_centavos_inserida 
                        
                        if quantidade_moeda_um_real_inserida  > 0:
                            estoque_notas[2] -= quantidade_moeda_um_real_inserida 
                        
                        if quantidade_cedula_dois_reais_inserida  > 0:
                            estoque_notas[3] -= quantidade_cedula_dois_reais_inserida 
                        
                        if quantidade_cedula_cinco_reais_inserida  > 0:
                            estoque_notas[4] -= quantidade_cedula_cinco_reais_inserida 
                        
                        if quantidade_cedula_dez_reais_inserida  > 0:
                            estoque_notas[5] -= quantidade_cedula_dez_reais_inserida 
                    
                    else:
    #            remove do estoque todas as cedulas e moedas necessarias para o troco
                        if quantidade_moeda_vinte_e_cinco_centavos_removida > 0:
                            estoque_notas[0] -= quantidade_moeda_vinte_e_cinco_centavos_removida
                        
                        if quantidade_moeda_cinquenta_centavos_removida > 0:
                            estoque_notas[1] -= quantidade_moeda_cinquenta_centavos_removida
                        
                        if quantidade_moeda_um_real_removida > 0:
                            estoque_notas[2] -= quantidade_moeda_um_real_removida
                        
                        if quantidade_cedula_dois_reais_removida > 0:
                            estoque_notas[3] -= quantidade_cedula_dois_reais_removida
                        
                        if quantidade_cedula_cinco_reais_removida > 0:
                            estoque_notas[4] -= quantidade_cedula_cinco_reais_removida
                        
                        if quantidade_cedula_dez_reais_removida > 0:
                            estoque_notas[5] -= quantidade_cedula_dez_reais_removida
                        
                        #maquina libera refrierantes 
                        liberar_refri(comando_maquina, dinheiro_depositado, estoque_latas, troco)

                elif pix_ou_dinheiro == 2:
                    #Pagamento por pix
                    pagar_pix(comando_maquina, estoque_latas) 