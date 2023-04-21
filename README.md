valor_moeda_cinco_centavos = float(0.05)

valor_moeda_dez_centavos = float(0.10)

valor_moeda_vinte_e_cinco_centavos = float(0.25)

valor_moeda_cinquenta_centavos = float(0.50)

valor_moeda_um_real = int(1.0)

valor_cedula_dois_reais = int(2)

valor_cedula_cinco_reais = int(5)

valor_cedula_dez_reais = int(10)

valor_cedula_vinte_reais = int(20)

valor_cedula_cinquenta_reais = int(50)

valor_cedula_cem_reais = int(100)

valor_cedula_duzentos_reais = int(200)

#quantidade de moedas inicialmente em estoque

quantidade_moeda_cinco_centavos = int(10)

quantidade_moeda_dez_centavos = int(15)

quantidade_moeda_vinte_e_cinco_centavos = int(20)

quantidade_moeda_cinquenta_centavos = int(42)

quantidade_moeda_um_real = int(60)

quantidade_cedula_dois_reais = int(80)

quantidade_cedula_cinco_reais = int(90)

quantidade_cedula_dez_reais = int(20)

quantidade_cedula_vinte_reais = int(10)

quantidade_cedula_cinquenta_reais = int(10)

quantidade_cedula_cem_reais = int(5)

quantidade_cedula_duzentos_reais = int(1)

preco_agua = float(2.50)

preco_guarana = float(5.25)

preco_coca_normal = float(6.50)

preco_coca_zero = float(7.75)


comando_maquina = int() #contador

while comando_maquina != 999: #999 para acabar com o loop
    
    print('=======================================================')
    print('Olá, seja bem-vindo! Escolha o numero de sua bebida:   ')
    print('                  1 - Guaraná Geladinho            ')
    print('                  2 - Coquinha Gelada              ')
    print('                  3 - Coca-Cola Zero               ')
    print('                  4 - Aguinha                      ')
    print('=======================================================')
        

    comando_maquina = int(input())
    
    #modo admin (codigo secreto, geralmente predifinido no manual da maquina)
    if comando_maquina == 23646:
            comando_administrador = 0 
        
            while comando_administrador >= 0 and comando_administrador < 5: 
                print("===MODO ADMINISTRADOR===")
                print("Selecione uma opção:")
                print("1 - Saldo máquina")
                print("2 - Estoque de cédulas e moedas")
                print("3 - Adicionar estoque de cédulas e moedas")
                print("4 - Remover estoque de cédulas e moedas")
                print("Digite qualquer outro número para voltar ao modo de usuário")
                comando_administrador = int(input()) 

            #calculo do saldo 
                if comando_administrador == int(1):
                    saldo_maquina = (quantidade_moeda_cinco_centavos * valor_moeda_cinco_centavos) + (quantidade_moeda_dez_centavos * valor_moeda_dez_centavos) + (quantidade_moeda_vinte_e_cinco_centavos * valor_moeda_vinte_e_cinco_centavos) +(quantidade_moeda_cinquenta_centavos * valor_moeda_cinquenta_centavos) + (quantidade_moeda_um_real * valor_moeda_um_real) + (quantidade_cedula_dois_reais * valor_cedula_dois_reais) + (quantidade_cedula_cinco_reais * valor_cedula_cinco_reais) + (quantidade_cedula_dez_reais * valor_cedula_dez_reais) + (quantidade_cedula_vinte_reais * valor_cedula_vinte_reais) + (quantidade_cedula_cinquenta_reais * valor_cedula_cinquenta_reais) + (quantidade_cedula_cem_reais * valor_cedula_cem_reais) + (quantidade_cedula_duzentos_reais * valor_cedula_duzentos_reais)  
                    print("O saldo da maquina é: R$", saldo_maquina)

            #quantidade de cedulas e moedas   
                elif comando_administrador == int(2):
                    print(quantidade_moeda_cinco_centavos, "moeda(s) de 5 centavos")
                    print(quantidade_moeda_dez_centavos, "moeda(s) de 10 centavos")
                    print(quantidade_moeda_vinte_e_cinco_centavos, "moeda(s) de 25 centavos")
                    print(quantidade_moeda_cinquenta_centavos, "moeda(s) de 50 centavos")
                    print(quantidade_moeda_um_real, "moeda(s) de 1 real")
                    print(quantidade_cedula_dois_reais, "cedula(s) de 2 reais")
                    print(quantidade_cedula_cinco_reais, "cedula(s) de 5 reais")
                    print(quantidade_cedula_dez_reais, "cedula(s) de 10 reais")
                    print(quantidade_cedula_vinte_reais, "cedula(s) de 20 reais")
                    print(quantidade_cedula_cinquenta_reais, "cedula(s) de 50 reais")
                    print(quantidade_cedula_cem_reais, "cedula(s) de 100 reais") 
                    print(quantidade_cedula_duzentos_reais, "cedula(s) de 200 reais")

            #Insere cedula/moeda no estoque da maquina      
                elif comando_administrador == int(3): 
                
                    print("Insira qual a nota ou moeda que sera inserida:") 
                    valor_inserido = float(input()) 
                    
                    if valor_inserido == valor_cedula_duzentos_reais: 
                        print("Quantas cédulas de 200 reais serão inseridas?") 
                        quantidade_inseridas = int(input()) 
                        quantidade_cedula_duzentos_reais = quantidade_cedula_duzentos_reais + quantidade_inseridas 
                        
                    elif valor_inserido == valor_cedula_cem_reais:
                        print("Quantas cédulas de 100 reais serão inseridas?")
                        quantidade_inseridas = int(input())
                        quantidade_cedula_cem_reais = quantidade_cedula_cem_reais + quantidade_inseridas
                        print("Inserido", quantidade_inseridas ,"cedula(s) de 100 reais")
                        
                    elif valor_inserido == valor_cedula_cinquenta_reais:
                        print("Quantas cédulas de 50 reais serão inseridas?")
                        quantidade_inseridas = int(input())
                        quantidade_cedula_cinquenta_reais = quantidade_cedula_cinquenta_reais + quantidade_inseridas
                        print("Inserido", quantidade_inseridas ,"cedula(s) de 50 reais")
                        
                    elif valor_inserido == valor_cedula_vinte_reais:
                        print("Quantas cédulas de 20 reais serão inseridas?")
                        quantidade_inseridas = int(input())
                        quantidade_cedula_vinte_reais = quantidade_cedula_vinte_reais + quantidade_inseridas
                        print("Inserido", quantidade_inseridas ,"cedula(s) de 25 reais")
                        
                    elif valor_inserido == valor_cedula_dez_reais:
                        print("Quantas cédulas de 10 reais serão inseridas?")
                        quantidade_inseridas = int(input())
                        quantidade_cedula_dez_reais = quantidade_cedula_dez_reais + quantidade_inseridas
                        print("Inserido", quantidade_inseridas ,"cedula(s) de 10 reais")
                        
                    elif valor_inserido == valor_cedula_cinco_reais:
                        print("Quantas cédulas de 5 reais serão inseridas?")
                        quantidade_inseridas = int(input())
                        quantidade_cedula_cinco_reais = quantidade_cedula_cinco_reais + quantidade_inseridas
                        print("Inserido", quantidade_inseridas ,"cedula(s) de 5 reais")
                        
                    elif valor_inserido == valor_cedula_dois_reais:
                        print("Quantas cédulas de 2 reais serão inseridas?")
                        quantidade_inseridas = int(input())
                        quantidade_cedula_dois_reais = quantidade_cedula_dois_reais + quantidade_inseridas
                        print("Inserido", quantidade_inseridas ,"cedula(s) de 2 reais")
                        
                    elif valor_inserido == valor_moeda_um_real:
                        print("Quantas moedas de 1 real serão inseridas?")
                        quantidade_inseridas = int(input())
                        quantidade_moeda_um_real = quantidade_moeda_um_real + quantidade_inseridas
                        print("Inserido", quantidade_inseridas ,"cedula(s) de 1 real")
                        
                    elif valor_inserido == valor_moeda_cinquenta_centavos:
                        print("Quantas moedas de 50 centavos serão inseridas?")
                        quantidade_inseridas = int(input())
                        quantidade_moeda_cinquenta_centavos = quantidade_moeda_cinquenta_centavos + quantidade_inseridas
                        print("Inserido", quantidade_inseridas ,"moeda(s) de 50 centavos")
                        
                    elif valor_inserido == valor_moeda_vinte_e_cinco_centavos:
                        print("Quantas moedas de 25 centavos serão inseridas?")
                        quantidade_inseridas = int(input())
                        quantidade_moeda_vinte_e_cinco_centavos = quantidade_moeda_vinte_e_cinco_centavos + quantidade_inseridas
                        print("Inserido", quantidade_inseridas ,"moeda(s) de 25 centavos")
                    
                    elif valor_inserido == valor_moeda_dez_centavos:
                        print("Quantas moedas de 10 centavos serão inseridas?")
                        quantidade_inseridas = int(input())
                        quantidade_moeda_dez_centavos = quantidade_moeda_dez_centavos + quantidade_inseridas
                        print("Inserido", quantidade_inseridas ,"moeda(s) de 10 centavos")
                    
                    elif valor_inserido == valor_moeda_cinco_centavos:
                        print("Quantas moedas de 5 centavos serão inseridas?")
                        quantidade_inseridas = int(input())
                        quantidade_moeda_cinco_centavos = quantidade_moeda_cinco_centavos + quantidade_inseridas
                        print("Inserido", quantidade_inseridas ,"moeda(s) de 5 centavos")
                
            #Remove cedula/moeda no estoque da maquina        
                elif comando_administrador == int(4): 
                    print("Insira qual a nota ou moeda que sera removida:") 
                    valor_remover = float(input()) 
                    
                    if valor_remover == valor_cedula_duzentos_reais: 
                        print("Na máquina existem", quantidade_cedula_duzentos_reais, "cédula(s) de R$200,00. Quantas serão removidas?") 
                        quantidade_removidas = int() 
                        subtracao_cedula = int(-1)  
                        while subtracao_cedula < 0:
                            quantidade_removidas = int(input()) 
                            subtracao_cedula = quantidade_cedula_duzentos_reais - quantidade_removidas  
                            if subtracao_cedula >= 0: 
                                quantidade_cedula_duzentos_reais = quantidade_cedula_duzentos_reais  - quantidade_removidas 
                                print("Removido", quantidade_removidas ,"cedula(s) de 200 reais") 
                            else: 
                                print('Valor inválido. Quantas cédulas deseja remover?')
                                
                    elif valor_remover == valor_cedula_cem_reais:
                        print("Na máquina existem", quantidade_cedula_cem_reais, "cédula(s) de R$100,00. Quantas serão removidas?")
                        quantidade_removidas = int()
                        subtracao_cedula = int(-1)
                        while subtracao_cedula < 0:
                            quantidade_removidas = int(input())
                            subtracao_cedula = quantidade_cedula_cem_reais - quantidade_removidas
                            if subtracao_cedula >= 0:
                                quantidade_cedula_cem_reais = quantidade_cedula_cem_reais  - quantidade_removidas
                                print("Removido", quantidade_removidas ,"cedula(s) de R$100,00 ")
                            else:
                                print('Valor inválido. Quantas cédulas deseja remover?')
                        
                    elif valor_remover == valor_cedula_cinquenta_reais:
                        print("Na máquina existem", quantidade_cedula_cinquenta_reais, "cédula(s) de R$50,00. Quantas serão removidas?")
                        quantidade_removidas = int()
                        subtracao_cedula = int(-1)
                        while subtracao_cedula < 0:
                            quantidade_removidas = int(input())
                            subtracao_cedula = quantidade_cedula_cinquenta_reais - quantidade_removidas
                            if subtracao_cedula >= 0:
                                quantidade_cedula_cinquenta_reais = quantidade_cedula_cinquenta_reais  - quantidade_removidas
                                print("Removido", quantidade_removidas ,"cedula(s) de R$50,00 ")
                            else:
                                print('Valor inválido. Quantas cédulas deseja remover?')
                        
                    elif valor_remover == valor_cedula_vinte_reais:
                        print("Na máquina existem", quantidade_cedula_vinte_reais, "cédula(s) de R$20,00. Quantas serão removidas?")
                        quantidade_removidas = int()
                        subtracao_cedula = int(-1)
                        while subtracao_cedula < 0:
                            quantidade_removidas = int(input())
                            subtracao_cedula = quantidade_cedula_vinte_reais - quantidade_removidas
                            if subtracao_cedula >= 0:
                                quantidade_cedula_vinte_reais = quantidade_cedula_vinte_reais  - quantidade_removidas
                                print("Removido", quantidade_removidas ,"cedula(s) de R$20,00 ")
                            else:
                                print('Valor inválido. Quantas cédulas deseja remover?')
                        
                    elif valor_remover == valor_cedula_dez_reais:
                        print("Na máquina existem", quantidade_cedula_dez_reais, "cédula(s) de R$10,00. Quantas serão removidas?")
                        quantidade_removidas = int()
                        subtracao_cedula = int(-1)
                        while subtracao_cedula < 0:
                            quantidade_removidas = int(input())
                            subtracao_cedula = quantidade_cedula_dez_reais - quantidade_removidas
                            if subtracao_cedula >= 0:
                                quantidade_cedula_dez_reais = quantidade_cedula_dez_reais  - quantidade_removidas
                                print("Removido", quantidade_removidas ,"cedula(s) de R$10,00 ")
                            else:
                                print('Valor inválido. Quantas cédulas deseja remover?')
                        
                    elif valor_remover == valor_cedula_cinco_reais:
                        print("Na máquina existem", quantidade_cedula_cinco_reais, "cédula(s) de R$5,00. Quantas serão removidas?")
                        quantidade_removidas = int()
                        subtracao_cedula = int(-1)
                        while subtracao_cedula < 0:
                            quantidade_removidas = int(input())
                            subtracao_cedula = quantidade_cedula_cinco_reais - quantidade_removidas
                            if subtracao_cedula >= 0:
                                quantidade_cedula_cinco_reais = quantidade_cedula_cinco_reais  - quantidade_removidas
                                print("Removido", quantidade_removidas ,"cedula(s) de R$5,00 ")
                            else:
                                print('Valor inválido. Quantas cédulas deseja remover?')

                    elif valor_remover == valor_cedula_dois_reais:
                        print("Na máquina existem", quantidade_cedula_dois_reais, "cédula(s) de R$2,00. Quantas serão removidas?")
                        quantidade_removidas = int()
                        subtracao_cedula = int(-1)
                        while subtracao_cedula < 0:
                            quantidade_removidas = int(input())
                            subtracao_cedula = quantidade_cedula_dois_reais - quantidade_removidas
                            if subtracao_cedula >= 0:
                                quantidade_cedula_dois_reais = quantidade_cedula_dois_reais  - quantidade_removidas
                                print("Removido", quantidade_removidas ,"cedula(s) de R$2,00 ")
                            else:
                                print('Valor inválido. Quantas cédulas deseja remover?')
                        
                    elif valor_remover == valor_moeda_um_real:
                        print("Na máquina existem", quantidade_moeda_um_real, "moeda(s) de R$1,00. Quantas serão removidas?")
                        quantidade_removidas = int()
                        subtracao_cedula = int(-1)
                        while subtracao_cedula < 0:
                            quantidade_removidas = int(input())
                            subtracao_cedula = quantidade_moeda_um_real - quantidade_removidas
                            if subtracao_cedula >= 0:
                                quantidade_moeda_um_real = quantidade_moeda_um_real - quantidade_removidas
                                print("Removido", quantidade_removidas ,"moeda(s) de R$1,00 ")
                            else:
                                print('Valor inválido. Quantas moedas deseja remover?')
                        
                    elif valor_remover == valor_moeda_cinquenta_centavos:
                        print("Na máquina existem", quantidade_moeda_cinquenta_centavos, "moeda(s) de R$0,50. Quantas serão removidas?")
                        quantidade_removidas = int()
                        subtracao_cedula = int(-1)
                        while subtracao_cedula < 0:
                            quantidade_removidas = int(input())
                            subtracao_cedula = quantidade_moeda_cinquenta_centavos - quantidade_removidas
                            if subtracao_cedula >= 0:
                                quantidade_moeda_cinquenta_centavos = quantidade_moeda_cinquenta_centavos - quantidade_removidas
                                print("Removido", quantidade_removidas ,"moeda(s) de R$0,50 ")
                            else:
                                print('Valor inválido. Quantas moedas deseja remover?')
                        
                    elif valor_remover == valor_moeda_vinte_e_cinco_centavos:
                        print("Na máquina existem", quantidade_moeda_vinte_e_cinco_centavos, "moeda(s) de R$0,25. Quantas serão removidas?")
                        quantidade_removidas = int()
                        subtracao_cedula = int(-1)
                        while subtracao_cedula < 0:
                            quantidade_removidas = int(input())
                            subtracao_cedula = quantidade_moeda_vinte_e_cinco_centavos - quantidade_removidas
                            if subtracao_cedula >= 0:
                                quantidade_moeda_vinte_e_cinco_centavos = quantidade_moeda_vinte_e_cinco_centavos  - quantidade_removidas
                                print("Removido", quantidade_removidas ,"cedula(s) de R$0,25 ")
                            else:
                                print('Valor inválido. Quantas moedas deseja remover?')
                    
                    elif valor_remover == valor_moeda_dez_centavos:
                        print("Na máquina existem", quantidade_moeda_dez_centavos, "cédula(s) de R$0,10. Quantas serão removidas?")
                        quantidade_removidas = int()
                        subtracao_cedula = int(-1)
                        while subtracao_cedula < 0:
                            quantidade_removidas = int(input())
                            subtracao_cedula = quantidade_moeda_dez_centavos - quantidade_removidas
                            if subtracao_cedula >= 0:
                                quantidade_moeda_dez_centavos = quantidade_moeda_dez_centavos  - quantidade_removidas
                                print("Removido", quantidade_removidas ,"cedula(s) de R$0,10 ")
                            else:
                                print('Valor inválido. Quantas moedas deseja remover?')
                    
                    elif valor_remover == valor_moeda_cinco_centavos:
                        print("Na máquina existem", quantidade_moeda_cinco_centavos, "cédula(s) de R$0,05. Quantas serão removidas?")
                        quantidade_removidas = int()
                        subtracao_cedula = int(-1)
                        while subtracao_cedula < 0:
                            quantidade_removidas = int(input())
                            subtracao_cedula = quantidade_moeda_cinco_centavos - quantidade_removidas
                            if subtracao_cedula >= 0:
                                quantidade_moeda_cinco_centavos = quantidade_moeda_cinco_centavos  - quantidade_removidas
                                print("Removido", quantidade_removidas ,"cedula(s) de R$0,05 ")
                            else:
                                print('Valor inválido. Quantas moedas deseja remover?')

    #Modo do comprador
    elif comando_maquina > 0 and comando_maquina < 5: 
            valor_produto = int() 
            if comando_maquina == int(1):
                valor_produto = preco_guarana 
            elif comando_maquina == int(2):
                valor_produto = preco_coca_normal 
            elif comando_maquina == int(3): 
                valor_produto = preco_coca_zero 
            elif comando_maquina == int(4): 
                valor_produto = preco_agua 

            print('Ótimo! O custo é de R$', valor_produto ,'. Insira o dinheiro em cédulas e/ou moedas na máquina.') 
            troco = float() 
            total_pago = float() 
            dinheiro_depositado = float() 
           
            while total_pago < valor_produto: 
                dinheiro_depositado = float(input()) 
                if dinheiro_depositado == 0: 
                        troco = total_pago 
                        break
                    
                #Acrescenta cedula/moeda no estoque da maquina
                if dinheiro_depositado == valor_cedula_duzentos_reais: 
                    quantidade_cedula_duzentos_reais = quantidade_cedula_duzentos_reais + 1 
                
                elif dinheiro_depositado == valor_cedula_cem_reais:
                    quantidade_cedula_cem_reais = quantidade_cedula_cem_reais + 1
                    
                elif dinheiro_depositado == valor_cedula_cinquenta_reais:
                    quantidade_cedula_cinquenta_reais = quantidade_cedula_cinquenta_reais + 1
                    
                elif dinheiro_depositado == valor_cedula_vinte_reais:
                    quantidade_cedula_vinte_reais = quantidade_cedula_vinte_reais + 1
                    
                elif dinheiro_depositado == valor_cedula_dez_reais:
                    quantidade_cedula_dez_reais = quantidade_cedula_dez_reais + 1
                    
                elif dinheiro_depositado == valor_cedula_cinco_reais:
                    quantidade_cedula_cinco_reais = quantidade_cedula_cinco_reais + 1
                    
                elif dinheiro_depositado == valor_cedula_dois_reais:
                    quantidade_cedula_dois_reais = quantidade_cedula_dois_reais + 1
                    
                elif dinheiro_depositado == valor_moeda_um_real:
                    quantidade_moeda_um_real = quantidade_moeda_um_real + 1
                    
                elif dinheiro_depositado == valor_moeda_cinquenta_centavos:
                    quantidade_moeda_cinquenta_centavos = quantidade_moeda_cinquenta_centavos + 1
                    
                elif dinheiro_depositado == valor_moeda_vinte_e_cinco_centavos:
                    quantidade_moeda_vinte_e_cinco_centavos = quantidade_moeda_vinte_e_cinco_centavos + 1
                
                elif dinheiro_depositado == valor_moeda_dez_centavos:
                    quantidade_moeda_dez_centavos = quantidade_moeda_dez_centavos + 1
                
                elif dinheiro_depositado == valor_moeda_cinco_centavos:
                    quantidade_moeda_cinco_centavos = quantidade_moeda_cinco_centavos + 1
                    
                total_pago = total_pago + dinheiro_depositado 
                
                if total_pago >= valor_produto: 
                    troco = total_pago - valor_produto 
                    
                else: 
                    print('Você pagou um total de R$', total_pago, '. Faltam R$:', (valor_produto - total_pago) ,' para finalizar a compra.')
                    print('                 Ou cancele a operação clicando no botão - 0 -')
                                 
            calculo_de_cedulas_e_moedas_do_troco = troco  
            
            while calculo_de_cedulas_e_moedas_do_troco >= valor_cedula_cem_reais: 
                if quantidade_cedula_cem_reais >= 1: 
                    calculo_de_cedulas_e_moedas_do_troco = calculo_de_cedulas_e_moedas_do_troco - valor_cedula_cem_reais
                    quantidade_cedula_cem_reais = quantidade_cedula_cem_reais - 1

                else:
                    break

            while calculo_de_cedulas_e_moedas_do_troco >= valor_cedula_cinquenta_reais:
                if quantidade_cedula_cinquenta_reais >= 1:      
                    calculo_de_cedulas_e_moedas_do_troco = calculo_de_cedulas_e_moedas_do_troco - valor_cedula_cinquenta_reais
                    quantidade_cedula_cinquenta_reais = quantidade_cedula_cinquenta_reais - 1
                else:
                    break

            while calculo_de_cedulas_e_moedas_do_troco >= valor_cedula_vinte_reais:
                 
                 if quantidade_cedula_vinte_reais >= 1:       
                    calculo_de_cedulas_e_moedas_do_troco = calculo_de_cedulas_e_moedas_do_troco - valor_cedula_vinte_reais 
                    quantidade_cedula_vinte_reais = quantidade_cedula_vinte_reais - 1 
                
                 else: 
                     break    

            while calculo_de_cedulas_e_moedas_do_troco >= valor_cedula_dez_reais: 
                if quantidade_cedula_dez_reais >= 1:        
                    calculo_de_cedulas_e_moedas_do_troco = calculo_de_cedulas_e_moedas_do_troco - valor_cedula_dez_reais
                    quantidade_cedula_dez_reais = quantidade_cedula_dez_reais - 1
                else:
                    break

            while calculo_de_cedulas_e_moedas_do_troco >= valor_cedula_cinco_reais: 
                if quantidade_cedula_cinco_reais >= 1:         
                    calculo_de_cedulas_e_moedas_do_troco = calculo_de_cedulas_e_moedas_do_troco - valor_cedula_cinco_reais
                    quantidade_cedula_cinco_reais = quantidade_cedula_cinco_reais - 1
                else:
                    break

            while calculo_de_cedulas_e_moedas_do_troco >= valor_cedula_dois_reais:
                if quantidade_cedula_dois_reais >= 1:        
                    calculo_de_cedulas_e_moedas_do_troco = calculo_de_cedulas_e_moedas_do_troco - valor_cedula_dois_reais
                    quantidade_cedula_dois_reais = quantidade_cedula_dois_reais - 1
                else:
                    break
                    
            while calculo_de_cedulas_e_moedas_do_troco >= valor_moeda_um_real:
                if quantidade_moeda_um_real >= 1:        
                    calculo_de_cedulas_e_moedas_do_troco = calculo_de_cedulas_e_moedas_do_troco - valor_moeda_um_real
                    quantidade_moeda_um_real = quantidade_moeda_um_real - 1
                else:
                    break

            while calculo_de_cedulas_e_moedas_do_troco >= valor_moeda_cinquenta_centavos:
                if quantidade_moeda_cinquenta_centavos >= 1:        
                    calculo_de_cedulas_e_moedas_do_troco = calculo_de_cedulas_e_moedas_do_troco - valor_moeda_cinquenta_centavos
                    quantidade_moeda_cinquenta_centavos = quantidade_moeda_cinquenta_centavos - 1
                else:
                    break

            while calculo_de_cedulas_e_moedas_do_troco >= valor_moeda_vinte_e_cinco_centavos:
                if quantidade_moeda_vinte_e_cinco_centavos >= 1:        
                    calculo_de_cedulas_e_moedas_do_troco = calculo_de_cedulas_e_moedas_do_troco - valor_moeda_vinte_e_cinco_centavos
                    quantidade_moeda_vinte_e_cinco_centavos = quantidade_moeda_vinte_e_cinco_centavos - 1
                else:
                    break

            while calculo_de_cedulas_e_moedas_do_troco >= valor_moeda_dez_centavos:
                if quantidade_moeda_dez_centavos >= 1:    
                    calculo_de_cedulas_e_moedas_do_troco = calculo_de_cedulas_e_moedas_do_troco - valor_moeda_dez_centavos
                    quantidade_moeda_dez_centavos = quantidade_moeda_dez_centavos - 1
                
                else:
                    break

            while calculo_de_cedulas_e_moedas_do_troco >= valor_moeda_cinco_centavos:
                if quantidade_moeda_cinco_centavos >= 1:
                    calculo_de_cedulas_e_moedas_do_troco = calculo_de_cedulas_e_moedas_do_troco - valor_moeda_cinco_centavos
                    quantidade_moeda_cinco_centavos = quantidade_moeda_cinco_centavos - 1
                else:
                    break

            if calculo_de_cedulas_e_moedas_do_troco != 0:                     
                print('Compra cancelada. Troco inválido')

            else: 
            #maquina libera refrierantes 
                if comando_maquina == int(1) and dinheiro_depositado != 0: 
                    print('Guarana liberado, pegue-o no compartimento!')
                    print('Obrigado pela compra, seu troco é de R$', troco,)
                    
                elif comando_maquina == int(2) and dinheiro_depositado != 0:
                    print('Coquinha normal liberada, pegue-o no compartimento!')
                    print('Obrigado pela compra, seu troco é de R$', troco,)
                
                elif comando_maquina == int(3) and dinheiro_depositado != 0:
                    print('Coquinha zero liberada, pegue-o no compartimento!')
                    print('Obrigado pela compra, seu troco é de R$', troco,)
                
                elif comando_maquina == int(4) and dinheiro_depositado != 0:
                    print('Aguinha liberada, pegue-o no compartimento!')
                    print('Obrigado pela compra, seu troco é de R$', troco,)
                
                else:
                    print("Compra cancelada")
