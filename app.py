import os

restaurantes = [{"nome":"Praça","categoria":"Japonesa", "ativo":False},
                {"nome":"Piza Suprema","categoria":"Pizza","ativo":True},
                {"nome":"Cantina","categoria":"Italiano", "ativo":False}]

def exibir_nome_do_programa():
    print(""""
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
""")

def exibir_opcoes():
    print("1. Cadastrar Restaurante")
    print("2. Listar RestauranteS")
    print("3. Alternar estado do Restaurante")
    print("4. Sair\n")

def finalizar_app():
    exibir_subtitulo("Finalizando App")

def voltar_ao_menu_principal():
    input("\nDigite qualquer tecla para voltar ao menu principal ")
    main()
    #POR MOTIVO DE MANUTENÇÃO (REAFATOREI) O CÓDIGO PARA QUE SEJA EXIBIDO UM PEQUENO ESPAÇO PARA O USUÁRIO,
    #CLICAR UMA TECLA PARA VOLTA

def opcao_invalida():
    print("Opção inválida\n")
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
     os.system("cls")
     linha = "*" * (len(texto) + 4)
     print(linha)
     print(texto)
     print(linha)
     print() #PRINT VAZIO PULA LINHA
     #FUNÇÃO PARA ADCIONAR UM SUBTITULO SE CASO SURGIR MAIS OPÇÕES NO APP. E JÁ COM LIMPA TELA

def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastar novo restaurantes")
    nome_do_restaurante = input("Informe o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do restaurante {nome_do_restaurante}: ")
    #Adicionar a variável a lista e dicionário com o append()
    #restaurantes.append(nome_do_restaurante)
    dados_do_restaurante = {"nome":nome_do_restaurante,"categoria":categoria,"ativo":False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n ")
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo("Listando Restaurantes")
    
    print(f"{'Nome do restaurante'.ljust(30)} | {'Categoria'.ljust(26)} | Status ")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        #USANDO O TERNÁRIO PARA MOSTRAR UMA MENSAGEM Ativado e Desativado AO INVÉS DE True E False
        ativo = "Ativado" if restaurante["ativo"] else "Desativado"
        #A FUNÇÃO .ljust() ELA DA UM ESPAÇO ENTRE AS PALAVRAS POR EXEMPLO
        print(f"- Restaurante: {nome_restaurante.ljust(15)} | Categoria: {categoria.ljust(15)} | {ativo}")

    voltar_ao_menu_principal()

def alternar_estado_do_restaurante():
    exibir_subtitulo("Alternando estado do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja ativar: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True # RESTAURANTE FOI ENCONTRADO POIS ELE É True
            #AQUI UTILIZANDO UM OPERADOR LÓGICO ( NOT ) PARA INVERTER O ESTADO DE "ativo"
            restaurante["ativo"] = not restaurante["ativo"]
            #TERNÁRIO
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
   #USANDO O not PARA SE NÃO EXISTIR UM RESTAURANTE SIGNIFICA QUE A CONDIÇÃO FOI False
    if not restaurante_encontrado:
        print("Restaurante não encontrado!")
    
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
    #   opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

    #match opcao_escolhida:
#    case 1:
#        print("Cadastrar restaurante")
#    case 2:
#        print("Listar restaurantes")
#    case 3:
#        print("Ativar restaurante")
#    case 4:
#        finalizar_app()
#    case _:
#        print("Opção inválida")

def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
  

if __name__ == '__main__':
    main()