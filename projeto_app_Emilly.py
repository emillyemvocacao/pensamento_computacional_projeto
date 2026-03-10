'''
CRUD 

HAMBURGUERIA






'''


print('\n === Sistema de Hamburgueria === \n')


print("1. Cadastro")
print("2. Cardápio")
print("3. Solicitar pedido")
print("4. Pagamento")
print("5. Acompanhar a entrega")
print("6. Cancelar pedido")
print("0. Sair")



while True:

    escolha_menu = input("\n Escolha uma opção: ")
    if escolha_menu == '1': 

        print("Cadastro...")
        nome_cliente = input("Variavel cliente: ")
        telefone_cliente = input("Digite o telefone do cliente: ")



    elif escolha_menu == '0':

        print("Saindo do sistema, Até logo!")
        break


    else: 
        print("opção inválida. Por favor, tente novamente.")