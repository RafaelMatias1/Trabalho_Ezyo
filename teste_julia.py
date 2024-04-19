# Inicializando a lista de agendamentos fora do bloco condicional

# Inicializando a lista de agendamentos fora do bloco condicional
agendamentos = {}

while True :

    print('Bem vindo ao sistema de agendamento de consultas')
    print('Selecione uma das opções abaixo:')
    print()
    print('1) Listar consultas agendadas')
    print('2) Agendar nova consulta')
    print('3) Desmarcar uma consulta')
    print('4) Sair')
    print()
    opcao_menu = input('Digite a opção desejada: ')



    if int(opcao_menu) == 1:
        print()
        print('Lista de consultas agendadas')
        print()
        for ind in agendamentos:
            print(agendamentos[ind])
        #linha = 0
        #for linha in range(len(agendamentos)):
        #    print(linha)
        #    print(agendamentos[linha])

    elif int(opcao_menu) == 2:
        print('Você está na área de agendamento de consultas!')
        print('Responda as seguintes perguntas para realizar o agendamento')
        nome = input('Qual o seu nome? ')
        telefone = input('Qual o seu número de telefone? ')
        email = input('Qual o seu e-mail? ')
        sexo = input('Qual o seu sexo? ')
        plano_saude = input('Qual o seu plano de saúde? ')
        dia = input('Qual o dia seria melhor para o agendamento da sua consulta? ')
        hora = input('Qual o melhor horário para a sua consulta no dia? ')

        print()
        print(nome, 'a sua consulta foi marcada para', dia, 'no horário', hora)
        print()

        input('Precione enter para continuar ')
        # Definindo um dicionário para representar o agendamento
        dados_paciente = {'nome': nome, 'telefone': telefone, 'email': email, 'sexo': sexo, 'plano_saude': plano_saude}

        # Adicionando o agendamento atual à lista de agendamentos
        agendamentos[dia + ' ' +  hora] = dados_paciente
        #append() é um método em Python usado para adicionar um elemento a uma lista. No caso do código que você forneceu:




    elif int(opcao_menu) == 3:
        print('Desmarcar uma consulta')

    elif int(opcao_menu) == 4:
        break